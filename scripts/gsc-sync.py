#!/usr/bin/env python3
"""
GSC Sync — збирає дані з Google Search Console і зберігає в Redis через API.
Запускається щодня о 00:00 через cron або вручну.

Використання:
  python3 scripts/gsc-sync.py

Cron (щодня о 00:30):
  30 0 * * * cd /Users/nikolaj/My\ vibecode\ aplications/profm-site-astro && python3 scripts/gsc-sync.py >> /tmp/gsc-sync.log 2>&1
"""
import google.auth
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import json
import urllib.request

# Config
SITE_URL = 'https://fulfillmentmtp.com.ua/'
API_URL = 'https://www.fulfillmentmtp.com.ua/api/gsc/'
DAYS_BACK = 7  # aggregate last 7 days

# Target keywords to track
TARGET_KEYWORDS = [
    'фулфілмент', 'фулфилмент', 'fulfillment',
    'фулфілмент київ', 'фулфилмент киев', 'fulfillment kyiv',
    'фулфілмент для маркетплейсів', 'фулфилмент для маркетплейсов',
    'фулфілмент україна', 'фулфилмент украина',
    'фулфілмент ціна', 'фулфилмент цена',
    'mtp group', '3pl ukraine',
    'фулфілмент для інтернет магазинів',
    'фулфілмент склад', 'склад фулфілмент київ',
    'фулфілмент бориспіль',
]

# Target pages
TARGET_PAGES = [
    '/', '/ru/', '/en/',
    '/ua/fulfilment-dlya-marketpleysiv/',
    '/fulfilment-dlya-marketpleysov/',
    '/en/fulfillment-for-marketplaces/',
    '/ua/fulfilment-kyiv/',
    '/fulfilment-kiev/',
    '/en/fulfillment-kyiv/',
    '/ua/services/', '/services/', '/en/services/',
    '/ua/tsiny/', '/tsenu/', '/en/prices/',
    '/ua/about/', '/about/', '/en/about/',
]

def main():
    print(f'[{datetime.now().isoformat()}] GSC Sync starting...')

    # Auth
    creds, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/webmasters'])
    gsc = build('searchconsole', 'v1', credentials=creds)

    end = datetime.now().strftime('%Y-%m-%d')
    start = (datetime.now() - timedelta(days=DAYS_BACK)).strftime('%Y-%m-%d')

    # 1. Get top queries
    print(f'  Fetching queries ({start} to {end})...')
    query_data = gsc.searchanalytics().query(siteUrl=SITE_URL, body={
        'startDate': start, 'endDate': end,
        'dimensions': ['query'],
        'rowLimit': 50
    }).execute()

    queries = []
    for row in query_data.get('rows', []):
        queries.append({
            'q': row['keys'][0],
            'clicks': row['clicks'],
            'impressions': row['impressions'],
            'ctr': round(row['ctr'] * 100, 1),
            'position': round(row['position'], 1),
        })

    # 2. Get target keyword positions
    print('  Fetching target keywords...')
    for kw in TARGET_KEYWORDS:
        # Skip if already in top queries
        if any(q['q'] == kw for q in queries):
            continue
        try:
            kw_data = gsc.searchanalytics().query(siteUrl=SITE_URL, body={
                'startDate': start, 'endDate': end,
                'dimensions': ['query'],
                'dimensionFilterGroups': [{'filters': [{'dimension': 'query', 'operator': 'equals', 'expression': kw}]}],
                'rowLimit': 1
            }).execute()
            for row in kw_data.get('rows', []):
                queries.append({
                    'q': row['keys'][0],
                    'clicks': row['clicks'],
                    'impressions': row['impressions'],
                    'ctr': round(row['ctr'] * 100, 1),
                    'position': round(row['position'], 1),
                    'tracked': True,
                })
        except:
            pass

    # 3. Get page performance
    print('  Fetching pages...')
    page_data = gsc.searchanalytics().query(siteUrl=SITE_URL, body={
        'startDate': start, 'endDate': end,
        'dimensions': ['page'],
        'rowLimit': 100
    }).execute()

    pages = []
    indexed_pages = set()
    for row in page_data.get('rows', []):
        url = row['keys'][0].replace('https://fulfillmentmtp.com.ua', '').replace('https://www.fulfillmentmtp.com.ua', '')
        indexed_pages.add(url)
        pages.append({
            'url': url,
            'clicks': row['clicks'],
            'impressions': row['impressions'],
            'position': round(row['position'], 1),
        })

    # Mark target pages that aren't indexed yet
    for tp in TARGET_PAGES:
        if tp not in indexed_pages:
            pages.append({
                'url': tp,
                'clicks': 0,
                'impressions': 0,
                'position': 0,
                'notIndexed': True,
            })

    # 4. Push to Redis via API
    payload = {
        'date': end,
        'queries': queries,
        'pages': pages,
    }

    print(f'  Pushing {len(queries)} queries, {len(pages)} pages to Redis...')
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode(),
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            print(f'  OK! Snapshots in history: {result.get("snapshots", "?")}')
    except Exception as e:
        print(f'  ERROR pushing to API: {e}')
        # Fallback: save locally
        with open('/tmp/gsc-snapshot.json', 'w') as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print('  Saved locally to /tmp/gsc-snapshot.json')

    print(f'[{datetime.now().isoformat()}] Done!')

if __name__ == '__main__':
    main()
