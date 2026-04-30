#!/usr/bin/env python3
"""GA4 28d snapshot — organic sessions, conversion events, top landing pages.
Output: docs/ga4/28d-organic-snapshot.json
"""
import os, sys, json
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(SCRIPT_DIR, 'ga4_token.json')
OUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'docs', 'ga4')

# fulfillmentmtp.com.ua property
PROPERTY_ID = '286651314'

def load_creds():
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds.valid and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE,'w') as f: f.write(creds.to_json())
    return creds

def report(client, pid, dims, mets, days=28, dim_filter=None, limit=200):
    from google.analytics.data_v1beta.types import (
        DateRange, Dimension, Metric, RunReportRequest, FilterExpression, Filter
    )
    args = {
        'property': f'properties/{pid}',
        'dimensions': [Dimension(name=d) for d in dims],
        'metrics': [Metric(name=m) for m in mets],
        'date_ranges': [DateRange(start_date=f'{days}daysAgo', end_date='today')],
        'limit': limit,
    }
    if dim_filter:
        n, v = dim_filter
        args['dimension_filter'] = FilterExpression(
            filter=Filter(field_name=n, string_filter=Filter.StringFilter(value=v))
        )
    return client.run_report(RunReportRequest(**args))

def rows(resp):
    out = []
    for r in resp.rows:
        out.append([d.value for d in r.dimension_values] + [m.value for m in r.metric_values])
    return out

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    creds = load_creds()
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    client = BetaAnalyticsDataClient(credentials=creds)
    days = 28
    pid = PROPERTY_ID

    out = {'generated_at': datetime.now().isoformat(), 'property_id': pid, 'period_days': days}

    # 1. Sessions by source/medium
    print('[1/6] Sessions by source/medium...')
    r = report(client, pid, ['sessionSource','sessionMedium'],
               ['sessions','totalUsers','engagedSessions','engagementRate','conversions'], days=days, limit=50)
    src = rows(r)
    src.sort(key=lambda x: int(x[2]), reverse=True)
    out['sessions_by_source'] = [{'source':r[0],'medium':r[1],'sessions':int(r[2]),
                                   'users':int(r[3]),'engaged':int(r[4]),
                                   'engagement_rate':round(float(r[5])*100,1),
                                   'conversions':float(r[6])} for r in src[:30]]

    # 2. Events by name
    print('[2/6] Events by name...')
    r = report(client, pid, ['eventName'], ['eventCount','totalUsers'], days=days, limit=100)
    evs = rows(r)
    evs.sort(key=lambda x: int(x[1]), reverse=True)
    out['events_by_name'] = [{'event':r[0],'count':int(r[1]),'users':int(r[2])} for r in evs[:30]]

    # 3. Key conversion events filter
    print('[3/6] Key conversion events...')
    out['conversions_28d'] = {}
    for ev in ['form_submit', 'generate_lead', 'phone_click', 'telegram_click', 'whatsapp_click']:
        try:
            r = report(client, pid, ['eventName'], ['eventCount','totalUsers'], days=days,
                       dim_filter=('eventName', ev))
            rs = rows(r)
            out['conversions_28d'][ev] = {
                'events': int(rs[0][1]) if rs else 0,
                'users': int(rs[0][2]) if rs else 0,
            }
        except Exception as e:
            out['conversions_28d'][ev] = {'error': str(e)[:120]}

    # 4. Top landing pages (organic only)
    print('[4/6] Top organic landing pages...')
    r = report(client, pid, ['landingPagePlusQueryString'],
               ['sessions','engagedSessions','engagementRate','conversions'],
               days=days, dim_filter=('sessionMedium','organic'), limit=50)
    lp = rows(r)
    lp.sort(key=lambda x: int(x[1]), reverse=True)
    out['organic_landing_pages'] = [{'landing':r[0],'sessions':int(r[1]),
                                      'engaged':int(r[2]),
                                      'engagement_rate':round(float(r[3])*100,1),
                                      'conversions':float(r[4])} for r in lp[:30]]

    # 5. Form submit by page
    print('[5/6] form_submit by page...')
    try:
        r = report(client, pid, ['eventName','pagePath'], ['eventCount','totalUsers'],
                   days=days, dim_filter=('eventName','form_submit'), limit=50)
        fs = rows(r)
        fs.sort(key=lambda x: int(x[2]), reverse=True)
        out['form_submit_by_page'] = [{'page':r[1],'events':int(r[2]),'users':int(r[3])} for r in fs[:20]]
    except Exception as e:
        out['form_submit_by_page'] = {'error':str(e)[:120]}

    # 6. AI search referrers
    print('[6/6] AI search referrers...')
    try:
        from google.analytics.data_v1beta.types import (
            DateRange, Dimension, Metric, RunReportRequest, FilterExpression,
            FilterExpressionList, Filter
        )
        ai_hosts = ['perplexity.ai','chat.openai.com','chatgpt.com',
                    'copilot.microsoft.com','gemini.google.com','claude.ai',
                    'you.com','phind.com','duckduckgo.com']
        ai_filter = FilterExpression(or_group=FilterExpressionList(expressions=[
            FilterExpression(filter=Filter(field_name='sessionSource',
                string_filter=Filter.StringFilter(value=h, match_type=Filter.StringFilter.MatchType.CONTAINS)))
            for h in ai_hosts
        ]))
        from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric
        req = RunReportRequest(
            property=f'properties/{pid}',
            dimensions=[Dimension(name='sessionSource'),Dimension(name='landingPagePlusQueryString')],
            metrics=[Metric(name='sessions'),Metric(name='totalUsers'),Metric(name='conversions')],
            date_ranges=[DateRange(start_date=f'{days}daysAgo', end_date='today')],
            dimension_filter=ai_filter, limit=50,
        )
        resp = client.run_report(req)
        out['ai_referrers'] = []
        for r in resp.rows:
            v = [d.value for d in r.dimension_values]
            m = [d.value for d in r.metric_values]
            out['ai_referrers'].append({'source':v[0],'landing':v[1],
                                         'sessions':int(m[0]),'users':int(m[1]),
                                         'conversions':float(m[2])})
        out['ai_referrers'].sort(key=lambda x: x['sessions'], reverse=True)
    except Exception as e:
        out['ai_referrers'] = {'error':str(e)[:200]}

    fp = os.path.join(OUT_DIR, '28d-organic-snapshot.json')
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f'\n=== TOP SOURCES (28d) ===')
    for s in out['sessions_by_source'][:10]:
        print(f"  {s['sessions']:>4} sess | {s['users']:>4} usr | eng {s['engagement_rate']:>5}% | conv {s['conversions']:>5.0f} | {s['source']}/{s['medium']}")

    print(f'\n=== KEY EVENTS (28d) ===')
    for ev, d in out['conversions_28d'].items():
        if 'error' in d:
            print(f"  {ev}: ERR {d['error']}")
        else:
            print(f"  {ev:20} : {d['events']} events / {d['users']} users")

    print(f'\n=== TOP ORGANIC LANDING PAGES (28d) ===')
    for p in out['organic_landing_pages'][:10]:
        print(f"  {p['sessions']:>3} sess | eng {p['engagement_rate']:>5}% | conv {p['conversions']:>4.0f} | {p['landing'][:60]}")

    print(f'\n=== AI REFERRERS (28d) ===')
    if isinstance(out['ai_referrers'], list):
        for ai in out['ai_referrers'][:10]:
            print(f"  {ai['sessions']:>3} sess | conv {ai['conversions']:>4.0f} | {ai['source']:<25} | {ai['landing'][:50]}")
        if not out['ai_referrers']:
            print('  (none)')

    print(f'\n✅ Saved: {fp}')

if __name__ == '__main__':
    main()
