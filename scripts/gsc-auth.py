#!/usr/bin/env python3
"""
GSC Auth + Core Web Vitals + Performance Report
Крок 1: Запусти цей скрипт — він відкриє браузер для авторизації
Крок 2: Після авторизації скрипт збереже токен і витягне дані
"""

import os
import json
import sys
from datetime import datetime, timedelta

SITE_URL = 'sc-domain:fulfillmentmtp.com.ua'
SITE_URL_ALT = 'https://www.fulfillmentmtp.com.ua/'
TOKEN_FILE = os.path.join(os.path.dirname(__file__), 'gsc_token.json')
CREDS_FILE = os.path.join(os.path.dirname(__file__), 'client_secret.json')

def check_creds():
    """Check if client_secret.json exists, if not — show instructions."""
    if os.path.exists(CREDS_FILE):
        return True

    print("""
╔══════════════════════════════════════════════════════════════╗
║  КРОК 0: Створити OAuth credentials (одноразово, 2 хвилини) ║
╚══════════════════════════════════════════════════════════════╝

1. Відкрий: https://console.cloud.google.com/apis/credentials
2. Вгорі натисни "CREATE CREDENTIALS" → "OAuth client ID"
3. Application type: "Desktop app"
4. Name: "GSC Script" (будь-яке)
5. Натисни "Create"
6. Натисни "DOWNLOAD JSON"
7. Збережи файл як:
   {creds_file}

Якщо API ще не увімкнене:
→ https://console.cloud.google.com/apis/library/searchconsole.googleapis.com
→ Натисни "Enable"

Після збереження файлу — запусти скрипт знову.
""".format(creds_file=CREDS_FILE))
    return False


def authenticate():
    """OAuth2 flow — opens browser, saves token."""
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.oauth2.credentials import Credentials

    SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        refreshed = False
        if creds and creds.expired and creds.refresh_token:
            try:
                from google.auth.transport.requests import Request
                creds.refresh(Request())
                refreshed = True
            except Exception as e:
                print(f'⚠️  Refresh token revoked/expired ({e.__class__.__name__}). Re-authorizing...')
                creds = None
        if not refreshed and not creds:
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
            creds = flow.run_local_server(port=8090, prompt='consent')

        with open(TOKEN_FILE, 'w') as f:
            f.write(creds.to_json())
        print(f'✅ Токен збережено: {TOKEN_FILE}')
    else:
        print('✅ Використовую збережений токен')

    return creds


def get_service(creds):
    from googleapiclient.discovery import build
    return build('searchconsole', 'v1', credentials=creds)


def list_sites(service):
    """List all sites in GSC to find the correct property."""
    result = service.sites().list().execute()
    sites = result.get('siteEntry', [])
    print(f'\n📋 Сайти в GSC ({len(sites)}):')
    for s in sites:
        print(f'  {s["permissionLevel"]:12s}  {s["siteUrl"]}')
    return [s['siteUrl'] for s in sites]


def performance_report(service, site_url):
    """Fetch last 28 days performance data — top queries and pages."""
    end = datetime.now().strftime('%Y-%m-%d')
    start = (datetime.now() - timedelta(days=28)).strftime('%Y-%m-%d')

    print(f'\n{"="*60}')
    print(f'📊 PERFORMANCE REPORT: {site_url}')
    print(f'   Період: {start} → {end}')
    print(f'{"="*60}')

    # Top queries
    req = {
        'startDate': start,
        'endDate': end,
        'dimensions': ['query'],
        'rowLimit': 20,
        'dimensionFilterGroups': []
    }
    try:
        resp = service.searchanalytics().query(siteUrl=site_url, body=req).execute()
        rows = resp.get('rows', [])
        print(f'\n🔍 ТОП-20 пошукових запитів:')
        print(f'  {"Запит":<45s} {"Кліки":>6s} {"Показ":>7s} {"CTR":>6s} {"Позиція":>8s}')
        print(f'  {"-"*45} {"-"*6} {"-"*7} {"-"*6} {"-"*8}')
        for r in rows:
            q = r['keys'][0][:44]
            print(f'  {q:<45s} {r["clicks"]:>6.0f} {r["impressions"]:>7.0f} {r["ctr"]*100:>5.1f}% {r["position"]:>7.1f}')
    except Exception as e:
        print(f'  ❌ Помилка запитів: {e}')

    # Top pages
    req['dimensions'] = ['page']
    req['rowLimit'] = 15
    try:
        resp = service.searchanalytics().query(siteUrl=site_url, body=req).execute()
        rows = resp.get('rows', [])
        print(f'\n📄 ТОП-15 сторінок:')
        print(f'  {"URL":<60s} {"Кліки":>6s} {"Показ":>7s} {"CTR":>6s} {"Позиція":>8s}')
        print(f'  {"-"*60} {"-"*6} {"-"*7} {"-"*6} {"-"*8}')
        for r in rows:
            url = r['keys'][0].replace('https://www.fulfillmentmtp.com.ua', '')[:59]
            print(f'  {url:<60s} {r["clicks"]:>6.0f} {r["impressions"]:>7.0f} {r["ctr"]*100:>5.1f}% {r["position"]:>7.1f}')
    except Exception as e:
        print(f'  ❌ Помилка сторінок: {e}')

    # Low CTR pages (high impressions, low clicks)
    req['dimensions'] = ['page']
    req['rowLimit'] = 50
    try:
        resp = service.searchanalytics().query(siteUrl=site_url, body=req).execute()
        rows = resp.get('rows', [])
        low_ctr = [r for r in rows if r['impressions'] > 100 and r['ctr'] < 0.02]
        low_ctr.sort(key=lambda x: x['impressions'], reverse=True)
        if low_ctr:
            print(f'\n⚠️  Сторінки з низьким CTR (>100 показів, <2% CTR):')
            print(f'  {"URL":<60s} {"Кліки":>6s} {"Показ":>7s} {"CTR":>6s} {"Позиція":>8s}')
            print(f'  {"-"*60} {"-"*6} {"-"*7} {"-"*6} {"-"*8}')
            for r in low_ctr[:10]:
                url = r['keys'][0].replace('https://www.fulfillmentmtp.com.ua', '')[:59]
                print(f'  {url:<60s} {r["clicks"]:>6.0f} {r["impressions"]:>7.0f} {r["ctr"]*100:>5.1f}% {r["position"]:>7.1f}')
    except Exception as e:
        print(f'  ❌ {e}')

    # Queries with position 1-10 but low CTR
    req['dimensions'] = ['query']
    req['rowLimit'] = 100
    try:
        resp = service.searchanalytics().query(siteUrl=site_url, body=req).execute()
        rows = resp.get('rows', [])
        fixable = [r for r in rows if r['position'] <= 10 and r['ctr'] < 0.05 and r['impressions'] > 50]
        fixable.sort(key=lambda x: x['impressions'], reverse=True)
        if fixable:
            print(f'\n🎯 Запити ТОП-10 з CTR <5% (потрібно покращити title/desc):')
            print(f'  {"Запит":<45s} {"Кліки":>6s} {"Показ":>7s} {"CTR":>6s} {"Позиція":>8s}')
            print(f'  {"-"*45} {"-"*6} {"-"*7} {"-"*6} {"-"*8}')
            for r in fixable[:10]:
                q = r['keys'][0][:44]
                print(f'  {q:<45s} {r["clicks"]:>6.0f} {r["impressions"]:>7.0f} {r["ctr"]*100:>5.1f}% {r["position"]:>7.1f}')
    except Exception as e:
        print(f'  ❌ {e}')

    # Device breakdown
    req['dimensions'] = ['device']
    req['rowLimit'] = 5
    try:
        resp = service.searchanalytics().query(siteUrl=site_url, body=req).execute()
        rows = resp.get('rows', [])
        print(f'\n📱 По пристроях:')
        for r in rows:
            dev = r['keys'][0]
            print(f'  {dev:<12s} кліки: {r["clicks"]:.0f}, показ: {r["impressions"]:.0f}, CTR: {r["ctr"]*100:.1f}%, позиція: {r["position"]:.1f}')
    except Exception as e:
        print(f'  ❌ {e}')


def url_inspection(service, site_url, urls):
    """Inspect specific URLs for indexing status."""
    print(f'\n{"="*60}')
    print(f'🔎 URL INSPECTION')
    print(f'{"="*60}')

    for url in urls:
        try:
            req = {'inspectionUrl': url, 'siteUrl': site_url}
            resp = service.urlInspection().index().inspect(body=req).execute()
            result = resp.get('inspectionResult', {})
            idx = result.get('indexStatusResult', {})
            mobile = result.get('mobileUsabilityResult', {})

            print(f'\n  📍 {url}')
            print(f'     Verdict: {idx.get("verdict", "?")}')
            print(f'     Coverage: {idx.get("coverageState", "?")}')
            print(f'     Indexing: {idx.get("indexingState", "?")}')
            print(f'     Last crawl: {idx.get("lastCrawlTime", "?")}')
            print(f'     Robots: {idx.get("robotsTxtState", "?")}')
            print(f'     Mobile: {mobile.get("verdict", "?")}')
        except Exception as e:
            print(f'\n  📍 {url}')
            print(f'     ❌ {e}')


def save_report(output):
    """Save report to file."""
    report_file = os.path.join(os.path.dirname(__file__), '..', 'docs', 'GSC_REPORT.md')
    os.makedirs(os.path.dirname(report_file), exist_ok=True)
    with open(report_file, 'w') as f:
        f.write(output)
    print(f'\n📁 Звіт збережено: {report_file}')


def main():
    if not check_creds():
        sys.exit(1)

    print('🔐 Авторизація в Google Search Console...')
    creds = authenticate()
    service = get_service(creds)

    # Find the right site property
    sites = list_sites(service)

    # Try both URL formats
    site_url = None
    for s in [SITE_URL, SITE_URL_ALT]:
        if s in sites:
            site_url = s
            break

    if not site_url and sites:
        site_url = sites[0]
        print(f'\n⚠️  Використовую перший доступний: {site_url}')
    elif not site_url:
        print('\n❌ Не знайдено жодного сайту в GSC!')
        sys.exit(1)

    print(f'\n✅ Використовую: {site_url}')

    # Performance report
    performance_report(service, site_url)

    # URL inspection for key pages
    inspect_urls = [
        'https://www.fulfillmentmtp.com.ua/',
        'https://www.fulfillmentmtp.com.ua/ru/',
        'https://www.fulfillmentmtp.com.ua/ua/fulfilment-dlya-kosmetyky/',
        'https://www.fulfillmentmtp.com.ua/ua/3pl-logistyka/',
        'https://www.fulfillmentmtp.com.ua/ua/paletne-zberigannya/',
    ]
    url_inspection(service, site_url, inspect_urls)

    print(f'\n{"="*60}')
    print('✅ ЗВІТ ЗАВЕРШЕНО')
    print(f'{"="*60}')
    print('\nСкопіюй вивід цього скрипта і вставь в чат — я дам аналіз.')


if __name__ == '__main__':
    main()
