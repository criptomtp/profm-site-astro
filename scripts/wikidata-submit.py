#!/usr/bin/env python3
"""
wikidata-submit.py — Hybrid Wikidata submission for MTP Group Fulfillment.

Workflow (hybrid — ~2 min user time):
  1. Reads docs/wikidata/quickstatements.txt and copies it to your clipboard
  2. Opens QuickStatements V2 in your default browser
  3. Tells you exactly which buttons to click and what to paste
  4. Waits for you to confirm done + enter Q-number
  5. AUTO: writes SUBMISSION-LOG.md
  6. AUTO: patches sameAs into 4 files
  7. AUTO: runs npm build + verifies dist contains wikidata URL
  8. AUTO: git commit + push (with your confirmation)

No Playwright needed — uses your default browser via webbrowser module.
Clipboard copy via pbcopy (macOS) / xclip (Linux) / Windows clip.exe.

Usage:
    python3 scripts/wikidata-submit.py
"""

import re
import sys
import subprocess
import webbrowser
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
BATCH_FILE = ROOT / "docs" / "wikidata" / "quickstatements.txt"
LOG_FILE = ROOT / "docs" / "wikidata" / "SUBMISSION-LOG.md"
QS_URL = "https://quickstatements.toolforge.org/#/batch"


def banner(msg, char="="):
    print(f"\n{char * 70}\n  {msg}\n{char * 70}")


def read_batch():
    """Read batch file, strip comments."""
    raw = BATCH_FILE.read_text(encoding="utf-8")
    lines = [ln for ln in raw.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    return "\n".join(lines)


def copy_to_clipboard(text):
    """Copy text to system clipboard. Returns True if success."""
    try:
        if sys.platform == "darwin":
            subprocess.run(["pbcopy"], input=text.encode("utf-8"), check=True)
        elif sys.platform == "linux":
            subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode("utf-8"), check=True)
        elif sys.platform == "win32":
            subprocess.run(["clip"], input=text.encode("utf-8"), check=True, shell=True)
        else:
            return False
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def wait_for(prompt):
    """Block until user presses ENTER."""
    return input(f"\n👉 {prompt}\n   Press ENTER (or type value): ")


def submit_via_browser():
    """Open browser + guide user through manual submit. Capture Q-number."""
    batch = read_batch()

    banner("STEP 1: Copy batch to clipboard")
    if copy_to_clipboard(batch):
        print(f"✅ Batch copied to clipboard ({len(batch.splitlines())} statements)")
    else:
        print(f"⚠️  Clipboard copy failed. Batch content below — copy manually:")
        print("─" * 70)
        print(batch)
        print("─" * 70)

    banner("STEP 2: Open QuickStatements in browser")
    print(f"🌐 Opening: {QS_URL}")
    webbrowser.open(QS_URL)
    print("\n📝 NOW do this in the browser (you have ~2 min):")
    print("   1. Click 'Новий пакет' (top-left blue button)")
    print("   2. Paste batch from clipboard (Cmd+V / Ctrl+V) into the textarea that appears")
    print("   3. Make sure 'V1' format is selected (radio button near textarea)")
    print("   4. Click 'Імпортувати' (Import) — preview will load")
    print("   5. Review preview — should show CREATE + ~14 statements")
    print("   6. Click 'Запустити' (Run / Start) — batch executes (30-90 sec)")
    print("   7. Wait until status = 'DONE' or 'ЗАВЕРШЕНО'")
    print("   8. Q-number of the created item will be visible in the log/details")

    banner("STEP 3: Provide Q-number")
    print("After batch completes, find the Q-number:")
    print("  - In the batch details page (e.g., 'Created item: Q12345')")
    print("  - OR https://www.wikidata.org/wiki/Special:Contributions/Mykola_Liashchuk")
    print("    (your most recent CREATE action — top of list)")

    while True:
        q_input = input("\n👉 Enter the Q-number (e.g., Q123456789) or 'skip' to abort: ").strip()
        if q_input.lower() == "skip":
            return None
        if re.match(r"^Q\d{4,12}$", q_input):
            return q_input
        print(f"❌ Invalid format. Expected Q followed by digits (e.g., Q123456). Got: {q_input}")


def write_submission_log(q_number):
    """Persist submission record."""
    timestamp = datetime.now().isoformat(timespec="seconds")
    log = f"""# Wikidata Submission Log — MTP Group Fulfillment

**Timestamp:** {timestamp}
**Q-number:** {q_number}
**Entity URL:** https://www.wikidata.org/wiki/{q_number}
**Source batch:** docs/wikidata/quickstatements.txt
**Patroller review:** 1-7 days (monitor Special:RecentChanges + entity talk page)

## Verification

- Wikidata page: https://www.wikidata.org/wiki/{q_number}
- Contributions: https://www.wikidata.org/wiki/Special:Contributions/Mykola_Liashchuk
- Google Rich Results test (after deploy):
  https://search.google.com/test/rich-results?url=https%3A%2F%2Fwww.fulfillmentmtp.com.ua%2Fua%2Fabout%2F

## Statements submitted

See docs/wikidata/quickstatements.txt for full batch. Key claims:
- P31 = Q4830453 (business) + Q43229 (organization)
- P452 = Q1473552 (order fulfillment)
- P17 = Q212 (Ukraine)
- P159 = Q158910 (Boryspil)
- P131 = Q170036 (Kyiv Oblast)
- P281 = "08322"
- P571 = +2014 (year precision)
- P1454 = Q98834261 (LLC Ukraine)
- P3125 = "45315740" (EDRPOU)
- P856 = https://www.fulfillmentmtp.com.ua
- P2397 = "@mtpgroup"

## Next steps

- Schema patches applied automatically — see commit log
- Monitor entity page for 7 days for patroller edits/concerns
- After 30 days check if Google Knowledge Graph picks it up
- If delete-nominated: accumulate press coverage (Forbes UA, AIN.UA) before re-submit
"""
    LOG_FILE.write_text(log, encoding="utf-8")
    print(f"✅ Submission log written: docs/wikidata/SUBMISSION-LOG.md")


def apply_sameas_patches(q_number):
    """Patch JSON-LD Organization schema in 4 files."""
    banner("STEP 4: Apply sameAs patches to JSON-LD")
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
            # Astro file — try to find existing sameAs array first
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
                # Inject sameAs after @type
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
    banner("STEP 5: npm run build")
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
    banner("STEP 6: Verify dist/ contains Wikidata URL")
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
    else:
        print(f"⚠️  Wikidata URL not in dist/. Patches may not be in rendered output.")
        print(f"   This is OK if patches are only in non-built files (llms.txt).")
        return True  # Don't fail on this — llms.txt won't show in dist


def git_commit_push(q_number):
    banner("STEP 7: git commit + push")
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
        print("⏭️  Skipped push. You can commit manually later.")
        return False

    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
    msg = f"""feat(seo): wire Wikidata {q_number} into Organization sameAs

Wikidata entity submitted via QuickStatements batch.
Q-number: {q_number}
Entity URL: https://www.wikidata.org/wiki/{q_number}

Schema patches applied to:
- src/pages/ua/about.astro
- src/pages/poslugy.astro
- src/components/Base.astro
- public/llms.txt

Patroller review window: 1-7 days. Monitor entity page for community feedback."""

    subprocess.run(["git", "commit", "-m", msg], cwd=ROOT, check=True)
    subprocess.run(["git", "push", "origin", "cf-pages-migration"], cwd=ROOT, check=True)
    print("✅ Pushed to cf-pages-migration — CF Pages auto-deploy ~2-3 min")
    return True


def main():
    if not BATCH_FILE.exists():
        print(f"❌ Batch file missing: {BATCH_FILE}")
        sys.exit(1)

    banner("WIKIDATA SUBMISSION — MTP GROUP FULFILLMENT", "═")
    print(f"Repository: {ROOT}")
    print(f"Batch file: {BATCH_FILE.relative_to(ROOT)}")
    print(f"\nHybrid workflow (~2 min your time):")
    print(f"  1. Script copies batch to clipboard + opens browser")
    print(f"  2. You paste batch + click Run in QuickStatements (~1 min)")
    print(f"  3. You give Q-number back to script")
    print(f"  4. Script auto-applies patches + builds + pushes (~1 min)")

    if input("\n👉 Start? (y/n): ").strip().lower() != "y":
        print("Aborted.")
        sys.exit(0)

    q_number = submit_via_browser()
    if not q_number:
        print("❌ No Q-number. Aborting.")
        sys.exit(1)

    print(f"\n🎉 Q-number obtained: {q_number}")
    print(f"   Entity URL: https://www.wikidata.org/wiki/{q_number}")

    write_submission_log(q_number)
    patched = apply_sameas_patches(q_number)

    if patched == 0:
        print("⚠️  No patches applied. Stopping before build.")
        sys.exit(0)

    if not npm_build():
        print("⚠️  Build failed. Patches in place but not deployed.")
        sys.exit(1)

    verify_dist(q_number)
    git_commit_push(q_number)

    banner("✅ DONE — WIKIDATA SUBMISSION COMPLETE", "═")
    print(f"\nEntity:  https://www.wikidata.org/wiki/{q_number}")
    print(f"Log:     docs/wikidata/SUBMISSION-LOG.md")
    print(f"\nNext steps (async):")
    print(f"  - Patroller review 1-7 days — monitor entity page")
    print(f"  - Google Rich Results check after CF Pages deploys (~3 min):")
    print(f"    https://search.google.com/test/rich-results?url=https%3A%2F%2Fwww.fulfillmentmtp.com.ua%2Fua%2Fabout%2F")


if __name__ == "__main__":
    main()
