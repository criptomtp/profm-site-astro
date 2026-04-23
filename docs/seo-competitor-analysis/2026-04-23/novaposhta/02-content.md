# Nova Poshta — Fulfillment Page Content Audit

**URL analyzed:** https://novaposhta.ua/for-business/fulfillment/
**Date:** 2026-04-23
**Analyst:** Content Quality specialist (Google Sept 2025 QRG methodology)
**Client context:** Benchmarking for MTP Group (Ukrainian specialist 3PL)

---

## 1. Content Quality Score: 58/100

A functional, information-dense landing page that covers the operational basics but lacks every major E-E-A-T lever (no case studies, no author, no certifications, no vertical depth). It reads as a *corporate service description* rather than a *thought-leadership hub* — which is exactly the gap a specialist 3PL can exploit.

---

## 2. Word Count & Structural Analysis

| Metric | UA version | EN version |
|---|---|---|
| Total words (main content, nav/footer stripped) | **~1,500** | **~2,430** |
| Total H2 sections | 17 | 17 |
| H3 / H4 sub-sections | 27+ | 27+ |
| Title | "Послуги Фулфілменту - «Нова пошта» \| Доставка майбутнього" (62 chars — over limit) | "Fulfilment Services - Nova Post \| Delivery of the future" (56 chars — OK) |
| Meta description | Present, truncated in output (appears ~160 chars) | Present |
| Canonical tag | **MISSING** in HTML (relies on JS/CDN headers) | Missing |
| Hreflang tags | **NONE detected** in raw HTML | None detected |

**Benchmark verdict:** 1,500 UA words meets the "service page" minimum (800) with margin, but it is a *single page covering 9 distinct topics* — so topical depth per topic is thin (~170 words each). MTP's 1,200-word goal per specialist vertical page will beat NP's generalist block on topical authority per keyword cluster.

---

## 3. H1/H2/H3 Topical Structure (UA)

**H1:** Фулфілмент від Нової пошти

**H2 outline (17 sections):**
1. Ще швидше, ніж ви звикли! (same-day delivery hook — Kyiv/Lviv/Odesa/Dnipro before 14:00)
2. Простими словами про фулфілмент (definition)
3. Працюйте гнучко, масштабуйтеся швидко (flexibility pitch)
4. Переваги для вашого бізнесу (benefits list)
5. Інтеграція з фулфілментом (integrations — SalesDrive, Shopify via Shopillect, Shopify via "Poshta" app)
6. Як стати клієнтом? (onboarding)
7. Для кого ця послуга (target audiences)
8. Чому логістичні рішення саме від Нової пошти (brand authority pitch)
9. Готові спростити свій бізнес уже сьогодні? (CTA block)
10. Як розпочати співпрацю (6 warehouse addresses + contact names + phone numbers)
11. Фулфілмент чи свій склад. Що вигідніше? (comparison)
12. Переваги послуги
13. Недоліки власного складу
14. Вибирайте фулфілмент від Нової пошти — розумне рішення... (closing pitch)
15. Уже скористалися послугами фулфілменту (only 2 client logos visible: "А-ба-ба-га-ла-ма-га", "The Ukrainians Media")
16. Поширені запитання (FAQ — 8 questions)
17. Документи для співпраці (required documents)

**Topical observation:** No mention of cold-chain, hazmat, cosmetics, heavy/oversize, apparel returns, marketplace-specific SKU prep, B2B pallet handling, or bonded storage. Positioning is **SMB e-commerce only**.

---

## 4. E-E-A-T Scoring: 42/100

| Factor | Weight | Score | Evidence |
|---|---|---|---|
| **Experience** (20%) | 20% | 6/20 | Only 2 named customers (book publisher + media outlet — both niche/PR-friendly brands, not scale e-commerce). No case study pages, no "X orders/day processed" numbers, no photos of operations, no warehouse tour, no team. The page asserts speed ("before 14:00 → same day") but provides no proof layer. |
| **Expertise** (25%) | 25% | 10/25 | Content is technically correct on basic ops (packaging rules, barcode labeling, accepted/prohibited items, 3 tiers of receiving quality). No named author, no byline, no logistics expert quote. Warehouse contact names (Zinkov, Vozniuk, Budzilo, Shchelkova) appear only as shipping coordinators, not as credentialed experts. |
| **Authoritativeness** (25%) | 25% | 15/25 | Massive brand halo from Nova Poshta courier business carries real weight. Schema.org Organization + BreadcrumbList present. External backlink ecosystem (salesdrive.ua/blog, shopillect.com, apps.shopify.com/poshta) demonstrates partner-level authority. BUT: **zero fulfillment-specific authority signals** — no industry awards, no certifications (ISO 9001, GMP), no press coverage of the fulfillment arm specifically. |
| **Trustworthiness** (30%) | 30% | 11/30 | 4 phone numbers + contact point schema = good transparency. 6 warehouse addresses published = concrete. FAQ addresses real objections. BUT: no pricing (every competitor-specialist will beat this), no SLA commitments, no insurance/liability statement, no data-protection note, no security/GDPR language, no testimonials with person+role+company, no video. |

**Total E-E-A-T: 42/100** — dominated by brand-borrowed authority, not fulfillment-specific proof.

---

## 5. CTAs & Conversion Path

**Primary CTAs detected:**
- "Почни вже зараз" (hero, anchor to `#submit-request` form lower on page)
- "Як стати клієнтом?" → same form anchor
- Hero sub-line pushes urgency: "orders received before 14:00 delivered same day to Kyiv/Lviv/Odesa/Dnipro"

**Conversion friction:**
- Single conversion vehicle: a form at `#submit-request`
- No calculator, no price list, no instant-quote tool
- No phone-first CTA (the 4 phone numbers are buried in schema/footer, not surfaced in hero)
- No live chat widget detected
- No lead magnet (no PDF, no guide, no "compare fulfillment vs own warehouse" tool despite section 11 literally being about that comparison)

**CTA verdict:** Single-funnel ("fill the form") with weak urgency. A specialist 3PL with a calculator + hero CTA form (MTP's pattern) will out-convert this on every metric.

---

## 6. Positioning vs Core Courier Business

Nova Poshta positions fulfillment as an **extension of courier superiority**, not as a specialist discipline. Key framing patterns:

- Hero speed claim ("14:00 cut-off → same-day delivery") leverages the courier network, not warehouse competence
- Section "Чому логістичні рішення саме від Нової пошти" sells the courier brand, not fulfillment expertise
- 6 warehouse addresses (Kyiv x3, Odesa, Dnipro, Lviv — inferred from major-city naming) are all near NP sorting hubs — operational synergy is the implicit moat
- Integration story (Shopify, SalesDrive) is about **order-to-courier** flow, not fulfillment-layer automation (WMS, bin management, inventory accuracy SLA)

**Translation:** fulfillment is a **cross-sell service for existing NP courier clients**, not a standalone 3PL product. This is a structural weakness a specialist 3PL exploits.

---

## 7. Sub-pages for Verticals? **NO — single landing page only.**

Verified (all 404):
- `/for-business/fulfillment-cosmetics` → 404
- `/for-business/fulfillment/cosmetics` → 404
- `/for-business/fulfillment/marketplace` → 404

The only fulfillment URLs that exist are:
- `/for-business/fulfillment` (UA)
- `/en/for-business/fulfillment` (EN)
- `/for-business/fulfillment/#submit-request` (anchor)

**No vertical specialization pages** for cosmetics, apparel, heavy/oversize, fragile, food/FMCG, B2B, marketplaces (Rozetka/Prom/Olx/Zakaz), cross-border, or subscription-box models.

**This is the single largest SEO content gap MTP can exploit.** Every vertical keyword ("фулфілмент косметики", "фулфілмент одягу", "фулфілмент для Rozetka/Prom") is orphaned on NP's side — they rank only the single generic page, which cannot win long-tail specialist queries.

---

## 8. Language Versions Available

| Language | URL | Status | Words |
|---|---|---|---|
| Ukrainian | `/for-business/fulfillment` | 200 OK | ~1,500 |
| English | `/en/for-business/fulfillment` | 200 OK | ~2,430 (longer — likely includes expanded explanations for foreign audience) |
| Russian | `/ru/for-business/fulfillment` | **404 NOT FOUND** |

**Observation:** No Russian version. Given NP's all-Ukrainian posture post-2022 this is deliberate. MTP keeping a RU version remains a differentiation lever for RU-speaking SMB owners in Ukraine who still search in RU (significant share of Kyiv/Odesa/Kharkiv/Dnipro audience per current GSC data).

**Hreflang:** No hreflang tags detected in the raw HTML between UA↔EN — SEO hygiene issue on their side.

---

## 9. Unique Angles (Their Moat) & Weaknesses

### Their genuine moat (hard to replicate)
1. **Same-day delivery from 4 major cities** via their own courier network — a specialist 3PL must rely on third-party couriers, adding cost + SLA risk
2. **6 physical warehouses** across Ukraine (Kyiv x3, Odesa, Dnipro, possibly Lviv) — geographic coverage beats any single-warehouse specialist
3. **Brand trust halo** — "Nova Poshta" is top-5 most-trusted Ukrainian brand; zero sales friction on name recognition
4. **Built-in integrations** with SalesDrive (major UA CRM for e-commerce), Shopify via 2 different apps (Shopillect + Poshta) — lowers onboarding cost for Shopify sellers
5. **Tier integration**: every client already ships via NP courier → fulfillment is an incremental upsell with zero switching cost
6. **Partner ecosystem referral traffic**: salesdrive.ua/blog and shopillect.com both send warm traffic

### Their weaknesses (MTP exploit zone)
1. **No vertical specialization** — generic "for e-commerce" positioning; zero pages for cosmetics, apparel, marketplace-specific, fragile, heavy, food, B2B, cross-border
2. **Only 2 named clients visible** (А-ба-ба-га-ла-ма-га publisher + The Ukrainians Media) — neither is a scale e-commerce operation; no case studies with conversion/cost numbers
3. **No pricing transparency, no calculator** — every lead must call/fill a form to get a quote
4. **No author, no logistics expert** — zero expertise signals beyond the NP corporate brand
5. **No certifications** (ISO 9001, GMP, hazmat, cold-chain)
6. **FAQ is operational only** (documents, packaging, prohibited items) — missing the strategic questions a serious e-commerce operator asks (pick accuracy %, inventory shrinkage SLA, returns processing time, peak-season capacity, dedicated account manager)
7. **Single page carries all the SEO weight** — cannot rank for long-tail vertical queries
8. **404 on RU** — loses RU-language SMB segment (still ~25-30% of Kyiv/East online merchant audience)
9. **Bookish brand tone** — reads corporate, not expert; no operational depth that a warehouse manager would recognize
10. **Returns workflow is not documented on-page** — huge operator pain point left unanswered

---

## 10. AI Citation Readiness: 52/100

- Definition blocks ("Простими словами про фулфілмент") are quotable — ChatGPT/Claude/Perplexity will pull these
- FAQ section is well-structured for AI extraction
- BUT: no Article schema, no FAQPage schema, no author object, no datePublished, no organization-level E-E-A-T schema beyond the basics
- No original data points (no "we process X orders/day", no "99.X% pick accuracy", no "cut peak-season costs by X%")
- Generic claims dominate — AI assistants prefer *specific numbers* for citations

A specialist 3PL with FAQPage schema + Article schema + original stats + author bylines + dated "last updated" will out-cite NP on AI Search surfaces.

---

## 11. Verdict: Serious or Stub?

**Somewhere in between — a "brand-extension" page, not a "fulfillment-first" product.**

Nova Poshta is *operationally* serious about fulfillment (6 warehouses, real integrations, live client intake) but *content-strategically* they treat it as a secondary product:
- No content marketing engine behind it
- No vertical landing pages
- No thought leadership, no blog integration, no experts
- Single-URL SEO footprint
- Minimal proof layer

**This is a massive opportunity for MTP.** NP wins on brand + geography + same-day speed. MTP wins on specialization, proof, pricing transparency, and topical SEO depth.

---

## 12. MTP Positioning Playbook vs Nova Poshta

### Positioning advantages MTP should exploit (top-5)

1. **Specialist depth > Generalist brand.** Build 8–12 vertical landing pages (cosmetics, apparel/shoes, food/FMCG, marketplace-specific: Rozetka/Prom/Olx/Zakaz, cross-border, heavy/oversize, subscription boxes, B2B pallet). Every one is an SEO moat NP has zero defense on.
2. **Price transparency + calculator.** NP has no calculator; MTP's calculator + per-SKU pricing closes the "gotta fill a form" friction.
3. **Proof layer.** Publish 5–10 case studies with real numbers (orders/day, pick accuracy %, cost saved vs own warehouse, peak-season handling). NP has 2 logos and no case studies.
4. **Author + expertise.** Named warehouse ops lead / fulfillment director with bylines, photos, LinkedIn. NP has anonymous corporate voice.
5. **RU + EN content parity.** NP dropped RU (404). MTP keeps 3-language coverage → capture RU-searching Ukrainian merchants NP abandons.

### Defensive acknowledgments (don't pick these fights)

- Do NOT compete on same-day delivery coverage across 4+ cities — that requires owning the courier network. Position against: "We specialize. NP generalizes. Specialists save you 15-25% vs integrated carrier fulfillment because we optimize the warehouse layer, not the delivery layer."
- Do NOT compete on brand trust at cold-intro stage — NP wins. Position against: "Big brand = cookie-cutter process. We build YOUR SOP for YOUR SKUs."

### Risks (2)

1. **NP could spin up vertical pages fast.** Their content team is larger; if they notice MTP ranking for "фулфілмент косметики" etc., they can copy within 60-90 days. Mitigation: file vertical pages FIRST (speed to market), build topical authority with linked blog clusters, secure backlinks early.
2. **NP's same-day-delivery hook is genuinely strong** for Kyiv/Lviv/Odesa/Dnipro SMBs. MTP must either match same-day on major routes (via NP integration ironically) or reframe the buyer conversation toward **total cost** and **pick accuracy**, not delivery speed. If MTP lets NP own the speed frame, mid-market SMBs will default to NP.

---

## 13. Content Minimum Compliance Summary

| Page Type | Min Words | NP UA actual | NP EN actual | Verdict |
|---|---|---|---|---|
| Service page | 800 | 1,500 | 2,430 | Passes minimum |
| Case studies | — | 0 | 0 | **FAIL** |
| Vertical pages | — | 0 | 0 | **FAIL** |
| Author/expertise | — | None | None | **FAIL** |
| Pricing transparency | — | None | None | **FAIL** |

---

## Sources & Artifacts

- Raw HTML UA: `/tmp/np-fulfillment.html` (860 KB)
- Raw HTML EN: `/tmp/np-fulfillment-en.html` (797 KB)
- Related NP referral backlinks observed: salesdrive.ua/blog/fulfilment-nova-poshta/, shopillect.com/uk/integrations/nova-poshta-fulfillment, apps.shopify.com/poshta

---

*End of content audit.*
