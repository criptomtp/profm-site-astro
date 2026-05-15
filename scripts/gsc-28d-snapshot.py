#!/usr/bin/env python3
"""Pull 28d GSC snapshot + diff vs existing 90d snapshot.
Output: docs/gsc/28d-pages.json, docs/gsc/28d-queries.json, docs/gsc/28d-opportunities.json
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
SCOPES = ['https://www.googleapis.com/auth/webmasters', 'https://www.googleapis.com/auth/indexing']

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
    start = (datetime.now() - timedelta(days=28)).strftime('%Y-%m-%d')
    print(f'Period: {start} -> {end}')

    # 1. Pages 28d
    print('[1/4] Pages 28d...')
    pages = q(service, {'startDate':start,'endDate':end,'dimensions':['page'],'rowLimit':1000})
    pages_rows = pages.get('rows', [])
    print(f'  -> {len(pages_rows)} pages')

    pages_out = [{
        'url': r['keys'][0],
        'clicks_28d': r.get('clicks',0),
        'impressions_28d': r.get('impressions',0),
        'ctr_pct': round(r.get('ctr',0)*100,2),
        'avg_position': round(r.get('position',0),1),
    } for r in pages_rows]
    pages_out.sort(key=lambda x: x['impressions_28d'], reverse=True)

    # 2. Queries 28d
    print('[2/4] Queries 28d...')
    queries = q(service, {'startDate':start,'endDate':end,'dimensions':['query'],'rowLimit':500})
    qrows = queries.get('rows', [])
    queries_out = [{
        'query': r['keys'][0],
        'clicks_28d': r.get('clicks',0),
        'impressions_28d': r.get('impressions',0),
        'ctr_pct': round(r.get('ctr',0)*100,2),
        'avg_position': round(r.get('position',0),1),
    } for r in qrows]
    queries_out.sort(key=lambda x: x['impressions_28d'], reverse=True)
    print(f'  -> {len(queries_out)} queries')

    # 3. Query+page combos 28d for opportunities + per-page diff
    print('[3/4] Query+page combos 28d...')
    qp = q(service, {'startDate':start,'endDate':end,'dimensions':['query','page'],'rowLimit':5000})
    qprows = qp.get('rows', [])
    print(f'  -> {len(qprows)} combos')
    combos = []
    opps = []
    for r in qprows:
        qry, page = r['keys']
        imp = r.get('impressions',0)
        pos = r.get('position',0)
        clk = r.get('clicks',0)
        ctr = r.get('ctr',0)*100
        combos.append({'query':qry,'page':page,'clicks':clk,'impressions':imp,
                       'ctr_pct':round(ctr,2),'avg_position':round(pos,1)})
        if pos >= 4 and pos <= 20 and imp >= 10:
            opps.append({'query':qry,'page':page,'clicks_28d':clk,'impressions_28d':imp,
                         'avg_position':round(pos,1),'ctr_pct':round(ctr,2),
                         'opportunity_score':round(imp/max(pos,1),1)})
    opps.sort(key=lambda x: x['opportunity_score'], reverse=True)

    # 4. Specific URL deep-dive: SLA tpost-redirected pages (track redirect impact)
    print('[4/4] SLA-redirected pages deep-dive...')
    sla_targets = [
        'https://www.fulfillmentmtp.com.ua/ua/blog/post/scho-take-sla-v-logistici/',
        'https://www.fulfillmentmtp.com.ua/ru/blog/post/chto-takoe-sla-v-logistike/',
        'https://www.fulfillmentmtp.com.ua/ua/blog/tpost/s7non1f0y1-scho-take-sla-v-logstits-chomu-tse-klyuc/',
        'https://www.fulfillmentmtp.com.ua/blog/tpost/pdjm77ogc1-chto-takoe-sla-v-logistike-i-pochemu-eto/',
    ]
    sla_data = {}
    for url in sla_targets:
        try:
            pq = q(service, {'startDate':start,'endDate':end,'dimensions':['query'],
                'dimensionFilterGroups':[{'filters':[{'dimension':'page','operator':'equals','expression':url}]}],
                'rowLimit':20})
            rows = pq.get('rows',[])
            sla_data[url] = {
                'total_imp_28d': sum(r.get('impressions',0) for r in rows),
                'total_clk_28d': sum(r.get('clicks',0) for r in rows),
                'queries': [{'query':r['keys'][0],'clicks':r.get('clicks',0),
                             'impressions':r.get('impressions',0),
                             'ctr':round(r.get('ctr',0)*100,2),
                             'position':round(r.get('position',0),1)} for r in rows]
            }
        except Exception as e:
            sla_data[url] = {'error':str(e)}
        time.sleep(0.1)

    # Save outputs
    out = {
        'generated_at': datetime.now().isoformat(),
        'period': f'{start} to {end}',
        'period_days': 28,
        'totals': {
            'clicks': sum(p['clicks_28d'] for p in pages_out),
            'impressions': sum(p['impressions_28d'] for p in pages_out),
            'pages_with_impr': len(pages_out),
            'unique_queries': len(queries_out),
        },
        'pages': pages_out,
        'queries': queries_out,
        'opportunities': opps[:200],
        'sla_redirect_tracking': sla_data,
        'all_combos_count': len(combos),
    }
    with open(os.path.join(OUT_DIR, '28d-snapshot.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    # ===== DIFF vs 90d =====
    print('\n[DIFF] Loading existing 90d snapshot...')
    with open(os.path.join(OUT_DIR, 'full-queries.json')) as f:
        d90q = json.load(f)
    with open(os.path.join(OUT_DIR, 'full-pages.json')) as f:
        d90p = json.load(f)

    # Map for fast lookup
    q90 = {r['query']: r for r in d90q['queries']}
    p90 = {r['url']: r for r in d90p['pages']}

    # NEW queries: in 28d but not in 90d (with >=10 impr)
    new_queries = []
    for r in queries_out:
        if r['query'] not in q90 and r['impressions_28d'] >= 10:
            new_queries.append(r)
    new_queries.sort(key=lambda x: x['impressions_28d'], reverse=True)

    # POSITION CHANGES (queries present in both, |delta_pos| >= 3)
    pos_changes = []
    for r in queries_out:
        if r['query'] in q90:
            old = q90[r['query']]
            if old['impressions_90d'] >= 10 or r['impressions_28d'] >= 10:
                delta = old['avg_position'] - r['avg_position']  # +ve = improved (lower pos #)
                if abs(delta) >= 3:
                    pos_changes.append({
                        'query': r['query'],
                        'pos_90d': old['avg_position'],
                        'pos_28d': r['avg_position'],
                        'delta': round(delta,1),
                        'imp_90d': old['impressions_90d'],
                        'imp_28d': r['impressions_28d'],
                        'clicks_28d': r['clicks_28d'],
                    })
    pos_changes.sort(key=lambda x: x['delta'], reverse=True)
    winners = [c for c in pos_changes if c['delta'] > 0][:15]
    losers = [c for c in pos_changes if c['delta'] < 0][:15]

    # PAGE-LEVEL diff (URL-level position changes)
    page_changes = []
    for r in pages_out:
        if r['url'] in p90:
            old = p90[r['url']]
            if (old['impressions_90d'] >= 30 or r['impressions_28d'] >= 30) and old['avg_position'] > 0:
                delta = old['avg_position'] - r['avg_position']
                if abs(delta) >= 3:
                    page_changes.append({
                        'url': r['url'],
                        'pos_90d': old['avg_position'],
                        'pos_28d': r['avg_position'],
                        'delta': round(delta,1),
                        'imp_90d': old['impressions_90d'],
                        'imp_28d': r['impressions_28d'],
                        'clicks_28d': r['clicks_28d'],
                        'ctr_28d': r['ctr_pct'],
                    })
    page_changes.sort(key=lambda x: x['delta'])  # losers first

    diff = {
        'new_queries': new_queries[:30],
        'striking_distance_new': [q for q in new_queries if 4 <= q['avg_position'] <= 20][:15],
        'winners_pos_change': winners,
        'losers_pos_change': losers,
        'page_changes': page_changes[:30],
    }
    with open(os.path.join(OUT_DIR, '28d-diff-vs-90d.json'), 'w', encoding='utf-8') as f:
        json.dump(diff, f, ensure_ascii=False, indent=2)

    # ===== Console summary =====
    print(f"\n=== 28D SUMMARY ({start} to {end}) ===")
    print(f"Total: {out['totals']['clicks']} clicks / {out['totals']['impressions']} impr "
          f"/ CTR {(out['totals']['clicks']/max(out['totals']['impressions'],1)*100):.2f}% "
          f"/ {out['totals']['pages_with_impr']} pages / {out['totals']['unique_queries']} queries")

    print(f"\n=== NEW queries (>=10 impr, not in 90d): {len(new_queries)} ===")
    for r in new_queries[:15]:
        print(f"  pos{r['avg_position']:>5} | {r['impressions_28d']:>3}imp | {r['clicks_28d']}clk | {r['query']}")

    print(f"\n=== Striking-distance NEW (pos 4-20, new): {len(diff['striking_distance_new'])} ===")
    for r in diff['striking_distance_new'][:10]:
        print(f"  pos{r['avg_position']:>5} | {r['impressions_28d']:>3}imp | {r['query']}")

    print(f"\n=== WINNERS (pos delta >= +3): {len(winners)} ===")
    for r in winners[:10]:
        print(f"  +{r['delta']:>4} | {r['pos_90d']:>4}->{r['pos_28d']:>4} | {r['imp_28d']:>3}imp/28d | {r['query']}")

    print(f"\n=== LOSERS (pos delta <= -3): {len(losers)} ===")
    for r in losers[:10]:
        print(f"  {r['delta']:>5} | {r['pos_90d']:>4}->{r['pos_28d']:>4} | {r['imp_28d']:>3}imp/28d | {r['query']}")

    print(f"\n=== TOP 10 28d OPPORTUNITIES (pos 4-20, imp>=10) ===")
    for o in opps[:10]:
        url_short = o['page'].replace('https://www.fulfillmentmtp.com.ua', '')[:50]
        print(f"  pos{o['avg_position']:>5} | {o['impressions_28d']:>3}imp | {o['clicks_28d']}clk | {o['query'][:35]:<35} -> {url_short}")

    # SLA redirect tracking
    print(f"\n=== SLA REDIRECT IMPACT (28d) ===")
    for url, data in sla_data.items():
        if 'error' in data:
            print(f"  ERR {url}: {data['error']}")
            continue
        url_short = url.replace('https://www.fulfillmentmtp.com.ua', '')
        print(f"  {url_short}")
        print(f"    28d: {data['total_imp_28d']}imp / {data['total_clk_28d']}clk")

    print(f"\n✅ Saved: {OUT_DIR}/28d-snapshot.json + 28d-diff-vs-90d.json")

if __name__ == '__main__':
    main()
