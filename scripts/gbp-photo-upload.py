#!/usr/bin/env python3
"""
GBP photo uploader — uploads photos from photo-queue.json to each branch
via Playwright. Tracks uploaded status in the queue so re-runs skip done.

Flow per branch:
  1. Navigate to profile admin URL
  2. Click "Фотографії" in the admin overlay
  3. Wait for photo management UI
  4. Dump HTML + screenshot for inspection
  5. Find "Додати фото" button
  6. On click, intercept filechooser and provide the next unuploaded photo
  7. Confirm upload, mark uploaded_{branch}=true in queue, move to next

Runs in headed mode so you can see progress and manually intervene if needed.
First run uploads 2 photos per branch as a test; re-run to continue.
"""
import json
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout

ROOT = Path(__file__).resolve().parent.parent
SESSION_FILE = ROOT / 'scripts' / 'gbp-session' / 'state.json'
QUEUE_FILE = ROOT / 'public' / 'images' / 'gbp' / 'photo-queue.json'
OUT_DIR = ROOT / 'docs' / 'gbp'
SCREEN_DIR = OUT_DIR / 'screenshots'

BATCH_PER_BRANCH = int((sys.argv[1] if len(sys.argv) > 1 else '2'))

BRANCHES = [
    {'code': 'MTPFUL1', 'key': 'uploaded_mtpful1',
     'url': 'https://business.google.com/n/15823209279675093443/profile?fid=6178464177003970104'},
    {'code': 'MTPFUL2', 'key': 'uploaded_mtpful2',
     'url': 'https://business.google.com/n/5471124292630647748/profile?fid=8491720345306679116'},
]


def pending_for(branch, queue):
    for p in queue['photos']:
        if p.get(branch['key']):
            continue
        if p['branch'] in ('BOTH', branch['code']):
            yield p


def click_photos_tab(page):
    """Click the Фотографії action button in admin overlay."""
    # Prefer nested elements over the containing section
    candidates = [
        'div[role="button"][aria-label="Фотографії"]',
        '[role="button"][aria-label="Фотографії"]',
        'button[aria-label="Фотографії"]',
        'span[aria-label="Фотографії"]',
        'a[aria-label="Фотографії"]',
        ':text("Фотографії")',
    ]
    for sel in candidates:
        try:
            el = page.locator(sel).first
            if el.count():
                el.scroll_into_view_if_needed(timeout=3000)
                el.click(timeout=4000)
                return sel
        except Exception:
            continue
    return None


def find_add_photo_trigger(page):
    """Find button that opens photo upload. Ukrainian label variants."""
    labels = [
        'Додати фото',
        'Додати фотографії',
        'Додати',
        'Завантажити фото',
        'Add photo',
        'Add photos',
        'Upload',
    ]
    for label in labels:
        for sel in [
            f'button[aria-label="{label}"]',
            f'[role="button"][aria-label="{label}"]',
            f'button:has-text("{label}")',
            f'div[role="button"]:has-text("{label}")',
        ]:
            try:
                el = page.locator(sel).first
                if el.count():
                    return el, sel
            except Exception:
                continue
    return None, None


def try_upload(page, branch, photo):
    """Try to upload a single photo. Returns (ok, note)."""
    # Expect file chooser on click
    trigger, sel = find_add_photo_trigger(page)
    if trigger is None:
        return False, 'no "Додати фото" trigger found'
    try:
        with page.expect_file_chooser(timeout=10000) as fc_info:
            trigger.click(timeout=4000)
        fc = fc_info.value
        fc.set_files(str(ROOT / photo['file']))
    except PwTimeout:
        # Try alternative: direct hidden file input
        inputs = page.locator('input[type="file"]')
        if inputs.count():
            try:
                inputs.first.set_input_files(str(ROOT / photo['file']))
            except Exception as e:
                return False, f'set_input_files failed: {e}'
        else:
            return False, 'no file chooser and no input[type=file]'
    except Exception as e:
        return False, f'click/filechooser error: {e}'

    # Wait for confirm button ("Опублікувати" / "Завантажити" / "Зберегти")
    page.wait_for_timeout(2500)
    page.screenshot(path=str(SCREEN_DIR / f'{branch["code"]}_upload_{int(time.time())}_prepost.png'), full_page=True)
    for label in ['Опублікувати', 'Завантажити', 'Зберегти', 'Post', 'Upload', 'Save']:
        try:
            btn = page.locator(f'button:has-text("{label}"), [role="button"][aria-label="{label}"]').first
            if btn.count():
                btn.click(timeout=4000)
                page.wait_for_timeout(3500)
                return True, f'confirmed via "{label}"'
        except Exception:
            continue
    return True, 'uploaded but no explicit confirm button found'


def main():
    if not SESSION_FILE.exists():
        print('Session missing — run scripts/gbp-auth.py')
        sys.exit(1)
    if not QUEUE_FILE.exists():
        print('Queue missing — run scripts/prepare-gbp-photos.py')
        sys.exit(1)

    queue = json.loads(QUEUE_FILE.read_text(encoding='utf-8'))

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context(
            storage_state=str(SESSION_FILE),
            locale='uk-UA',
            viewport={'width': 1400, 'height': 900},
        )
        page = context.new_page()

        for branch in BRANCHES:
            print(f'=== {branch["code"]} ===')
            page.goto(branch['url'], wait_until='domcontentloaded', timeout=45000)
            page.wait_for_timeout(4000)

            sel = click_photos_tab(page)
            print(f'  photos tab click: {sel}')
            page.wait_for_timeout(3500)
            page.screenshot(path=str(SCREEN_DIR / f'{branch["code"]}_photos_pane.png'), full_page=True)
            (OUT_DIR / f'_raw_{branch["code"]}_photos_pane.html').write_text(page.content(), encoding='utf-8')

            pending = list(pending_for(branch, queue))[:BATCH_PER_BRANCH]
            print(f'  to upload: {len(pending)} photo(s)')
            for photo in pending:
                print(f'  -> {photo["file"]}')
                ok, note = try_upload(page, branch, photo)
                print(f'     {"OK" if ok else "FAIL"}: {note}')
                if ok:
                    photo[branch['key']] = True
                    QUEUE_FILE.write_text(
                        json.dumps(queue, ensure_ascii=False, indent=2),
                        encoding='utf-8')
                # Return to photos pane
                page.goto(branch['url'], wait_until='domcontentloaded', timeout=45000)
                page.wait_for_timeout(3000)
                click_photos_tab(page)
                page.wait_for_timeout(3500)

        browser.close()

    print('Done. Queue saved.')


if __name__ == '__main__':
    main()
