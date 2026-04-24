#!/usr/bin/env python3
"""
GA4 Lead Audit — чи долітають події `form_submit` і `generate_lead` до GA4?

Логіка:
1. Взяти перший GA4 property з акаунта користувача (або визначений MEASUREMENT_ID у .env).
2. Запросити Data API: events by name за останні 14 днів, кількість подій + active_users.
3. Окремо — розбивка по page_location для form_submit (де саме форми спрацьовують).
4. Порівняти з tel:/Telegram конверсіями (через event_name = 'conversion').
5. Зберегти звіт у docs/ga4/lead-audit-YYYY-MM-DD.md.

Передумови:
- python3 scripts/ga4-auth.py виконано (є ga4_token.json)
- pip install google-analytics-data (входить у google-cloud пакет)
"""

import os
import sys
import json
from datetime import datetime, timedelta

TOKEN_FILE = os.path.join(os.path.dirname(__file__), 'ga4_token.json')
REPORT_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ga4')


def load_creds():
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
    if not os.path.exists(TOKEN_FILE):
        print(f'❌ Немає {TOKEN_FILE}. Запусти: python3 scripts/ga4-auth.py')
        sys.exit(1)
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds.valid and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE, 'w') as f:
            f.write(creds.to_json())
    return creds


def list_properties(creds):
    """Return list of GA4 property_ids available to the authenticated user."""
    from googleapiclient.discovery import build
    svc = build('analyticsadmin', 'v1beta', credentials=creds)
    accounts = svc.accounts().list().execute().get('accounts', [])
    props = []
    for a in accounts:
        pr = svc.properties().list(filter=f'parent:{a["name"]}').execute().get('properties', [])
        for p in pr:
            props.append({
                'account': a.get('displayName'),
                'property_id': p['name'].replace('properties/', ''),
                'display_name': p.get('displayName'),
                'time_zone': p.get('timeZone'),
                'currency': p.get('currencyCode'),
            })
    return props


def run_report(creds, property_id, dimensions, metrics, days=14, dim_filter=None):
    """Run a GA4 Data API report. Returns (headers, rows)."""
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        DateRange, Dimension, Metric, RunReportRequest, FilterExpression, Filter
    )
    client = BetaAnalyticsDataClient(credentials=creds)
    req_args = {
        'property': f'properties/{property_id}',
        'dimensions': [Dimension(name=d) for d in dimensions],
        'metrics': [Metric(name=m) for m in metrics],
        'date_ranges': [DateRange(start_date=f'{days}daysAgo', end_date='today')],
        'limit': 200,
    }
    if dim_filter:
        dim_name, dim_value = dim_filter
        req_args['dimension_filter'] = FilterExpression(
            filter=Filter(field_name=dim_name, string_filter=Filter.StringFilter(value=dim_value))
        )
    req = RunReportRequest(**req_args)
    resp = client.run_report(req)
    headers = [h.name for h in resp.dimension_headers] + [h.name for h in resp.metric_headers]
    rows = []
    for r in resp.rows:
        row = [d.value for d in r.dimension_values] + [m.value for m in r.metric_values]
        rows.append(row)
    return headers, rows


def build_report(creds, prop, days=14):
    """Build a full lead audit report for one GA4 property. Returns markdown string."""
    pid = prop['property_id']
    out = []
    out.append(f'# GA4 Lead Audit — {prop["display_name"]}\n')
    out.append(f'- Property ID: `{pid}`')
    out.append(f'- Account: {prop["account"]}')
    out.append(f'- Time zone: {prop["time_zone"]} · Currency: {prop["currency"]}')
    out.append(f'- Period: last {days} days · generated {datetime.now().isoformat(timespec="seconds")}')
    out.append('')

    # 1. All events by name — baseline
    out.append(f'## 1. Всі події за останні {days} днів (топ-25 за кількістю)\n')
    try:
        _, rows = run_report(creds, pid, ['eventName'], ['eventCount', 'totalUsers'], days=days)
        rows.sort(key=lambda r: int(r[1]), reverse=True)
        out.append('| Event Name | Events | Users |')
        out.append('|---|---:|---:|')
        for r in rows[:25]:
            out.append(f'| `{r[0]}` | {r[1]} | {r[2]} |')
        out.append('')
    except Exception as e:
        out.append(f'❌ Помилка: {e}\n')

    # 2. form_submit breakdown
    out.append(f'## 2. `form_submit` — деталі за {days} днів\n')
    try:
        _, rows = run_report(creds, pid, ['eventName'], ['eventCount', 'totalUsers'], days=days,
                             dim_filter=('eventName', 'form_submit'))
        total_fs = int(rows[0][1]) if rows else 0
        users_fs = int(rows[0][2]) if rows else 0
        out.append(f'- Всього `form_submit`: **{total_fs}**')
        out.append(f'- Унікальних користувачів: **{users_fs}**\n')
        if total_fs == 0:
            out.append('🚨 **0 подій form_submit** — подія не долітає до GA4. Можливі причини:')
            out.append('  - Adblock/ITP блокує gtag')
            out.append('  - Race condition — форма відправлена раніше ніж gtag завантажився')
            out.append('  - Помилка у коді `mtpSubmitLead`')
            out.append('  - Події надходять у інший property ID\n')

        # 2a. by page
        out.append('### 2a. По сторінках (topic: звідки йдуть ліди)\n')
        _, rows = run_report(creds, pid, ['eventName', 'pagePath'], ['eventCount', 'totalUsers'],
                             days=days, dim_filter=('eventName', 'form_submit'))
        rows.sort(key=lambda r: int(r[2]), reverse=True)
        if rows:
            out.append('| Page | Events | Users |')
            out.append('|---|---:|---:|')
            for r in rows[:30]:
                out.append(f'| `{r[1]}` | {r[2]} | {r[3]} |')
        else:
            out.append('_(немає даних)_')
        out.append('')

        # 2b. by source/medium
        out.append('### 2b. По джерелу трафіку\n')
        _, rows = run_report(creds, pid, ['eventName', 'sessionSource', 'sessionMedium'],
                             ['eventCount'], days=days, dim_filter=('eventName', 'form_submit'))
        rows.sort(key=lambda r: int(r[3]), reverse=True)
        if rows:
            out.append('| Source | Medium | Events |')
            out.append('|---|---|---:|')
            for r in rows[:20]:
                out.append(f'| `{r[1]}` | `{r[2]}` | {r[3]} |')
        else:
            out.append('_(немає даних)_')
        out.append('')

        # 2c. daily trend
        out.append(f'### 2c. По днях (тренд за {days} днів)\n')
        _, rows = run_report(creds, pid, ['eventName', 'date'], ['eventCount'],
                             days=days, dim_filter=('eventName', 'form_submit'))
        rows.sort(key=lambda r: r[1])
        if rows:
            out.append('| Date | Events |')
            out.append('|---|---:|')
            for r in rows:
                out.append(f'| {r[1]} | {r[2]} |')
        else:
            out.append('_(немає даних)_')
        out.append('')
    except Exception as e:
        out.append(f'❌ Помилка form_submit breakdown: {e}\n')

    # 3. generate_lead
    out.append(f'## 3. `generate_lead` за {days} днів\n')
    try:
        _, rows = run_report(creds, pid, ['eventName'], ['eventCount', 'totalUsers', 'eventValue'],
                             days=days, dim_filter=('eventName', 'generate_lead'))
        if rows:
            out.append(f'- Events: **{rows[0][1]}** · Users: **{rows[0][2]}** · Value: **{rows[0][3]}**\n')
        else:
            out.append('🚨 0 подій generate_lead\n')
    except Exception as e:
        out.append(f'❌ {e}\n')

    # 4. Key Events (Conversions)
    out.append('## 4. Key Events (Conversions) за 14 днів\n')
    try:
        _, rows = run_report(creds, pid, ['eventName'], ['keyEvents'], days=days)
        rows = [r for r in rows if float(r[1]) > 0]
        rows.sort(key=lambda r: float(r[1]), reverse=True)
        if rows:
            out.append('| Event | Key Events (conversions) |')
            out.append('|---|---:|')
            for r in rows:
                out.append(f'| `{r[0]}` | {r[1]} |')
            out.append('')
            has_form_submit_key = any(r[0] == 'form_submit' for r in rows)
            has_generate_lead_key = any(r[0] == 'generate_lead' for r in rows)
            if not has_form_submit_key and not has_generate_lead_key:
                out.append('🚨 **НІ `form_submit` НІ `generate_lead` НЕ позначені як Key Event** у GA4. '
                           'Events летять — але у UI «Конверсії» вони не рахуються.')
                out.append('  - Admin → Events → Mark as key event для `form_submit` і `generate_lead`.')
                out.append('')
        else:
            out.append('🚨 Жодного Key Event не зафіксовано за період\n')
    except Exception as e:
        out.append(f'❌ {e}\n')

    # 5. Realtime snapshot (last 30 min)
    out.append('## 5. Realtime (останні 30 хв)\n')
    try:
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.analytics.data_v1beta.types import (
            Dimension, Metric, RunRealtimeReportRequest
        )
        client = BetaAnalyticsDataClient(credentials=creds)
        req = RunRealtimeReportRequest(
            property=f'properties/{pid}',
            dimensions=[Dimension(name='eventName')],
            metrics=[Metric(name='eventCount'), Metric(name='activeUsers')],
            limit=20,
        )
        resp = client.run_realtime_report(req)
        if resp.rows:
            out.append('| Event | Events | Users |')
            out.append('|---|---:|---:|')
            for r in resp.rows:
                name = r.dimension_values[0].value
                ec = r.metric_values[0].value
                au = r.metric_values[1].value
                out.append(f'| `{name}` | {ec} | {au} |')
        else:
            out.append('_(realtime порожній — ніхто не на сайті)_')
        out.append('')
    except Exception as e:
        out.append(f'❌ {e}\n')

    # 6. Recommendations
    out.append('## 6. Діагностика і рекомендації\n')
    out.append('- **Якщо секція 2 показує >0 form_submit але секція 4 не містить їх** → подія є, але '
               'не марковано як Key Event. Admin → Events → toggle «Mark as key event».')
    out.append('- **Якщо секція 2 = 0** → події не долітають. Перевір DevTools → Network → filter '
               '`collect?` на `https://region1.google-analytics.com/g/collect`. Якщо там нічого під '
               'час submit — gtag не завантажений (adblock, slow network, race condition).')
    out.append('- **Якщо realtime (секція 5) працює, а історія (секція 1) — ні** → фільтр Internal '
               'Traffic чи DebugView режим виключає продакшн-трафік. Admin → Data Filters.')
    out.append('- **Перевірити стан на продакшн**: відкрити сайт у Chrome Incognito + DevTools Network, '
               'submit форму, очікувати POST на `g/collect?...en=form_submit` зі status 204/200.')
    out.append('')

    return '\n'.join(out)


def main():
    days = int(os.environ.get('DAYS', '14'))
    creds = load_creds()
    print(f'🔐 Авторизація OK. Scopes: {creds.scopes}')
    print('📋 Шукаю GA4 properties...')
    props = list_properties(creds)
    if not props:
        print('❌ Жодного GA4 property не знайдено на цьому акаунті.')
        print('   Перевір: https://analytics.google.com/ — чи правильний Google-акаунт?')
        sys.exit(1)

    print(f'✅ Знайдено {len(props)} properties:')
    for p in props:
        print(f'   - {p["display_name"]} · ID {p["property_id"]} · TZ {p["time_zone"]}')

    os.makedirs(REPORT_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')

    for p in props:
        print(f'\n🔍 Будую звіт для "{p["display_name"]}" (ID {p["property_id"]})...')
        try:
            md = build_report(creds, p, days=days)
        except Exception as e:
            print(f'   ❌ Помилка: {e}')
            continue
        safe_name = p['display_name'].replace('/', '_').replace(' ', '_')[:60]
        fp = os.path.join(REPORT_DIR, f'lead-audit-{today}-{safe_name}-{p["property_id"]}.md')
        with open(fp, 'w') as f:
            f.write(md)
        print(f'   ✅ Saved: {fp}')

    print(f'\n✅ Готово. Звіти у: {REPORT_DIR}/')


if __name__ == '__main__':
    main()
