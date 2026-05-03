#!/usr/bin/env python3
"""
gsc-delta.py — Compare current GSC data vs a captured baseline.

Companion to gsc-baseline-capture.py. Run at observation checkpoint
(7-14 days post-uplift) to see what moved and decide Phase B vs pivot.

Pulls fresh 14-day GSC data for same URLs as baseline, computes per-URL
deltas (clicks, impressions, ctr, avg_position, top queries), classifies
each as winner / loser / unchanged, writes ranked report.

Usage:
    python3 scripts/gsc-delta.py                            # uses latest baseline-*.json
    python3 scripts/gsc-delta.py docs/gsc/baseline-2026-05-02.json
"""

import os
import sys
import json
import glob
from datetime import datetime, timedelta, date
from pathlib import Path

ROOT = Path(__file__).parent.parent
TOKEN_FILE = ROOT / "scripts" / "gsc_token.json"
GSC_DIR = ROOT / "docs" / "gsc"
SITE_URL = "sc-domain:fulfillmentmtp.com.ua"

# Movement thresholds (how big a change counts as material)
SIGNIFICANT_IMP_DELTA_PCT = 10   # ±10% impressions
SIGNIFICANT_POS_DELTA = 3        # ±3 position points
SIGNIFICANT_CLICK_DELTA = 1      # any click change is meaningful at our volume
MIN_IMP_FOR_POS_SIGNAL = 10      # require ≥10 imp on BOTH sides before counting
                                 # position drops — otherwise tiny samples
                                 # produce false-positive 'losers' when the
                                 # page broadens query coverage (new long-tail
                                 # queries at pos 30-50 drag weighted avg down).


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
        clicks = sum(r.get("clicks", 0) for r in rows)
        impressions = sum(r.get("impressions", 0) for r in rows)
        ctr = clicks / impressions if impressions else 0
        if impressions:
            position = sum(r.get("position", 0) * r.get("impressions", 0) for r in rows) / impressions
        else:
            position = 0
        top_queries = sorted(rows, key=lambda r: -r.get("impressions", 0))[:5]
        return {
            "clicks": clicks,
            "impressions": impressions,
            "ctr": round(ctr, 4),
            "avg_position": round(position, 2),
            "top_queries": [
                {
                    "query": r["keys"][1] if len(r["keys"]) > 1 else "",
                    "impressions": r.get("impressions", 0),
                    "clicks": r.get("clicks", 0),
                    "position": round(r.get("position", 0), 1),
                }
                for r in top_queries
            ],
        }
    except Exception as e:
        return {"error": str(e)[:200]}


def classify(baseline, current):
    """Return ('winner'|'loser'|'unchanged', reason_string)."""
    if "error" in baseline or "error" in current:
        return ("unknown", "API error")

    base_imp = baseline.get("impressions", 0)
    cur_imp = current.get("impressions", 0)
    base_clk = baseline.get("clicks", 0)
    cur_clk = current.get("clicks", 0)
    base_pos = baseline.get("avg_position", 0)
    cur_pos = current.get("avg_position", 0)

    imp_delta = cur_imp - base_imp
    imp_delta_pct = (imp_delta / base_imp * 100) if base_imp > 0 else (100 if cur_imp > 0 else 0)
    clk_delta = cur_clk - base_clk
    pos_delta = cur_pos - base_pos  # negative = better (lower position number)

    reasons = []
    score = 0

    if abs(imp_delta_pct) >= SIGNIFICANT_IMP_DELTA_PCT:
        reasons.append(f"imp {imp_delta:+d} ({imp_delta_pct:+.0f}%)")
        score += (1 if imp_delta_pct > 0 else -1)
    if abs(clk_delta) >= SIGNIFICANT_CLICK_DELTA:
        reasons.append(f"clk {clk_delta:+d}")
        score += (2 if clk_delta > 0 else -2)
    # Position-shift requires meaningful sample on both sides — otherwise a
    # page that gains query breadth (1 brand query → 5 long-tail queries)
    # gets falsely flagged as 'loser' when its weighted avg moves from pos 2
    # to pos 40 purely from sample composition change. See investigation
    # 2026-05-03 (vazhkykh-tovariv, fulfilment-kyiv, heavy-goods).
    sample_ok = base_imp >= MIN_IMP_FOR_POS_SIGNAL and cur_imp >= MIN_IMP_FOR_POS_SIGNAL
    if base_pos > 0 and cur_pos > 0 and abs(pos_delta) >= SIGNIFICANT_POS_DELTA and sample_ok:
        # Lower position = better, so flip sign for score
        reasons.append(f"pos {base_pos:.1f}→{cur_pos:.1f}")
        score += (-2 if pos_delta < 0 else 2) * (-1)  # better pos = positive score
    elif base_pos > 0 and cur_pos > 0 and abs(pos_delta) >= SIGNIFICANT_POS_DELTA:
        # Position moved but sample too small — note it but don't count for verdict
        reasons.append(f"pos {base_pos:.1f}→{cur_pos:.1f} (low-sample)")
    elif base_pos == 0 and cur_pos > 0:
        reasons.append(f"NEW @ pos {cur_pos:.1f}")
        score += 3
    elif cur_pos == 0 and base_pos > 0:
        reasons.append(f"DROPPED from pos {base_pos:.1f}")
        score -= 3

    if score > 0:
        return ("winner", ", ".join(reasons) if reasons else "marginal up")
    elif score < 0:
        return ("loser", ", ".join(reasons) if reasons else "marginal down")
    else:
        return ("unchanged", "stable")


def main():
    if len(sys.argv) > 1:
        baseline_path = Path(sys.argv[1])
        if not baseline_path.is_absolute():
            baseline_path = ROOT / baseline_path
    else:
        candidates = sorted(GSC_DIR.glob("baseline-*.json"))
        if not candidates:
            print(f"ERROR: no baseline-*.json in {GSC_DIR}", file=sys.stderr)
            sys.exit(1)
        baseline_path = candidates[-1]

    if not baseline_path.exists():
        print(f"ERROR: baseline file not found: {baseline_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Baseline: {baseline_path.relative_to(ROOT)}")

    with open(baseline_path, encoding="utf-8") as f:
        baseline = json.load(f)

    base_window = f"{baseline['window_start']} → {baseline['window_end']}"
    print(f"Baseline window: {base_window}")

    try:
        from googleapiclient.discovery import build
    except ImportError:
        print("ERROR: pip install google-api-python-client", file=sys.stderr)
        sys.exit(1)

    creds = get_credentials()
    service = build("searchconsole", "v1", credentials=creds)

    today = date.today()
    end_date = (today - timedelta(days=3)).isoformat()
    start_date = (today - timedelta(days=17)).isoformat()
    print(f"Current window: {start_date} → {end_date}")
    print()

    urls = list(baseline["urls"].keys())
    print(f"Comparing {len(urls)} URLs...\n")

    results = {}
    winners, losers, unchanged, errors = [], [], [], []

    for i, url in enumerate(urls, 1):
        base_data = baseline["urls"][url]
        cur_data = query_url(service, url, start_date, end_date)
        verdict, reason = classify(base_data, cur_data)
        results[url] = {
            "baseline": base_data,
            "current": cur_data,
            "verdict": verdict,
            "reason": reason,
        }
        marker = {"winner": "🟢", "loser": "🔴", "unchanged": "·", "unknown": "❓"}.get(verdict, "?")
        short_url = url.replace("https://www.fulfillmentmtp.com.ua", "")[-50:]
        if verdict == "winner":
            winners.append((url, reason))
        elif verdict == "loser":
            losers.append((url, reason))
        elif verdict == "unknown":
            errors.append((url, reason))
        else:
            unchanged.append(url)
        print(f"  {marker} [{i:>2}/{len(urls)}] {short_url:<52} {reason}")

    base_total_imp = baseline.get("totals", {}).get("impressions", sum(d.get("impressions", 0) for d in baseline["urls"].values() if "error" not in d))
    base_total_clk = baseline.get("totals", {}).get("clicks", sum(d.get("clicks", 0) for d in baseline["urls"].values() if "error" not in d))
    cur_total_imp = sum(r["current"].get("impressions", 0) for r in results.values() if "error" not in r["current"])
    cur_total_clk = sum(r["current"].get("clicks", 0) for r in results.values() if "error" not in r["current"])

    imp_delta = cur_total_imp - base_total_imp
    imp_delta_pct = (imp_delta / base_total_imp * 100) if base_total_imp > 0 else 0
    clk_delta = cur_total_clk - base_total_clk

    print()
    print("=" * 80)
    print(f"AGGREGATE DELTA")
    print("=" * 80)
    print(f"  Impressions: {base_total_imp:>5} → {cur_total_imp:>5}  ({imp_delta:+5d}, {imp_delta_pct:+.1f}%)")
    print(f"  Clicks:      {base_total_clk:>5} → {cur_total_clk:>5}  ({clk_delta:+5d})")
    print()
    print(f"  🟢 Winners:    {len(winners):>3}")
    print(f"  🔴 Losers:     {len(losers):>3}")
    print(f"  ·  Unchanged:  {len(unchanged):>3}")
    print(f"  ❓ Errors:     {len(errors):>3}")
    print()

    print("=" * 80)
    print("STRATEGY DECISION GATE (per docs/pillar-uplift-strategy.md)")
    print("=" * 80)
    if imp_delta_pct >= 10:
        print(f"  ✅ Aggregate impressions {imp_delta_pct:+.1f}% ≥ +10% — PROCEED Phase B as planned")
    elif imp_delta_pct <= -5:
        print(f"  🔴 Aggregate impressions {imp_delta_pct:+.1f}% ≤ -5% — INVESTIGATE regression before any further changes")
    else:
        print(f"  🟡 Aggregate impressions {imp_delta_pct:+.1f}% within noise band — PIVOT: run psi-audit, gsc-monitor, internal-linking review before more content writing")
    print()

    out_file = GSC_DIR / f"delta-{today.isoformat()}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({
            "baseline_file": str(baseline_path.relative_to(ROOT)),
            "baseline_window": base_window,
            "current_window": f"{start_date} → {end_date}",
            "captured_at": today.isoformat(),
            "totals": {
                "baseline_impressions": base_total_imp,
                "current_impressions": cur_total_imp,
                "imp_delta": imp_delta,
                "imp_delta_pct": round(imp_delta_pct, 2),
                "baseline_clicks": base_total_clk,
                "current_clicks": cur_total_clk,
                "clk_delta": clk_delta,
                "winners": len(winners),
                "losers": len(losers),
                "unchanged": len(unchanged),
            },
            "winners": [{"url": u, "reason": r} for u, r in winners],
            "losers": [{"url": u, "reason": r} for u, r in losers],
            "per_url": results,
        }, f, indent=2, ensure_ascii=False)

    print(f"Full report: {out_file.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
