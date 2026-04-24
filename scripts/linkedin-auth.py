#!/usr/bin/env python3
"""
One-time LinkedIn authenticator for Company Page automation.

Run: python3 scripts/linkedin-auth.py

Opens a visible Chromium window pointed at linkedin.com.
You log in manually (email + password + 2FA / email code).
When feed loads, come back to terminal and press Enter.
Session saved to scripts/linkedin-session/state.json.

Re-run if later scripts report auth failure (LinkedIn cookies
usually live ~30 days if you don't log out elsewhere).
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SESSION_DIR = ROOT / 'scripts' / 'linkedin-session'
STATE_FILE = SESSION_DIR / 'state.json'
SESSION_DIR.mkdir(exist_ok=True)

PAGE_ID = '112973784'
COMPANY_URL = 'https://www.linkedin.com/company/mtpgroupfulfillment/'
ADMIN_URL = f'https://www.linkedin.com/company/{PAGE_ID}/admin/dashboard/'


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=['--disable-blink-features=AutomationControlled'],
        )
        context = browser.new_context(
            locale='uk-UA',
            viewport={'width': 1400, 'height': 900},
            user_agent=(
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/131.0.0.0 Safari/537.36'
            ),
        )
        page = context.new_page()
        page.goto('https://www.linkedin.com/login', wait_until='domcontentloaded')

        print('=' * 60)
        print('LINKEDIN AUTH — ручний крок')
        print('=' * 60)
        print('1. У вікні Chromium увійди в LinkedIn')
        print('   (той акаунт, що admin Company Page mtpgroupfulfillment)')
        print('2. Пройди 2FA / email-код якщо треба')
        print('3. Дочекайся стрічки feed (linkedin.com/feed/)')
        print('4. Переконайся що можеш перейти у Company Page:')
        print(f'   {COMPANY_URL}')
        print('5. Повернись у термінал і натисни Enter')
        print('=' * 60)
        input('Натисни Enter коли залогінишся...')

        print(f'Current URL: {page.url}')

        # quick smoke-test: try to reach company admin view
        try:
            page.goto(ADMIN_URL, wait_until='domcontentloaded', timeout=15000)
            print(f'Admin URL after redirect: {page.url}')
            if 'login' in page.url or 'authwall' in page.url:
                print('WARNING: redirected to login — auth не прийнявся')
                sys.exit(1)
        except Exception as e:
            print(f'WARNING: admin probe failed ({e}) — все одно зберігаю state')

        context.storage_state(path=str(STATE_FILE))
        print(f'OK: session saved to {STATE_FILE}')
        print(f'Size: {STATE_FILE.stat().st_size} bytes')

        browser.close()


if __name__ == '__main__':
    main()
