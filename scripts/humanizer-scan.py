#!/usr/bin/env python3
"""
humanizer-scan.py — Phase 1 diagnostic scan for AI-tells across all site pages.

Reads pages from src/pages/**/*.astro (excluding SKIP routes), counts:
- AI-tells per language (UA/RU/EN) per docs/humanizer-ua-mtp.md
- "Soft" AI-vocab (landscape/ensure — context-dependent, reported separately)
- MTP anchor-numbers (concrete facts that anchor authority)
- file size and approximate word count

Outputs a ranked table to stdout AND CSV to docs/humanizer-scan-results.csv.

This is READ-ONLY. Does not modify any files.
"""

import re
import os
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
PAGES = ROOT / "src" / "pages"
OUTPUT_CSV = ROOT / "docs" / "humanizer-scan-results.csv"

SKIP_PATTERNS = [
    r"^admin/", r"^api/", r"^thanks/", r"^files/", r"^schedule/",
    r"^new/", r"blog/tpost/", r"^404", r"privacy\.astro$",
    r"recalls\.astro$",
]

UA_TELLS = [
    "у сучасному світі", "у сьогоднішніх реаліях", "в умовах сьогодення",
    "у динамічному світі", "варто зазначити", "слід підкреслити",
    "необхідно відзначити", "варто звернути увагу", "комплексне рішення",
    "оптимальне рішення", "професійне рішення", "індивідуальне рішення",
    "ключова перевага", "ключовий фактор", "ключовий момент",
    "вирішальний фактор", "це означає, що", "це означає що",
    "практичний наслідок", "що це дає вам", "з огляду на вищесказане",
    "отже, можна зробити висновок", "підсумовуючи",
    "забезпечення виконання", "здійснення процесу", "у разі потреби",
    "ефективна оптимізація", "весь спектр послуг", "повний цикл послуг",
    "під ключ", "Розглянемо детальніше", "Перейдемо до",
    "ідеальним вибором", "Все, що потрібно знати про",
]

RU_TELLS = [
    "в современных реалиях", "в сегодняшнем мире", "в условиях современного",
    "стоит отметить", "следует подчеркнуть", "необходимо отметить",
    "комплексное решение", "оптимальное решение", "индивидуальный подход",
    "ключевое преимущество", "ключевой фактор", "решающий фактор",
    "это означает, что", "это означает что", "практическое следствие",
    "что это даёт вам", "в свете вышесказанного", "подводя итоги",
    "обеспечение выполнения", "осуществление процесса",
    "весь спектр услуг", "полный цикл услуг", "под ключ",
    "идеальным выбором",
]

EN_TELLS = [
    "in today's", "in the current landscape", "in the modern world",
    "delve into", "leverage", "navigate the complex", "harness the power",
    "unlock the potential", "comprehensive solution", "optimal solution",
    "tailored solution", "end-to-end solution", "key advantage",
    "key factor", "crucial element", "critical component",
    "it's worth noting", "needless to say", "this means that",
    "practical implication", "moreover,", "furthermore,",
    "in conclusion", "to sum up", "all in all", "at the end of the day",
    "robust", "seamless", "cutting-edge", "state-of-the-art",
    "world-class", "elevate your business", "we are committed to",
    "we strive to", "perfect choice",
]

SOFT_TELLS = ["landscape", " ensure ", " ensures "]

ANCHORS = [
    r"3\s?700\s?м", r"3,700\s?m", r"2\.?6\s?млн",
    r"2[,.]?6M\b", r"2\.?6\s?million", r"800\s?мс", r"800\s?ms",
    r"47\s?(?:хв|минут|minutes)", r"18\s?грн",
    r"21\s?(?:робочий|рабочий|working|day)",
    r"0\s?(?:днів|дней|days)",
    r"ЄДРПОУ|EDRPOU|45315740", r"Lloyd",
    r"350\s?(?:кВА|kVA)", r"Starlink",
    r"14\s?(?:днів|дней|days)",
]


def should_skip(rel_path: str) -> bool:
    return any(re.search(p, rel_path) for p in SKIP_PATTERNS)


def count_matches(text, patterns, regex=False):
    total = 0
    for p in patterns:
        if regex:
            total += len(re.findall(p, text, re.IGNORECASE))
        else:
            total += text.lower().count(p.lower())
    return total


def approximate_word_count(text):
    cleaned = re.sub(r"<script[^>]*>.*?</script>", "", text, flags=re.DOTALL)
    cleaned = re.sub(r"<style[^>]*>.*?</style>", "", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"^---\s*\n.*?\n---\s*\n", "", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"<[^>]+>", " ", cleaned)
    return len(cleaned.split())


def detect_language(rel_path):
    if rel_path.startswith("ru/"): return "RU"
    if rel_path.startswith("en/"): return "EN"
    return "UA"


def priority(tells):
    if tells >= 10: return "MUST FIX"
    if tells >= 5: return "should fix"
    if tells >= 2: return "minor"
    return "OK"


def main():
    if not PAGES.exists():
        print(f"ERROR: {PAGES} not found", file=sys.stderr)
        sys.exit(1)

    rows = []
    skipped = 0

    for astro_file in PAGES.rglob("*.astro"):
        rel = str(astro_file.relative_to(PAGES))
        if should_skip(rel):
            skipped += 1
            continue

        text = astro_file.read_text(encoding="utf-8", errors="replace")
        lang = detect_language(rel)

        ua = count_matches(text, UA_TELLS)
        ru = count_matches(text, RU_TELLS)
        en = count_matches(text, EN_TELLS)
        soft = count_matches(text, SOFT_TELLS)
        total_tells = ua + ru + en

        anchors = count_matches(text, ANCHORS, regex=True)
        words = approximate_word_count(text)

        rows.append({
            "file": rel,
            "lang": lang,
            "tells": total_tells,
            "soft": soft,
            "anchors": anchors,
            "words": words,
            "tells_per_kw": round(total_tells / max(words, 1) * 1000, 1),
            "priority": priority(total_tells),
        })

    rows.sort(key=lambda r: (-r["tells"], -r["tells_per_kw"]))

    print(f"\n{'='*100}")
    print(f"HUMANIZER SCAN — {len(rows)} pages scanned, {skipped} skipped")
    print(f"{'='*100}")
    print(f"{'PRI':<11} {'LNG':<4} {'TELL':>5} {'SOFT':>5} {'ANCH':>5} {'WRD':>5} {'/kw':>5}  FILE")
    print("-" * 100)

    by_pri = {"MUST FIX": 0, "should fix": 0, "minor": 0, "OK": 0}
    for r in rows:
        by_pri[r["priority"]] += 1
        if r["tells"] > 0:
            print(f"{r['priority']:<11} {r['lang']:<4} {r['tells']:>5} "
                  f"{r['soft']:>5} {r['anchors']:>5} {r['words']:>5} "
                  f"{r['tells_per_kw']:>5}  {r['file']}")

    print("-" * 100)
    print(f"\nSummary by priority:")
    for k in ["MUST FIX", "should fix", "minor", "OK"]:
        print(f"  {k:<12}: {by_pri[k]} pages")
    print(f"  Total tells across site: {sum(r['tells'] for r in rows)}")
    print(f"  Total soft tells: {sum(r['soft'] for r in rows)}")

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["file", "lang", "tells", "soft",
                                                "anchors", "words",
                                                "tells_per_kw", "priority"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nFull CSV: {OUTPUT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
