#!/usr/bin/env python3
"""
GA4 OAuth — одноразова авторизація для Google Analytics 4 Data API.

Використовує той самий client_secret.json що і GSC, але зберігає окремий
ga4_token.json зі scope analytics.readonly, щоб не зламати gsc_token.json.

Запусти один раз:
    python3 scripts/ga4-auth.py

У браузері кликни Approve → токен збережеться в scripts/ga4_token.json.
Після цього запускай scripts/ga4-lead-audit.py.
"""

import os
import sys

TOKEN_FILE = os.path.join(os.path.dirname(__file__), 'ga4_token.json')
CREDS_FILE = os.path.join(os.path.dirname(__file__), 'client_secret.json')

SCOPES = [
    'https://www.googleapis.com/auth/analytics.readonly',
]


def main():
    if not os.path.exists(CREDS_FILE):
        print(f'❌ Немає {CREDS_FILE}. Скопіюй з GSC setup (console.cloud.google.com).')
        sys.exit(1)

    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request

    creds = None
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except Exception:
            creds = None

    if creds and creds.valid:
        print('✅ Токен валідний. Нічого робити не треба.')
        return

    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            with open(TOKEN_FILE, 'w') as f:
                f.write(creds.to_json())
            print(f'✅ Токен оновлено: {TOKEN_FILE}')
            return
        except Exception as e:
            print(f'⚠️ Refresh не вдався ({e}), роблю повну авторизацію...')

    print('🔐 Відкриваю браузер для OAuth (scope: analytics.readonly)...')
    print('   Якщо побачиш попередження "unverified app" — натисни Advanced → Go to app.')
    flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
    creds = flow.run_local_server(port=8091, prompt='consent', access_type='offline')

    with open(TOKEN_FILE, 'w') as f:
        f.write(creds.to_json())
    print(f'✅ Токен збережено: {TOKEN_FILE}')
    print('\nТепер запусти:  python3 scripts/ga4-lead-audit.py')


if __name__ == '__main__':
    main()
