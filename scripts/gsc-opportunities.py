#!/usr/bin/env python3
"""Find striking-distance queries: pos 4-20 with impressions >= 50.
Output: docs/gsc/opportunities.json — ranked by (impressions / position) score.
"""
import os, sys, json, csv
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(SCRIPT_DIR, 'gsc_token.json')
OUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'docs', 'gsc')
SITE = 'sc-domain:fulfillmentmtp.com.ua'
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE,'w') as f: f.write(creds.to_json())
    service = build('searchconsole', 'v1', credentials=creds)

    end = datetime.now().strftime('%Y-%m-%d')
    start = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
    resp = service.searchanalytics().query(siteUrl=SITE, body={
        'startDate':start,'endDate':end,
        'dimensions':['query','page'],
        'rowLimit':5000
    }).execute()
    rows = resp.get('rows', [])
    print(f'Total query+page combos: {len(rows)}')

    opps = []
    for r in rows:
        qry, page = r['keys']
        imp = r.get('impressions',0)
        pos = r.get('position',0)
        clk = r.get('clicks',0)
        if pos >= 4 and pos <= 20 and imp >= 30:
            score = imp / max(pos,1)
            opps.append({
                'query': qry, 'page': page,
                'clicks_90d': clk, 'impressions_90d': imp,
                'avg_position': round(pos,1),
                'ctr_pct': round(r.get('ctr',0)*100,2),
                'opportunity_score': round(score,1)
            })
    opps.sort(key=lambda x: x['opportunity_score'], reverse=True)
    print(f'Striking-distance opps (pos 4-20, imp>=30): {len(opps)}')

    with open(os.path.join(OUT_DIR,'opportunities.json'),'w',encoding='utf-8') as f:
        json.dump({'total':len(opps),'generated_at':datetime.now().isoformat(),
                   'opportunities':opps[:200]}, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUT_DIR,'opportunities.csv'),'w',newline='',encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['query','page','clicks','impressions','avg_position','ctr_pct','opportunity_score'])
        for o in opps[:200]:
            w.writerow([o['query'],o['page'],o['clicks_90d'],o['impressions_90d'],
                        o['avg_position'],o['ctr_pct'],o['opportunity_score']])
    print(f'Top 20 opportunities:')
    for o in opps[:20]:
        print(f"  pos{o['avg_position']:>5} | {o['impressions_90d']:>4}imp | {o['clicks_90d']:>2}clk | {o['query'][:50]:<50} -> {o['page'][-60:]}")

if __name__ == '__main__':
    main()
