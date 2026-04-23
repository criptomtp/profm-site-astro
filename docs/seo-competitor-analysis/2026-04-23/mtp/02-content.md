# MTP Group — Content & E-E-A-T Analysis
**Date:** 2026-04-23
**Site:** https://www.fulfillmentmtp.com.ua
**Benchmark:** Nova Poshta fulfillment, Sender Ukraine, LP-Sklad
**Framework:** Google QRG (Sept 2025) + hub-and-spoke topical authority

---

## 1. Executive scorecard

| Dimension | Score | Notes |
|---|---:|---|
| Topical authority (breadth) | 78/100 | Strong hub/spoke — pillar + 9 service spokes live. Blog breadth weak once dead tpost redirects excluded. |
| Topical authority (depth) | 82/100 | Pillar 2,778 words UA; service hub 1,016; top blog 4,104. All above competitor averages we benchmark. |
| Experience (first-hand) | 88/100 | Named founder, 150+ clients with specific brands (Carter's, I.Love.My.Cycle, EcoDrive, Elemis, ORNER), 60 000 shipments/mo, 2 warehouses with addresses, 0 days downtime since Feb 2022 — highly specific, verifiable. |
| Expertise | 76/100 | Author bio on pillar + blog (Микола Лящук, 11+ yrs). Missing on services/pricing/recalls/about. Inconsistent surfacing. |
| Authoritativeness | 72/100 | Press mentions (Europa Plus, Гроші Плюс, Top100.company), YouTube case videos, 10 named reviewers. No industry body affiliations, no external awards cited. |
| Trustworthiness | 81/100 | Phone, Telegram, 2 physical addresses, SLA/matriotvid contracts mentioned, privacy page, material responsibility clause. Missing: legal entity details, contract PDFs, security/data page. |
| AI citation readiness | 87/100 | Dual-MD system unique advantage; structured facts (tariffs, timelines, stats) quotable. FAQ schema on 5/8 pillar pages. "Main thing in 30 seconds" TL;DR boxes on pillar. |
| Overall content quality | **81/100** | Above competitor average; held back by 34+ dead blog redirects and author-bio inconsistency. |

---

## 2. Hub-and-spoke inventory

### 2.1 Pillar hub (/ua/shcho-take-fulfilment/)
- **Word count:** 2,778 (clean markdown)
- **Structure:** 8 numbered sections, TL;DR box, author bio, breadcrumbs, 8-question FAQ, comparison tables, ROI formula, 10-criteria operator-selection list, myth busters, 12 internal links
- **Schema:** Article + BreadcrumbList + FAQPage + ImageObject + Organization + Person + 6 Q&A
- **Verdict:** Best-in-class for UA fulfillment sector. Sender/Nova Poshta do not have a dedicated long-form pillar answering "what is fulfillment" at this depth.

### 2.2 Service hub (/ua/services/)
- **Word count:** 1,016
- **Structure:** 10 service cards with tariff, video tour embed, dynamic tariff ladder, comparison table (own warehouse vs MTP), 6-question FAQ
- **Schema:** Service + AggregateOffer + FAQPage + Organization
- **Gap:** No author bio, no update timestamp, no case proof inline

### 2.3 Pricing (/ua/tsiny/)
- **Word count:** 1,121 — above 800-word service-page floor
- **Schema:** AggregateOffer + LocalBusiness + FAQPage + BreadcrumbList
- **Transparency:** Full tariff ladder (26→18 UAH based on volume), storage rates, worked examples. Rare in UA market — Nova Poshta/Sender do not publish full ladders.

### 2.4 Calculator (/ua/calculator/)
- **Word count:** 949
- **Only explanatory copy around interactive tool**
- **Gap:** Add sample calculations for 3 personas (cosmetics / clothing / heavy goods) as crawlable text

### 2.5 Service spokes (9 landing pages)
| URL | Words | Floor (800) | Status |
|---|---:|---|---|
| /ua/fulfilment-ukraina/ | 1,422 | OK | Healthy |
| /ua/fulfilment-dlya-internet-magazynu/ | 1,185 | OK | Healthy |
| /ua/fulfilment-dlya-marketpleysiv/ | 1,502 | OK | Healthy |
| /ua/fulfilment-dlya-kosmetyky/ | 2,338 | OK | Excellent (FEFO depth) |
| /ua/fulfilment-vazhkykh-tovariv/ | 1,076 | OK | Healthy |
| /ua/fulfilment-kyiv/ | 1,086 | OK | Healthy |
| /ua/3pl-logistyka/ | 890 | OK | Borderline |
| /ua/paletne-zberigannya/ | 695 | **<800** | **Thin** |
| /ua/skladski-poslugy/ | 724 | **<800** | **Thin** |

**Average spoke depth:** 1,213 words. Competitor average for the same queries on Sender/LP-Sklad is ~600-900 — MTP is already at competitor+20% on 7 of 9 spokes.

### 2.6 Proof pages
- **/ua/recalls/:** 1,016 words, 8 video testimonials (real client YouTube), 3 structured case studies with metrics (Carter's 10→72 ship/day, I.Love.My.Cycle 25→73, EcoDrive 0 damage), 10 named star reviews with AggregateRating schema + 10× Review/Person schema. **Strongest E-E-A-T asset on the site.**
- **/ua/about/:** 1,131 words. Origin story, two named warehouses with m², team size evolution 3→50, technology stack, resilience story. Missing: team photos beyond founder, legal entity (ЄДРПОУ), year founded in structured data.

### 2.7 Blog
- **Live index:** 38 cards displayed
- **Real articles (200):** 3 — top-fulfilment-operatoriv-2026 (4,104 words, comparison pillar), top-marketpleysiv-ukrayiny, scho-take-fulfilment (1,613 words)
- **Dead cards (301 to /ua/blog/):** ~34 legacy /tpost/* URLs still rendered as clickable cards. Every click = loop to blog index. Major content-integrity + UX + crawl-budget bug.
- **Verdict:** Blog appears rich; in reality only 3 real posts. This is the single biggest authority leak.

---

## 3. E-E-A-T breakdown (weighted QRG Sept 2025)

### Experience — 88/100 (weight 20%)
Strongest pillar. Multiple first-hand signals:
- Named founder with 11-year timeline, on-warehouse photo, linked on every pillar
- Specific case studies with before/after metrics (not generic "we helped a client")
- Physical verification possible: 2 named warehouses (Shchaslyve 2,800 m², Bilohorodka 1,100 m²)
- Warehouse video tour with facade-loaded YouTube embed
- Blackout narrative with hardware specifics (3× diesel, 180 kW, 36 h autonomy, 5-day fuel reserve, 2× Starlink)
- Concrete uptime claim: "0 days downtime since Feb 2022" — date-anchored, verifiable
- 150+ client count aligned with 60 000+/month shipments — mathematically consistent (~400 orders/client/month avg)

### Expertise — 76/100 (weight 25%)
- Author bio (Person schema with sameAs LinkedIn + Telegram) on pillar + top-10-operators blog
- **Missing author surfacing on:** /ua/services/, /ua/tsiny/, /ua/calculator/, /ua/recalls/, /ua/about/, 7 of 9 spokes
- No team bios beyond founder
- Terminology usage correct (FEFO, FBA, 3PL, WMS, SLA, picking, pRRO)
- No industry certifications mentioned (ISO 9001, FIATA, EBA member)

### Authoritativeness — 72/100 (weight 25%)
Mentions:
- Europa Plus radio interview (linked to YouTube)
- Touch Magazine (Гроші Плюс) feature
- Top100.company listing
- Rozetka/Prom/Kasta/Horoshop/KeyCRM/SalesDrive integrations visible
- LinkedIn company page linked from Person schema
**Missing:** industry association memberships, award badges, Ukrainian E-Commerce Association endorsements, Google Business Profile link on-page, Wikipedia/external knowledge panel seeds.

### Trustworthiness — 81/100 (weight 30%)
Present:
- Phone +38 (050) 144-46-45 on every page header
- Telegram direct link to @nikolay_mtp
- Two warehouse addresses (Shchaslyve, Bilohorodka)
- Privacy policy at /ua/privacy/
- Contract + SLA + material responsibility language
- Transparent published pricing (rare)
- Dual-md noindex canonical guard correctly implemented
Missing:
- ЄДРПОУ / legal entity full name (required for B2B trust in UA)
- Signed contract sample PDF
- Refund/compensation policy dedicated page
- Security/data handling statement (GDPR/UA equivalents)
- Team "About the warehouse" page with multiple staff photos

---

## 4. Content depth vs competitor average

Based on prior-round competitor audits (Nova Poshta fulfillment, Sender, LP-Sklad, Unipost, Rozetka Fulfillment):

| Page type | Competitor avg | MTP | Delta |
|---|---:|---:|---:|
| Homepage | ~800 w | 1,036 w | +30% |
| "What is fulfillment" pillar | ~1,200 w | 2,778 w | **+131%** |
| Service hub | ~900 w | 1,016 w | +13% |
| Pricing page | ~400 w (or hidden) | 1,121 w | +180% |
| Category spoke | ~700 w | 1,213 w avg | +73% |
| About | ~600 w | 1,131 w | +88% |
| Reviews/cases | ~400 w (often missing) | 1,016 w | +154% |

**Verdict:** MTP beats the competitor+20% target on 6 of 7 page types. Homepage is the one at risk — only 1,036 words, barely above the +20% threshold vs Nova Poshta's fulfillment landing (~800 w) and below Rozetka's. Consider hero-adjacent SEO-text expansion with value-specific copy (not keyword stuffing).

---

## 5. Thin pages

| URL | Words | Action |
|---|---:|---|
| /ua/paletne-zberigannya/ | 695 | Expand to 1,000-1,200: add pallet dimensions table, weight classes, sample tariffs for 10/50/200 pallets, FEFO workflow, photos |
| /ua/skladski-poslugy/ | 724 | Expand to 1,000+: differentiate from /ua/services/ (or merge). Add service-matrix vs 3PL vs fulfillment. |
| /ua/calculator/ | 949 | Borderline — add 3 worked-example personas + link to pillar sections |
| /ua/privacy/ | 549 | Acceptable for legal page — no action |

---

## 6. Unique angles (not copied by competitors)

### 6.1 Blackout-proof infrastructure narrative
Positioned on home, pillar, services, recalls, about. Hardware-specific, date-anchored, supported by client quote ("Жодного збою навіть під час важких обстрілів" — Ірина Савченко, OrnerUA). **No competitor matches this specificity.** Nova Poshta claims reliability generically; Sender does not address blackouts on landing.

### 6.2 CIS-entry funnel (/ru/services/)
Distinctive RU angle: "21-day Ukraine market entry for brands from KZ/MD/GE/AM/UZ/AZ" — customs, УкрСЕПРО, UAH/USD/EUR settlement, Rozetka/Prom onboarding. 3,055 words. **This is a zero-competition SERP** — Ukrainian fulfillment operators do not market to CIS inbound; Russian-speaking KZ/MD entrepreneurs lack a dedicated destination.

### 6.3 Trilingual non-translation strategy
UA / RU / EN have different angles per CLAUDE.md policy. EN home 4,157 words, EN services 1,399, EN blog 1,044. This creates three authority surfaces for different search intents without hreflang duplicate-content penalty (confirmed consistent cross-linking).

### 6.4 Dual-md AI access
Every page auto-generates a clean markdown twin with frontmatter (title, description, canonical, lang, generated timestamp) and `X-Robots-Tag: noindex, follow` + per-page `Link: rel=canonical`. **First fulfillment provider in UA with this.** Already producing structured, quotable outputs for AI engines — the reason this very audit was faster and more accurate than competitor audits.

### 6.5 Public tariff ladder
26 → 25 → 23 → 22 → 20 → 19 → 18 UAH volume ladder published openly. Nova Poshta, Sender, LP-Sklad all require a quote request. Reduces friction and doubles as a quotable fact for AI citations.

### 6.6 Founder-authored pillar
Микола Лящук named as author with Person schema (jobTitle, url, sameAs LinkedIn+Telegram) and inline "Автор" attribution with photo. Neither Nova Poshta fulfillment page nor Sender UA surface a named author.

---

## 7. Content gaps vs fulfillment search intent (UA/CIS)

### 7.1 Missing topical coverage
| Missing topic | Intent volume signal | Recommended page type |
|---|---|---|
| "фулфілмент для Shopify / WooCommerce / OpenCart" — platform-specific | High mid-funnel | 3 spoke pages |
| "фулфілмент Львів / Одеса / Дніпро" | City long-tail | 3 regional pages |
| "фулфілмент FBA підготовка" (prep for Amazon/Bol/Kaufland) | CIS/EU outbound | 1 spoke |
| "повернення товару фулфілмент" (returns-as-a-service) | Deep funnel | Dedicated service page |
| "фулфілмент для БАД / дієтичних добавок" | Regulated niche | 1 spoke (cosmetics exists, BAD different compliance) |
| "SLA фулфілмент шаблон" | Informational | Downloadable asset + pillar |
| "як підписати договір фулфілмент" | Bottom funnel | FAQ hub |
| "фулфілмент для B2B / опт" | New segment | Service page |

### 7.2 Missing formats
- **Video page:** embed warehouse tour + case videos on one `/ua/video/` hub with transcripts
- **Glossary/terminology page:** WMS, FEFO, FIFO, SKU, pick rate, 3PL, 4PL, FBA, FBO, FBS — high AI-citation surface
- **Comparison landing pages:** `MTP vs Nova Poshta fulfillment`, `MTP vs Sender`, `MTP vs LP-Sklad` (see `seo-competitor-pages` skill)
- **Case-study hub:** individual deep dives per client (currently only tile summaries on /recalls/)
- **Integration tutorials:** `Horoshop + MTP фулфілмент`, `KeyCRM + MTP`, `Rozetka MTP setup` — each 600-1000 words

### 7.3 Freshness signals
- Pillar shows "Опубліковано: 3 квітня 2026 р. · Оновлено: 22 квітня 2026 р." — excellent
- /ua/services/, /ua/tsiny/, /ua/about/, /ua/recalls/, /ua/calculator/ — **no visible publish or update date**. Add `dateModified` schema property across pillar landing pages.

---

## 8. AI citation readiness (87/100)

Strong:
- Dual-md delivery (5-10× lower token cost for AI crawlers)
- TL;DR "Головне за 30 секунд" bulleted summaries on pillar
- Specific quotable facts: "150+ clients", "60 000+ shipments/mo", "0 days downtime since Feb 2022", "30-second pick time", "99.7% pick accuracy", "36-hour generator autonomy", "from 18 UAH/order"
- Comparison tables in markdown (parse-ready)
- FAQ schema on 5 of top 8 pages
- Author Person schema with sameAs LinkedIn

Weak:
- No HowTo schema (process steps are narrative, not schema-marked)
- No SoftwareApplication schema for WMS/calculator
- No Offer/Service schema on spoke pages consistently
- llms.txt exists (83 lines) but worth expanding with per-URL short description + last-updated stamps
- No canonical TL;DR on spokes (only on pillar)

---

## 9. AI-generated content markers (QRG Sept 2025 scan)

Pages checked: pillar, services, recalls, about, top-10-operators blog, RU /services/, /ua/tsiny/.

No flags for:
- Generic phrasing (all copy references specific numbers, named clients, UA-market context)
- Lack of specificity (exhaustive tariff breakdowns, named warehouses with m², specific client growth curves)
- No first-hand experience (war-era blackout narrative is deeply first-hand)
- Factual inaccuracies (all checked facts internally consistent; Amazon FBA 1999 date correct)
- Repetitive structure (pillar/service/spoke templates differ meaningfully)

One mild flag: blog index has 34+ cards that loop-redirect — not an AI marker per se, but a Helpful-Content-System risk (user dissatisfaction signal).

---

## 10. Prioritised improvements

### P0 — Fix within 7 days
1. **Remove or resurrect 34 dead tpost blog cards.** Either delete from blog index (cleanest) or rebuild 5-10 high-value legacy posts as real /ua/blog/[slug] pages. Current state inflates internal linking to loop.
2. **Expand 2 thin spokes** (/ua/paletne-zberigannya/ to 1,100 w, /ua/skladski-poslugy/ to 1,000 w) with tariff tables, FEFO details, sample configurations.
3. **Add author bio component** to /ua/services/, /ua/tsiny/, /ua/calculator/, /ua/about/, /ua/recalls/ — reuse pillar pattern (photo + name + jobTitle + 2 sameAs).
4. **Add dateModified schema** across all landing pages (not just pillar).

### P1 — Within 30 days
5. Build 3 platform-spokes: Shopify, WooCommerce, Horoshop integration pages.
6. Build 3 MTP-vs-competitor comparison pages (see seo-competitor-pages skill).
7. Add ЄДРПОУ + legal entity block to /ua/about/ + footer.
8. Add glossary page for AI citation capture (/ua/terminy/).
9. Expand homepage to 1,400+ words with case-specific hero-adjacent block.

### P2 — Within 90 days
10. 3 regional pages (Lviv, Odesa, Dnipro).
11. Returns-as-a-service dedicated page.
12. 5 deep case-study pages (one per named client).
13. FBA-prep spoke for CIS→EU outbound flow.
14. Video hub with transcripts.

---

## 11. Competitive positioning summary

Against the benchmarked three competitors (Nova Poshta fulfillment, Sender Ukraine, LP-Sklad):
- **Content volume:** MTP wins on 6/7 page types measured.
- **E-E-A-T:** MTP leads on Experience (named founder, named clients, quantified outcomes) and Trust (transparent pricing). Trails on Authoritativeness (fewer external endorsements visible on-page) — addressable with award badges + association memberships block.
- **Unique moats:** blackout narrative, CIS-inbound funnel, dual-md, public tariff ladder, trilingual non-translation strategy. Each difficult for competitors to replicate in under 6 months.
- **Single biggest risk:** 34 dead blog redirects diluting authority and creating a Helpful-Content-System negative signal in the March 2024 core algorithm.

---

## 12. Appendix — word counts (measured from dual-md on 2026-04-23)

| URL | Words | Floor | Status |
|---|---:|---|---|
| / (UA home) | 1,036 | 500 | OK |
| /ua/shcho-take-fulfilment/ (pillar) | 2,778 | 1,500 | Excellent |
| /ua/services/ | 1,016 | 800 | OK |
| /ua/tsiny/ | 1,121 | 800 | OK |
| /ua/calculator/ | 949 | 800 | OK |
| /ua/about/ | 1,131 | 500 | OK |
| /ua/recalls/ | 1,016 | 500 | OK |
| /ua/blog/ (index) | 1,186 | n/a | OK structure, broken links |
| /ua/faq/ | 1,183 | 500 | OK |
| /ua/guide/ | 1,641 | 1,500 | OK |
| /ua/api-docs/ | 983 | 500 | OK |
| /ua/privacy/ | 549 | 300 | OK (legal) |
| /ua/fulfilment-ukraina/ | 1,422 | 800 | OK |
| /ua/fulfilment-dlya-internet-magazynu/ | 1,185 | 800 | OK |
| /ua/fulfilment-dlya-marketpleysiv/ | 1,502 | 800 | OK |
| /ua/fulfilment-dlya-kosmetyky/ | 2,338 | 800 | Excellent |
| /ua/fulfilment-vazhkykh-tovariv/ | 1,076 | 800 | OK |
| /ua/fulfilment-kyiv/ | 1,086 | 800 | OK |
| /ua/3pl-logistyka/ | 890 | 800 | OK |
| /ua/paletne-zberigannya/ | 695 | 800 | **Thin** |
| /ua/skladski-poslugy/ | 724 | 800 | **Thin** |
| /ru/services/ | 3,055 | 800 | Excellent (CIS angle) |
| /en/ | 4,157 | 500 | Excellent |
| /en/services/ | 1,399 | 800 | OK |
| /ua/blog/top-fulfilment-operatoriv-2026/ | 4,104 | 1,500 | Excellent |
| /ua/blog/scho-take-fulfilment/ | 1,613 | 1,500 | OK |

**End of report.**
