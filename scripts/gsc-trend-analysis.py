#!/usr/bin/env python3
"""gsc-trend-analysis.py — Weekly trend analysis since GSC property creation.

GSC property `sc-domain:fulfillmentmtp.com.ua` was verified ~early April 2026
(during CF Pages migration). No data before that date. Therefore we can't
do "since Jan 2026" trend analysis — instead pull weekly slices since Apr 1
(when data first appeared) and report what's actually visible.

Output: markdown report with weekly totals, MoW deltas, query trajectory,
top pages, geo + device, strategic recs.
"""

import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path("/Users/nikolaj/My vibecode aplications/profm-site-astro")
sys.path.insert(0, str(ROOT / "scripts"))

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/webmasters",
    "https://www.googleapis.com/auth/indexing",
]
TOKEN_FILE = ROOT / "scripts" / "gsc_token.json"
SITE = "sc-domain:fulfillmentmtp.com.ua"
OUT_DIR = ROOT / "docs" / "gsc"
TODAY = date.today()

# Weekly slices since GSC property creation date (~Apr 1 2026).
# 5 windows of 7 days each = 35 days covering Apr + first week of May.
WINDOWS = [
    ("Apr W1 (1-7)",   "2026-04-01", "2026-04-07"),
    ("Apr W2 (8-14)",  "2026-04-08", "2026-04-14"),
    ("Apr W3 (15-21)", "2026-04-15", "2026-04-21"),
    ("Apr W4 (22-28)", "2026-04-22", "2026-04-28"),
    ("Apr-May W5",     "2026-04-29", "2026-05-02"),  # 4 days, partial
]


def get_service():
    creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("searchconsole", "v1", credentials=creds)


def query(service, start, end, dimensions, row_limit=25000):
    """Run one GSC search analytics query. row_limit=25000 max per API."""
    body = {
        "startDate": start,
        "endDate": end,
        "dimensions": dimensions,
        "rowLimit": row_limit,
    }
    resp = service.searchanalytics().query(siteUrl=SITE, body=body).execute()
    return resp.get("rows", [])


def site_totals_real(service, start, end):
    """Pull TRUE site totals via no-dimension query (avoids row_limit truncation)."""
    body = {"startDate": start, "endDate": end, "dimensions": []}
    resp = service.searchanalytics().query(siteUrl=SITE, body=body).execute()
    rows = resp.get("rows", [])
    if not rows:
        return 0, 0, 0, 0
    r = rows[0]
    imp = r.get("impressions", 0)
    clk = r.get("clicks", 0)
    ctr = clk / imp if imp else 0
    pos = r.get("position", 0)
    return imp, clk, ctr, pos


def short_url(url):
    return url.replace("https://www.fulfillmentmtp.com.ua", "") or "/"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    service = get_service()

    print(f"Pulling GSC data for {len(WINDOWS)} weekly windows...")
    monthly = {}
    for label, start, end in WINDOWS:
        print(f"  {label}: {start} → {end}")
        # Site totals (no-dimension query for accurate count)
        totals = site_totals_real(service, start, end)
        # Top pages (raise row_limit to avoid truncation)
        rows_p = query(service, start, end, ["page"], row_limit=1000)
        # Top queries
        rows_q = query(service, start, end, ["query"], row_limit=1000)
        # Country
        rows_c = query(service, start, end, ["country"], row_limit=30)
        # Device
        rows_d = query(service, start, end, ["device"], row_limit=10)
        monthly[label] = {
            "rows_p": rows_p,
            "rows_q": rows_q,
            "rows_c": rows_c,
            "rows_d": rows_d,
            "totals": totals,
        }

    # ============== Build report ==============
    out = []
    out.append(f"# GSC Trend Analysis — April 2026 weekly trajectory")
    out.append(f"")
    out.append(f"**Generated:** {TODAY.isoformat()}  ")
    out.append(f"**Site:** `{SITE}`  ")
    out.append(f"**Windows:** {' · '.join(w[0] for w in WINDOWS)}  ")
    out.append(f"")
    out.append("> ⚠️ **Data limitation.** GSC property `sc-domain:fulfillmentmtp.com.ua`")
    out.append("> was verified ~early April 2026 (during CF Pages migration). No GSC")
    out.append("> data exists before 2026-04-01. We cannot do 'since Jan 2026' analysis;")
    out.append("> instead this report uses 5 weekly slices from Apr 1 → May 2.")
    out.append(">")
    out.append("> If you need pre-Apr data, sources outside GSC are needed: Google")
    out.append("> Analytics 4 (if it was running on the old site), Tilda Analytics,")
    out.append("> or referrer logs from the previous Vercel/Tilda hosting.")
    out.append("")
    out.append("---")
    out.append("")

    # ===== Section 1: Site-level totals =====
    out.append("## 1. Site-level weekly totals")
    out.append("")
    out.append("| Week | Days | Impressions | Clicks | CTR | Avg Position |")
    out.append("|---|---:|---:|---:|---:|---:|")
    for label, start, end in WINDOWS:
        imp, clk, ctr, pos = monthly[label]["totals"]
        days = (date.fromisoformat(end) - date.fromisoformat(start)).days + 1
        out.append(f"| {label} | {days} | {imp:,} | {clk:,} | {ctr*100:.2f}% | {pos:.1f} |")
    out.append("")

    # WoW deltas
    out.append("### Week-over-week changes")
    out.append("")
    out.append("| Period | Δ Impressions | Δ Clicks | Δ CTR | Δ Avg Pos |")
    out.append("|---|---:|---:|---:|---:|")
    for i in range(1, len(WINDOWS)):
        prev_label = WINDOWS[i-1][0]
        cur_label = WINDOWS[i][0]
        p_imp, p_clk, p_ctr, p_pos = monthly[prev_label]["totals"]
        c_imp, c_clk, c_ctr, c_pos = monthly[cur_label]["totals"]
        d_imp = c_imp - p_imp
        d_imp_pct = (d_imp / p_imp * 100) if p_imp else 0
        d_clk = c_clk - p_clk
        d_clk_pct = (d_clk / p_clk * 100) if p_clk else 0
        d_ctr = (c_ctr - p_ctr) * 100
        d_pos = c_pos - p_pos
        out.append(f"| {prev_label} → {cur_label} | {d_imp:+,} ({d_imp_pct:+.1f}%) | {d_clk:+,} ({d_clk_pct:+.1f}%) | {d_ctr:+.2f}pp | {d_pos:+.1f} |")
    out.append("")

    # Effective baseline: first window with imp > 0 (handles property-added-mid-April case)
    w1_label = next((w[0] for w in WINDOWS if monthly[w[0]]["totals"][0] > 0), WINDOWS[0][0])
    w4_label = WINDOWS[3][0]  # last full week (Apr 22-28)
    if w1_label != WINDOWS[0][0]:
        out.append(f"> 📌 First week with non-zero data: **{w1_label}** (earlier weeks had 0 imp — GSC property still indexing).")
        out.append("")
    w1_imp = monthly[w1_label]["totals"][0]
    w4_imp = monthly[w4_label]["totals"][0]
    w1_clk = monthly[w1_label]["totals"][1]
    w4_clk = monthly[w4_label]["totals"][1]
    overall_imp_pct = ((w4_imp - w1_imp) / w1_imp * 100) if w1_imp else 0
    overall_clk_pct = ((w4_clk - w1_clk) / w1_clk * 100) if w1_clk else 0
    out.append("### Apr W1 → W4 trajectory (full weeks only)")
    out.append("")
    out.append(f"- **Impressions:** {w1_imp:,} (W1) → {w4_imp:,} (W4) = **{overall_imp_pct:+.1f}%** over 4 weeks")
    out.append(f"- **Clicks:** {w1_clk:,} (W1) → {w4_clk:,} (W4) = **{overall_clk_pct:+.1f}%** over 4 weeks")
    if overall_imp_pct > 30:
        out.append(f"- 🟢 **Trajectory: STRONG GROWTH** — impressions up {overall_imp_pct:.0f}% across April. Indexation + content cadence working.")
    elif overall_imp_pct > 5:
        out.append(f"- 🟡 **Trajectory: MODERATE GROWTH** — impressions up {overall_imp_pct:.0f}% across April. Below high-growth threshold but positive.")
    elif overall_imp_pct > -5:
        out.append(f"- ⚪ **Trajectory: STABLE** — impressions {overall_imp_pct:+.0f}% across April. Likely indexation steady-state.")
    else:
        out.append(f"- 🔴 **Trajectory: DECLINING** — impressions down {abs(overall_imp_pct):.0f}% across April. Investigate.")
    out.append("")
    out.append("---")
    out.append("")

    # ===== Section 2: Top queries trend =====
    out.append("## 2. Top queries trend (Apr W1 vs W4)")
    out.append("")
    out.append("Top 25 queries by Apr W4 impressions, with W1 baseline. Position negative delta = better ranking. NEW = entered after W1.")
    out.append("")

    jan_qmap = {r["keys"][0]: r for r in monthly[w1_label]["rows_q"]}
    apr_qmap = {r["keys"][0]: r for r in monthly[w4_label]["rows_q"]}
    apr_top = sorted(monthly[w4_label]["rows_q"], key=lambda r: -r.get("impressions", 0))[:25]

    out.append("| # | Query | W4 Imp | W4 Pos | Δ Imp (W1→W4) | Δ Pos (W1→W4) |")
    out.append("|---:|---|---:|---:|---|---|")
    for i, r in enumerate(apr_top, 1):
        q = r["keys"][0]
        a_imp = r.get("impressions", 0)
        a_pos = r.get("position", 0)
        j = jan_qmap.get(q)
        if j:
            j_imp = j.get("impressions", 0)
            j_pos = j.get("position", 0)
            d_imp = a_imp - j_imp
            d_imp_pct = (d_imp / j_imp * 100) if j_imp else 0
            d_pos = a_pos - j_pos
            d_imp_str = f"{d_imp:+d} ({d_imp_pct:+.0f}%)"
            d_pos_str = f"{d_pos:+.1f}" + (" 🟢" if d_pos < -1 else (" 🔴" if d_pos > 1 else ""))
        else:
            d_imp_str = f"NEW (+{a_imp})"
            d_pos_str = "NEW"
        # Truncate long queries
        q_disp = q if len(q) < 50 else q[:47] + "..."
        out.append(f"| {i} | `{q_disp}` | {a_imp} | {a_pos:.1f} | {d_imp_str} | {d_pos_str} |")
    out.append("")

    # ===== Section 3: Trending queries (biggest movers) =====
    out.append("## 3. Biggest movers (queries that grew or shrank most)")
    out.append("")

    # Common queries Jan + Apr
    common = set(jan_qmap) & set(apr_qmap)
    movements = []
    for q in common:
        j = jan_qmap[q]
        a = apr_qmap[q]
        j_imp = j.get("impressions", 0)
        a_imp = a.get("impressions", 0)
        j_pos = j.get("position", 0)
        a_pos = a.get("position", 0)
        d_imp = a_imp - j_imp
        d_pos = a_pos - j_pos
        # Score by absolute impression change, weighted by sample size
        if j_imp >= 5 or a_imp >= 5:
            movements.append((q, j_imp, a_imp, j_pos, a_pos, d_imp, d_pos))

    out.append("### 🟢 Top 10 RISERS (gained impressions)")
    out.append("")
    out.append("| Query | Jan | Apr | Δ Imp | Jan Pos | Apr Pos | Δ Pos |")
    out.append("|---|---:|---:|---:|---:|---:|---:|")
    risers = sorted(movements, key=lambda m: -m[5])[:10]
    for q, ji, ai, jp, ap, di, dp in risers:
        q_disp = q if len(q) < 45 else q[:42] + "..."
        out.append(f"| `{q_disp}` | {ji} | {ai} | {di:+d} | {jp:.1f} | {ap:.1f} | {dp:+.1f} |")
    out.append("")

    out.append("### 🔴 Top 10 FALLERS (lost impressions)")
    out.append("")
    out.append("| Query | Jan | Apr | Δ Imp | Jan Pos | Apr Pos | Δ Pos |")
    out.append("|---|---:|---:|---:|---:|---:|---:|")
    fallers = sorted(movements, key=lambda m: m[5])[:10]
    for q, ji, ai, jp, ap, di, dp in fallers:
        q_disp = q if len(q) < 45 else q[:42] + "..."
        out.append(f"| `{q_disp}` | {ji} | {ai} | {di:+d} | {jp:.1f} | {ap:.1f} | {dp:+.1f} |")
    out.append("")

    # New queries entering Apr that weren't in Jan
    only_apr = set(apr_qmap) - set(jan_qmap)
    if only_apr:
        out.append("### 🆕 Top 10 NEW queries (appeared in W4, absent in W1)")
        out.append("")
        out.append("| Query | Apr Imp | Apr Pos |")
        out.append("|---|---:|---:|")
        new_q = sorted([(q, apr_qmap[q]) for q in only_apr], key=lambda x: -x[1].get("impressions", 0))[:10]
        for q, r in new_q:
            q_disp = q if len(q) < 50 else q[:47] + "..."
            out.append(f"| `{q_disp}` | {r.get('impressions',0)} | {r.get('position',0):.1f} |")
        out.append("")

    only_jan = set(jan_qmap) - set(apr_qmap)
    if only_jan:
        sorted_only_jan = sorted([(q, jan_qmap[q]) for q in only_jan], key=lambda x: -x[1].get("impressions", 0))[:10]
        if sorted_only_jan and sorted_only_jan[0][1].get("impressions", 0) >= 3:
            out.append("### 👻 Top 10 LOST queries (in W1, gone by W4)")
            out.append("")
            out.append("| Query | Jan Imp | Jan Pos |")
            out.append("|---|---:|---:|")
            for q, r in sorted_only_jan:
                q_disp = q if len(q) < 50 else q[:47] + "..."
                out.append(f"| `{q_disp}` | {r.get('impressions',0)} | {r.get('position',0):.1f} |")
            out.append("")

    out.append("---")
    out.append("")

    # ===== Section 4: Top pages trend =====
    out.append("## 4. Top pages trend (Apr W1 vs W4)")
    out.append("")
    out.append("Top 25 pages by Apr W4 impressions, with W1 baseline.")
    out.append("")

    jan_pmap = {r["keys"][0]: r for r in monthly[w1_label]["rows_p"]}
    apr_pmap = {r["keys"][0]: r for r in monthly[w4_label]["rows_p"]}
    apr_top_p = sorted(monthly[w4_label]["rows_p"], key=lambda r: -r.get("impressions", 0))[:25]

    out.append("| # | Page | W4 Imp | W4 Clk | W4 Pos | Δ Imp (W1→W4) |")
    out.append("|---:|---|---:|---:|---:|---|")
    for i, r in enumerate(apr_top_p, 1):
        url = r["keys"][0]
        a_imp = r.get("impressions", 0)
        a_clk = r.get("clicks", 0)
        a_pos = r.get("position", 0)
        j = jan_pmap.get(url)
        if j:
            j_imp = j.get("impressions", 0)
            d_imp = a_imp - j_imp
            d_imp_pct = (d_imp / j_imp * 100) if j_imp else 0
            d_imp_str = f"{d_imp:+d} ({d_imp_pct:+.0f}%)"
        else:
            d_imp_str = f"NEW (+{a_imp})"
        out.append(f"| {i} | `{short_url(url)}` | {a_imp} | {a_clk} | {a_pos:.1f} | {d_imp_str} |")
    out.append("")

    out.append("---")
    out.append("")

    # ===== Section 5: Country + Device =====
    out.append(f"## 5. Geographic + device breakdown ({w4_label})")
    out.append("")
    out.append("### Top 10 countries by impressions")
    out.append("")
    out.append("| Country | Imp | Clk | CTR | Pos |")
    out.append("|---|---:|---:|---:|---:|")
    for r in sorted(monthly[w4_label]["rows_c"], key=lambda x: -x.get("impressions", 0))[:10]:
        c = r["keys"][0]
        imp = r.get("impressions", 0)
        clk = r.get("clicks", 0)
        ctr = clk / imp * 100 if imp else 0
        pos = r.get("position", 0)
        out.append(f"| {c} | {imp:,} | {clk} | {ctr:.2f}% | {pos:.1f} |")
    out.append("")

    out.append("### Device split")
    out.append("")
    out.append("| Device | Imp | Clk | CTR | Pos |")
    out.append("|---|---:|---:|---:|---:|")
    for r in monthly[w4_label]["rows_d"]:
        d = r["keys"][0]
        imp = r.get("impressions", 0)
        clk = r.get("clicks", 0)
        ctr = clk / imp * 100 if imp else 0
        pos = r.get("position", 0)
        out.append(f"| {d} | {imp:,} | {clk} | {ctr:.2f}% | {pos:.1f} |")
    out.append("")

    out.append("---")
    out.append("")

    # ===== Section 6: Strategic findings + recommendations =====
    out.append("## 6. Strategic findings + recommendations")
    out.append("")

    # Auto-derive findings from data
    findings = []
    risers_top3 = sorted(movements, key=lambda m: -m[5])[:3]
    fallers_top3 = sorted(movements, key=lambda m: m[5])[:3]

    findings.append(f"**Apr W1 → W4:** impressions {w1_imp:,} → {w4_imp:,} ({overall_imp_pct:+.1f}%); clicks {w1_clk:,} → {w4_clk:,} ({overall_clk_pct:+.1f}%).")

    # Position trajectory
    apr_pos = monthly[w4_label]["totals"][3]
    jan_pos = monthly[w1_label]["totals"][3]
    pos_delta = apr_pos - jan_pos
    if pos_delta < -2:
        findings.append(f"**Avg position improving:** W1 {jan_pos:.1f} → W4 {apr_pos:.1f} ({pos_delta:+.1f}). Pages climbing toward visibility threshold.")
    elif pos_delta > 2:
        findings.append(f"**Avg position deteriorating:** W1 {jan_pos:.1f} → W4 {apr_pos:.1f} ({pos_delta:+.1f}). Likely caused by more long-tail queries entering at low positions (good for breadth, bad for weighted avg).")
    else:
        findings.append(f"**Avg position stable:** W1 {jan_pos:.1f} → W4 {apr_pos:.1f}.")

    if risers_top3:
        top_riser = risers_top3[0]
        findings.append(f"**Biggest query winner:** `{top_riser[0]}` — {top_riser[1]}→{top_riser[2]} imp ({top_riser[5]:+d}), pos {top_riser[3]:.1f}→{top_riser[4]:.1f}.")
    if fallers_top3:
        top_faller = fallers_top3[0]
        findings.append(f"**Biggest query loss:** `{top_faller[0]}` — {top_faller[1]}→{top_faller[2]} imp ({top_faller[5]:+d}), pos {top_faller[3]:.1f}→{top_faller[4]:.1f}.")

    # New queries breadth
    new_count = len(only_apr)
    findings.append(f"**Query breadth expansion:** {new_count} queries appeared in W4 that weren't in W1. {len(only_jan)} disappeared.")

    # CTR insight
    apr_ctr = monthly[w4_label]["totals"][2]
    jan_ctr = monthly[w1_label]["totals"][2]
    findings.append(f"**CTR trajectory:** {jan_ctr*100:.2f}% (W1) → {apr_ctr*100:.2f}% (W4). " + (
        "Improving — title/description optimization may be paying off." if apr_ctr > jan_ctr else
        "Declining — pages ranking but not converting clicks. Investigate title/snippet quality."
    ))

    # Country dominance
    if monthly[w4_label]["rows_c"]:
        top_c = sorted(monthly[w4_label]["rows_c"], key=lambda x: -x.get("impressions", 0))[0]
        c_share = top_c.get("impressions", 0) / w4_imp * 100 if w4_imp else 0
        findings.append(f"**Geographic concentration:** {top_c['keys'][0]} = {c_share:.0f}% of W4 impressions.")

    # Device split
    if monthly[w4_label]["rows_d"]:
        d_map = {r["keys"][0]: r.get("impressions", 0) for r in monthly[w4_label]["rows_d"]}
        mob = d_map.get("MOBILE", 0)
        des = d_map.get("DESKTOP", 0)
        if mob and des:
            mob_share = mob / (mob + des + d_map.get("TABLET", 0)) * 100
            findings.append(f"**Device split:** mobile {mob_share:.0f}% / desktop {(des/(mob+des+d_map.get('TABLET',0)))*100:.0f}%.")

    out.append("### Key findings")
    out.append("")
    for f in findings:
        out.append(f"- {f}")
    out.append("")

    # Recommendations
    out.append("### Recommendations (data-driven)")
    out.append("")
    recs = []
    if overall_imp_pct > 20:
        recs.append("**Continue current Phase B cadence** — impression growth >20% YTD validates the content + reindex strategy. Maintain weekly pillar uplift cycle.")
    elif overall_imp_pct > 0:
        recs.append("**Maintain content cadence but investigate stalling causes** — modest growth suggests ceiling effect. Audit (a) Core Web Vitals on top-traffic pillars, (b) backlink profile, (c) brand search trend.")
    else:
        recs.append("**Pause new content, run root-cause analysis** — declining impressions need explanation before more content investment. Check (a) GSC Coverage report for indexation drops, (b) Manual Actions, (c) algorithm update overlap with our deploy timeline.")

    if apr_ctr < jan_ctr:
        recs.append("**CTR optimization batch** — pages rank but don't convert clicks. Audit titles + meta descriptions for top-20 queries (especially RU/UA where mobile fold is small).")

    if new_count > 20:
        recs.append(f"**Capitalize on query breadth expansion** — {new_count} new queries appeared in Apr. Pull `query` dimension monthly and add FAQ items targeting top new queries before they get crowded out.")

    if fallers_top3 and fallers_top3[0][5] < -10:
        recs.append(f"**Investigate top fallers** — `{fallers_top3[0][0]}` lost {abs(fallers_top3[0][5])} imp. Check if competitors took position or our page ranking dropped (use this report's 'top fallers' table).")

    recs.append("**Re-run this trend analysis monthly** (`python3 scripts/gsc-trend-analysis.py`) to track trajectory and catch regressions early.")

    for r in recs:
        out.append(f"- {r}")
    out.append("")

    out.append("---")
    out.append("")
    out.append("## Methodology + caveats")
    out.append("")
    out.append("- Data source: Google Search Console Search Analytics API")
    out.append("- Site filter: `sc-domain:fulfillmentmtp.com.ua` (all subdomains incl. www)")
    out.append("- **GSC property added ~Apr 1 2026** — no data exists before this date in GSC")
    out.append("- Windows: 4 full weeks Apr 1-28 + 1 partial week Apr 29 - May 2 (4 days, included for trend continuity)")
    out.append("- Site totals computed via no-dimension query (avoids row_limit truncation that occurs with dimensioned queries)")
    out.append("- Position = weighted average across all queries (each query weighted by its impression count)")
    out.append("- 'Mover' analysis filters to queries with ≥5 impressions in either window to reduce noise")
    out.append("- 'New' / 'lost' query lists are top-10 limited and may include long-tail noise")
    out.append("- GSC reports CTR after deduplication; impressions count once per SERP appearance regardless of scroll")
    out.append("- AI Overviews citations not separable in current API (will be in 2026-Q3 per Google roadmap)")
    out.append("- For pre-Apr 2026 historical data: use Google Analytics 4 if it was running, Tilda Analytics from old hosting, or referrer logs")
    out.append("")
    out.append("*Generated by `scripts/gsc-trend-analysis.py`. Re-run anytime for fresh data.*")

    out_path = OUT_DIR / f"trend-analysis-{TODAY.isoformat()}.md"
    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"\n✅ Report written: {out_path.relative_to(ROOT)}")
    print(f"   Length: {sum(len(line) for line in out):,} chars, {len(out)} lines")

    return out_path


if __name__ == "__main__":
    main()
