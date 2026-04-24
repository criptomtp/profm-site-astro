#!/usr/bin/env python3
"""
Publish a post to LinkedIn Company Page (mtpgroupfulfillment).

Usage:
  python3 scripts/linkedin-post.py --text "post body" [--url "https://..."] [--image path.jpg] [--dry-run]
  python3 scripts/linkedin-post.py --from-file post.md

Flow:
  1. load session from scripts/linkedin-session/state.json
  2. goto Company Page admin feed
  3. click "Start a post" as page → paste text → (optional) attach link/image
  4. click Post

If the session is stale, script prints "AUTH_STALE" and exits non-zero.
Re-run scripts/linkedin-auth.py to refresh.
"""
import argparse
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / 'scripts' / 'linkedin-session' / 'state.json'
PAGE_ID = '112973784'  # MTP Group Fulfillment (numeric — required for admin URLs)
COMPANY_URL = f'https://www.linkedin.com/company/{PAGE_ID}/admin/page-posts/published/'


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('--text', help='post text (plain)')
    ap.add_argument('--url', help='optional link to attach (triggers preview card)')
    ap.add_argument('--image', help='optional local image path')
    ap.add_argument('--from-file', help='read post text from file (first line = ignored if starts with #)')
    ap.add_argument('--dry-run', action='store_true', help='open composer but do not click Post')
    ap.add_argument('--headless', action='store_true', help='run without UI')
    return ap.parse_args()


def load_text(args):
    if args.from_file:
        raw = Path(args.from_file).read_text(encoding='utf-8').strip()
        # strip single leading markdown title if present
        lines = raw.splitlines()
        if lines and lines[0].startswith('# '):
            lines = lines[1:]
        return '\n'.join(lines).strip()
    if args.text:
        return args.text
    print('ERROR: --text or --from-file required', file=sys.stderr)
    sys.exit(2)


def main():
    args = parse_args()
    text = load_text(args)

    if not STATE_FILE.exists():
        print(f'ERROR: {STATE_FILE} not found. Run scripts/linkedin-auth.py first.', file=sys.stderr)
        sys.exit(1)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=args.headless,
            args=['--disable-blink-features=AutomationControlled'],
        )
        context = browser.new_context(
            storage_state=str(STATE_FILE),
            locale='uk-UA',
            viewport={'width': 1400, 'height': 900},
            user_agent=(
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/131.0.0.0 Safari/537.36'
            ),
        )
        page = context.new_page()
        page.goto(COMPANY_URL, wait_until='domcontentloaded')
        time.sleep(2)

        if 'login' in page.url or 'authwall' in page.url:
            print('AUTH_STALE: session expired — re-run scripts/linkedin-auth.py', file=sys.stderr)
            browser.close()
            sys.exit(3)

        # click composer trigger — exact labels vary by locale
        # uk-UA: "Створити допис" (confirmed via linkedin-debug.py)
        start_selectors = [
            'button:has-text("Створити допис")',
            'button:has-text("Create a post")',
            'button:has-text("Start a post")',
            'button:has-text("Почати публікацію")',
            'button[aria-label*="Start a post" i]',
            'button[aria-label*="Create a post" i]',
            'button[aria-label*="Створити допис" i]',
            '[data-test-id="share-box-trigger"]',
        ]
        clicked = False
        for sel in start_selectors:
            try:
                btn = page.locator(sel).first
                if btn.is_visible(timeout=2000):
                    btn.click()
                    clicked = True
                    break
            except Exception:
                continue
        if not clicked:
            print('ERROR: could not find "Start a post" button. LinkedIn UI changed?', file=sys.stderr)
            page.screenshot(path=str(ROOT / 'scripts' / 'linkedin-session' / 'debug-no-start.png'))
            browser.close()
            sys.exit(4)

        time.sleep(2)

        # composer — contenteditable div
        editor = page.locator('div[role="textbox"][contenteditable="true"]').first
        editor.wait_for(state='visible', timeout=10000)
        editor.click()
        editor.type(text, delay=15)
        time.sleep(1)

        # optional image attach
        if args.image:
            img_path = Path(args.image)
            if not img_path.exists():
                print(f'WARNING: image {img_path} not found — skipping', file=sys.stderr)
            else:
                add_media_selectors = [
                    'button[aria-label*="media" i]',
                    'button[aria-label*="Add a photo" i]',
                    'button[aria-label*="Додати фото" i]',
                ]
                for sel in add_media_selectors:
                    try:
                        btn = page.locator(sel).first
                        if btn.is_visible(timeout=2000):
                            btn.click()
                            break
                    except Exception:
                        continue
                # file input appears
                file_input = page.locator('input[type="file"]').first
                file_input.set_input_files(str(img_path))
                time.sleep(3)
                # click "Done" inside media dialog
                for sel in ['button:has-text("Done")', 'button:has-text("Готово")']:
                    try:
                        b = page.locator(sel).first
                        if b.is_visible(timeout=2000):
                            b.click()
                            break
                    except Exception:
                        continue
                time.sleep(2)

        if args.dry_run:
            print('DRY-RUN: composer ready. Leaving window open 20s for inspection.')
            time.sleep(20)
            browser.close()
            return

        # click Post — locale variants
        post_selectors = [
            'button:has-text("Опублікувати")',  # uk
            'button:has-text("Post")',            # en
            'button:has-text("Опубликовать")',    # ru (fallback)
            'button[aria-label*="Опублікувати" i]',
            'button[aria-label*="Post" i]',
        ]
        posted = False
        for sel in post_selectors:
            try:
                btn = page.locator(sel).first
                if btn.is_visible(timeout=2000) and btn.is_enabled():
                    btn.click()
                    posted = True
                    break
            except Exception:
                continue

        if not posted:
            print('ERROR: could not find enabled Post button', file=sys.stderr)
            page.screenshot(path=str(ROOT / 'scripts' / 'linkedin-session' / 'debug-no-post.png'))
            browser.close()
            sys.exit(5)

        time.sleep(4)
        print('OK: post submitted')
        # save refreshed session (cookies may have rotated)
        context.storage_state(path=str(STATE_FILE))
        browser.close()


if __name__ == '__main__':
    main()
