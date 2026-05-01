#!/usr/bin/env python3
"""
gsc-reindex.py — Submit URL_UPDATED notifications to Google Indexing API.

Use after schema/content uplift to nudge Google to re-crawl pages within
1-3 days instead of waiting for the regular crawl cycle (1-4 weeks).

Auth: reuses scripts/gsc_token.json from gsc-auth.py if it has the
indexing scope. If not, prints clear re-auth instructions.

Quota: Google Indexing API allows ~200 publish requests / day per project.

Usage:
    python3 scripts/gsc-reindex.py            # uses default URL list below
    python3 scripts/gsc-reindex.py URL1 URL2  # submit specific URLs

Output:
    Per-URL status to stdout + full JSON dump to
    docs/gsc/reindex-<timestamp>.json for audit trail.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
TOKEN_FILE = ROOT / "scripts" / "gsc_token.json"
CREDS_FILE = ROOT / "scripts" / "client_secret.json"
OUT_DIR = ROOT / "docs" / "gsc"

# 16 triplets × 3 URLs = 48 URLs from this session's schema uplift work,
# plus 3 odyahu (GeoCoords earlier in session). Removed duplicates.
DEFAULT_URLS = [
    # P0 (4)
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
    # P1 (4)
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
    # P2 (5)
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
    # P3 words top-up today
    "https://www.fulfillmentmtp.com.ua/ua/fulfilment-dlya-marketpleysiv/",
    "https://www.fulfillmentmtp.com.ua/ua/fulfilment-dlya-maloho-biznesu/",
    # Odyahu GeoCoords earlier
    "https://www.fulfillmentmtp.com.ua/fulfilment-dlya-odyahu/",
    "https://www.fulfillmentmtp.com.ua/ru/fulfilment-dlya-odezhdy/",
    "https://www.fulfillmentmtp.com.ua/en/fulfilment-for-clothing/",
]


def get_credentials():
    """Load existing token; refresh if expired."""
    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        print("ERROR: pip install google-auth google-auth-oauthlib google-auth-httplib2", file=sys.stderr)
        sys.exit(1)

    SCOPES = [
        "https://www.googleapis.com/auth/webmasters",
        "https://www.googleapis.com/auth/indexing",
    ]

    creds = None
    if TOKEN_FILE.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
        except Exception as e:
            print(f"WARN: could not load token: {e}", file=sys.stderr)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"WARN: refresh failed: {e}, re-auth needed", file=sys.stderr)
                creds = None
        if not creds:
            if not CREDS_FILE.exists():
                print(f"ERROR: {CREDS_FILE} not found — see scripts/gsc-auth.py for setup", file=sys.stderr)
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return creds


def submit_url(creds, url):
    """POST URL_UPDATED to Indexing API. Returns (success, message)."""
    import requests
    endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    payload = {"url": url, "type": "URL_UPDATED"}
    headers = {"Authorization": f"Bearer {creds.token}", "Content-Type": "application/json"}
    try:
        r = requests.post(endpoint, json=payload, headers=headers, timeout=15)
        if r.status_code == 200:
            data = r.json()
            ts = data.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", "")
            return (True, f"OK ({ts})")
        else:
            return (False, f"HTTP {r.status_code}: {r.text[:200]}")
    except Exception as e:
        return (False, f"EXCEPTION: {e}")


def main():
    urls = sys.argv[1:] if len(sys.argv) > 1 else DEFAULT_URLS
    print(f"Submitting {len(urls)} URLs to Google Indexing API...")
    print()

    creds = get_credentials()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    log_file = OUT_DIR / f"reindex-{ts}.json"

    results = []
    ok_count = 0
    for i, url in enumerate(urls, 1):
        success, msg = submit_url(creds, url)
        if success:
            ok_count += 1
            mark = "✅"
        else:
            mark = "❌"
        print(f"  {mark} [{i:>2}/{len(urls)}] {url}")
        if not success:
            print(f"        {msg}")
        results.append({"url": url, "success": success, "message": msg})

    with open(log_file, "w", encoding="utf-8") as f:
        json.dump({"timestamp": ts, "ok": ok_count, "fail": len(urls) - ok_count, "results": results}, f, indent=2, ensure_ascii=False)

    print()
    print(f"Submitted: {ok_count}/{len(urls)}")
    print(f"Log: {log_file.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
