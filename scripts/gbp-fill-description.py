#!/usr/bin/env python3
"""
GBP description + services filler via Playwright.

Approach:
  1. Navigate to each branch admin URL
  2. Try to find and click "Про компанію" / description edit entry point
  3. Fill description textarea with prepared text
  4. Save
  5. Move to services section — add each from list

If any step fails we stop, screenshot, and let user finish manually.
Headed mode so user can watch and intervene.
"""
import json
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
        'label': 'Щасливе',
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
        'label': 'Білогородка',
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

SERVICES = [
    'Приймання товару',
    'Зберігання',
    'Упаковка замовлень',
    'Відправка',
    'Обробка повернень',
    'Автодозвін клієнтам',
    'Штрихкодування товарів',
    'Фотофіксація товару',
    'Прийом платежів',
    'Доукомплектація',
]


def dump(page, branch, tag):
    ts = int(time.time())
    png = SCREEN_DIR / f'{branch["code"]}_{tag}_{ts}.png'
    html = OUT_DIR / f'_raw_{branch["code"]}_{tag}_{ts}.html'
    try:
        page.screenshot(path=str(png), full_page=True)
        html.write_text(page.content(), encoding='utf-8')
        print(f'     dump: {png.name}')
    except Exception as e:
        print(f'     dump failed: {e}')


def click_by_text(page, texts, timeout=5000):
    """Try to click element by visible text — many variants."""
    for text in texts:
        for sel in [
            f'[role="button"][aria-label="{text}"]',
            f'button[aria-label="{text}"]',
            f'div[role="button"]:has-text("{text}")',
            f'button:has-text("{text}")',
            f'a[aria-label="{text}"]',
            f'[data-value="{text}"]',
        ]:
            try:
                el = page.locator(sel).first
                if el.count():
                    el.scroll_into_view_if_needed(timeout=2000)
                    el.click(timeout=timeout)
                    return text, sel
            except Exception:
                continue
    return None, None


def fill_description(page, branch):
    """Find and fill description textarea."""
    print(f'  [{branch["code"]}] looking for description entry...')

    # Entry points that open the description editor
    entry_labels = [
        'Опис',
        'Про компанію',
        'Додайте опис',
        'Редагувати опис',
        'Редагувати профіль',
        'Edit profile',
        'Description',
        'About',
    ]
    hit, sel = click_by_text(page, entry_labels, timeout=4000)
    if not hit:
        print('     ❌ no description entry found')
        dump(page, branch, 'desc_entry_fail')
        return False
    print(f'     clicked: "{hit}"')
    page.wait_for_timeout(3000)
    dump(page, branch, 'desc_editor_open')

    # Find textarea
    textarea_sels = [
        'textarea[aria-label*="пис" i]',
        'textarea[aria-label*="description" i]',
        'textarea[aria-label*="company" i]',
        'textarea[aria-label*="company" i]',
        'textarea[maxlength="750"]',
        'textarea[maxlength="1000"]',
        'textarea',
    ]
    textarea = None
    for sel in textarea_sels:
        try:
            el = page.locator(sel).first
            if el.count() and el.is_visible(timeout=1000):
                textarea = el
                print(f'     found textarea: {sel}')
                break
        except Exception:
            continue

    if textarea is None:
        print('     ❌ no textarea visible')
        return False

    try:
        textarea.click(timeout=3000)
        page.keyboard.press('ControlOrMeta+A')
        page.wait_for_timeout(200)
        page.keyboard.press('Delete')
        page.wait_for_timeout(200)
        textarea.fill(branch['description'])
        page.wait_for_timeout(1500)
        dump(page, branch, 'desc_filled')
    except Exception as e:
        print(f'     ❌ fill failed: {e}')
        return False

    # Click Save
    save_labels = ['Зберегти', 'Save', 'Готово', 'Done']
    hit, _ = click_by_text(page, save_labels, timeout=4000)
    if not hit:
        print('     ⚠️  no Save button found — description may not persist')
        return False
    print(f'     ✅ saved via "{hit}"')
    page.wait_for_timeout(3000)
    return True


def main():
    if not SESSION_FILE.exists():
        print('Session missing — run scripts/gbp-auth.py')
        sys.exit(1)

    branches_to_run = sys.argv[1:] if len(sys.argv) > 1 else ['MTPFUL1', 'MTPFUL2']

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, slow_mo=400,
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
            print(f'\n=== {branch["code"]} ({branch["label"]}) ===')
            try:
                page.goto(branch['url'], wait_until='domcontentloaded', timeout=45000)
                page.wait_for_timeout(5000)
                dump(page, branch, 'landing')
            except Exception as e:
                print(f'  navigation failed: {e}')
                results[branch['code']] = 'nav_fail'
                continue

            ok = fill_description(page, branch)
            results[branch['code']] = 'description_ok' if ok else 'description_fail'

            # Brief pause between branches
            page.wait_for_timeout(2000)

        print('\n=== Summary ===')
        for code, status in results.items():
            marker = '✅' if 'ok' in status else '❌'
            print(f'  {marker} {code}: {status}')

        input('\nНатисни Enter щоб закрити браузер (перевір що все збереглось)...')
        browser.close()


if __name__ == '__main__':
    main()
