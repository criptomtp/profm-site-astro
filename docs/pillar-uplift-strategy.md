# Pillar Uplift Strategy — 6-Week Roadmap

**Last updated:** 2026-05-01
**Next checkpoint:** 2026-05-15 (end of Phase A, 7-day GSC observation window opens)
**Owner:** Nikolaj
**Branch of work:** weekly review sessions, ~1–2 h committed per week
**Companion doc:** `docs/pillar-uplift-tracker.md` — tactical per-batch log. This file is **strategic** decisions only; do not duplicate per-batch session entries here.

> **Note on inputs.** This strategy imports the PASS=20 / FAIL=34 cohort, the 9-must-have-schemas gate, and the brand-anchor numbers (3,700 m², 800 ms, 47 min, 18 UAH, 0 days down since 2022, EDRPOU 45315740) from the local-machine tracker, scorecard, checklist, and humanizer files. They are not duplicated here. Live signals (GSC impressions/position, word counts, schema counts) are pulled from `docs/gsc/full-pages.csv` and the `src/pages/{ua,ru,en}/*.astro` source.

---

## 1. Current state synthesis

54 pillar pages across UA / RU / EN. Per the local scorecard: **PASS=20, FAIL=34**. Schema regressions resolved (Phase 1–2 closed). Failure profile of the 34:

| Failure type | Pages affected | Notes |
|---|---|---|
| `words<2500` | 33 | Dominant gate; only 2 pages above threshold today (en/what-is-fulfillment 2967w, ua/shcho-take-fulfilment 2392w). 3 pages within 600w of gate. |
| `h1_generic` ⚠ | 15 | Mostly EN + service-hub. Examples: en/index "3PL Fulfillment for Your E-commerce in Ukraine", en/services "E-commerce Fulfillment Services in Ukraine", ua/services "Фулфілмент послуги для інтернет-магазинів". |
| `schemas<9` | unknown count, likely most | Service pages currently carry 2–4 schemas (Service, BreadcrumbList, FAQPage, LocalBusiness). The 9-schema bar pushes Review, Person, Offer/AggregateOffer, AggregateRating, and Organization into every pillar. |
| Language purity / hreflang quartet | <5 | Most quartet issues are in legacy Tilda blog HTML (per `docs/LANGUAGE_AUDIT.md`), not in scope here. |

**Severity split (1-fail vs 2+-fail).** The 33 word-gap pages are mostly multi-fail (word + H1 or word + schema), making them high-leverage when touched. Single-fail pages are <8 (mostly H1-only or schema-only). Strategy: when a page is opened for any one fix, pay all the gates in one pass to avoid double GSC reindex spend.

**Business class triage.**
- **Conversion** (12 pages): ua/tsiny, ru/tsenu, en/prices, ua/calculator, ru/calculator, en/calculator, ua/fulfilment-dlya-internet-magazynu, ru/fulfilment-dlya-internet-magazynu, ua/fulfilment-dlya-marketpleysiv, ru/fulfilment-dlya-marketpleysov, ua/fulfilment-dlya-maloho-biznesu, ru/fulfilment-dlya-malogo-biznesa.
- **Top-of-funnel** (12): ua/shcho-take-fulfilment, ru/chto-takoe-fulfilment, en/what-is-fulfillment, ua/guide, ru/guide, en/guide, ua/faq, ru/faq, en/faq, ua/fulfilment-ukraina, ru/fulfilment-ukraina, en/fulfillment-ukraine.
- **Awareness/authority** (rest): about, recalls, 3pl-logistyka/logistika/logistics, services hubs, paletne/paletnoe/pallet-storage, skladski/skladskie/warehouse-services, fulfilment-kyiv/kiev/-kyiv, fulfilment-vazhkykh-tovariv / heavy-goods, kosmetyky/kosmetiki (no EN equivalent in src).

**GSC reindex queue (50 URLs).** Already submitted in active weeks. Expected timing per cohort:
- 7–14 days: Googlebot recrawl + index refresh.
- 14–28 days: position movement on the affected queries.
- 28–60 days: AI Overviews citation pickup (per `docs/AI_VISIBILITY_OPTIMIZATION.md`).
Two phantom EN URLs (`/en/fulfillment-for-marketplaces/` 139 impressions @ pos 4.8 and `/en/fulfillment-for-cosmetics/` 36 @ pos 63.9) appear in GSC but have **no Astro source file** — likely Tilda redirect targets ranking on legacy content. Flagged as Phase A investigation, not assumed broken.

---

## 2. Strategic phasing

### PHASE A — Quick wins (week 1, 3–5 hrs)

**Goal:** +6–10 PASS pages, zero ranking risk.

1. **Smallest-gap content top-up (3 pages, ~2h):** UA/RU `kosmetyky` cluster + `ru/chto-takoe-fulfilment`. All three are within 600w of 2500. Add one FAQ block (~250w) plus one expanded use-case section (~300–400w) per page using anchor numbers from CLAUDE.md and humanizer-ua-mtp.md voice rules.
2. **H1 rewrites — mechanical batch (6–8 pages, 1h):** Propose new H1s **inline below** for batch-approve. Keyword preserved, brand-anchor injected. Targets:
    - `en/services` → "E-commerce Fulfillment in Ukraine — 3,700 m² warehouse, 800 ms pick"
    - `en/prices` → "Fulfillment Pricing in Ukraine from 18 UAH per Order"
    - `ua/services` → "Фулфілмент послуги в Україні — склад 3,700 м², піки 47 хв"
    - `ru/services` → "Фулфилмент услуги в Украине — склад 3,700 м², пик 47 мин"
    - `ua/3pl-logistyka` → "3PL логістика в Україні — 3,700 м², 0 днів простою з 2022"
    - `ru/3pl-logistika` → "3PL логистика в Украине — 3,700 м², 0 дней простоя с 2022"
    - `en/3pl-logistics` → "3PL Logistics in Ukraine — 3,700 m² Bonded Warehouse, EDRPOU 45315740"
    - `en/fulfillment-ukraine` → "Ukraine Fulfillment Services — 3,700 m², 47-minute Peak Picks"
3. **Duplicate-schema cleanup (3 pages, 30min):** `ru/tsenu`, `en/prices`, `en/heavy-goods` carry duplicate Service+LocalBusiness blocks left over from Phase 1 enrichment. Collapse to single canonical block per type. No content change → near-zero SEO risk.
4. **Phantom-URL audit (30min):** Verify `/en/fulfillment-for-marketplaces/` and `/en/fulfillment-for-cosmetics/` redirect chains in `vercel.json` / `astro.config.mjs`. If they 200 via Tilda legacy, decide rebuild-vs-redirect in Phase B planning.

**Phase A exit:** 7-day GSC observation window opens. No new content writing during the wait — reserve time for `gsc-monitor.py` runs.

### PHASE B — Content depth (weeks 2–4, 8–12 hrs/week)

**Goal:** +15–20 PASS pages via word-count uplift on the top-priority cohort.

**Priority formula (computed in section 7 table):**
```
priority_score = log10(impressions_90d + 10) × (60 / max(avg_position, 5)) × class_weight
class_weight   = 1.5 (conversion) | 1.0 (TOFU/authority) | 0.5 (utility)
```

**Per-page workflow** (≈4–6 hrs/page):
1. **Competitor pull** (30min) — WebSearch top-3 UA + top-3 RU + top-3 EN for the page's primary keyword from `docs/MTP_SEMANTIC_CORE_FULL.md`. WebFetch top result for full content.
2. **Outline** (30min) — bullet skeleton of 4–6 new sections that fill the word gap and address competitor angle gaps. User reviews and approves outline before writing.
3. **Write** (2–3h) — 800–1500 new words across the new sections. Stick to humanizer-ua-mtp.md voice rules (banned AI phrases per language, anchor-number injection, burstiness — short sentences mixed with long, avoid "способів"/"максимум"/"активно"/"аутсорс" in UA).
4. **Humanizer pass** (30min) — second-pass edit through humanizer-ua-mtp.md checklist.
5. **Build + validate** (30min) — `npm run build`, then `python3 scripts/validate-seo-improvements.py` for hreflang/lang/schema spot-check.
6. **Deploy + reindex** (30min) — `npx vercel --prod`, then GSC URL Inspection → Request Indexing.

**Cadence:** 2 sessions/week × 4 weeks = ~10 pages. Multi-language pages count as one cluster (UA+RU+EN deployed lockstep per CLAUDE.md), so ~8 clusters across the 3 weeks. Sequence per the priority queue in section 7.

**GSC quota:** ~30/day during active weeks; well under the 200/day cap.

### PHASE C — Final polish (weeks 5–6, 3–5 hrs)

**Goal:** Close the long-tail and finalise the H1 narrative.

1. **Hardest H1 rewrites (5–8 pages, 2h):** Pages where the H1 is the brand front door and needs craft, not mechanics. Candidates:
    - `en/index` (current: "3PL Fulfillment for Your E-commerce in Ukraine") — homepage, weight matters.
    - `ua/fulfilment-dlya-internet-magazynu` (current: bare "Фулфілмент для інтернет-магазину") — top conversion page.
    - `ru/fulfilment-dlya-internet-magazynu` — same intent, RU side.
    - `en/fulfillment-kyiv` (current: "Your logistics base in Eastern Europe.") — has hook but no number, add "3,700 m²".
    - `ua/fulfilment-ukraina` (current: "Фулфілмент в Україні — економія до 49% vs власний склад") — already strong, audit only.
    - 2–3 service-hub pages remaining after Phase A.
   These need user batch-approve before apply.
2. **Edge cases (1h):** Add `privacy` and `thanks` pages to checklist exclusions (legal/utility, exempt from 2500w gate). Document in `docs/pillar-page-checklist.md` as `exempt: [privacy, thanks]`.
3. **Final reindex sweep (30min):** GSC URL Inspection → Request Indexing on all pages touched in Phases A+B+C. Quota: ~20 URLs.
4. **Wait 7–14 days** before deciding next cycle. Pull GSC delta, write a one-page "Cycle 1 outcome" memo at the bottom of the tracker.

---

## 3. Decision gates

**After Phase A — pause 7 days.**
Pull aggregate impressions on the initial 50-URL reindex queue (already in flight before Phase A). Compare 7-day post-deploy window to 14-day pre-deploy baseline.
- **If aggregate impressions +10% or better** → proceed Phase B as planned.
- **If flat or negative** → pause Phase B writing. Run root-cause: (a) `bash scripts/psi-audit.sh` for Core Web Vitals on the 10 highest-impression pillars; (b) `python3 scripts/gsc-monitor.py` for indexation status changes; (c) skim `docs/INTERNAL_LINKING_GUIDE.md` for orphan-page fixes. Resume Phase B only after a written hypothesis.

**After Phase B — pause 14 days.**
Same logic, longer window.
- **If positions move materially** (≥5 positions on ≥6 pillars) → accelerate Phase C, optionally pull forward Phase 4 (HowTo + VideoObject schema layer).
- **If not** → assume content is not the binding constraint. Likely candidates: backlink profile (separate track), brand authority, EEAT author bio gap (`docs/AUDIT_CONTENT_EEAT.md` flags this — "blog article author credited to Organization rather than a named person"). Write findings before scheduling more content writing.

**Continuous tripwires.**
- Track PASS-count weekly in tracker.
- **Real success metric** = (a) GSC clicks delta on touched pillars, (b) Telegram lead volume from `/api/telegram` payloads tagged `hero /[lang]/[slug]/`, (c) `form_submit` GA4 events on touched pages. PASS-count is a leading indicator only.

---

## 4. Rollback triggers

Per-page rollback if **any** of:

- Average position −20% within 7 days post-deploy (vs 14-day pre-deploy baseline)
- Page CR −15% within 7 days (Telegram leads ÷ sessions, or GA4 `form_submit` ÷ sessions)
- GSC indexation flips Indexed → "Crawled — currently not indexed"
- Manual user request

**Procedure.** `git revert <sha>` for the per-page commit, `npm run build`, `npx vercel --prod`, GSC URL Inspection → Request Indexing. Log the rollback in `docs/pillar-uplift-tracker.md` and create `docs/design-system/pages/[slug]-rollback.md` per the existing redesign system.

**Hard rule.** UA / RU / EN versions deploy lockstep. If one language triggers rollback, the other two get reverted in the same commit even if they're tracking fine — this preserves the parity the hreflang quartet promises.

---

## 5. Out of scope (this 6-week cycle)

Explicit non-goals — included to prevent scope creep and make this doc unambiguous about what it is **not**:

1. **New pillar creation.** `docs/MTP_SEMANTIC_CORE_FULL.md` lists 120+ planned pillars; only ~54 exist. Net-new pages are a separate cycle. This cycle uplifts what exists.
2. **Legacy Tilda blog uplift.** 35 language violations + 50 long titles in `/blog/tpost/*` per `docs/LANGUAGE_AUDIT.md` and `docs/TITLES_TO_FIX.md`. Different domain (content quality of legacy HTML vs structural completeness of pillars). Separate cycle.
3. **Design redesign of pillars.** Tier-NOW redesigns of `/ua/`, `/ru/`, calculator pages live in `docs/design-system/README.md`. They run in parallel by another track and do **not** block content uplift. If a redesign lands during this cycle, the per-page baseline resets — coordinate with that track before deploying content uplift on the same page in the same week.
4. **Backlink campaign.** Tracked separately in `docs/CAMPAIGN_MASTER_PLAN.md` and `docs/OUTREACH_BATCH_*.md`.
5. **Competitor comparison / alternatives pages.** Separate sprint via the `seo-competitor-ext` skill.
6. **Schema enrichment beyond the 9-schema baseline.** `HowTo`, `VideoObject`, `ImageObject`, `AggregateRating` deepening — Phase 4+ candidate.
7. **Mobile / Core Web Vitals optimisation.** Separate track. CWV regressions during content uplift trigger rollback under the rules in section 4 but are not pursued proactively here.
8. **EEAT author-bio retrofit** (named blog author, founder bio schema). High-impact per `docs/AUDIT_CONTENT_EEAT.md`, but a separate refactor that touches `Base.astro` schema injection, not per-pillar content. Queue as a Phase 4 candidate.

---

## 6. Open questions for user

**Resolved 2026-05-01** by Nikolaj.

| # | Decision | Answer |
|---|---|---|
| 1 | Priority weight | KEEP 60/40 traffic-conversion + tie-bump conversion |
| 2 | Time per week | KEEP review-only + outline-first gate (5-min approve before 2-3hr write) |
| 3 | EN tone | KEEP strict humanizer (compatible with EN Industrial archetype) |
| 4 | EN depth | OVERRIDE — differential gates: international entry pillars 2500w / industry pillars 2000w / utility 1500w / privacy/thanks exempt |
| 5 | Phantom EN URLs | OVERRIDE — phantom is US-spelling "fulfillment" (LL) vs UK-spelling "fulfilment" (L). 301 redirect US→UK in `public/_redirects` (no rebuild needed; UK-spelling Astro pages already PASS) |

### Original questions (kept for context)

These cannot be auto-decided. Default in **bold** is what the plan uses unless overridden.

1. **Priority weight — traffic vs conversion?** Default: **60/40 traffic-driven / conversion-class blended** (see formula in section 2 / table in section 7). Alternative: 100% conversion-class first (calculator → prices → internet-magazynu → marketpleysiv) regardless of GSC impression. Override moves the section-7 ranking.
2. **Time per week — review only or some writing capacity?** Default: **review only**, all writing falls on AI + humanizer with batch-approve gates at outline + final draft. Confirm or adjust.
3. **Tone latitude per language.** Default: **strict humanizer-ua-mtp.md per-language rules**. Alternative: allow EN to lean more "industrial/direct" matching the EN archetype (more numbers, shorter sentences). Override changes Phase B writing brief.
4. **EN depth investment.** Default: **parity with UA/RU at 2500w gate**. Alternative: accept 1500w on EN pages where intent volume is small (only ~5 EN URLs accumulate meaningful GSC impressions); reallocate the saved hours to UA/RU depth. Override drops 4–6 EN pages from the priority queue.
5. **Phantom EN URLs** (`/en/fulfillment-for-marketplaces/`, `/en/fulfillment-for-cosmetics/`) — these have GSC impressions (139 @ pos 4.8 and 36 @ pos 63.9) but **no Astro source file**. Rebuild as Astro pillars (~5h/page in Phase B) or keep as Tilda redirects? The 4.8-position page is a high-value candidate to convert.

---

## 7. Per-pillar priority queue

Word counts measured from `src/pages/*.astro` body (frontmatter, `<script>`, `<style>` stripped). "—" = no source file in that language. Word gap = `max(0, 2500 − words)`. Priority rank = applied formula from section 2.

### 6-week timeline overview

| Week | Phase | Action | Expected PASS delta | GSC quota |
|---|---|---|---|---|
| 1 | A | Top-up 3 smallest-gap pages, 6–8 H1 batch, dup-schema cleanup, phantom-URL audit | +6–10 | ~25 URLs |
| 2 | B | 2–3 cluster uplifts (top of queue: internet-magazynu, marketpleysiv) | +5–7 | ~25 URLs |
| 3 | B | 2–3 cluster uplifts (fulfilment-ukraina, prices/tsiny/tsenu) | +5–7 | ~25 URLs |
| 4 | B | 2–3 cluster uplifts (kosmetyky finalise, vazhki-tovary, fulfilment-kyiv) | +5–6 | ~25 URLs |
| 5 | C | Hardest H1 batch + edge case exemptions | +2–4 | ~10 URLs |
| 6 | C | Final reindex sweep + observation buffer | 0 (observation) | ~10 URLs |

**Cycle target:** PASS 20 → 43–54.

### Priority queue table

| Rank | Pillar (cluster) | UA path | RU path | EN path | Words (UA/RU/EN) | Word gap to 2500 (UA/RU/EN) | Est hrs | Phase |
|---|---|---|---|---|---|---|---|---|
| 1 | internet-magazynu | /ua/fulfilment-dlya-internet-magazynu/ | /ru/fulfilment-dlya-internet-magazynu/ | — (phantom `/en/fulfillment-for-online-store/` ?) | 1132 / 986 / — | 1368 / 1514 / — | 8 | B |
| 2 | marketpleysiv | /ua/fulfilment-dlya-marketpleysiv/ | /ru/fulfilment-dlya-marketpleysov/ | — (phantom `/en/fulfillment-for-marketplaces/` 139 imp @ 4.8) | 1467 / 1338 / — | 1033 / 1162 / — | 6–11¹ | B |
| 3 | fulfilment-ukraina | /ua/fulfilment-ukraina/ | /ru/fulfilment-ukraina/ | /en/fulfillment-ukraine/ | 1267 / 863 / 1063 | 1233 / 1637 / 1437 | 9 | B |
| 4 | prices/tsiny/tsenu | /ua/tsiny/ | /ru/tsenu/ | /en/prices/ | 907 / 903 / 626 | 1593 / 1597 / 1874 | 9 | B |
| 5 | kosmetyky | /ua/fulfilment-dlya-kosmetyky/ | /ru/fulfilment-dlya-kosmetiki/ | — (phantom `/en/fulfillment-for-cosmetics/` 36 imp @ 63.9) | 2278 / 1904 / — | 222 / 596 / — | 3 | A |
| 6 | vazhki-tovary / heavy-goods | /ua/fulfilment-vazhkykh-tovariv/ | /ru/fulfilment-vazhkykh-tovariv/ | /en/heavy-goods/ | 1027 / 962 / 1309 | 1473 / 1538 / 1191 | 9 | B |
| 7 | fulfilment-kyiv | /ua/fulfilment-kyiv/ | /ru/fulfilment-kiev/ | /en/fulfillment-kyiv/ | 1014 / 920 / 1205 | 1486 / 1580 / 1295 | 9 | B |
| 8 | what-is-fulfilment | /ua/shcho-take-fulfilment/ | /ru/chto-takoe-fulfilment/ | /en/what-is-fulfillment/ | 2392 / 2182 / 2967 | 108 / 318 / 0 | 2 | A |
| 9 | maloho-biznesu / SMB | /ua/fulfilment-dlya-maloho-biznesu/ | /ru/fulfilment-dlya-malogo-biznesa/ | — | 1420 / 1558 / — | 1080 / 942 / — | 6 | B |
| 10 | services hub | /ua/services/ | /ru/services/ | /en/services/ | 947 / 1066 / 1347 | 1553 / 1434 / 1153 | 9 | B |
| 11 | 3pl-logistyka | /ua/3pl-logistyka/ | /ru/3pl-logistika/ | /en/3pl-logistics/ | 790 / 726 / 841 | 1710 / 1774 / 1659 | 9 | B |
| 12 | guide | /ua/guide/ | /ru/guide/ | /en/guide/ | 1560 / 1573 / 944 | 940 / 927 / 1556 | 8 | B |
| 13 | about | /ua/about/ | /ru/about/ | /en/about/ | 1033 / 1435 / 1224 | 1467 / 1065 / 1276 | 8 | B |
| 14 | recalls | /ua/recalls/ | /ru/recalls/ | /en/recalls/ | 929 / 1308 / 751 | 1571 / 1192 / 1749 | 8 | B |
| 15 | faq | /ua/faq/ | /ru/faq/ | /en/faq/ | 1158 / 1151 / 1089 | 1342 / 1349 / 1411 | 8 | B/C² |
| 16 | calculator | /ua/calculator/ | /ru/calculator/ | /en/calculator/ | 840 / 840 / 469 | 1660 / 1660 / 2031 | 6³ | C |
| 17 | paletne / pallet-storage | /ua/paletne-zberigannya/ | /ru/paletnoe-khranenie/ | /en/pallet-storage/ | 672 / 675 / 771 | 1828 / 1825 / 1729 | 9 | B |
| 18 | skladski / warehouse-services | /ua/skladski-poslugy/ | /ru/skladskie-uslugi/ | /en/warehouse-services/ | 637 / 639 / 747 | 1863 / 1861 / 1753 | 9 | B |
| 19 | privacy (exempt candidate) | /ua/privacy/ | /ru/privacy/ | /en/privacy/ | 491 / 493 / 742 | exempt | 1 | C |

¹ Marketpleysiv hours include phantom-EN rebuild decision from section 6 question 5.
² FAQ pillar — likely auto-PASS once schemas confirmed; defer to Phase C if so.
³ Calculator — UI-led page; word uplift via supporting copy below the calculator widget. Lower bar (1500w may be the practical ceiling); discuss in section 6 question 4.

### Notes on the queue

- **Top three (internet-magazynu, marketpleysiv, fulfilment-ukraina)** carry ~50% of pillar GSC impressions in `docs/gsc/full-pages.csv`. They get done first for a reason; do not let me reshuffle this without rollback-trigger discipline.
- **Kosmetyky cluster ranked #5, scheduled in Phase A** — small word gap (UA already 2278 / 91% to gate), highest PASS-per-hour ratio. Confidence move to bank early wins.
- **what-is-fulfilment cluster ranked #8** — EN already at gate, UA at 96%, RU at 87%. Smallest-effort full-cluster PASS in the queue; bundle with kosmetyky in Phase A.
- **Phantom EN URLs** in clusters 1, 2, 5 hold the rebuild-vs-redirect decision. Resolved in section 6 question 5 before Phase B starts.
- **Calculator cluster** intentionally deferred to Phase C — its conversion role is the widget itself, not the surrounding copy. Avoid over-investing word count on a page where the UI does the work.
- **Privacy** — recommend formal exemption (section 5 follow-up) rather than padding legal copy to hit a marketing-page word bar.

---

## Appendix — verification checklist after each phase

- `npm run build` exits 0
- `python3 scripts/validate-seo-improvements.py` reports 4 hreflangs + correct lang attr + schema present per language sample
- `curl -sI "https://fulfillmentmtp.com.ua/<path>/"` returns 301 → www
- `curl -sI "https://www.fulfillmentmtp.com.ua/<path>/"` returns 200
- Telegram QA gate: send a test phone number through the page's hero form and confirm a Telegram message lands at @nikolay_mtp (per CLAUDE.md hard rule on hero CTA)
- GSC URL Inspection → Request Indexing on the touched URL
- PASS count delta logged in `docs/pillar-uplift-tracker.md`

---

## Footnotes

This strategy doc references but does **not** duplicate `docs/pillar-uplift-tracker.md` (per-batch tactical log) or the local-machine scorecard / checklist / humanizer files. When a number here disagrees with the tracker, the tracker is the source of truth — file an update on this doc, do not silently drift.

If the cohort PASS=20 / FAIL=34 changes between this doc and the next checkpoint, update the header `Last updated` and add a single dated bullet at the bottom of section 1 — do not rewrite the strategy. The strategy holds for the cycle; only the tactical layer churns.
