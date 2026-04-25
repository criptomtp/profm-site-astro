# MTP Group — Content Quality + E-E-A-T Delta Audit
**Date:** 2026-04-25
**Site:** https://www.fulfillmentmtp.com.ua
**Baseline:** docs/seo-competitor-analysis/2026-04-23/mtp/02-content.md
**Framework:** Google QRG (Sept 2025) + hub-and-spoke topical authority
**Methodology:** measured against `dist/` build artefacts (HTML + dual-md) and `src/pages/`.

---

## 1. E-E-A-T scorecard (delta vs 2026-04-23)

| Axis | Weight | 2026-04-23 | 2026-04-25 | Δ | Drivers |
|---|---:|---:|---:|---:|---|
| Experience | 20% | 88 | **90** | +2 | Pillar EN landed (3,501 w war-resilient narrative); RU pillar (2,702 w) extends CIS angle; quantified facts unchanged but propagated to new surfaces. |
| Expertise | 25% | 76 | **82** | +6 | Person schema (Mykola Liashchuk / Микола Лящук) now on 50+ HTML pages (Article-level author + visible byline on 12). Trilingual byline localisation correct (UA "Лящук", EN "Liashchuk", RU localized). Still missing visible byline on services/pricing/calculator/about/recalls landings. |
| Authoritativeness | 25% | 72 | **75** | +3 | All 3 pillars cross-linked; PillarHub component renders on 3 pillars with 70+ internal links each (~2.4/100 w); 34 dead `tpost` redirects fully removed from blog index. No new external endorsements. |
| Trustworthiness | 30% | 81 | **83** | +2 | EDRPOU 45315740 + ТОВ "МТП Груп Фулфілмент" now visible on UA/RU/EN about pages. datePublished/dateModified added to Article schema on pillars + blog. Two phones in footer (050 + 093). **Footer still missing legal entity / EDRPOU / year founded** — biggest remaining trust gap. |
| AI citation readiness | — | 87 | **89** | +2 | TL;DR boxes localized to UA + RU pillars (EN missing canonical "30-second answer" block). Dual-md generation healthy (`/index.md` exists for every key URL we sampled). FAQPage on every spoke (10/10). |
| **Overall content score** | — | **81** | **84** | **+3** | Single biggest unlock would be footer legal block + visible bylines on remaining 13 service pages. |

---

## 2. Pillar pages (the 3 new hubs)

| Pillar | Words | H2 | H3 | Internal links | FAQ | TL;DR | Byline | Person | datePub | dateMod |
|---|---:|---:|---:|---:|:---:|:---:|:---:|:---:|:---:|:---:|
| /ua/shcho-take-fulfilment/ | **2,950** (+172 vs 04-23) | 13 | 34 | 72 | yes | yes | yes | yes | 2026-04-21 | 2026-04-24 |
| /ru/chto-takoe-fulfilment/ | **2,702** (new) | 12 | 28 | 70 | yes | yes | yes | yes | yes | yes |
| /en/what-is-fulfillment/ | **3,501** (new) | 16 | 36 | 69 | yes | **no** | yes | yes | yes | yes |

Verdict: best-in-class for the UA fulfillment sector. Three competitors (Nova Poshta fulfillment, Sender Ukraine, LP-Sklad) have nothing comparable. EN pillar leads on length (DTC EU gateway angle) but lacks the canonical "In 30 seconds" TL;DR block that UA + RU carry — easy fix.

Files:
- `src/pages/ua/shcho-take-fulfilment.astro`
- `src/pages/ru/chto-takoe-fulfilment.astro`
- `src/pages/en/what-is-fulfillment.astro`

---

## 3. Word-count distribution per page type

| Page | UA | RU | EN | Floor | Verdict |
|---|---:|---:|---:|---:|---|
| Home | 1,036 | 953 | 1,715 | 500 | OK; RU borderline against 1,400-w competitor target |
| Pillar | 2,950 | 2,702 | 3,501 | 1,500 | Excellent |
| Pricing | 1,121 | n/a | n/a | 800 | OK |
| Calculator | 949 | n/a | n/a | 800 | OK (borderline) |
| About | 1,409 | 1,875 | 1,693 | 500 | Excellent (UA expanded +278 since 04-23) |
| Recalls | 1,016 | n/a | n/a | 500 | Excellent |
| FAQ | 1,183 | n/a | n/a | 500 | OK |
| Guide | 1,641 | n/a | n/a | 1,500 | OK |
| Glossary | 691 (`/glosariy/`) | 705 | 754 | 500 | OK |
| Pallet storage | **932** | **702** | **784** | 800 | **Mixed: UA OK, RU/EN thin** |
| Warehouse services | **2,536** (+1,812!) | n/a | n/a | 800 | **Excellent** (was 724, expanded) |
| Service spokes (UA) | 1,025–2,338 | — | — | 800 | All 10 spokes ≥800 w; avg ≈ 1,490 w |

UA service spoke detail (10 spokes, all ≥ 800 w):

| URL | Words | Δ vs 04-23 |
|---|---:|---:|
| /ua/fulfilment-ukraina/ | 1,422 | 0 |
| /ua/fulfilment-dlya-internet-magazynu/ | 1,185 | 0 |
| /ua/fulfilment-dlya-marketpleysiv/ | 1,502 | 0 |
| /ua/fulfilment-dlya-kosmetyky/ | 2,338 | 0 |
| /ua/fulfilment-vazhkykh-tovariv/ | 1,076 | 0 |
| /ua/fulfilment-kyiv/ | 1,086 | 0 |
| /ua/3pl-logistyka/ | 1,025 | +135 |
| /ua/skladski-poslugy/ | 2,536 | +1,812 |
| /ua/paletne-zberigannya/ | 932 | +237 |
| /ua/fulfilment-dlya-maloho-biznesu/ | 1,640 | new since 04-23 |

---

## 4. Author bylines + Person schema (sample of 15 pages)

| Page | Visible byline | Person schema | Δ |
|---|:---:|:---:|---|
| /ua/shcho-take-fulfilment/ | yes | yes | unchanged |
| /ru/chto-takoe-fulfilment/ | yes | yes | new |
| /en/what-is-fulfillment/ | yes | yes | new |
| /ua/about/ | no | yes | Person schema new |
| /ua/recalls/ | no | yes (10 reviewers) | unchanged |
| /ua/3pl-logistyka/ (services hub) | no | no | gap |
| /ua/tsiny/ | no | no | gap |
| /ua/calculator/ | no | no | gap |
| /ua/fulfilment-ukraina/ | no | no | gap |
| /ua/fulfilment-dlya-marketpleysiv/ | no | no | gap |
| /ua/fulfilment-dlya-kosmetyky/ | no | no | gap |
| /ua/paletne-zberigannya/ | no | no | gap |
| /ua/skladski-poslugy/ | no | no | gap |
| /ua/blog/scho-take-fulfilment/ | yes | yes | unchanged |
| /en/blog/post/what-is-fulfillment-complete-guide/ | yes | yes | unchanged |

Visible `author-byline` component count (build): **12 pages** (3 pillars + 9 blog × 3 langs).
Person schema in JSON-LD (any context): **50+ pages** — includes Article author blocks across 38 EN blog posts.

Gap: 13 service / landing pages still have no `<AuthorByline>` component nor Article-level Person schema. These are the highest-impact pages for E-E-A-T uplift since they target commercial intent.

---

## 5. datePublished / dateModified coverage

| Page class | datePublished | dateModified |
|---|:---:|:---:|
| 3 pillars (UA/RU/EN) | yes (all) | yes (all) |
| Blog (38 EN + 4 UA + 4 RU) | yes (all sampled) | yes (all sampled) |
| Recalls (`/ua/recalls/`) | yes | no |
| About (`/ua/about/`) | no | no |
| Services hub (`/ua/3pl-logistyka/`) | no | no |
| Tsiny / Calculator / Fulfilment-* spokes | **no** (0/10) | **no** (0/10) |
| Homepage `/` | no | no |
| FAQ / Guide / Glossary | no | no |

P0 fix: add `dateModified` (and where appropriate `datePublished`) to the Service / WebPage schema on all spoke and landing pages. Currently Google sees "evergreen but stale" signal — the same issue flagged in 04-23 baseline, only partially resolved.

---

## 6. Pillar hub internal-link integrity

`PillarHub.astro` rendered (visual map of ecosystem) on 3 pillars only:

| Pillar | PillarHub block | Internal links | links/100w |
|---|:---:|---:|---:|
| /ua/shcho-take-fulfilment/ | yes | 72 | 2.44 |
| /ru/chto-takoe-fulfilment/ | yes | 70 | 2.59 |
| /en/what-is-fulfillment/ | yes | 69 | 1.97 |

Service-page sample (5 pages) — **none surface PillarHub**:

- /ua/3pl-logistyka/, /ua/tsiny/, /ua/calculator/, /ua/fulfilment-ukraina/, /ua/fulfilment-dlya-marketpleysiv/: 0/5

This is a topical-authority leak: only a visitor who already lands on the pillar sees the hub map. Spokes don't carry the cross-link graph back. Consider adding a compact `<PillarHub mode="related">` on every spoke (not full hub — just 4-6 contextual related links) or a footer-row "карта екосистеми" CTA.

---

## 7. Trust signals

| Signal | Footer | Homepage | About (UA) | About (RU) | About (EN) |
|---|:---:|:---:|:---:|:---:|:---:|
| Phone | yes (2 lines) | yes | yes | yes | yes |
| Email | yes | yes | yes | yes | yes |
| Warehouse address | no | yes (Shchaslyve, Bilohorodka) | yes | yes | yes |
| Founder name | no | partial | yes | yes | yes |
| EDRPOU 45315740 | **no** | no | **yes** | **yes** | **yes** (new since 04-23) |
| Legal name "ТОВ МТП Груп Фулфілмент" | no | no | yes | yes | yes |
| Year founded (2023) | no | no | yes | yes | yes |
| Privacy policy link | yes | yes | n/a | n/a | n/a |
| Social profiles | yes (5) | n/a | n/a | n/a | n/a |

P1 fix: add a 1-line legal block to `src/components/Footer.astro` — "ТОВ «МТП Груп Фулфілмент» · ЄДРПОУ 45315740 · Засновано 2023". This single change carries weight on B2B trust evaluations and aligns with 2026 UA Cabinet of Ministers transparency requirements.

---

## 8. Thin-content remediation

| Page | 04-23 | 04-25 | Floor | Status |
|---|---:|---:|---:|---|
| /ua/paletne-zberigannya/ | 695 | **932** | 800 | **Above floor**, 68 w short of 1,000-w P0 target. Pricing table + FEFO workflow visible; 10/50/200-pallet examples still missing. |
| /ua/skladski-poslugy/ | 724 | **2,536** | 800 | **Resolved** (+250%). |
| /ru/paletnoe-khranenie/ | n/a | **702** | 800 | **Thin, new flag** — 98 w below floor. |
| /en/pallet-storage/ | n/a | **784** | 800 | **Thin, new flag** — 16 w below floor. |
| /ua/calculator/ | 949 | 949 | 800 | OK (borderline; persona examples still recommended). |

---

## 9. AI-generated content markers (QRG Sept 2025)

No flags raised on:
- Generic phrasing (specific numbers/named clients across all 3 pillars).
- First-hand experience (war-era blackout narrative present in UA, RU, EN with consistent hardware specifics).
- Factual consistency (150+ clients × 60,000+/mo = ~400 orders/client/mo — math holds).
- Repetitive structure (UA/RU/EN pillars have meaningfully different angles per CLAUDE.md "non-translation" policy: UA = market guide, RU = CIS-entry funnel, EN = DTC EU-gateway).
- Author attribution (named human, photo, jobTitle, sameAs LinkedIn).

One mild flag: on EN pillar the byline header mentions Mykola Liashchuk but the body lacks a canonical "TL;DR / 30-second answer" box that UA and RU carry — small consistency dent.

---

## 10. Issues by priority

### P0 — fix within 7 days

1. **Footer legal entity block** — add ТОВ «МТП Груп Фулфілмент» / ЄДРПОУ 45315740 / "Засновано 2023" to `src/components/Footer.astro` (single line above the copyright). Trilingual labels.
   - File: `src/components/Footer.astro:24`
2. **Visible AuthorByline on 5 commercial landings** — services hub, pricing, calculator, about (UA/RU/EN), recalls.
   - Files: `src/pages/ua/3pl-logistyka.astro`, `src/pages/ua/tsiny.astro`, `src/pages/ua/calculator.astro`, `src/pages/ua/about.astro`, `src/pages/ua/recalls.astro` (+ RU/EN siblings where they exist).
3. **dateModified on Service / WebPage schema** for all 10 UA spokes, all RU spokes, all EN spokes, plus `/`, `/ru/`, `/en/`.
   - 30+ files; pattern is `Article|Service|WebPage` schema block with `"dateModified": "2026-04-25"`.
4. **EN pillar TL;DR** — add a "In 30 seconds" box mirroring UA/RU pattern.
   - File: `src/pages/en/what-is-fulfillment.astro`
5. **Pallet-storage thin pages (RU/EN)** — bring `/ru/paletnoe-khranenie/` to ≥1,000 w and `/en/pallet-storage/` to ≥1,000 w. Mirror UA's pricing table + 10/50/200 examples.
   - Files: `src/pages/ru/paletnoe-khranenie.astro`, `src/pages/en/pallet-storage.astro`

### P1 — within 30 days

6. **Add `<PillarHub mode="related">` block to spokes** — 4–6 contextual related links per spoke pulling from the pillar hub data (avoid full 30-link block).
   - Component: extend `src/components/PillarHub.astro` with `mode` prop.
7. **AuthorByline + Article/Service schema with author** on remaining 8 UA spokes.
8. **Homepage word-count expansion** — UA home 1,036 w → target 1,400 w; RU home 953 w → 1,200 w. Add hero-adjacent value-block (NOT keyword-stuffed text).
   - Files: `src/pages/index.astro`, `src/pages/ru/index.astro`
9. **Pillar /ua/paletne-zberigannya/** — close last 68 w gap to 1,000 w with 10/50/200-pallet sample table + FEFO workflow diagram caption.
10. **Industry-association block on /ua/about/** — even one membership (Ukrainian E-Commerce Association, EBA) would lift Authoritativeness from 75 → 80.

### P2 — within 90 days

11. Comparison-page content (MTP vs Nova Poshta, MTP vs Sender) — see `seo-competitor-pages` skill.
12. Glossary term-by-term schema (DefinedTerm) for AI citation capture.
13. Video hub `/ua/video/` with transcripts.
14. 5 deep case-study pages (one per named client: Carter's, OrnerUA, EcoDrive, etc.).
15. Regional spokes: Lviv, Odesa, Dnipro.

---

## 11. Delta summary table

| Metric | 04-23 | 04-25 | Δ |
|---|---:|---:|---:|
| E-E-A-T overall | 81 | **84** | +3 |
| Pillar pages live | 1 (UA only) | **3 (UA/RU/EN)** | +2 |
| Total pillar words | 2,778 | **9,153** | +6,375 |
| Service spokes ≥ 800 w (UA) | 7/9 | **10/10** | +3 |
| Visible AuthorByline pages | ~3 | **12** | +9 |
| Person schema in JSON-LD | ~5 | **50+** | +45 |
| Pages with dateModified | 1 (pillar) | 50+ (pillars + blog) | major |
| Dead `tpost` redirects in blog index | 34 | **0** | resolved |
| EDRPOU on About | 0/3 langs | **3/3** | resolved |
| Footer legal entity | no | **no** | unchanged (P0) |

---

## 12. Files referenced

- `/Users/nikolaj/My vibecode aplications/profm-site-astro/src/pages/ua/shcho-take-fulfilment.astro`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/src/pages/ru/chto-takoe-fulfilment.astro`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/src/pages/en/what-is-fulfillment.astro`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/src/pages/ua/paletne-zberigannya.astro`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/src/pages/ru/paletnoe-khranenie.astro`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/src/pages/en/pallet-storage.astro`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/src/components/Footer.astro`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/src/components/PillarHub.astro`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/src/components/AuthorByline.astro`

**End of report.**
