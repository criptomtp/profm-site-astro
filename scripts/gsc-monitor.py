#!/usr/bin/env python3
"""
GSC Monitor — автоматичний моніторинг позицій в Google Search Console
Використання: python3 scripts/gsc-monitor.py
"""
import google.auth
from googleapiclient.discovery import build
from datetime import datetime, timedelta

creds, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/webmasters'])
gsc = build('searchconsole', 'v1', credentials=creds)

SITE = 'https://fulfillmentmtp.com.ua/'
END = datetime.now().strftime('%Y-%m-%d')
START = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

# Our target pages
TARGET_PAGES = [
    '/ua/fulfilment-dlya-marketpleysiv/',
    '/fulfilment-dlya-marketpleysov/',
    '/en/fulfillment-for-marketplaces/',
    '/ua/fulfilment-kyiv/',
    '/fulfilment-kiev/',
    '/en/fulfillment-kyiv/',
    '/',
    '/ru/',
    '/en/',
]

# Target keywords
TARGET_KEYWORDS = [
    'фулфілмент', 'фулфилмент', 'fulfillment',
    'фулфілмент київ', 'фулфилмент киев', 'fulfillment kyiv',
    'фулфілмент для маркетплейсів', 'фулфилмент для маркетплейсов',
    'фулфілмент україна', 'фулфилмент украина',
    'фулфілмент ціна', 'фулфилмент цена',
    '3pl ukraine', 'fulfillment ukraine',
]

print(f'GSC Monitor — {START} to {END}')
print('=' * 90)

# 1. Top queries
print('\n📊 TOP 25 QUERIES')
print(f'{"Query":50s} {"Pos":>5s} {"Clicks":>7s} {"Impr":>7s} {"CTR":>6s}')
print('-' * 80)

data = gsc.searchanalytics().query(siteUrl=SITE, body={
    'startDate': START, 'endDate': END,
    'dimensions': ['query'],
    'rowLimit': 25
}).execute()

for row in data.get('rows', []):
    q = row['keys'][0]
    print(f'{q:50s} {row["position"]:5.1f} {row["clicks"]:7.0f} {row["impressions"]:7.0f} {row["ctr"]*100:5.1f}%')

# 2. Target keywords positions
print(f'\n🎯 TARGET KEYWORDS')
print(f'{"Keyword":50s} {"Pos":>5s} {"Clicks":>7s} {"Impr":>7s}')
print('-' * 75)

for kw in TARGET_KEYWORDS:
    data = gsc.searchanalytics().query(siteUrl=SITE, body={
        'startDate': START, 'endDate': END,
        'dimensions': ['query'],
        'dimensionFilterGroups': [{'filters': [{'dimension': 'query', 'operator': 'equals', 'expression': kw}]}],
        'rowLimit': 1
    }).execute()
    rows = data.get('rows', [])
    if rows:
        r = rows[0]
        print(f'{kw:50s} {r["position"]:5.1f} {r["clicks"]:7.0f} {r["impressions"]:7.0f}')
    else:
        print(f'{kw:50s}   —       —       —')

# 3. New pages performance
print(f'\n📄 NEW PAGES PERFORMANCE')
print(f'{"Page":60s} {"Pos":>5s} {"Clicks":>7s} {"Impr":>7s}')
print('-' * 85)

data = gsc.searchanalytics().query(siteUrl=SITE, body={
    'startDate': START, 'endDate': END,
    'dimensions': ['page'],
    'rowLimit': 50
}).execute()

page_data = {}
for row in data.get('rows', []):
    p = row['keys'][0].replace('https://fulfillmentmtp.com.ua', '').replace('https://www.fulfillmentmtp.com.ua', '')
    page_data[p] = row

for tp in TARGET_PAGES:
    if tp in page_data:
        r = page_data[tp]
        print(f'{tp:60s} {r["position"]:5.1f} {r["clicks"]:7.0f} {r["impressions"]:7.0f}')
    else:
        print(f'{tp:60s}   — (not indexed yet)')

print('\n✅ Done')
