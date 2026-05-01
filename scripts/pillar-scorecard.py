#!/usr/bin/env python3
"""
pillar-scorecard.py — runs scripts/pillar-page-validate.sh on every
pillar-candidate page in dist/ and produces a ranked scorecard.

Discovery: walks dist/ for index.html files, excludes blog/admin/api/
thanks/files/schedule/new/tpost/404/privacy/recalls. For each candidate,
runs validate script, parses output, builds row.

Output: stdout table sorted by fail count + CSV at docs/pillar-scorecard.csv.

Usage:
  python3 scripts/pillar-scorecard.py
"""

import subprocess
import re
import csv
from pathlib import Path

ROOT = Path(__file__).parent.parent
DIST = ROOT / "dist"
VALIDATE = ROOT / "scripts" / "pillar-page-validate.sh"
OUT = ROOT / "docs" / "pillar-scorecard.csv"

EXCLUDE = re.compile(
    r'/(blog|admin|api|thanks|files|schedule|new|tpost|404|privacy|recalls)/',
    re.I
)

# Non-pillar utility pages — wrong shape for the gate (FAQ hubs are short by
# design, glossaries don't need LocalBusiness, etc). Keep separate from
# pillar uplift work; these have their own (looser) standards.
NON_PILLAR = re.compile(
    r'/(faq|glosariy|glossariy|glossary|about|api-docs|guide|contact)/?$',
    re.I
)

def discover():
    candidates, skipped_non_pillar = [], []
    for path in DIST.rglob("index.html"):
        rel = str(path.relative_to(DIST))
        full_path = "/" + rel.replace("/index.html", "/")
        if EXCLUDE.search(full_path):
            continue
        if NON_PILLAR.search(full_path):
            skipped_non_pillar.append(path)
            continue
        candidates.append(path)
    return sorted(candidates), sorted(skipped_non_pillar)

def run_validate(file_path):
    try:
        r = subprocess.run(
            ["bash", str(VALIDATE), str(file_path)],
            capture_output=True, text=True, timeout=15
        )
        out = r.stdout
        if "ALL CHECKS PASSED" in out:
            return (True, 0, out)
        m = re.search(r'TOTAL FAILS: (\d+)', out)
        if m:
            return (False, int(m.group(1)), out)
        return (False, -1, out)
    except Exception as e:
        return (False, -1, str(e))

def detect_lang(html_path):
    try:
        text = html_path.read_text(encoding="utf-8", errors="replace")[:1000]
        if 'lang="ru"' in text: return "RU"
        if 'lang="en"' in text: return "EN"
    except Exception:
        pass
    return "UA"

def parse_checks(output):
    """Per-check status: ✅ pass / ⚠️ warn / ❌ fail / ? unknown."""
    checks = {
        'schemas': '?', 'words': '?', 'h1_hook': '?',
        'h1_ws': '?', 'hreflang': '?', 'lang_purity': '?'
    }
    for line in output.split('\n'):
        marker = '✅' if '✅' in line else ('⚠️' if '⚠️' in line else ('❌' if '❌' in line else None))
        if not marker: continue
        if 'schemas' in line: checks['schemas'] = marker
        elif 'words:' in line: checks['words'] = marker
        elif 'h1' in line and ('brand-hook' in line or 'generic' in line or 'h1: not found' in line):
            checks['h1_hook'] = marker
        elif 'whitespace' in line: checks['h1_ws'] = marker
        elif 'hreflang' in line and 'reciprocal' not in line:
            checks['hreflang'] = marker
        elif 'language' in line:
            checks['lang_purity'] = marker
    return checks

def main():
    if not VALIDATE.exists():
        print(f"ERROR: {VALIDATE} not found"); return
    if not DIST.exists():
        print(f"ERROR: {DIST} not found — run 'npm run build' first"); return

    candidates, skipped = discover()
    print(f"Discovered {len(candidates)} REAL pillars")
    print(f"  (skipped {len(skipped)} non-pillar utility pages: faq, glossary, about, api-docs, guide)")
    print(f"Running validate on each...\n")

    rows = []
    for i, path in enumerate(candidates, 1):
        rel = str(path.relative_to(DIST))
        slug = rel.replace("/index.html", "") or "(home)"
        lang = detect_lang(path)
        passed, fails, output = run_validate(path)
        checks = parse_checks(output)
        if lang == 'EN' and checks['lang_purity'] == '?':
            checks['lang_purity'] = '-'  # not applicable
        rows.append({
            'slug': slug,
            'lang': lang,
            'passed': passed,
            'fails': fails,
            **checks,
        })

    rows.sort(key=lambda r: (-r['fails'], r['slug']))

    print(f"{'F':>2} {'L':<3} {'SCH':<4} {'WRD':<4} {'H1H':<4} {'H1W':<4} {'HRF':<4} {'LNG':<4}  SLUG")
    print("-" * 95)
    for r in rows:
        marker = '✅' if r['passed'] else '❌'
        print(f"{r['fails']:>2} {r['lang']:<3} {r['schemas']:<4} {r['words']:<4} "
              f"{r['h1_hook']:<4} {r['h1_ws']:<4} {r['hreflang']:<4} {r['lang_purity']:<4}  "
              f"{marker} {r['slug']}")

    passed_n = sum(1 for r in rows if r['passed'])
    print("-" * 95)
    print(f"\nTotal pages: {len(rows)}  |  ✅ PASS: {passed_n}  |  ❌ FAIL: {len(rows) - passed_n}")

    fail_types = {'schemas': 0, 'words': 0, 'h1_hook': 0, 'h1_ws': 0, 'hreflang': 0, 'lang_purity': 0}
    warn_types = dict(fail_types)
    for r in rows:
        for k in fail_types:
            if r[k] == '❌': fail_types[k] += 1
            elif r[k] == '⚠️': warn_types[k] += 1
    print("\nFail breakdown by check (❌ + ⚠️):")
    for k in sorted(fail_types.keys(), key=lambda x: -(fail_types[x] + warn_types[x])):
        total = fail_types[k] + warn_types[k]
        if total: print(f"  {k:<14}: {total} ({fail_types[k]} ❌ + {warn_types[k]} ⚠️)")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nFull CSV: {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
