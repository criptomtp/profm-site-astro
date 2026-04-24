#!/usr/bin/env python3
"""
GSC URL Inspection for 8 pillar URLs (action #9).

Reads the existing gsc_token.json (webmasters.readonly scope) and calls
`urlInspection.index.inspect` for each pillar. Dumps a markdown table to
docs/gsc/YYYY-MM-DD_pillar-inspection.md with verdict, coverage state,
last-crawl date, mobile usability, and an actionable next-step per URL.

Note: the Indexing API cannot submit general URL reindex requests (it is
limited to JobPosting / BroadcastEvent schema). For actual "Request
Indexing" the operator must use the GSC UI — this script surfaces the
list of URLs and their current state so the operator can click through
systematically.
"""

import json
import os
import sys
from datetime import datetime

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SITE_PROPERTY = 'sc-domain:fulfillmentmtp.com.ua'
BASE = 'https://www.fulfillmentmtp.com.ua'
TOKEN_FILE = os.path.join(os.path.dirname(__file__), 'gsc_token.json')

PILLAR_URLS = [
    '/ua/shcho-take-fulfilment/',
    '/ru/chto-takoe-fulfilment/',
    '/en/what-is-fulfillment/',
    '/ua/3pl-logistyka/',
    '/ua/paletne-zberigannya/',
    '/ua/skladski-poslugy/',
    '/ua/about/',
    '/ua/blog/',
]

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']


def load_service():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    return build('searchconsole', 'v1', credentials=creds, cache_discovery=False)


def inspect(service, url):
    body = {
        'inspectionUrl': BASE + url,
        'siteUrl': SITE_PROPERTY,
        'languageCode': 'uk-UA',
    }
    try:
        return service.urlInspection().index().inspect(body=body).execute()
    except Exception as e:
        return {'error': str(e)}


def next_step(verdict, coverage):
    if verdict == 'PASS':
        return 'OK — indexed. Request reindex in GSC if content changed recently.'
    if coverage and 'DISCOVERED' in coverage.upper() and 'NOT_INDEXED' in coverage.upper():
        return 'GSC UI -> URL Inspection -> Request Indexing. Crawl not yet scheduled.'
    if coverage and 'CRAWLED' in coverage.upper() and 'NOT_INDEXED' in coverage.upper():
        return 'Crawled but rejected. Check content uniqueness + dup canonical before reindex.'
    if coverage and 'ALTERNATE' in coverage.upper():
        return 'Alternate page with canonical. Verify hreflang and canonical resolution.'
    if coverage and 'DUPLICATE' in coverage.upper():
        return 'Duplicate — Google chose another canonical. Check for competing URL.'
    if verdict == 'FAIL':
        return 'FAIL — review indexing errors in GSC before resubmitting.'
    return 'Review full inspection payload in the JSON dump.'


def main():
    if not os.path.exists(TOKEN_FILE):
        print(f'Token not found: {TOKEN_FILE}', file=sys.stderr)
        sys.exit(1)

    service = load_service()
    today = datetime.utcnow().strftime('%Y-%m-%d')

    results = []
    for path in PILLAR_URLS:
        print(f'Inspecting {path} ...')
        r = inspect(service, path)
        results.append({'path': path, 'raw': r})

    out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs', 'gsc')
    os.makedirs(out_dir, exist_ok=True)
    json_path = os.path.join(out_dir, f'{today}_pillar-inspection.json')
    md_path = os.path.join(out_dir, f'{today}_pillar-inspection.md')

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    lines = [
        f'# GSC URL Inspection — pillar URLs ({today})',
        '',
        'Source: urlInspection.index.inspect (webmasters.readonly).',
        f'Property: `{SITE_PROPERTY}`  |  Base: `{BASE}`',
        '',
        '| URL | Verdict | Coverage | Last crawl | Google canonical | Next step |',
        '|-----|---------|----------|------------|------------------|-----------|',
    ]

    for r in results:
        path = r['path']
        raw = r['raw']
        if 'error' in raw:
            lines.append(f'| `{path}` | ERROR | — | — | — | `{raw["error"]}` |')
            continue
        ir = raw.get('inspectionResult', {})
        status = ir.get('indexStatusResult', {})
        verdict = status.get('verdict', '—')
        coverage = status.get('coverageState', '—')
        last_crawl = status.get('lastCrawlTime', '—')
        gcan = status.get('googleCanonical', '—')
        step = next_step(verdict, coverage)
        lines.append(
            f'| `{path}` | {verdict} | {coverage} | {last_crawl} | `{gcan}` | {step} |'
        )

    lines += [
        '',
        '## Manual reindex procedure',
        '',
        'The Indexing API is limited to JobPosting and BroadcastEvent — it cannot',
        'submit general URLs. Use the GSC UI:',
        '',
        '1. Open https://search.google.com/search-console?resource_id=' + SITE_PROPERTY.replace(':', '%3A'),
        '2. For each URL above: paste into "Inspect any URL" bar (top), press Enter.',
        '3. Click "Request Indexing" after inspection finishes.',
        '4. Expect "URL added to priority crawl queue" confirmation.',
        '5. Google crawls within 1-3 days; indexing decision may take 1-4 weeks.',
        '',
        '## Full JSON',
        '',
        f'See `{os.path.basename(json_path)}` in this folder for the raw payloads.',
    ]

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    print(f'\nSaved: {md_path}')
    print(f'Saved: {json_path}')


if __name__ == '__main__':
    main()
