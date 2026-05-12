#!/usr/bin/env python3
"""
wikidata-submit.py — End-to-end Wikidata entity submission for MTP Group Fulfillment.

Workflow:
  1. Opens browser at QuickStatements
  2. Waits for you to login + authorize OAuth (you press ENTER in terminal when done)
  3. Pastes batch from docs/wikidata/quickstatements.txt
  4. Runs the batch
  5. Captures the created Q-number from logs / Special:RecentChanges
  6. Writes /docs/wikidata/SUBMISSION-LOG.md
  7. Applies sameAs patches to JSON-LD on 4 files
  8. Runs npm run build
  9. Verifies dist/ HTML contains the Wikidata URL
 10. Commits + pushes (you confirm before push)

Usage:
    pip install playwright
    python3 -m playwright install chromium
    python3 scripts/wikidata-submit.py

Or if Playwright already installed:
    python3 scripts/wikidata-submit.py
"""

import re
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("❌ Playwright not installed. Run:")
    print("   pip install playwright && python3 -m playwright install chromium")
    sys.exit(1)

ROOT = Path(__file__).parent.parent
BATCH_FILE = ROOT / "docs" / "wikidata" / "quickstatements.txt"
LOG_FILE = ROOT / "docs" / "wikidata" / "SUBMISSION-LOG.md"
QS_URL = "https://quickstatements.toolforge.org/#/batch"


def banner(msg, char="="):
    print(f"\n{char * 70}\n{msg}\n{char * 70}")


def read_batch():
    """Read batch file, strip comments."""
    raw = BATCH_FILE.read_text(encoding="utf-8")
    lines = [ln for ln in raw.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    return "\n".join(lines)


def wait_for_user(prompt):
    """Block until user presses ENTER."""
    print(f"\n👉 {prompt}")
    input("   Press ENTER to continue...")


def run_quickstatements(page):
    """Submit batch via QuickStatements V2 UI."""
    batch = read_batch()
    print(f"\n📋 Batch loaded: {len(batch.splitlines())} statements")

    banner("STEP 1: open QuickStatements")
    page.goto(QS_URL, wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    print(f"\n🌐 Opened: {page.url}")

    # Check if already logged in (look for username in header)
    page_text = page.content()
    if "Login" in page_text and "Logout" not in page_text and "user" not in page_text.lower():
        print("\n📝 You need to login first:")
        print("   1. Click the login link/button in the browser")
        print("   2. Authorize OAuth handshake on wikidata.org")
        wait_for_user("Logged in + back at QuickStatements? Press ENTER.")
    else:
        print("✅ Already logged in (detected user session)")

    banner("STEP 2: open new batch + paste content")

    # V2 UI: click "Новий пакет" / "New batch" button first
    print("🔘 Clicking 'New batch' / 'Новий пакет' button...")
    new_batch_selectors = [
        'button:has-text("Новий пакет")',
        'button:has-text("New batch")',
        'a:has-text("Новий пакет")',
        'a:has-text("New batch")',
        '[href*="/batch"]:has-text("Новий")',
        '[href*="/batch"]:has-text("New")',
    ]
    clicked_new = False
    for sel in new_batch_selectors:
        try:
            el = page.query_selector(sel)
            if el and el.is_visible():
                el.click()
                clicked_new = True
                print(f"   ✅ Clicked using selector: {sel}")
                break
        except Exception:
            continue

    if not clicked_new:
        # Try direct URL approach
        print("⚠️  Auto-click failed, navigating directly to new batch URL...")
        page.goto("https://quickstatements.toolforge.org/#/batch/new", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)

    # Wait for textarea to appear
    print("⏳ Waiting for batch input textarea...")
    page.wait_for_timeout(2000)

    textarea_selectors = [
        'textarea#batch_input',
        'textarea[name="batch"]',
        'textarea[placeholder*="CREATE"]',
        'textarea[placeholder*="command"]',
        'textarea',
    ]
    textarea = None
    for sel in textarea_selectors:
        try:
            textarea = page.wait_for_selector(sel, timeout=8000, state="visible")
            if textarea:
                print(f"   ✅ Found textarea: {sel}")
                break
        except PlaywrightTimeout:
            continue

    if not textarea:
        print("\n❌ Could not find batch textarea. Saving screenshot for debug.")
        page.screenshot(path=str(ROOT / "docs" / "wikidata" / "debug-qs-no-textarea.png"))
        print(f"   Screenshot: docs/wikidata/debug-qs-no-textarea.png")
        print("\n⚠️  Manual fallback: paste this content yourself into the textarea:")
        print("─" * 70)
        print(batch[:500] + "...")
        print("─" * 70)
        wait_for_user("Pasted manually and clicked Import? Press ENTER.")
    else:
        print("✏️  Filling textarea with batch content...")
        textarea.fill(batch)
        page.wait_for_timeout(1000)

        # Look for "V1" format toggle if exists
        print("🔘 Checking for V1 format toggle...")
        v1_toggle_selectors = [
            'input[type=radio][value="v1"]',
            'label:has-text("V1")',
            'button:has-text("V1")',
        ]
        for sel in v1_toggle_selectors:
            try:
                el = page.query_selector(sel)
                if el and el.is_visible():
                    el.click()
                    print(f"   ✅ Selected V1 format")
                    page.wait_for_timeout(500)
                    break
            except Exception:
                continue

        # Click Import V1 / Import / Run button
        print("🔘 Clicking 'Import V1 commands' / 'Імпортувати' button...")
        import_selectors = [
            'button:has-text("Import V1")',
            'button:has-text("Import")',
            'button:has-text("Імпортувати")',
            'button:has-text("Виконати")',
            'button:has-text("Run")',
            'input[type=submit][value*="V1"]',
            'input[type=submit][value*="Import"]',
            'input[type=submit][value*="Run"]',
        ]
        clicked_import = False
        for sel in import_selectors:
            try:
                btn = page.query_selector(sel)
                if btn and btn.is_visible():
                    btn.click()
                    clicked_import = True
                    print(f"   ✅ Clicked: {sel}")
                    break
            except Exception:
                continue

        if not clicked_import:
            print("⚠️  Could not auto-click Import. Pausing for manual click.")
            wait_for_user("Click 'Import V1 commands' / 'Імпортувати' manually, then ENTER.")

    # Wait for preview / running state
    print("\n⏳ Waiting for preview or running state...")
    page.wait_for_timeout(3000)

    # Take screenshot of current state for user reference
    page.screenshot(path=str(ROOT / "docs" / "wikidata" / "debug-qs-preview.png"))

    print("\n👀 PREVIEW REVIEW:")
    print("   In the browser, you should see preview with statements like:")
    print("   - CREATE")
    print("   - LAST P3125 = 45315740")
    print("   - LAST P31 = Q4830453")
    print("   - LAST P159 = Q158910 (Boryspil)")
    print("\n   If preview is wrong, press Ctrl+C now.")

    wait_for_user("Preview correct? Press ENTER to RUN the batch (or it may have already started).")

    # Try clicking Run button if there's a separate Run step
    print("\n🚀 Looking for 'Run' button (some V2 flows auto-run)...")
    run_selectors = [
        'button:has-text("Run")',
        'button:has-text("Виконати")',
        'a:has-text("Run")',
        'input[type=submit][value*="Run"]',
    ]
    for sel in run_selectors:
        try:
            btn = page.query_selector(sel)
            if btn and btn.is_visible():
                btn.click()
                print(f"   ✅ Clicked Run: {sel}")
                break
        except Exception:
            continue

    # Wait for batch to complete
    print("\n⏳ Waiting for batch execution (typically 30-90 sec)...")
    print("   Watch the browser for status updates / Q-number appearing.")

    wait_for_user("Batch finished (DONE state visible)? Press ENTER to capture Q-number.")

    return capture_q_number(page)


def capture_q_number(page):
    """Try to extract Q-number from page content or via Special:RecentChanges."""
    banner("STEP 3: capture Q-number")

    # Try to find Q-number in current page content
    content = page.content()
    matches = re.findall(r"\bQ(\d{6,12})\b", content)
    if matches:
        # Filter out P-numbers and known reference Q-numbers from our batch
        known_refs = {"4830453", "43229", "1473552", "212", "158910", "170036",
                      "98834261", "23048710"}
        new_qs = [q for q in matches if q not in known_refs]
        if new_qs:
            # Most recent/largest Q-number is likely ours
            q = max(set(new_qs), key=int)
            print(f"\n✅ Detected new entity: Q{q}")
            confirmed = input(f"   Is Q{q} the correct number? (y/n/manual): ").strip().lower()
            if confirmed == "y":
                return f"Q{q}"
            elif confirmed == "manual":
                manual_q = input("   Enter Q-number manually (e.g., Q123456789): ").strip()
                return manual_q

    # Fallback — navigate to Special:RecentChanges
    print("\n🔍 Auto-detection unclear. Opening Special:RecentChanges...")
    page.goto("https://www.wikidata.org/wiki/Special:RecentChanges?hideanons=1&limit=50",
              wait_until="domcontentloaded")
    print("\n👀 In browser: find your most recent 'created Q...' edit at top of list")
    manual_q = input("Enter Q-number you see (e.g., Q123456789): ").strip()
    if not manual_q.startswith("Q") or not manual_q[1:].isdigit():
        print(f"❌ Invalid Q-number format: {manual_q}")
        return None
    return manual_q


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
- Special:RecentChanges (filter by your username): https://www.wikidata.org/wiki/Special:RecentChanges
- Google Rich Results test (after deploy): https://search.google.com/test/rich-results?url=https%3A%2F%2Fwww.fulfillmentmtp.com.ua%2Fua%2Fabout%2F

## What was submitted

See docs/wikidata/quickstatements.txt for full batch contents.
Key statements:
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
- P2397 = "@mtpgroup" (YouTube)

## Next steps

- Schema patches applied automatically — see commit log
- Monitor entity page for 7 days, watch for patroller edits/concerns
- If delete-nominated: accumulate press coverage before re-submit
"""
    LOG_FILE.write_text(log, encoding="utf-8")
    print(f"✅ Submission log written: {LOG_FILE}")


def apply_sameas_patches(q_number):
    """Patch JSON-LD Organization schema in 4 files."""
    banner("STEP 4: apply sameAs patches")
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

        # Skip if already patched
        if wikidata_url in content:
            print(f"⏭️  Already patched: {fp.relative_to(ROOT)}")
            continue

        original = content

        # Strategy 1: file is llms.txt — append to top
        if fp.name == "llms.txt":
            if "## Verifiable identifiers" in content:
                # Insert wikidata link into existing section
                content = re.sub(
                    r"(## Verifiable identifiers[^\n]*\n)",
                    rf"\1- Wikidata entity: {wikidata_url}\n",
                    content, count=1
                )
            else:
                # Insert near top after first ## section
                identifier_block = f"""
## Verifiable identifiers
- EDRPOU (Ukraine state register): 45315740
- Wikidata entity: {wikidata_url}
- YouControl profile: https://youcontrol.com.ua/catalog/company_details/45315740/
"""
                # Insert after first top-level heading
                content = re.sub(
                    r"^(# [^\n]+\n+(?:[^#\n][^\n]*\n)*)",
                    rf"\1{identifier_block}",
                    content, count=1, flags=re.MULTILINE
                )

        else:
            # Astro file with JSON-LD Organization schema in const schemaJson
            # Strategy: find "@type":"Organization" block, then add/update "sameAs"
            if '"@type":"Organization"' in content or "'@type':'Organization'" in content:
                # Try to find sameAs array and add Wikidata URL to it
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
                else:
                    # No sameAs yet — inject after "@type":"Organization"
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
    """Run npm run build."""
    banner("STEP 5: npm run build")
    result = subprocess.run(
        ["npm", "run", "build"],
        cwd=ROOT, capture_output=True, text=True, timeout=300
    )
    if result.returncode != 0:
        print(f"❌ Build failed:\n{result.stderr[-2000:]}")
        return False
    # Show last few lines of output
    print(result.stdout.splitlines()[-5:])
    print("✅ Build complete")
    return True


def verify_dist(q_number):
    """Grep dist/ for Wikidata URL."""
    banner("STEP 6: verify dist/ contains Wikidata URL")
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
        print(f"❌ Wikidata URL not in dist/. Build may not have picked up patches.")
        return False


def git_commit_push(q_number):
    """Commit + push to remote."""
    banner("STEP 7: git commit + push")

    # Check there are changes
    status = subprocess.run(
        ["git", "status", "--short"],
        cwd=ROOT, capture_output=True, text=True
    ).stdout.strip()

    if not status:
        print("⏭️  No changes to commit")
        return True

    print("Changes to commit:")
    print(status)

    confirm = input(f"\n👉 Commit + push to cf-pages-migration with Q-number {q_number}? (y/n): ")
    if confirm.strip().lower() != "y":
        print("⏭️  Skipped git push. You can commit manually later.")
        return False

    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
    msg = f"""feat(seo): wire Wikidata {q_number} into Organization sameAs

Wikidata entity submitted via QuickStatements automated batch.
Q-number: {q_number}
Entity URL: https://www.wikidata.org/wiki/{q_number}

Schema patches applied to:
- src/pages/ua/about.astro
- src/pages/poslugy.astro
- src/components/Base.astro
- public/llms.txt

Build verified — Wikidata URL emitted in dist/ HTML.

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
    print(f"\nThis will:")
    print(f"  1. Open QuickStatements in a browser")
    print(f"  2. Wait for you to login + authorize OAuth (~30 sec)")
    print(f"  3. Auto-submit the batch")
    print(f"  4. Capture Q-number")
    print(f"  5. Apply patches to 4 files")
    print(f"  6. Build + verify")
    print(f"  7. Commit + push (with your confirmation)")

    if input("\n👉 Start? (y/n): ").strip().lower() != "y":
        print("Aborted.")
        sys.exit(0)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context()
        page = context.new_page()

        try:
            q_number = run_quickstatements(page)
            if not q_number:
                print("❌ No Q-number obtained. Aborting.")
                return

            print(f"\n🎉 Q-number obtained: {q_number}")
            print(f"   Entity URL: https://www.wikidata.org/wiki/{q_number}")

            write_submission_log(q_number)
            patched = apply_sameas_patches(q_number)

            if patched == 0:
                print("⚠️  No patches applied. Stopping before build.")
                return

            if not npm_build():
                print("⚠️  Build failed. Patches in place but not deployed.")
                return

            if not verify_dist(q_number):
                print("⚠️  Wikidata URL not in dist. Investigate before commit.")
                return

            git_commit_push(q_number)

            banner("✅ DONE — WIKIDATA SUBMISSION COMPLETE", "═")
            print(f"\nEntity:  https://www.wikidata.org/wiki/{q_number}")
            print(f"Log:     docs/wikidata/SUBMISSION-LOG.md")
            print(f"\nNext steps (async):")
            print(f"  - Patroller review 1-7 days — monitor entity page")
            print(f"  - Google Rich Results check after CF Pages deploys (~3 min):")
            print(f"    https://search.google.com/test/rich-results?url=https%3A%2F%2Fwww.fulfillmentmtp.com.ua%2Fua%2Fabout%2F")

        except KeyboardInterrupt:
            print("\n⛔ Aborted by user.")
        finally:
            input("\nPress ENTER to close browser...")
            browser.close()


if __name__ == "__main__":
    main()
