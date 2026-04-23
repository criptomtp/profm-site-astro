# MTP Group — Keyword Footprint & Intent Coverage Map

**Date:** 2026-04-23
**Source:** sitemap-0.xml (109 URLs), src/pages (file-level audit), docs/MTP_SEMANTIC_CORE_FULL.md (121-page roadmap)
**Scope:** own site only — competitor benchmarks live in sibling folders (novaposhta / senderukraine / lp-sklad)

---

## 1. URL Enumeration (sitemap-0.xml)

| Language bucket | URL count | Notes |
|---|---|---|
| Root (UA-canonical, no prefix) | 1 | `/` + `/glosariy/` + `/thanks/` (thanks excluded from sitemap) |
| `/ua/*` (legacy UA) | 26 | All pillar service + landing pages still on legacy prefix |
| `/ru/*` | 24 | Full parity except `/ru/thanks/`, blog missing |
| `/en/*` | 52 | Heavy blog presence (30 posts), 18 landings |
| `/blog/*` (root — RU legacy posts) | 4 | Only 3 posts + index, migrated from Tilda |
| **Total in sitemap** | **109** | UA root policy not yet reflected — `/ua/*` still dominant |

Key observation: the 2026-04-22 URL policy decision ("new UA without `/ua/`") has NOT yet produced any new root-level UA pages beyond `/` and `/glosariy/`. All ~23 pillar/service UA pages remain under `/ua/*`. Going forward, new UA pages should land at root; old pages stay put (per memory note).

---

## 2. Page-Level Metadata Sample (15 high-intent URLs)

| URL | Title | H1 | H2 themes | Meta desc focus |
|---|---|---|---|---|
| `/` | Фулфілмент від 18 грн — MTP Group \| 150+ клієнтів, 10 років | Фулфілмент для інтернет-магазинів. Від 18 грн за відправку. | Pain recognition, full-cycle, warehouse tour, testimonials, "Start in 1 day", FAQ, UA guide, blog | Price anchor + trust stack (10y / 150 / 24/7) |
| `/ua/services/` | Фулфілмент послуги Київ \| MTP Group | Фулфілмент послуги для інтернет-магазинів | Propositions, warehouse, 7-step cycle, dynamic tariff, CRM integrations, vs own warehouse, FAQ | Service list + from-18-UAH hook |
| `/ua/shcho-take-fulfilment/` | (pillar — extracted from body) | Що таке фулфілмент. Повний гід... 2026 | Definition, 7 steps, vs own warehouse table, real 2026 tariffs, for-whom, blackout USP, fulfilment vs 3PL vs dropship, FAQ | Informational pillar, ~2200 words |
| `/ua/tsiny/` | Ціни на фулфілмент 2026 \| MTP Group Fulfillment | Ціни на фулфілмент для інтернет-магазинів | Shipment tariff (dynamic), storage + receiving, add-ons, vs own warehouse, calculator embed, price FAQ, cost formation | Concrete numbers (18 UAH + 650 UAH/m³) |
| `/ua/fulfilment-kyiv/` | Фулфілмент Київ — від 18 грн \| MTP Group | Фулфілмент у Києві. Склад під ключ від 18 грн. | Delivery speed, warehouse tour, 1-hour dispatch, BFCM/NY readiness, pricing, FAQ, "Why Kyiv region is best hub" | Local + speed + scale (3900 m²) |
| `/ua/fulfilment-dlya-marketpleysiv/` | Фулфілмент для маркетплейсів \| MTP Group | Фулфілмент для маркетплейсів. Rozetka, Prom, Kasta — без свого складу. | 3 seller pains, Carter's case, supported MPs, own vs MTP, 3-day onboarding, transparent pricing, FAQ, Rozetka/Prom/Kasta differences | Rozetka/Prom/Kasta + Carter's case proof |
| `/ua/fulfilment-dlya-kosmetyky/` | Фулфілмент для косметики Україна — від 18 грн \| MTP | Фулфілмент для косметики | Problems solved, 2h onboarding, own vs MTP, cost, who it fits, beauty changes, FAQ, beauty 2026 guide | FEFO + temperature + 30-sec picking |
| `/ua/fulfilment-dlya-maloho-biznesu/` | Фулфілмент для малого бізнесу від 18 грн \| MTP Group | Фулфілмент для малого бізнесу | When to switch, true costs, 5 pains/solutions, "big warehouse for small", 3-day onboarding, small-biz tariffs, FAQ, guide | Low-barrier entry + WMS 24/7 + 2h CRM integration |
| `/ua/fulfilment-vazhkykh-tovariv/` | Фулфілмент важких товарів в Україні \| MTP Group | Фулфілмент важких товарів. Великий габарит. Без компромісів. | Eligible product types, EcoDrive 50/day case, trust factors, pricing, FAQ, heavy-goods logistics guide | 50kg+ / pallets 1t + solar panels + EcoDrive case |
| `/ua/fulfilment-dlya-internet-magazynu/` | Фулфілмент для інтернет-магазину від 18 грн \| MTP | Фулфілмент для інтернет-магазину | Why e-shops choose MTP, cosmetics case 80→400/day, pricing, FAQ, 5-criteria e-com guide | Classic e-commerce positioning |
| `/ua/3pl-logistyka/` | 3PL логістика для e-commerce — від 18 грн \| MTP Group | 3PL логістика для брендів — повний аутсорсинг складу та доставки | Client results, savings calc, 2h CRM, what's included, Ukraine-wide delivery, FAQ, 3PL primer | 3PL vocabulary + outsourcing framing |
| `/ua/skladski-poslugy/` | Складські послуги Київ від 650 грн/м³ — 2 склади \| MTP | Складські послуги для інтернет-магазинів у Києві та області | From intake to phone control, price, warehouse tour, testimonials, professional warehouse message, FAQ, operator-selection guide | Storage-focused + 2 warehouses (Boryspil + Bilohorodka) |
| `/ua/paletne-zberigannya/` | Палетне зберігання Київ — від 450 грн/міс \| MTP Group | Палетне зберігання товарів у Київській області | Own vs MTP, rack utilization 74%, 4 placement steps, pallet price, who it fits, "26% spots free", FAQ, pallet-storage primer | Pallet-specific + 320 WMS slots + FEFO + generators |
| `/ua/fulfilment-ukraina/` | Фулфілмент в Україні — від 18 грн \| MTP Group | Фулфілмент в Україні — економія до 49% vs власний склад | Uptime (MTP never stops), price, Carter's case, own vs MTP, economics, testimonials, FAQ, how to choose | National framing + blackout-resilience |
| `/ru/services/` | (RU mirror, different angle) | Украинский фулфилмент для брендов из СНГ | 6 launch-killers, 3-week contract-to-sale, 8 services, where MTP can route product, 3-country view, 1-day onboarding, Q&A, "why enter Ukraine now" | CIS-brands-entering-Ukraine angle (NOT a translation of UA) |

Title-length check: most titles sit at 55–64 chars — all within acceptable range. `Складські послуги Київ від 650 грн/м³ — 2 склади \| MTP` is the longest (~60). Meta descriptions 140–165 chars — tight.

---

## 3. Coverage by Intent Cluster

### Informational (top-of-funnel)
- `/ua/shcho-take-fulfilment/` (pillar 2200 words) — STRONG
- `/ua/guide/`, `/en/guide/`, `/ru/guide/` — pillar guides
- `/glosariy/`, `/en/glossary/`, `/ru/glossariy/` — glossary
- `/blog/chto-takoe-fulfilment/` (RU blog)
- EN blog (~30 posts covering war, SKU, SLA, fulfillment cost, fraud, returns, Valentine/March-8 seasonal)
- UA blog only has 3 posts (chto-takoe, top-operatoriv, top-marketpleysiv) — thin on UA informational
- **Verdict:** EN informational strong, UA informational THIN (only 3 blog posts vs 30 EN)

### Commercial investigation (compare / choose)
- `/ua/tsiny/`, `/ru/tsenu/`, `/en/prices/` — transparent price pages
- `/ua/fulfilment-vs-vlasnyy-sklad` sections embedded in every landing
- `/ua/blog/top-fulfilment-operatoriv-2026/` — comparison/rating (published 2026)
- Missing: direct MTP-vs-Competitor pages (MTP vs NP, MTP vs Unipost, MTP vs FLG) — all in roadmap but NOT built
- **Verdict:** pricing owned, but "vs competitor" plays all missing

### Transactional (ready to buy)
- `/ua/calculator/`, `/ru/calculator/`, `/en/calculator/` — pricing calculator
- Hero forms on every landing → Telegram
- `/ua/services/` — full service catalog
- 12 vertical landings (internet-magazin, marketpleys, kosmetyka, maly biznes, vazhki tovary)
- **Verdict:** strong transactional for 5 verticals, weak for 21 more (semantic core roadmap)

### Local (geo)
- `/ua/fulfilment-kyiv/` — Kyiv landing (only geo page)
- `/ua/fulfilment-ukraina/` — national framing
- `/ua/paletne-zberigannya/` — implicit "Kyiv region"
- **Missing:** `/ua/3pl-boryspil/`, `/ua/fulfilment-bilohorodka/`, `/ua/fulfilment-kyivska-oblast/`, Lviv/Odesa informational
- **Verdict:** only 1 true local page despite 2 physical warehouses

---

## 4. Coverage by Vertical

| Vertical | Dedicated page | Depth | Status |
|---|---|---|---|
| E-commerce (general) | `/ua/fulfilment-dlya-internet-magazynu/` + `/` | High | Owned |
| Marketplaces | `/ua/fulfilment-dlya-marketpleysiv/` | High (Rozetka/Prom/Kasta) | Owned |
| Cosmetics / beauty | `/ua/fulfilment-dlya-kosmetyky/` | High (FEFO, temp) | Owned |
| Heavy goods | `/ua/fulfilment-vazhkykh-tovariv/` | High (EcoDrive case) | Owned |
| Small business | `/ua/fulfilment-dlya-maloho-biznesu/` | Medium | Owned |
| Fashion / clothing | — | — | GAP (roadmap ID #2) |
| Electronics | — | — | GAP (#3) |
| Children / toys | — | — | GAP (#4) |
| Sports / fitness | — | — | GAP (#5) |
| Food / snacks | — | — | GAP (#8) |
| Pet products | — | — | GAP (#7) |
| Auto parts | — | — | GAP (#10) |
| Solar panels | Case only (inside heavy-goods) | Medium | Partial |
| Jewelry / bijouterie | — | — | GAP (#14) |
| Supplements / vitamins | — | — | GAP (#21) |
| Handmade | — | — | GAP (#18) |
| Books | — | — | GAP (#9) |
| Furniture / large items | Mentioned in heavy-goods | Low | Partial |
| Home / decor | — | — | GAP (#6) |
| Household chemicals | — | — | GAP (#16) |
| Subscription boxes | — | — | GAP (#38) |
| B2B / wholesale | — | — | GAP (#30) |
| FOP / individual entrepreneurs | — | — | GAP (#34) |
| Dropshipping | — | — | GAP (#31) |
| Brands / premium | — | — | GAP (#33) |
| Startups | — | — | GAP (#29) |

Vertical coverage: **5 out of 26 planned** = 19% of semantic core, Axis 1+2.

---

## 5. Top-10 MTP Keyword Footprints (where we target AND have depth)

1. **"фулфілмент від 18 грн"** — homepage + 9 landings repeat this anchor. Dominant pricing-hook signal. STRONG.
2. **"фулфілмент для маркетплейсів Rozetka Prom Kasta"** — dedicated page with Carter's case + comparison table. STRONG.
3. **"фулфілмент для косметики"** — FEFO + temperature + 30-sec picking + 2200-word guide. STRONG.
4. **"ціни на фулфілмент 2026"** — tsiny page with dynamic tariff + concrete numbers + calculator embed. STRONG.
5. **"фулфілмент важких товарів"** — heavy-goods + EcoDrive 50/day case + pallet-1t positioning. STRONG (rare competitive angle).
6. **"3PL логістика Україна"** — dedicated page, 2h CRM integration hook, client results stats. MEDIUM-STRONG.
7. **"палетне зберігання Київ"** — 320 WMS slots + FEFO + 74% utilization + 450 UAH/mo anchor. STRONG (narrow niche).
8. **"фулфілмент Київ"** — geo landing with 3900 m² + 1-hour dispatch + "why Kyiv region is best hub" educational section. MEDIUM-STRONG.
9. **"фулфілмент для інтернет-магазину"** — dedicated page + 80→400 orders case + 5-criteria guide. STRONG.
10. **"blackout-стійкий фулфілмент / 0 днів простою з 2022"** — unique USP, in shcho-take + fulfilment-ukraina. STRONG defensive moat (no Ukrainian competitor owns this frame).

Supporting dominance factors: consistent price anchor (18 UAH), trust stack (150+ clients / 10y / 2 warehouses / 3 generators / Starlink), hero CTA forms → Telegram on every page, embedded calculator, vs-own-warehouse comparison table on 9 of 10 landings.

---

## 6. Top-10 Intent GAPS (create pages here)

Priority ranked by a mix of commercial value, roadmap priority flag, and competitor pressure:

1. **"фулфілмент для одягу/взуття"** — huge vertical, Sender + Nova Poshta cover it, we don't. `/ua/fulfilment-dlya-odyahu/` (roadmap 🟠).
2. **"фулфілмент для FOP / ФОП"** — high-volume UA search, zero competitor pages, direct fit for our small-biz positioning. `/ua/fulfilment-dlya-fop/` (🟠).
3. **"B2B фулфілмент / оптова логістика"** — LP-Sklad owns this, we have no dedicated page. `/ua/b2b-fulfilment/` (🟠).
4. **"фулфілмент для брендів СНД / виходу в Україну"** — already nailed in `/ru/services/`, but NO UA/EN parallel page, and no blog article feeding it. Bridge content gap.
5. **"MTP vs Нова Пошта фулфілмент"** — critical comparison intent we leave on the table; NP sends branded traffic, we need the counter-narrative. `/ua/blog/mtp-vs-nova-poshta-fulfilment/` (🟡 but high ROI).
6. **"фулфілмент в Бориспіль / біля аеропорту"** — we physically operate there, competitors don't. Easy local win. `/ua/3pl-boryspil/` (🟠).
7. **"фулфілмент для дропшипінгу"** — trending SMB query, roadmap calls it 🟡 but SERP competition is weak. `/ua/fulfilment-dropshipping/`.
8. **"фулфілмент Shopify / WooCommerce Україна"** — integration-centric queries, zero UA competitors indexed well. `/ua/fulfilment-shopify/`, `/ua/fulfilment-woocommerce/` (🟡).
9. **"як вибрати фулфілмент оператора"** — classic commercial-investigation pillar, blog gap — UA blog has only 3 posts. `/ua/blog/yak-vybrati-fulfilment/` (🟠).
10. **"вартість фулфілменту 2026 / реальні тарифи ринку"** — AI-cited content (Perplexity loves price roundups). Complements `/ua/tsiny/` with market-wide framing. `/ua/blog/vartist-fulfilmentu-2026/` (🟠).

Secondary gaps worth flagging: `/ua/faq/` exists but `/ua/blog/*` is thin; case-study library (`/ua/blog/case-ecodrive/`, `/ua/blog/case-kosmetyka/`) is planned but not built — these are AI-visibility goldmines; `/en/*` blog is strong but `/en/*` service pages lack cosmetics / fashion / electronics verticals so inbound EU traffic lands only on generic `/en/fulfillment-ukraine/`.

---

## 7. Cross-Language Coverage Inconsistencies

- UA has pillar `/ua/shcho-take-fulfilment/` + EN `/en/what-is-fulfillment/` + RU `/ru/chto-takoe-fulfilment/` — parity OK.
- UA has `/ua/paletne-zberigannya/` + RU `/ru/paletnoe-khranenie/` + EN `/en/pallet-storage/` — parity OK.
- UA and EN have `/calculator/`, `/tsiny/`(prices), `/services/` — parity OK.
- **Missing RU blog entirely** (only 3 legacy RU root-level posts at `/blog/*`, no `/ru/blog/` index). RU traffic for informational queries lands back on Tilda legacy URLs.
- **Missing UA blog depth** — 3 posts vs 30 EN posts; any UA informational query goes to competitors first.
- **Missing RU `thanks`** — conversion tracking hole for RU form submissions? Verify.

---

## 8. Quick-Win Keywords to Attack (next 4 weeks)

1. **"фулфілмент для одягу Україна"** — build `/ua/fulfilment-dlya-odyahu/` using cosmetics page as template. Sender ranks #1–3 here; we can challenge with fashion-specific FEFO-like angle (size/SKU variants, seasonal packs).
2. **"фулфілмент Бориспіль"** — `/ua/3pl-boryspil/` local page. We PHYSICALLY operate in Shchaslyve (Boryspil district) — unique geo-authenticity. Zero real competition on this exact phrase.
3. **"MTP vs Нова Пошта фулфілмент"** — blog comparison `/ua/blog/mtp-vs-nova-poshta-fulfilment/`. NP is searched 10× more than us; writing the comparison content captures branded NP traffic researching alternatives.

Bonus (4th if bandwidth allows): `/ua/blog/yak-vybrati-fulfilment/` — 10 criteria checklist. Universal commercial-investigation content, cheap to produce, high AI-citation potential.

---

## 9. Summary Stats

- **Pages in sitemap:** 109 (UA-26 / RU-24 / EN-52 / other-7)
- **High-intent UA landings sampled:** 14/15 OK (1 RU mirror)
- **Semantic core roadmap completion:** ~12 of 121 planned pages = **10%**
- **Vertical coverage:** 5 of 26 planned = **19%**
- **Blog depth UA:** 3 posts (target 24) = **12%**
- **Blog depth EN:** 30 posts (target 12) = **250%** over-invested on EN
- **Blog depth RU:** 3 legacy posts (no target set)
- **Unique defensible footprints:** 3 (blackout-resilience, Boryspil geo, EcoDrive heavy-goods case)
- **Obvious conversion funnel leaks:** 0 (calculator + hero form + tsiny page all present)
