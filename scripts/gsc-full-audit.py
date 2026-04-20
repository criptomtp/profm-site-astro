#!/usr/bin/env python3
"""Pull ALL site pages + their top queries for 90d GSC window.
Output: docs/gsc/full-pages.json + full-pages.csv
Also: docs/gsc/full-queries.json (top 500 queries site-wide)
"""
import os, sys, json, csv, time
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(SCRIPT_DIR, 'gsc_token.json')
OUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'docs', 'gsc')
SITE = 'sc-domain:fulfillmentmtp.com.ua'
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

def load_creds():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE, 'w') as f:
            f.write(creds.to_json())
    return creds

def q(service, body):
    return service.searchanalytics().query(siteUrl=SITE, body=body).execute()

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    creds = load_creds()
    service = build('searchconsole', 'v1', credentials=creds)
    end = datetime.now().strftime('%Y-%m-%d')
    start = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')

    print(f'[1/3] Pages 90d...')
    pages = q(service, {'startDate':start,'endDate':end,'dimensions':['page'],'rowLimit':1000})
    pages_rows = pages.get('rows', [])
    print(f'  -> {len(pages_rows)} pages')

    print(f'[2/3] Top queries site-wide...')
    queries = q(service, {'startDate':start,'endDate':end,'dimensions':['query'],'rowLimit':500})
    qrows = queries.get('rows', [])
    print(f'  -> {len(qrows)} queries')

    print(f'[3/3] Top queries per page (top 50 pages only)...')
    top_pages = sorted(pages_rows, key=lambda r: r.get('impressions',0), reverse=True)[:50]
    page_queries = {}
    for i, p in enumerate(top_pages):
        url = p['keys'][0]
        try:
            pq = q(service, {'startDate':start,'endDate':end,'dimensions':['query'],
                'dimensionFilterGroups':[{'filters':[{'dimension':'page','operator':'equals','expression':url}]}],
                'rowLimit':10})
            page_queries[url] = [{'query':r['keys'][0],'clicks':r.get('clicks',0),'impressions':r.get('impressions',0),
                'ctr':round(r.get('ctr',0)*100,2),'position':round(r.get('position',0),1)} for r in pq.get('rows',[])]
            print(f'  [{i+1}/50] {url[:70]} -> {len(page_queries[url])}q')
        except Exception as e:
            print(f'  [{i+1}/50] ERR {e}', file=sys.stderr)
            page_queries[url] = []
        time.sleep(0.1)

    pages_out = []
    for r in pages_rows:
        url = r['keys'][0]
        pages_out.append({
            'url': url,
            'clicks_90d': r.get('clicks',0),
            'impressions_90d': r.get('impressions',0),
            'ctr_pct': round(r.get('ctr',0)*100,2),
            'avg_position': round(r.get('position',0),1),
            'top_queries': page_queries.get(url, [])
        })
    pages_out.sort(key=lambda x: x['impressions_90d'], reverse=True)

    queries_out = [{
        'query': r['keys'][0],
        'clicks_90d': r.get('clicks',0),
        'impressions_90d': r.get('impressions',0),
        'ctr_pct': round(r.get('ctr',0)*100,2),
        'avg_position': round(r.get('position',0),1),
    } for r in qrows]
    queries_out.sort(key=lambda x: x['impressions_90d'], reverse=True)

    with open(os.path.join(OUT_DIR,'full-pages.json'),'w',encoding='utf-8') as f:
        json.dump({'total':len(pages_out),'period_days':90,'generated_at':datetime.now().isoformat(),
                   'pages':pages_out}, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUT_DIR,'full-queries.json'),'w',encoding='utf-8') as f:
        json.dump({'total':len(queries_out),'period_days':90,'generated_at':datetime.now().isoformat(),
                   'queries':queries_out}, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUT_DIR,'full-pages.csv'),'w',newline='',encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['url','clicks_90d','impressions_90d','ctr_pct','avg_position','top_queries'])
        for p in pages_out:
            w.writerow([p['url'],p['clicks_90d'],p['impressions_90d'],p['ctr_pct'],p['avg_position'],
                        ' | '.join(f"{q['query']}({q['impressions']})" for q in p['top_queries'])])
    with open(os.path.join(OUT_DIR,'full-queries.csv'),'w',newline='',encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['query','clicks_90d','impressions_90d','ctr_pct','avg_position'])
        for x in queries_out:
            w.writerow([x['query'],x['clicks_90d'],x['impressions_90d'],x['ctr_pct'],x['avg_position']])

    total_clk = sum(p['clicks_90d'] for p in pages_out)
    total_imp = sum(p['impressions_90d'] for p in pages_out)
    print(f'\nSUMMARY: {len(pages_out)} pages, {len(queries_out)} queries, {total_clk:.0f} clicks, {total_imp:.0f} impressions (90d)')
    print(f'Output: {OUT_DIR}/full-pages.{json,csv} + full-queries.{json,csv}')

if __name__ == '__main__':
    main()
