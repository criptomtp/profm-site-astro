#!/usr/bin/env python3
"""
wikidata-postsubmit.py — Run AFTER Wikidata entity created manually (via
Special:NewItem UI or Computer Use agent following CLICKWORK-BRIEF.md).

Takes Q-number as argument, applies sameAs patches, builds, commits, pushes.

Usage:
    python3 scripts/wikidata-postsubmit.py Q123456789
"""

import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
LOG_FILE = ROOT / "docs" / "wikidata" / "SUBMISSION-LOG.md"


def banner(msg, char="="):
    print(f"\n{char * 70}\n  {msg}\n{char * 70}")


def write_submission_log(q_number):
    timestamp = datetime.now().isoformat(timespec="seconds")
    log = f"""# Wikidata Submission Log — MTP Group Fulfillment

**Timestamp:** {timestamp}
**Q-number:** {q_number}
**Entity URL:** https://www.wikidata.org/wiki/{q_number}
**Submission method:** Manual via Special:NewItem (account not autoconfirmed,
QuickStatements blocked). Used CLICKWORK-BRIEF.md instructions.

## What was submitted (7 core statements)

- P31 instance of = business (Q4830453)
- P3125 EDRPOU code = "45315740"
- P17 country = Ukraine (Q212)
- P856 official website = https://www.fulfillmentmtp.com.ua
- P571 inception = 2014 (year precision)
- P1454 legal form = limited liability company in Ukraine (Q98834261)
- P159 headquarters location = Boryspil (Q158910)

Labels added in: en, uk, ru

## Pending statements (to add later via QuickStatements after autoconfirmed)

After account reaches autoconfirmed status (4+ days old, 50+ edits), these
additional statements can be added via `docs/wikidata/quickstatements.txt`:

- P31 also = organization (Q43229)
- P452 industry = order fulfillment (Q1473552)
- P131 located in = Kyiv Oblast (Q170036)
- P281 postal code = "08322"
- P2397 YouTube channel = "@mtpgroup"

## Verification

- Wikidata page: https://www.wikidata.org/wiki/{q_number}
- Contributions: https://www.wikidata.org/wiki/Special:Contributions/Mykola_Liashchuk
- Google Rich Results (after deploy):
  https://search.google.com/test/rich-results?url=https%3A%2F%2Fwww.fulfillmentmtp.com.ua%2Fua%2Fabout%2F

## Patroller review

1-7 days community review. Monitor entity page for edits/concerns.
If delete-nominated: accumulate press coverage (Forbes UA, AIN.UA, interviews)
before re-submit.
"""
    LOG_FILE.write_text(log, encoding="utf-8")
    print(f"✅ Submission log written: docs/wikidata/SUBMISSION-LOG.md")


def apply_sameas_patches(q_number):
    banner("Apply sameAs patches to JSON-LD")
    wikidata_url = f"https://www.wikidata.org/wiki/{q_number}"

    targets = [
        ROOT / "src" / "pages" / "ua" / "about.astro",
        ROOT / "src" / "pages" / "poslugy.astro",
        ROOT / "src" / "components" / "Base.astro",
        ROOT / "public" / "llms.txt",
    ]

    patched_count = 0
    for fp in targets:
        if not fp.exists():
            print(f"⚠️  Skip (not found): {fp.relative_to(ROOT)}")
            continue

        content = fp.read_text(encoding="utf-8")

        if wikidata_url in content:
            print(f"⏭️  Already patched: {fp.relative_to(ROOT)}")
            continue

        original = content

        if fp.name == "llms.txt":
            if "## Verifiable identifiers" in content:
                content = re.sub(
                    r"(## Verifiable identifiers[^\n]*\n)",
                    rf"\1- Wikidata entity: {wikidata_url}\n",
                    content, count=1
                )
            else:
                identifier_block = f"""
## Verifiable identifiers
- EDRPOU (Ukraine state register): 45315740
- Wikidata entity: {wikidata_url}
- YouControl profile: https://youcontrol.com.ua/catalog/company_details/45315740/
"""
                content = re.sub(
                    r"^(# [^\n]+\n+(?:[^#\n][^\n]*\n)*)",
                    rf"\1{identifier_block}",
                    content, count=1, flags=re.MULTILINE
                )
        else:
            samesa_pattern = r'("sameAs"\s*:\s*\[)([^\]]*?)(\])'
            m = re.search(samesa_pattern, content)
            if m:
                existing = m.group(2).strip()
                if wikidata_url in existing:
                    continue
                new_array = f'{m.group(1)}"{wikidata_url}"'
                if existing:
                    new_array += "," + existing
                new_array += m.group(3)
                content = content[:m.start()] + new_array + content[m.end():]
            elif '"@type":"Organization"' in content or "'@type':'Organization'" in content:
                sameas_insert = f',"sameAs":["{wikidata_url}"]'
                content = re.sub(
                    r'("@type"\s*:\s*"Organization")',
                    rf'\1{sameas_insert}',
                    content, count=1
                )
            else:
                print(f"⏭️  No Organization schema in {fp.relative_to(ROOT)}, skip")
                continue

        if content != original:
            fp.write_text(content, encoding="utf-8")
            print(f"✅ Patched: {fp.relative_to(ROOT)}")
            patched_count += 1

    print(f"\n📝 Total files patched: {patched_count}")
    return patched_count


def npm_build():
    banner("npm run build")
    result = subprocess.run(
        ["npm", "run", "build"],
        cwd=ROOT, capture_output=True, text=True, timeout=300
    )
    if result.returncode != 0:
        print(f"❌ Build failed:\n{result.stderr[-2000:]}")
        return False
    print(*(result.stdout.splitlines()[-5:]), sep="\n")
    print("✅ Build complete")
    return True


def verify_dist(q_number):
    banner("Verify dist/ HTML contains Wikidata URL")
    wikidata_url = f"wikidata.org/wiki/{q_number}"
    result = subprocess.run(
        ["grep", "-r", "-l", wikidata_url, str(ROOT / "dist")],
        capture_output=True, text=True
    )
    if result.returncode == 0 and result.stdout.strip():
        files = result.stdout.strip().split("\n")
        print(f"✅ Found Wikidata URL in {len(files)} HTML files")
        for f in files[:5]:
            print(f"   - {Path(f).relative_to(ROOT)}")
        return True
    print(f"⚠️  Wikidata URL not in dist/ HTML (may be OK if patches only in llms.txt)")
    return True


def git_commit_push(q_number):
    banner("git commit + push")
    status = subprocess.run(
        ["git", "status", "--short"],
        cwd=ROOT, capture_output=True, text=True
    ).stdout.strip()

    if not status:
        print("⏭️  No changes to commit")
        return True

    print("Changes to commit:")
    print(status)

    confirm = input(f"\n👉 Commit + push to cf-pages-migration with {q_number}? (y/n): ")
    if confirm.strip().lower() != "y":
        print("⏭️  Skipped push. Commit manually later.")
        return False

    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
    msg = f"""feat(seo): wire Wikidata {q_number} into Organization sameAs

Wikidata entity created manually via Special:NewItem (account not autoconfirmed,
QuickStatements blocked). 7 core statements added — see SUBMISSION-LOG.md.

Q-number: {q_number}
Entity URL: https://www.wikidata.org/wiki/{q_number}

Schema patches applied to:
- src/pages/ua/about.astro
- src/pages/poslugy.astro
- src/components/Base.astro
- public/llms.txt

Additional statements pending — will add via QuickStatements after 50+
manual edits accumulate autoconfirmed status (~4 days).

Patroller review window: 1-7 days. Monitor entity for community edits."""

    subprocess.run(["git", "commit", "-m", msg], cwd=ROOT, check=True)
    subprocess.run(["git", "push", "origin", "cf-pages-migration"], cwd=ROOT, check=True)
    print("✅ Pushed — CF Pages auto-deploy ~2-3 min")
    return True


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/wikidata-postsubmit.py Q<number>")
        print("       e.g., python3 scripts/wikidata-postsubmit.py Q123456789")
        sys.exit(1)

    q_number = sys.argv[1].strip()
    if not re.match(r"^Q\d{4,12}$", q_number):
        print(f"❌ Invalid Q-number format: {q_number}")
        print("   Expected: Q followed by 4-12 digits (e.g., Q123456789)")
        sys.exit(1)

    banner(f"POST-SUBMIT AUTOMATION — {q_number}", "═")
    print(f"Entity URL: https://www.wikidata.org/wiki/{q_number}")

    write_submission_log(q_number)
    patched = apply_sameas_patches(q_number)

    if patched == 0:
        print("⚠️  No patches applied (already patched or no Organization schema?)")
        sys.exit(0)

    if not npm_build():
        sys.exit(1)

    verify_dist(q_number)
    git_commit_push(q_number)

    banner(f"✅ DONE — {q_number} wired into site", "═")
    print(f"\nEntity:  https://www.wikidata.org/wiki/{q_number}")
    print(f"Log:     docs/wikidata/SUBMISSION-LOG.md")
    print(f"\nNext (async):")
    print(f"  - Patroller review 1-7 days — monitor entity page")
    print(f"  - After 50 manual edits → autoconfirmed → add remaining statements")
    print(f"  - Google Rich Results check after CF Pages deploy (~3 min)")


if __name__ == "__main__":
    main()
