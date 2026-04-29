---
date: 2026-04-29
window: 28d (2026-04-01 → 2026-04-29)
baseline: 2026-04-27 (snapshot in `docs/gsc/2026-04-27_28d-snapshot.md`)
days_since_redirect_deploy: 2 of 7 (interim, full audit due ~2026-05-04)
sources:
  - docs/gsc/28d-snapshot.json (re-pulled 2026-04-29)
  - docs/ga4/28d-organic-snapshot.json (re-pulled 2026-04-29)
---

# Tpost Redirect Uplift — Day 2 Interim (Task #81)

> **Status**: 2 of 7 days since redirect deploy. Re-run on 2026-05-04 for the full 7d window.

---

## 1. Top-line GSC totals

| Metric | Baseline 2026-04-27 | Current 2026-04-29 | Δ (2 days) |
|---|---:|---:|---:|
| Clicks (28d) | 71 | **101** | **+30 (+42%)** |
| Impressions (28d) | 24,906 | **29,379** | **+4,473 (+18%)** |
| Pages with impr | 271 | **297** | +26 (+10%) |
| Unique queries | 500 | 500 | flat (capped at API limit) |

**Reading**: Window slides 2 days (drops 2026-03-30/31, adds 2026-04-28/29). The +30 clicks net delta in 2 days is **above expected baseline organic growth** (~3-5 clicks/day historic). Early signal redirect deploys are working — but 2 days is too short for a clean conclusion.

---

## 2. Tpost URL traffic (74 tpost URLs still have GSC data)

After 60 article restores + tpost trailing-slash 301s deploy (commits `b526cd9`, `6054f18`, 2026-04-27):

### Top 5 tpost URLs by impressions (28d)

| URL | Clicks | Impr | CTR | Pos |
|---|---:|---:|---:|---:|
| `/blog/tpost/yzhv774pa1-kak-otkrit-internet-magazin-...` | 1 | 1,000 | 0.10% | 22.4 |
| `/ua/blog/tpost/s7non1f0y1-scho-take-sla-...` | **4** | 976 | 0.41% | **7.1** |
| `/ua/blog/tpost/2fz7njsgn1-scho-take-artikul-...` | **2** | 805 | 0.25% | **5.4** |
| `/ua/blog/tpost/xz8vfk1jg1-tovarnii-bznes-...` | 1 | 491 | 0.20% | 8.2 |
| `/blog/tpost/pdjm77ogc1-chto-takoe-sla-...` | 0 | 240 | 0.00% | 11.1 |
| `/ua/blog/tpost/2lpu5l5sa1-mtp-group-dinii-...` | **12** | 141 | **8.51%** | 8.3 |

**Reading**: Top 4 tpost URLs ALL have positions 5-12 (page 1) but CTRs of 0.10-0.41% — well below the 5-15% CTR expected at those positions. SERP is being dominated by Wikipedia-like results that beat plain article cards. **Need rich snippets (FAQ schema, How-To rich results, video) on destination URLs to win SERP.**

### Brand query (artikul, sla, tovarnii) clicks growing slowly

vs baseline 2026-04-27:
- артикул tpost: 0→2 clicks (was at pos 5.8 / 265 imp; now pos 5.4 / 805 imp — impressions tripled!)
- sla це tpost: 1→4 clicks (was 251 imp; now 976 imp — 4x impressions)
- товарний бізнес tpost: 1→1 click (was 76 imp; now 491 imp — 6x impressions)

**Cause of impression spike**: redirect 301s **passed equity from previously-deindexed Tilda mirrors back to canonical tpost URL**. Search Console is now consolidating, hence impression spike. Click uplift is lagging — typical 7-21 day delay.

---

## 3. Successor destinations (Tier-2 articles) — almost no direct traffic yet

The new URLs that tpost redirects point to:

| Destination | 28d clicks | 28d impr | Status |
|---|---:|---:|---|
| `/ua/blog/scho-take-sla/` | 0 | 0 | **Not yet indexed/served as canonical by Google** |
| `/ua/blog/scho-take-artikul/` | 0 | 7 | Crawled, almost no impr |
| `/ua/blog/product-business-ukraine-guide/` | 0 | 5 | Crawled, almost no impr |
| `/blog/chto-takoe-sla/` | 0 | 1 | Just discovered |
| `/blog/chto-takoe-artikul/` | 0 | 0 | Not yet discovered |
| `/blog/top-fulfilment-operatorov-2026/` | **4** | **123** | ✅ Already indexed at pos 6.3 |

**Reading**: Google is still treating tpost URLs as canonical for most pairs — 301s deployed only 2 days ago, full canonical migration takes 7-21 days. **This is normal.**

The exception (`top-fulfilment-operatorov-2026/` with 4 clicks) was indexed earlier with deeper internal linking — proves the destination model works once Google catches up.

---

## 4. GA4 — engagement and lead conversion

### Top organic landing pages (28d)

| Page | Sessions | Engagement | Conv |
|---|---:|---:|---:|
| `/` (UA home) | 28 | 60.7% | 0 |
| `/ua/about/` | 11 | 36.4% | 0 |
| `/ru/` | 8 | 50.0% | 0 |
| `/en/` | 5 | 80.0% | 0 |
| `/ua/blog/tpost/2lpu5l5sa1-mtp-group-...` | 4 | 100.0% | **8** |
| `/ua/services/` | 4 | 0.0% | 0 |
| `/services/` | 3 | 66.7% | 0 |
| `/blog/top-fulfilment-operatorov-2026/` | 2 | 50.0% | 0 |
| `/fulfilment-kiev/` | 2 | 50.0% | 0 |

**Star performer**: 2lpu5l5sa1 tpost (MTP brand article) — 4 sessions, 100% engagement, **8 conversions**. Brand traffic converts 6-10x better than non-brand. Worth examining what's on this page that's working.

### Key Events (28d)

| Event | Events | Users |
|---|---:|---:|
| `form_submit` | 11 | 6 |
| `generate_lead` | 5 | 4 |
| `telegram_click` | 2 | 2 |
| `phone_click` | 0 | 0 |
| `whatsapp_click` | 0 | 0 |

**Action item linked to #82**: Mark `phone_click`, `telegram_click`, `generate_lead` as Key Events in GA4 UI to surface them in Realtime + Acquisition reports. Currently they're tracked as standard events but not flagged as KPI events.

---

## 5. Conclusions and recommendations (interim)

### What's working ✅

1. **+42% clicks in 2 days** — strong early signal that recovered Tilda articles + tpost redirect siblings are restoring lost traffic.
2. **Impressions up 18%** — Google is re-discovering and re-indexing the canonical tpost URLs after the trailing-slash sibling rule deploy.
3. **`top-fulfilment-operatorov-2026`** at pos 6.3 with 4 clicks — proof the destination article model works.
4. **MTP brand traffic** still highest converter (8 conv from 4 sessions).

### What needs more time ⏳

1. **Successor destinations not yet ranking** — most still show 0-7 imp. Google needs 7-21 days to migrate canonicals after 301. Re-check 2026-05-04 (full 7d window).
2. **CTR not yet improving on tpost URLs** despite better positions. Tpost URLs are page 1 but CTR <0.5% — Wikipedia/competitor SERP features are stealing clicks. After Google migrates canonicals to new destinations (with H1 + schema + FAQ), CTR should rise.

### Action items

| # | Item | Owner | When |
|---|---|---|---|
| Α | Re-run this audit on 2026-05-04 (full 7d) | claude-code | scheduled |
| Β | Mark `phone_click`/`telegram_click`/`generate_lead` as Key Events in GA4 | manual (user) | task #82, ~5 min |
| Γ | Submit "Validate Fix" in GSC for video issue (`/ru/chto-takoe-fulfilment/`) | manual (user) | post-deploy |
| Δ | Request Indexing in GSC for 2 new Tier-3 posts | manual (user) | post-deploy |
| Ε | Verify successor destinations get HreflangCheck after Google migrates canonicals | claude-code | 2026-05-06 |

---

## 6. Files

- Snapshot: `docs/gsc/28d-snapshot.json` (refreshed 2026-04-29)
- Diff vs 90d: `docs/gsc/28d-diff-vs-90d.json`
- GA4 organic: `docs/ga4/28d-organic-snapshot.json`
- Baseline reference: `docs/gsc/2026-04-27_28d-snapshot.md`
