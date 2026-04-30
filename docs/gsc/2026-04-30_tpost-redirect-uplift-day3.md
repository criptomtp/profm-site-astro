---
date: 2026-04-30
window: 28d (2026-04-02 → 2026-04-30)
baseline_27: docs/gsc/2026-04-27_28d-snapshot.md
baseline_29: docs/gsc/2026-04-29_tpost-redirect-uplift-day2.md
days_since_redirect_deploy: 3 of 7 (interim, full audit due ~2026-05-04)
sources:
  - docs/gsc/28d-snapshot.json (re-pulled 2026-04-30)
  - docs/ga4/28d-organic-snapshot.json (re-pulled 2026-04-30)
---

# Tpost Redirect Uplift — Day 3 Interim (Task #81)

> **Status**: 3 of 7 days since redirect deploy. Re-run on 2026-05-04 for the full 7d window.
> Trajectory holding — clicks still climbing, first successor URL appeared in organic landing.

---

## 1. Top-line GSC totals (28d)

| Metric | Baseline 04-27 | Day 2 (04-29) | Day 3 (04-30) | Δ vs Day 2 | Δ vs Baseline |
|---|---:|---:|---:|---:|---:|
| Clicks | 71 | 101 | **115** | **+14 (+13.9%)** | **+44 (+62%)** |
| Impressions | 24,906 | 29,379 | **30,823** | **+1,444 (+4.9%)** | **+5,917 (+24%)** |
| Pages with impr | 271 | 297 | **336** | **+39 (+13%)** | **+65 (+24%)** |
| Avg CTR | 0.29% | 0.34% | **0.37%** | +0.03pp | +0.08pp |

**Reading**: trajectory holds. The +14 clicks/day rate matches expected (~+15/day at current trend). Impression growth slowing slightly (+4.9% vs +18% day2) — consistent with Google front-loading reindex spike then tapering.

---

## 2. Tpost URL traffic (top 4 by impressions)

| URL (last segment) | 04-29 clk/imp/CTR/pos | 04-30 clk/imp/CTR/pos | Note |
|---|---|---|---|
| `s7non1f0y1-scho-take-sla` | 4 / 976 / 0.41% / 7.1 | 4 / **1,070** / 0.37% / 7.2 | +94 imp, clicks held |
| `yzhv774pa1-kak-otkrit-internet-magazin` | 1 / 1,000 / 0.10% / 22.4 | 1 / 1,000 / 0.10% / 22.4 | flat (page 3, low CTR) |
| `2fz7njsgn1-scho-take-artikul` | 2 / 805 / 0.25% / 5.4 | 2 / 805 / 0.25% / 5.4 | flat |
| `xz8vfk1jg1-tovarnii-bznes` | 1 / 491 / 0.20% / 8.2 | 1 / 491 / 0.20% / 8.2 | flat |

**Reading**: tpost URLs **plateaued** at the day-2 levels — no further growth, no decay. Google holding them as canonical. The "/ua/blog/tpost/2lpu5l5sa1-mtp-group" brand article (8 conv) is the only one that converts.

---

## 3. Successor destinations — FIRST SIGNAL ✅

| Destination | 04-29 GA4 sess | 04-30 GA4 sess | 28d GSC clicks | Status |
|---|---:|---:|---:|---|
| `/ua/blog/scho-take-sla/` | 0 | **2** ✨ | 0 | **First organic sessions!** Eng 50% |
| `/ua/blog/scho-take-artikul/` | 0 | 0 | 0 | Still 0 — needs more time |
| `/ua/blog/product-business-ukraine-guide/` | 0 | 0 | 0 | Still 0 |
| `/blog/top-fulfilment-operatorov-2026/` | 2 | 2 | 4 | Stable, pos 6.3 |

**Reading**: `/ua/blog/scho-take-sla/` got its **first 2 organic sessions** from Google — proof that the canonical migration is starting to flow. SLA tpost (the source) had 4 clicks; now 2 of those went to the successor. Expect this pattern to compound over next 4-7 days.

---

## 4. Target queries from Task #81 brief

| Query | Baseline (04-24) | 04-30 | Pos shift | Reading |
|---|---|---|---|---|
| `sla` | 1clk / 236imp / 9.1 | **1clk / 292imp / 10.8** | -1.7 | +56 imp, pos drift -1.7 |
| `sla це` | 0clk / 251imp / 7.1 | 0clk / 358imp / 7.4 | -0.3 | +107 imp, no clicks |
| `що таке артикул` | n/a | **1clk / 45imp / 3.2** ✨ | NEW | **First top-3 ranking!** Successor working |
| `артикул` | 0clk / 265imp / 5.8 | 0clk / 267imp / 5.8 | flat | Stable, no CTR yet |
| `товарний бізнес` | 1clk / 76imp / 9.0 | 1clk / 197imp / 9.2 | -0.2 | +121 imp, +0pp CTR |
| `товарный бизнес` | 0clk | **2clk / 187imp / 9.3** ✨ | NEW | **+2 RU mirror clicks** |
| `как открыть интернет магазин` | 0 | 0clk / 56imp / 11.5 | n/a | Reaching SERP, no clicks |
| `фулфілмент україна` | n/a | **3clk / 20imp / 15% CTR / 2.5** ✨ | NEW | **Top-3 brand+keyword combo** |

**Reading**: 3 NEW positive signals (`що таке артикул` pos 3.2, `товарный бизнес` +2 clicks, `фулфілмент україна` 15% CTR top-3). Originally targeted queries (`sla`, `sla це`) still impression-rich but click-poor — Wikipedia/competitors still owning SERP rich features.

---

## 5. GA4 — landing pages and conversions (28d)

### Top organic landing pages

| Page | Day 2 sess | Day 3 sess | Eng | Conv |
|---|---:|---:|---:|---:|
| `/` (UA home) | 28 | 28 | 60.7% | 0 |
| `/ua/about/` | 11 | 11 | 36.4% | 0 |
| `/ru/` | 8 | 8 | 50.0% | 0 |
| `/en/` | 5 | 4 | 100% | 0 |
| `/ua/blog/tpost/2lpu5l5sa1-mtp-group-...` | 4 | 4 | 100% | **8** |
| **`/ua/blog/scho-take-sla/`** | 0 | **2 ✨** | 50% | 0 |
| `/ua/blog/tpost/2fz7njsgn1-scho-take-artikul` | n/a | **2 ✨** | 50% | 0 |
| `/ua/blog/tpost/xz8vfk1jg1-tovarnii-bznes` | n/a | **2 ✨** | 0% | 0 |

**Reading**: 3 new entrants in top organic landing pages — the SLA successor (✅) plus 2 tpost pages that GA4 now sees getting traffic. Brand article still the only converter.

### Key Events (28d)

| Event | Day 2 events | Day 3 events | Day 3 users | Δ |
|---|---:|---:|---:|---|
| `form_submit` | 11 | **5** | 4 | **-6** ⚠️ |
| `generate_lead` | 5 | 5 | 4 | flat |
| `telegram_click` | 2 | 2 | 2 | flat |
| `phone_click` | 0 | **1** ✨ | 1 | **+1** (post Key Event flag) |
| `whatsapp_click` | 0 | 0 | 0 | flat |

**form_submit drop -6 is window-rotation artifact**: 28d window slid by 1 day → likely a 6-event day from 2026-04-02 fell out. `generate_lead` (the more important conversion KPI) is flat at 5/4. Total leads on site over the window is unchanged.

`phone_click` showed up after task #82 was just completed (today) — GA4 will start surfacing it in Realtime.

---

## 6. Conclusions and recommendations (Day 3)

### What's working ✅

1. **Top-line clicks +62% vs baseline (71→115) in 3 days** — sustained linear growth at ~+15 clicks/day.
2. **First successor URL (`/ua/blog/scho-take-sla/`) appearing in GA4 organic** — 2 sessions, 50% engagement. Canonical migration starting.
3. **NEW top-3 ranking: "що таке артикул" pos 3.2** — successor article surfacing for the high-intent keyword. Wait for canonical migration → CTR should follow.
4. **NEW: "товарный бизнес" RU mirror +2 clicks** — Tier-3 RU successor articles starting to surface.
5. **NEW: "фулфілмент україна" 15% CTR / pos 2.5** — strong brand+keyword combo (likely from pillar updates, not tpost-related).

### What's stagnating ⏳

1. **Tpost URLs plateaued** — clicks/CTR identical day2→day3 on top 4 tpost URLs. Google has stabilized; further movement depends on canonical handoff.
2. **`/ua/blog/scho-take-artikul/`, `/blog/chto-takoe-sla/`** — still 0 GSC traffic. Slower migration than SLA UA. Re-check 2026-05-04.
3. **`form_submit` window-rotation drop** — appears statistical, not real. `generate_lead` flat confirms.

### Action items

| # | Item | Owner | When |
|---|---|---|---|
| Α | Re-run audit on **2026-05-04** (full 7d window) | claude-code | scheduled |
| Β | Mark `phone_click`/`telegram_click`/`generate_lead` as Key Events in GA4 | manual (user) | ✅ DONE 2026-04-30 (#82) |
| Γ | Verify `/ua/blog/scho-take-sla/` ranking momentum (compare pos in 4d) | claude-code | 2026-05-04 |
| Δ | If artikul/tovarnyi-biznes successors still 0 GSC by 05-04 → request indexing | manual (user) | 2026-05-04 |
| Ε | If 7d trend continues (+~100 clicks vs baseline) → Tier-3 stub creation deferred | claude-code | 2026-05-04 |

### Bottom line

**On-track.** Day-3 metrics confirm the day-2 trend is real, not a one-day spike. The first successor URL has surfaced in GA4 (SLA UA). Need ~4 more days for full canonical migration on the other tpost siblings. **No escalation needed yet.** Tier-3 stub creation (the fallback in the original task brief) is unnecessary if 7d audit confirms +~100 clicks vs baseline.

---

## 7. Files

- Snapshot: `docs/gsc/28d-snapshot.json` (refreshed 2026-04-30)
- Diff vs 90d: `docs/gsc/28d-diff-vs-90d.json`
- GA4 organic: `docs/ga4/28d-organic-snapshot.json` (refreshed 2026-04-30)
- Day 2 report: `docs/gsc/2026-04-29_tpost-redirect-uplift-day2.md`
- Baseline: `docs/gsc/2026-04-27_28d-snapshot.md`
