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
    ap.add_argument('--keep-open', type=int, default=0, help='keep browser open N seconds after first Post click (lets user complete visibility dialog manually)')
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

        # click Post — locale variants. LinkedIn has up to 3 stages:
        #   stage 1: composer "Далі/Next" (only if photo/poll attached)
        #   stage 2: composer "Опублікувати/Post"
        #   stage 3: visibility confirm modal — sometimes appears with second "Опублікувати"
        post_selectors = [
            'button:has-text("Опублікувати")',  # uk
            'button:has-text("Post")',            # en
            'button:has-text("Опубликовать")',    # ru (fallback)
            'button[aria-label*="Опублікувати" i]',
            'button[aria-label*="Post" i]',
        ]

        def screenshot(tag):
            try:
                page.screenshot(path=str(ROOT / 'scripts' / 'linkedin-session' / f'debug-{tag}.png'))
            except Exception:
                pass

        def click_first_visible(selectors, label, timeout_ms=2500):
            for sel in selectors:
                try:
                    btn = page.locator(sel).first
                    if btn.is_visible(timeout=timeout_ms) and btn.is_enabled():
                        btn.click()
                        print(f'  → clicked {label}: {sel}', file=sys.stderr)
                        return True
                except Exception:
                    continue
            return False

        # stage 2: main publish button
        screenshot('pre-post')
        if not click_first_visible(post_selectors, 'Post (stage 2)'):
            print('ERROR: could not find enabled Post button', file=sys.stderr)
            screenshot('no-post')
            if args.keep_open:
                print(f'KEEP-OPEN: leaving browser open {args.keep_open}s for manual completion', file=sys.stderr)
                time.sleep(args.keep_open)
            browser.close()
            sys.exit(5)

        # stage 3: "Налаштування дописів" (Post Settings) dialog appears.
        #   "Хто може побачити ваш допис?" → click "Будь-хто" radio → click "Готово"
        time.sleep(3)
        screenshot('after-post-1')

        settings_dialog = False
        try:
            heading = page.locator('h2:has-text("Налаштування дописів"), h2:has-text("Post settings")').first
            settings_dialog = heading.is_visible(timeout=1500)
        except Exception:
            pass

        if settings_dialog:
            print('  → "Налаштування дописів" dialog detected — selecting visibility', file=sys.stderr)
            # click "Будь-хто" / "Anyone" row to ensure radio is active and Done becomes enabled
            visibility_selectors = [
                'div[role="dialog"] button:has-text("Будь-хто")',
                'div[role="dialog"] button:has-text("Anyone")',
                'div[role="dialog"] label:has-text("Будь-хто")',
                'div[role="dialog"] label:has-text("Anyone")',
                'div[role="dialog"] [role="radio"]:has-text("Будь-хто")',
                'div[role="dialog"] [role="radio"]:has-text("Anyone")',
                # fallback: click the row containing "Будь-хто в LinkedIn чи поза ним"
                'div[role="dialog"] :has-text("Будь-хто в LinkedIn")',
            ]
            click_first_visible(visibility_selectors, 'visibility=Anyone', timeout_ms=2500)
            time.sleep(1)

            # now click "Готово"/"Done"
            done_selectors = [
                'div[role="dialog"] button:has-text("Готово"):not([disabled])',
                'div[role="dialog"] button:has-text("Done"):not([disabled])',
                'div[role="dialog"] button:has-text("Готово")',
                'div[role="dialog"] button:has-text("Done")',
            ]
            done_clicked = False
            # poll up to 8s for Done to enable
            for attempt in range(8):
                if click_first_visible(done_selectors, f'Done (attempt {attempt+1})', timeout_ms=1500):
                    done_clicked = True
                    break
                time.sleep(1)

            time.sleep(3)
            screenshot('after-post-2')

            if not done_clicked and args.keep_open:
                print(f'KEEP-OPEN: "Готово" stayed disabled. Browser open {args.keep_open}s — click manually.', file=sys.stderr)
                time.sleep(args.keep_open)
                browser.close()
                sys.exit(6)

            # 2026-05-12 LinkedIn UI update: "Готово" only closes Settings dialog,
            # does NOT publish. After dialog closes, click "Опублікувати" again.
            time.sleep(2)
            screenshot('after-done-click')
            print('  → settings dialog closed — clicking final Опублікувати', file=sys.stderr)
            final_post_selectors = [
                'button:has-text("Опублікувати"):not([disabled])',
                'button:has-text("Post"):not([disabled])',
                'div.share-actions button:has-text("Опублікувати")',
                'div.share-actions button:has-text("Post")',
            ]
            final_clicked = False
            for attempt in range(5):
                if click_first_visible(final_post_selectors, f'Final Опублікувати (attempt {attempt+1})', timeout_ms=2000):
                    final_clicked = True
                    break
                time.sleep(1)
            if not final_clicked:
                print('WARN: could not find final Опублікувати after Settings dialog', file=sys.stderr)
                screenshot('no-final-post')
                if args.keep_open:
                    print(f'KEEP-OPEN: browser open {args.keep_open}s — click "Опублікувати" manually', file=sys.stderr)
                    time.sleep(args.keep_open)
                    browser.close()
                    sys.exit(7)
            time.sleep(4)
            screenshot('final-post-clicked')

        print('OK: post submitted')
        if args.keep_open:
            print(f'KEEP-OPEN: leaving browser open {args.keep_open}s for verification', file=sys.stderr)
            time.sleep(args.keep_open)
        # save refreshed session (cookies may have rotated)
        context.storage_state(path=str(STATE_FILE))
        browser.close()


if __name__ == '__main__':
    main()
