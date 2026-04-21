#!/usr/bin/env python3
"""
One-time Google Business Profile authenticator.

Run: python3 scripts/gbp-auth.py

Opens a visible Chromium window pointed at business.google.com.
You log in manually (Google password + 2FA if required).
When you see the company list ("Компанії" — MTPFUL1 / MTPFUL2),
come back to the terminal and press Enter. The session (cookies +
localStorage) is saved to scripts/gbp-session/state.json so later
scripts can load it without re-authenticating.

Session expires when Google invalidates the cookies (usually weeks).
Re-run this script if later scripts report auth failure.
"""
import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SESSION_DIR = ROOT / 'scripts' / 'gbp-session'
STATE_FILE = SESSION_DIR / 'state.json'
SESSION_DIR.mkdir(exist_ok=True)


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
        page.goto('https://business.google.com/', wait_until='domcontentloaded')

        print('=' * 60)
        print('GBP AUTH — ручний крок')
        print('=' * 60)
        print('1. У відкритому вікні Chromium увійди в Google-акаунт')
        print('   (lnpromo392@gmail.com або той, що керує GBP)')
        print('2. Пройди 2FA якщо треба')
        print('3. Дочекайся списку "Компанії" (MTPFUL1 / MTPFUL2)')
        print('4. Повернись у термінал і натисни Enter')
        print('=' * 60)
        input('Натисни Enter коли залогінишся...')

        current_url = page.url
        print(f'Current URL: {current_url}')

        context.storage_state(path=str(STATE_FILE))
        print(f'OK: session saved to {STATE_FILE}')
        print(f'Size: {STATE_FILE.stat().st_size} bytes')

        browser.close()


if __name__ == '__main__':
    main()
