#!/usr/bin/env python3
"""
gsc-baseline-capture.py — Capture GSC baseline metrics for pillar URLs
before observation window starts.

After Phase A schema/H1 uplift + 55 reindex submissions, we need to fix
a "before" snapshot to compare against in 7-14 days. Without this we
can't measure ROI of the work.

Pulls last 14 days of data per URL: clicks, impressions, ctr, position.
Saves JSON to docs/gsc/baseline-<YYYY-MM-DD>.json for future delta diff.

Usage:
    python3 scripts/gsc-baseline-capture.py
"""

import os
import sys
import json
from datetime import datetime, timedelta, date
from pathlib import Path

ROOT = Path(__file__).parent.parent
TOKEN_FILE = ROOT / "scripts" / "gsc_token.json"
OUT_DIR = ROOT / "docs" / "gsc"
SITE_URL = "sc-domain:fulfillmentmtp.com.ua"

# Same URL list as gsc-reindex.py — keep the two files in sync
URLS = [
    "https://www.fulfillmentmtp.com.ua/ua/tsiny/",
    "https://www.fulfillmentmtp.com.ua/ru/tsenu/",
    "https://www.fulfillmentmtp.com.ua/en/prices/",
    "https://www.fulfillmentmtp.com.ua/ua/calculator/",
    "https://www.fulfillmentmtp.com.ua/ru/calculator/",
    "https://www.fulfillmentmtp.com.ua/en/calculator/",
    "https://www.fulfillmentmtp.com.ua/poslugy/",
    "https://www.fulfillmentmtp.com.ua/ru/services/",
    "https://www.fulfillmentmtp.com.ua/en/services/",
    "https://www.fulfillmentmtp.com.ua/",
    "https://www.fulfillmentmtp.com.ua/ru/",
    "https://www.fulfillmentmtp.com.ua/en/",
    "https://www.fulfillmentmtp.com.ua/ua/shcho-take-fulfilment/",
    "https://www.fulfillmentmtp.com.ua/ru/chto-takoe-fulfilment/",
    "https://www.fulfillmentmtp.com.ua/en/what-is-fulfillment/",
    "https://www.fulfillmentmtp.com.ua/ua/3pl-logistyka/",
    "https://www.fulfillmentmtp.com.ua/ru/3pl-logistika/",
    "https://www.fulfillmentmtp.com.ua/en/3pl-logistics/",
    "https://www.fulfillmentmtp.com.ua/fulfilment-rozetka/",
    "https://www.fulfillmentmtp.com.ua/ru/fulfilment-rozetka/",
    "https://www.fulfillmentmtp.com.ua/en/fulfillment-for-rozetka-sellers/",
    "https://www.fulfillmentmtp.com.ua/fulfilment-prom/",
    "https://www.fulfillmentmtp.com.ua/ru/fulfilment-prom/",
    "https://www.fulfillmentmtp.com.ua/en/fulfilment-prom/",
    "https://www.fulfillmentmtp.com.ua/ua/fulfilment-kyiv/",
    "https://www.fulfillmentmtp.com.ua/ru/fulfilment-kiev/",
    "https://www.fulfillmentmtp.com.ua/en/fulfillment-kyiv/",
    "https://www.fulfillmentmtp.com.ua/ua/fulfilment-ukraina/",
    "https://www.fulfillmentmtp.com.ua/ru/fulfilment-ukraina/",
    "https://www.fulfillmentmtp.com.ua/en/fulfillment-ukraine/",
    "https://www.fulfillmentmtp.com.ua/ua/fulfilment-vazhkykh-tovariv/",
    "https://www.fulfillmentmtp.com.ua/ru/fulfilment-vazhkykh-tovariv/",
    "https://www.fulfillmentmtp.com.ua/en/heavy-goods/",
    "https://www.fulfillmentmtp.com.ua/ua/paletne-zberigannya/",
    "https://www.fulfillmentmtp.com.ua/ru/paletnoe-khranenie/",
    "https://www.fulfillmentmtp.com.ua/en/pallet-storage/",
    "https://www.fulfillmentmtp.com.ua/ua/skladski-poslugy/",
    "https://www.fulfillmentmtp.com.ua/ru/skladskie-uslugi/",
    "https://www.fulfillmentmtp.com.ua/en/warehouse-services/",
    "https://www.fulfillmentmtp.com.ua/ua/fulfilment-dlya-marketpleysiv/",
    "https://www.fulfillmentmtp.com.ua/ua/fulfilment-dlya-maloho-biznesu/",
    "https://www.fulfillmentmtp.com.ua/fulfilment-dlya-odyahu/",
    "https://www.fulfillmentmtp.com.ua/ru/fulfilment-dlya-odezhdy/",
    "https://www.fulfillmentmtp.com.ua/en/fulfilment-for-clothing/",
]


def get_credentials():
    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
    except ImportError:
        print("ERROR: pip install google-auth google-auth-oauthlib", file=sys.stderr)
        sys.exit(1)
    SCOPES = [
        "https://www.googleapis.com/auth/webmasters",
        "https://www.googleapis.com/auth/indexing",
    ]
    creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return creds


def query_url(service, url, start_date, end_date):
    """Query Search Analytics for a specific URL."""
    request = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": ["page", "query"],
        "dimensionFilterGroups": [{
            "filters": [{"dimension": "page", "operator": "equals", "expression": url}]
        }],
        "rowLimit": 100,
    }
    try:
        response = service.searchanalytics().query(siteUrl=SITE_URL, body=request).execute()
        rows = response.get("rows", [])
        # Aggregate per-URL totals
        clicks = sum(r.get("clicks", 0) for r in rows)
        impressions = sum(r.get("impressions", 0) for r in rows)
        ctr = clicks / impressions if impressions else 0
        # Position = weighted average by impressions
        if impressions:
            position = sum(r.get("position", 0) * r.get("impressions", 0) for r in rows) / impressions
        else:
            position = 0
        # Top 5 queries for context
        top_queries = sorted(rows, key=lambda r: -r.get("impressions", 0))[:5]
        top_queries_summary = [
            {
                "query": r["keys"][1] if len(r["keys"]) > 1 else "",
                "impressions": r.get("impressions", 0),
                "clicks": r.get("clicks", 0),
                "position": round(r.get("position", 0), 1),
            }
            for r in top_queries
        ]
        return {
            "clicks": clicks,
            "impressions": impressions,
            "ctr": round(ctr, 4),
            "avg_position": round(position, 2),
            "top_queries": top_queries_summary,
        }
    except Exception as e:
        return {"error": str(e)[:200]}


def main():
    try:
        from googleapiclient.discovery import build
    except ImportError:
        print("ERROR: pip install google-api-python-client", file=sys.stderr)
        sys.exit(1)

    creds = get_credentials()
    service = build("searchconsole", "v1", credentials=creds)

    today = date.today()
    end_date = (today - timedelta(days=3)).isoformat()  # GSC has ~3 day lag
    start_date = (today - timedelta(days=17)).isoformat()  # 14-day window

    print(f"GSC baseline capture: {len(URLS)} URLs, window {start_date} → {end_date}")
    print()

    results = {
        "captured_at": today.isoformat(),
        "window_start": start_date,
        "window_end": end_date,
        "url_count": len(URLS),
        "urls": {},
    }
    total_imp, total_clicks = 0, 0

    for i, url in enumerate(URLS, 1):
        data = query_url(service, url, start_date, end_date)
        results["urls"][url] = data
        if "error" not in data:
            mark = "✅" if data["impressions"] > 0 else "·"
            total_imp += data["impressions"]
            total_clicks += data["clicks"]
            print(f"  {mark} [{i:>2}/{len(URLS)}] {data['impressions']:>5} imp / "
                  f"{data['clicks']:>3} clk / pos {data['avg_position']:>5.1f}  {url[40:]}")
        else:
            print(f"  ❌ [{i:>2}/{len(URLS)}] ERROR: {data['error'][:80]}")

    results["totals"] = {"impressions": total_imp, "clicks": total_clicks}

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUT_DIR / f"baseline-{today.isoformat()}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print()
    print(f"Total: {total_imp} impressions, {total_clicks} clicks across {len(URLS)} URLs (14-day window)")
    print(f"Baseline saved: {out_file.relative_to(ROOT)}")
    print(f"Next checkpoint: pull delta in 7-14 days with `python3 scripts/gsc-delta.py {out_file.name}`")


if __name__ == "__main__":
    main()
