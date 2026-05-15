#!/usr/bin/env python3
"""One-shot 2026-05-15 trend report:
- current 28d (Apr 17 - May 15)  -> docs/gsc/28d-snapshot.json
- previous 28d (Mar 30 - Apr 27) -> docs/gsc/2026-04-27_28d-snapshot.md totals + we'll re-pull queries
- 90d baseline (Jan 20 - Apr 20) -> docs/gsc/full-queries.json (normalized per 28d)

Pulls fresh "previous 28d" window (Mar 20 - Apr 17) so we have proper apples-to-apples,
plus 2-month-ago window (Feb 20 - Mar 20) bounded by GSC verification date Apr 1 2026
(so the 2-month window will be partial).
"""
import os, sys, json, time
from datetime import datetime, timedelta
from pathlib import Path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

ROOT = Path(__file__).parent.parent
TOKEN_FILE = ROOT / 'scripts' / 'gsc_token.json'
OUT_DIR = ROOT / 'docs' / 'gsc'
SITE = 'sc-domain:fulfillmentmtp.com.ua'
SCOPES = ['https://www.googleapis.com/auth/webmasters', 'https://www.googleapis.com/auth/indexing']

def load_creds():
    creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE, 'w') as f:
            f.write(creds.to_json())
    return creds

def q(service, start, end, dims, limit=2000, filters=None):
    body = {'startDate':start,'endDate':end,'dimensions':dims,'rowLimit':limit}
    if filters:
        body['dimensionFilterGroups'] = filters
    return service.searchanalytics().query(siteUrl=SITE, body=body).execute().get('rows', [])

def main():
    creds = load_creds()
    service = build('searchconsole', 'v1', credentials=creds)

    today = datetime.now().date()
    # Current 28d
    cur_end = today
    cur_start = today - timedelta(days=28)
    # Previous 28d (immediately before current)
    prev_end = cur_start - timedelta(days=1)
    prev_start = prev_end - timedelta(days=28)
    # 2-months-ago 28d
    m2_end = prev_start - timedelta(days=1)
    m2_start = m2_end - timedelta(days=28)

    windows = {
        'current_28d': (cur_start.isoformat(), cur_end.isoformat()),
        'previous_28d': (prev_start.isoformat(), prev_end.isoformat()),
        'two_months_ago_28d': (m2_start.isoformat(), m2_end.isoformat()),
    }
    print('Windows:')
    for k, v in windows.items():
        print(f'  {k}: {v[0]} -> {v[1]}')

    snap = {'generated_at': datetime.now().isoformat(), 'windows': windows, 'periods': {}}

    for label, (s, e) in windows.items():
        print(f'\n[{label}] {s} -> {e}')
        # Totals via no-dim query
        totals_rows = q(service, s, e, [], limit=1)
        # GSC doesn't allow empty dims; use site totals via summing page rows
        # Better: pull page-dim and sum
        pages = q(service, s, e, ['page'], limit=2000)
        queries = q(service, s, e, ['query'], limit=2000)
        qpage = q(service, s, e, ['query','page'], limit=5000)

        total_clk = sum(r.get('clicks',0) for r in pages)
        total_imp = sum(r.get('impressions',0) for r in pages)
        snap['periods'][label] = {
            'window': f'{s} -> {e}',
            'totals': {
                'clicks': total_clk,
                'impressions': total_imp,
                'ctr_pct': round(total_clk/max(total_imp,1)*100, 3),
                'pages_with_impr': len(pages),
                'queries_count': len(queries),
            },
            'pages': [{'url':r['keys'][0],'clicks':r.get('clicks',0),'impressions':r.get('impressions',0),
                       'ctr':round(r.get('ctr',0)*100,2),'position':round(r.get('position',0),1)} for r in pages],
            'queries': [{'query':r['keys'][0],'clicks':r.get('clicks',0),'impressions':r.get('impressions',0),
                         'ctr':round(r.get('ctr',0)*100,2),'position':round(r.get('position',0),1)} for r in queries],
            'qpage': [{'query':r['keys'][0],'page':r['keys'][1],'clicks':r.get('clicks',0),
                       'impressions':r.get('impressions',0),'ctr':round(r.get('ctr',0)*100,2),
                       'position':round(r.get('position',0),1)} for r in qpage],
        }
        print(f'  -> {total_clk} clicks / {total_imp} impr / {len(queries)} queries / {len(pages)} pages')
        time.sleep(0.3)

    # === Build winners / losers ===
    cur_q = {r['query']: r for r in snap['periods']['current_28d']['queries']}
    prev_q = {r['query']: r for r in snap['periods']['previous_28d']['queries']}
    cur_qp = snap['periods']['current_28d']['qpage']
    # Map (query) -> best page (most impressions) for context
    qp_map = {}
    for r in cur_qp:
        qry = r['query']
        if qry not in qp_map or r['impressions'] > qp_map[qry]['impressions']:
            qp_map[qry] = r

    # Winners: had >=1 impression in both, gained clicks OR improved position by >=3
    winners = []
    losers = []
    for qry, cur in cur_q.items():
        if qry in prev_q:
            prev = prev_q[qry]
            clk_delta = cur['clicks'] - prev['clicks']
            pos_delta = prev['position'] - cur['position']  # positive=improved
            imp_delta = cur['impressions'] - prev['impressions']
            # ignore tiny-sample false signals
            if max(cur['impressions'], prev['impressions']) < 5:
                continue
            page = qp_map.get(qry, {}).get('page','')
            entry = {
                'query': qry,
                'page': page.replace('https://www.fulfillmentmtp.com.ua',''),
                'clicks_prev': prev['clicks'],
                'clicks_cur': cur['clicks'],
                'clicks_delta': clk_delta,
                'imp_prev': prev['impressions'],
                'imp_cur': cur['impressions'],
                'imp_delta': imp_delta,
                'pos_prev': prev['position'],
                'pos_cur': cur['position'],
                'pos_delta': round(pos_delta, 1),
            }
            # winner score
            score = clk_delta * 3 + (pos_delta if abs(pos_delta) >= 3 else 0) + (imp_delta / 50.0)
            entry['score'] = round(score, 2)
            if clk_delta > 0 or pos_delta >= 3:
                winners.append(entry)
            elif clk_delta < 0 or pos_delta <= -3:
                losers.append(entry)

    winners.sort(key=lambda x: x['score'], reverse=True)
    losers.sort(key=lambda x: x['score'])

    # New entrants: in current, not in previous, >=10 imp
    new_entrants = []
    for qry, cur in cur_q.items():
        if qry not in prev_q and cur['impressions'] >= 10:
            page = qp_map.get(qry, {}).get('page','')
            new_entrants.append({
                'query': qry,
                'page': page.replace('https://www.fulfillmentmtp.com.ua',''),
                'impressions': cur['impressions'],
                'clicks': cur['clicks'],
                'position': cur['position'],
                'ctr': cur['ctr'],
            })
    new_entrants.sort(key=lambda x: x['impressions'], reverse=True)

    # CTR rescue: pos 1-15, imp>=20, ctr<1%
    ctr_rescue = []
    for r in cur_q.values():
        if 1 <= r['position'] <= 15 and r['impressions'] >= 20 and r['ctr'] < 1.0:
            page = qp_map.get(r['query'], {}).get('page','')
            ctr_rescue.append({
                'query': r['query'],
                'page': page.replace('https://www.fulfillmentmtp.com.ua',''),
                'impressions': r['impressions'],
                'position': r['position'],
                'ctr': r['ctr'],
                'clicks': r['clicks'],
            })
    ctr_rescue.sort(key=lambda x: x['impressions'], reverse=True)

    # Striking distance: pos 6-15, imp>=50
    striking = []
    for r in cur_q.values():
        if 6 <= r['position'] <= 15 and r['impressions'] >= 50:
            page = qp_map.get(r['query'], {}).get('page','')
            potential = r['impressions'] * (3.0 - r['ctr']/100)  # rough potential clicks at 3% CTR
            striking.append({
                'query': r['query'],
                'page': page.replace('https://www.fulfillmentmtp.com.ua',''),
                'impressions': r['impressions'],
                'position': r['position'],
                'ctr': r['ctr'],
                'clicks': r['clicks'],
                'potential_score': round(potential, 0),
            })
    striking.sort(key=lambda x: x['potential_score'], reverse=True)

    output = {
        'generated_at': snap['generated_at'],
        'windows': windows,
        'totals_by_period': {k: v['totals'] for k, v in snap['periods'].items()},
        'winners_top20': winners[:20],
        'losers_top20': losers[:20],
        'new_entrants_top10': new_entrants[:10],
        'ctr_rescue_top15': ctr_rescue[:15],
        'striking_distance_top30': striking[:30],
    }

    out_path = OUT_DIR / '2026-05-15_trend-report.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    # Also save the full snapshot
    snap_path = OUT_DIR / '2026-05-15_three-period-snapshot.json'
    with open(snap_path, 'w', encoding='utf-8') as f:
        json.dump(snap, f, ensure_ascii=False, indent=2)

    print('\n=== TOTALS BY PERIOD ===')
    for k, v in snap['periods'].items():
        t = v['totals']
        print(f"  {k}: {t['clicks']} clk / {t['impressions']} imp / CTR {t['ctr_pct']}% / {t['queries_count']} queries")

    print(f"\n=== TOP 20 WINNERS ({len(winners)}) ===")
    for w in winners[:20]:
        print(f"  +clk={w['clicks_delta']:+d} pos {w['pos_prev']:.1f}->{w['pos_cur']:.1f} ({w['pos_delta']:+.1f}) imp {w['imp_prev']}->{w['imp_cur']} | {w['query'][:50]}")

    print(f"\n=== TOP 20 LOSERS ({len(losers)}) ===")
    for w in losers[:20]:
        print(f"  clk={w['clicks_delta']:+d} pos {w['pos_prev']:.1f}->{w['pos_cur']:.1f} ({w['pos_delta']:+.1f}) imp {w['imp_prev']}->{w['imp_cur']} | {w['query'][:50]}")

    print(f"\n=== TOP 10 NEW ENTRANTS ===")
    for n in new_entrants[:10]:
        print(f"  imp={n['impressions']} pos={n['position']:.1f} | {n['query'][:60]}")

    print(f"\n=== CTR RESCUE TOP 15 ===")
    for c in ctr_rescue[:15]:
        print(f"  pos={c['position']:.1f} imp={c['impressions']} ctr={c['ctr']:.2f}% | {c['query'][:50]} -> {c['page'][:40]}")

    print(f"\n=== STRIKING DISTANCE TOP 30 ===")
    for s in striking[:30]:
        print(f"  pos={s['position']:.1f} imp={s['impressions']} ctr={s['ctr']:.2f}% | {s['query'][:50]} -> {s['page'][:40]}")

    print(f"\nSaved: {out_path}")
    print(f"Saved: {snap_path}")

if __name__ == '__main__':
    main()
