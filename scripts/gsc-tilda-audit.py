#!/usr/bin/env python3
"""
GSC Tilda URL Audit — pulls impression/click/position data for all /tpost/ URLs
to decide 301 vs 410 strategy during legacy cleanup (Drilldown Q6).

Output:
  docs/gsc/tilda-audit.csv — all Tilda URLs with 90-day metrics
  docs/gsc/tilda-audit.json — same data + structural mapping proposal
"""
import os
import json
import sys
import csv
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(SCRIPT_DIR, 'gsc_token.json')
SITE_URL = 'sc-domain:fulfillmentmtp.com.ua'
SITE_URL_ALT = 'https://www.fulfillmentmtp.com.ua/'
OUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'docs', 'gsc')
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

def load_creds():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(TOKEN_FILE, 'w') as f:
                f.write(creds.to_json())
        else:
            raise RuntimeError('Token invalid and no refresh token')
    return creds

def fetch_tilda_pages(service, site):
    """Query GSC for pages containing /tpost/ over last 90 days."""
    end = datetime.now().strftime('%Y-%m-%d')
    start = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')

    req = {
        'startDate': start,
        'endDate': end,
        'dimensions': ['page'],
        'dimensionFilterGroups': [{
            'filters': [{
                'dimension': 'page',
                'operator': 'contains',
                'expression': '/tpost/'
            }]
        }],
        'rowLimit': 500,
    }
    resp = service.searchanalytics().query(siteUrl=site, body=req).execute()
    return resp.get('rows', [])

def fetch_queries_for_page(service, site, page_url):
    """Top 10 queries that drove traffic to this page."""
    end = datetime.now().strftime('%Y-%m-%d')
    start = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
    req = {
        'startDate': start,
        'endDate': end,
        'dimensions': ['query'],
        'dimensionFilterGroups': [{
            'filters': [{
                'dimension': 'page',
                'operator': 'equals',
                'expression': page_url
            }]
        }],
        'rowLimit': 10,
    }
    try:
        resp = service.searchanalytics().query(siteUrl=site, body=req).execute()
        return [r['keys'][0] for r in resp.get('rows', [])]
    except Exception:
        return []

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    creds = load_creds()
    service = build('searchconsole', 'v1', credentials=creds)

    # Try both URL prefix and sc-domain
    rows = []
    used_site = None
    for site in [SITE_URL, SITE_URL_ALT]:
        try:
            rows = fetch_tilda_pages(service, site)
            used_site = site
            if rows:
                break
        except Exception as e:
            print(f'[WARN] {site}: {e}', file=sys.stderr)

    print(f'Found {len(rows)} Tilda URLs via {used_site}')

    results = []
    for r in rows:
        url = r['keys'][0]
        clicks = r.get('clicks', 0)
        imps = r.get('impressions', 0)
        ctr = r.get('ctr', 0) * 100
        pos = r.get('position', 0)
        # Only fetch queries for non-zero-impression pages to save API calls
        top_queries = fetch_queries_for_page(service, used_site, url) if imps > 0 else []
        results.append({
            'url': url,
            'clicks_90d': clicks,
            'impressions_90d': imps,
            'ctr_pct': round(ctr, 2),
            'avg_position': round(pos, 1),
            'top_queries': top_queries,
        })
        print(f'  {clicks:>4.0f} clicks / {imps:>5.0f} impr / pos {pos:>4.1f}  {url}')

    # Sort by impressions descending
    results.sort(key=lambda x: x['impressions_90d'], reverse=True)

    # Classification for 301 vs 410
    for r in results:
        if r['impressions_90d'] >= 100 or r['clicks_90d'] >= 5:
            r['action'] = '301_SPECIFIC'  # redirect to topical match
        elif r['impressions_90d'] >= 10:
            r['action'] = '301_HUB'  # redirect to /blog/ hub
        else:
            r['action'] = '410_OR_HUB'  # gone / hub-redirect, no SEO value

    # Write CSV
    csv_path = os.path.join(OUT_DIR, 'tilda-audit.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['url', 'clicks_90d', 'impressions_90d', 'ctr_pct', 'avg_position', 'action', 'top_queries'])
        for r in results:
            w.writerow([
                r['url'], r['clicks_90d'], r['impressions_90d'],
                r['ctr_pct'], r['avg_position'], r['action'],
                ' | '.join(r['top_queries'])
            ])
    print(f'\nCSV: {csv_path}')

    # Write JSON with summary
    summary = {
        'total_urls': len(results),
        'total_clicks_90d': sum(r['clicks_90d'] for r in results),
        'total_impressions_90d': sum(r['impressions_90d'] for r in results),
        'by_action': {
            '301_SPECIFIC': sum(1 for r in results if r['action'] == '301_SPECIFIC'),
            '301_HUB': sum(1 for r in results if r['action'] == '301_HUB'),
            '410_OR_HUB': sum(1 for r in results if r['action'] == '410_OR_HUB'),
        },
        'generated_at': datetime.now().isoformat(),
        'period_days': 90,
        'urls': results,
    }
    json_path = os.path.join(OUT_DIR, 'tilda-audit.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f'JSON: {json_path}')
    print(f'\nSummary:')
    print(f'  Total Tilda URLs: {summary["total_urls"]}')
    print(f'  Total 90d clicks: {summary["total_clicks_90d"]:.0f}')
    print(f'  Total 90d impressions: {summary["total_impressions_90d"]:.0f}')
    print(f'  301 specific match: {summary["by_action"]["301_SPECIFIC"]}')
    print(f'  301 to hub: {summary["by_action"]["301_HUB"]}')
    print(f'  410 or hub: {summary["by_action"]["410_OR_HUB"]}')

if __name__ == '__main__':
    main()
