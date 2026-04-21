#!/usr/bin/env python3
"""
GBP description filler v2 — works with iframe-based admin UI.

Key insight from v1 failure:
  Google admin UI lives in iframe inside SERP. Clicking "Опис" in the parent
  opens another iframe with the editor. The textarea we need is INSIDE that
  iframe — but v1 picked up the Google SEARCH BAR textarea instead.

v2 approach:
  1. Navigate to branch admin URL
  2. Before/after each click — enumerate all frames and print their URLs
  3. Click "Опис" entry via aria-label="Опис" (more specific than text match)
  4. Wait for new frame with /profile/edit or /info path
  5. Search textarea specifically INSIDE that frame
  6. Fill via keyboard (focus element, type) — more reliable than .fill() in iframes
"""
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout

ROOT = Path(__file__).resolve().parent.parent
SESSION_FILE = ROOT / 'scripts' / 'gbp-session' / 'state.json'
OUT_DIR = ROOT / 'docs' / 'gbp'
SCREEN_DIR = OUT_DIR / 'screenshots'
SCREEN_DIR.mkdir(parents=True, exist_ok=True)

BRANCHES = [
    {
        'code': 'MTPFUL1',
        'url': 'https://business.google.com/n/15823209279675093443/profile?fid=6178464177003970104',
        'description': (
            "MTP Group Fulfillment — 3PL оператор для інтернет-магазинів України. "
            "Склад 2 800 м² у Щасливому (Київська обл.) — адресне зберігання, "
            "сканування кожного товару, відправка 4 рази на день Новою Поштою, "
            "Укрпоштою і Meest. Працюємо з 2015 року, 150+ клієнтів, 60 000+ "
            "відправок на місяць. Інтеграції з Rozetka, Prom.ua, Horoshop, "
            "KeyCRM, WooCommerce, OpenCart, SalesDrive. Ціни від 18 грн/замовлення. "
            "Blackout-proof: 3 генератори + Starlink, без жодного простою з 2022. "
            "Підключення за 1–3 дні. Калькулятор на сайті."
        ),
    },
    {
        'code': 'MTPFUL2',
        'url': 'https://business.google.com/n/5471124292630647748/profile?fid=8491720345306679116',
        'description': (
            "MTP Group Fulfillment — другий склад 1 100 м² у Білогородці "
            "(Київська обл.). Розвантаження, зберігання, комплектація, відправка. "
            "Адресне зберігання + WMS-контроль залишків. 4 забори на день "
            "Новою Поштою, пряма інтеграція з Укрпоштою і Meest. Для клієнтів "
            "з маркетплейсами — sync у реальному часі з Rozetka, Prom, Kasta. "
            "10 років на ринку, 150+ активних інтернет-магазинів. Від 18 грн "
            "за замовлення. Мінімум 5 000 грн/міс, без комісії за подключення. "
            "Працюємо з 08:00 до 20:00, 7 днів на тиждень."
        ),
    },
]


def dump_frames(page, tag):
    print(f'  [{tag}] frames:')
    for i, f in enumerate(page.frames):
        url = f.url[:100] if f.url else '(no url)'
        print(f'    [{i}] {url}')


def shot(page, branch, tag):
    ts = int(time.time())
    try:
        page.screenshot(path=str(SCREEN_DIR / f'{branch["code"]}_v2_{tag}_{ts}.png'), full_page=True)
    except Exception:
        pass


def find_edit_frame(page):
    """Find the frame that contains the edit form (URL pattern /profile or /info)."""
    for f in page.frames:
        if not f.url:
            continue
        if '/local/business/' in f.url and any(x in f.url for x in ['/profile', '/info', '/edit', '/about']):
            return f
    return None


def fill_description(page, branch):
    print(f'\n=== {branch["code"]} ===')
    page.goto(branch['url'], wait_until='domcontentloaded', timeout=45000)
    page.wait_for_timeout(6000)
    shot(page, branch, 'landing')
    dump_frames(page, 'landing')

    # Try to click "Опис" — use aria-label selector first (more specific)
    clicked = False
    for sel in [
        'div[role="button"][aria-label="Опис"]',
        '[role="button"][aria-label="Опис"]',
        'button[aria-label="Опис"]',
    ]:
        try:
            el = page.locator(sel).first
            if el.count():
                el.scroll_into_view_if_needed(timeout=2000)
                el.click(timeout=4000)
                print(f'  ✅ clicked Опис via: {sel}')
                clicked = True
                break
        except Exception as e:
            print(f'  retry ({sel}): {type(e).__name__}')
            continue

    if not clicked:
        # Fallback: text match but filter by tile size (not search bar)
        try:
            page.get_by_role('button', name='Опис', exact=True).first.click(timeout=4000)
            print('  ✅ clicked Опис via role button')
            clicked = True
        except Exception as e:
            print(f'  ❌ all click attempts failed: {e}')
            return False

    page.wait_for_timeout(4000)
    shot(page, branch, 'after_click')
    dump_frames(page, 'after_click')

    # Search for textarea in each frame
    for i, frame in enumerate(page.frames):
        url = frame.url[:120] if frame.url else ''
        # Skip Google search frame
        if 'google.com/search' in url and 'local/business' not in url:
            continue
        try:
            # Try various textarea selectors within this frame
            for sel in [
                'textarea[aria-label*="пис" i]',
                'textarea[aria-label*="опис" i]',
                'textarea[aria-label*="description" i]',
                'textarea[maxlength="750"]',
                'textarea:not([name="q"]):not([aria-label="Пошук"])',
            ]:
                loc = frame.locator(sel).first
                if loc.count():
                    try:
                        if loc.is_visible(timeout=1500):
                            print(f'  🎯 textarea found in frame[{i}] ({url[:80]}) via {sel}')
                            loc.click(timeout=3000)
                            frame.page.keyboard.press('ControlOrMeta+A')
                            frame.page.keyboard.press('Delete')
                            loc.fill(branch['description'])
                            frame.page.wait_for_timeout(1500)
                            shot(page, branch, 'filled')
                            # Try save
                            for save_sel in [
                                'button[aria-label="Зберегти"]',
                                'div[role="button"][aria-label="Зберегти"]',
                                'button:has-text("Зберегти")',
                            ]:
                                try:
                                    sb = frame.locator(save_sel).first
                                    if sb.count():
                                        sb.click(timeout=3000)
                                        print(f'  💾 saved via {save_sel}')
                                        frame.page.wait_for_timeout(3000)
                                        shot(page, branch, 'saved')
                                        return True
                                except Exception:
                                    continue
                            print('  ⚠️  filled but save button not found')
                            return False
                    except Exception:
                        continue
        except Exception as e:
            print(f'  frame[{i}] scan error: {type(e).__name__}')

    print('  ❌ no description textarea in any frame')
    return False


def main():
    if not SESSION_FILE.exists():
        print('Session missing — run scripts/gbp-auth.py')
        sys.exit(1)

    branches_to_run = sys.argv[1:] if len(sys.argv) > 1 else ['MTPFUL1']

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, slow_mo=500,
            args=['--disable-blink-features=AutomationControlled'])
        context = browser.new_context(
            storage_state=str(SESSION_FILE),
            locale='uk-UA',
            viewport={'width': 1400, 'height': 900},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        )
        page = context.new_page()

        results = {}
        for branch in BRANCHES:
            if branch['code'] not in branches_to_run:
                continue
            try:
                ok = fill_description(page, branch)
                results[branch['code']] = 'OK' if ok else 'FAIL'
            except Exception as e:
                print(f'  EXCEPTION: {e}')
                results[branch['code']] = f'ERR: {type(e).__name__}'
            page.wait_for_timeout(2000)

        print('\n=== Summary ===')
        for c, s in results.items():
            print(f'  {c}: {s}')

        print('\nБраузер закриється через 10с — перевір результат...')
        page.wait_for_timeout(10000)
        browser.close()


if __name__ == '__main__':
    main()
