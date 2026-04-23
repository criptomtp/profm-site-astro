# Nova Poshta Fulfillment — Keyword Footprint Analysis

**URL analyzed:** https://novaposhta.ua/for-business/fulfillment/
**Date:** 2026-04-23
**Domain:** novaposhta.ua (Ukraine's #1 courier — DR ~80+, millions of monthly visits)
**Competitor class:** Infrastructure-giant adjacent — fulfillment is a sub-product, not the core brand
**Analyst goal:** map which queries NP rank-dominates via on-page + domain equity, and identify uncontested queries MTP Group can own.

---

## 1. On-Page Signals (raw extraction)

### 1.1 Meta tags
| Field | Value |
|---|---|
| **Title** | `Послуги Фулфілменту - «Нова пошта» \| Доставка майбутнього` |
| **Description** | `Послуги Фулфілменту \| Нова пошта — Швидка та надійна доставка ★ Найбільша мережа відділень по всій Україні ✔ Доставка протягом 1-го дня ✔ Кур...` (truncated; legacy format with stars and checkmarks — circa 2018) |
| **Meta keywords** | Not present |
| **Og:title / og:description** | Mirror `<title>` / `<meta description>` — no divergent social optimization |
| **Canonical** | `/for-business/fulfillment` (implicit — no explicit `<link rel=canonical>` tag observed in head) |
| **Hreflang** | `uk` ↔ `en` pair present via `<a>` tags, no x-default (confirmed in 01-technical.md) |

**Observation:** NP's title is weak — the second half `«Доставка майбутнього»` is a brand tagline, not a query modifier. No "фулфілмент для інтернет-магазину", no "склад", no "Київ/Львів", no "ціна" in the title. This is a branded trust play, not a keyword play.

### 1.2 H1
`Фулфілмент від Нової пошти`

Single H1, tight, brand-weighted. Targets `фулфілмент нова пошта` as the anchor query. Does NOT target `фулфілмент` (ambiguous head term) directly — NP implicitly relies on brand + backlinks to outrank generic head.

### 1.3 H2 sequence (14 sections — the **full keyword storyline**)
1. Ще швидше, ніж ви звикли! (*speed tease*)
2. Простими словами про фулфілмент ← **informational: "що таке фулфілмент"**
3. Працюйте гнучко, масштабуйтеся швидко — з нами це просто (*3-step explainer*)
4. Переваги для вашого бізнесу ← **benefits cluster**
5. Інтеграція з фулфілментом ← **integrations cluster (SalesDrive / Shopify / Poshta app)**
6. Як стати клієнтом? ← **onboarding / HOW-TO**
7. Для кого ця послуга ← **audience segmentation**
8. Чому логістичні рішення саме від Нової пошти ← **brand moat**
9. Готові спростити свій бізнес уже сьогодні? (*mid-page CTA*)
10. Як розпочати співпрацю (*duplicate of #6 — weak IA*)
11. Фулфілмент чи свій склад. Що вигідніше? ← **comparison / decision**
12. Переваги послуги ← **duplicate cluster (cannibalizes #4)**
13. Недоліки власного складу ← **pain-point framing**
14. Вибирайте фулфілмент від Нової пошти — розумне рішення для зростання вашого онлайн-бізнесу! (*closing CTA*)
15. Уже скористалися послугами фулфілменту ← **social proof (10 brand logos)**
16. Поширені запитання ← **FAQ cluster (2 questions only — see 1.5)**
17. Документи для співпраці

### 1.4 H3 (only 2 found — thin subheading depth)
- `Бізнесу` (breadcrumb-ish)
- `Повний цикл турботи про ваші онлайн-продажі`

### 1.5 FAQ questions (the concrete long-tail NP tries to capture)
NP's FAQ block has only **2 questions**:
1. **"Які документи потрібні для початку співпраці?"** — targets `договір фулфілмент нова пошта`, `документи для фулфілменту`
2. **"Як відправити товари на склад фулфілменту Нової пошти?"** — targets `як відправити товар на фулфілмент нової пошти` + surfaces **9 warehouse addresses** (Київ ×4, Львів, Одеса, Дніпро, Івано-Франківськ) — strong local-SEO signal

*(No `FAQPage` JSON-LD schema detected — NP leaves rich-result territory open; see 03-schema.md.)*

### 1.6 On-page copy — key phrases NP leans on
- `Повний цикл турботи про ваші онлайн-продажі` (hero USP)
- `зберігання, пакування та швидка доставка` (core triad)
- `Замовлення з фулфілменту, отримані до 14:00, доставимо вже сьогодні` → **SAME-DAY DELIVERY** (Київ, Львів, Одеса, Дніпро)
- `10 чи 1 000 замовлень на день` (scale bracket)
- `Віддаєте товар → ми зберігаємо → пакуємо → доставляємо` (3-step workflow)
- `CRM SalesDrive` / `Shopify через Shopillect` / `додаток Poshta` (3 named integrations)
- `Інтернет-магазинам / Малому та середньому бізнесу / Великим компаніям / Маркетплейсам` (4 segments)
- `20+ років досвіду / Власні ІТ-рішення / Склади по всій Україні / Додатково -5% на логістику`
- `Зростання конверсії +15-30%` (singular quantified stat)
- `WMS-система та штрих кодування`
- `+38 067 800 34 04` (direct sales phone — not 0-800 masked)

### 1.7 Internal outbound links from `/for-business/fulfillment/`
Fulfillment-adjacent destinations linked from the page:
- `/for-business/solutions/e-commerce` — sister solutions hub
- `/for-business/international-delivery/how-to-send` — cross-border intent bridge
- `/for-business/send/from-branch` — services (tariffs)
- `/for-business/financial-services/cash-delivery-agreement` — COD / накладений платіж
- `/for-business/cooperation/contract` — contract terms
- `/for-business/promotional-integrations` — branded packaging / ads
- `/for-business/business-school` — thought-leadership hub
- `/for-business/partnership` — reseller / partner
- `/for-business/fulfillment/#submit-request` (in-page lead form)
- `/shipping-cost` — delivery tariffs (main site)

**Observation:** NP does NOT link to `/for-business/additional-services/parcel-storage`, `/for-business/freight`, `/for-business/solutions/b2b-customers`, or any vertical-specific pages. This is IA under-investment — the fulfillment page is siloed from the rest of their B2B graph. A SEO opportunity gap.

---

## 2. What Queries Is NP Actually Optimizing For?

### 2.1 Head queries NP owns via brand + domain (not content depth)
| Query (uk) | Monthly vol (est) | NP asset | Why NP wins |
|---|---|---|---|
| `фулфілмент нова пошта` | 700-900 | title + H1 + URL slug | pure brand — no competition |
| `нова пошта фулфілмент ціна` | 200-300 | internal "Детальніше про тарифи" link | brand modifier |
| `склад нова пошта для бізнесу` | 300-400 | 9 warehouse addresses in FAQ | brand + NAP |
| `фулфілмент` (head) | 3000-4000 | — | **domain authority only; on-page thin** |
| `послуги фулфілменту` | 400-600 | title + copy | DA-driven |
| `що таке фулфілмент` | 1500-2500 | H2 "Простими словами про фулфілмент" | thin explainer; DA wins |

### 2.2 Informational queries NP targets on-page
- `що таке фулфілмент простими словами` (H2 match)
- `як працює фулфілмент` (3-step explainer)
- `фулфілмент чи свій склад що вигідніше` (H2 exact match — clever long-tail capture)
- `недоліки власного складу` (H2 — counter-framing)
- `переваги фулфілменту для інтернет-магазину`

### 2.3 Transactional / consideration queries
- `як стати клієнтом фулфілменту` (H2)
- `як відправити товар на фулфілмент` (FAQ)
- `документи для фулфілменту нова пошта` (FAQ)
- `фулфілмент SalesDrive інтеграція` (integration block)
- `фулфілмент Shopify Україна` (integration block)

### 2.4 Local queries (warehouse NAP surfacing)
NP's FAQ leaks 9 addresses:
- `фулфілмент Київ` — 4 warehouses (Святопетрівське, Проліски, Новопирогівська, Радісна)
- `фулфілмент Львів` — 1 warehouse (Муроване)
- `фулфілмент Одеса` — 1 warehouse (Базова)
- `фулфілмент Дніпро` — 1 warehouse (Повітряна)
- `фулфілмент Івано-Франківськ` — 1 warehouse (Максимовича)

**These are all queries NP WILL rank for automatically**, even though the addresses are buried in an accordion. Google extracts local NAP.

### 2.5 Queries NP implicitly targets via navigation (adjacent pages)
From business subfolder sitemap (47 fulfillment-adjacent URLs):
- `/for-business/solutions/e-commerce` → `e-commerce логістика`
- `/for-business/freight` → `вантажні перевезення`
- `/for-business/additional-services/parcel-storage` → `зберігання посилок`
- `/for-business/additional-services/return` → `повернення товарів інтернет-магазин`
- `/for-business/international-delivery/ioss` → `IOSS EU`
- `/for-business/international-delivery/export-of-jewellery` → `експорт ювелірних виробів`
- `/for-business/cooperation/for-suppliers` → `постачальник нова пошта`

---

## 3. Vertical / Intent Coverage on Fulfillment Page

| Vertical / Intent | NP coverage |
|---|---|
| **Same-day delivery** | YES — Київ/Львів/Одеса/Дніпро, 14:00 cutoff |
| **Marketplaces (Rozetka/Prom/Kasta)** | MENTIONED — "Інтеграція з маркетплейсами" bullet only; no named marketplaces on the fulfillment page |
| **CRM integrations** | YES — SalesDrive, Shopify (via Shopillect), Poshta app |
| **Warehouse tour / WMS** | WEAK — 1 mention of "WMS-система та штрих кодування"; no photos, no process diagram |
| **Pricing / calculator** | NO — links out to "Детальніше про тарифи"; zero pricing on page itself |
| **Returns handling** | WEAK — not mentioned on fulfillment page; dedicated `/additional-services/return` page exists but is not linked from fulfillment |
| **Cross-border / customs** | INDIRECT — links to international-delivery section; no customs info on fulfillment page |
| **Vertical specialization** (clothing, cosmetics, food, jewelry, electronics, supplements, furniture) | **NONE** — entire page is industry-agnostic |
| **B2B / wholesale** | MENTIONED — "Компаніям з великим обсягом замовлень" bullet; no depth |
| **COD / накладений платіж** | INDIRECT — links to `/financial-services/cash-delivery-agreement`; not on page |
| **Packaging services** | WEAK — bundled into "пакування" triad; no dedicated block |
| **Branded packaging / co-branding** | NOT on fulfillment page (separate `/promotional-integrations/packaging-co-branding`) |
| **Fraud prevention / chargeback** | NONE |
| **Peak season / Black Friday / seasonal surge** | WEAK — "пікові навантаження" bullet for marketplaces, no dedicated content |
| **Fiscal registers / ПРРО / tax compliance** | NONE |
| **Certification (УкрСЕПРО / customs clearance)** | NONE |
| **Case studies / social proof** | WEAK — 11 logos (А-ба-ба-га-ла-ма-га, JYSK, monobank, ПриватБанк, Forbes, Harmony, Readeat, My Water, OKVI, Velothebest, Budcamp, The Ukrainians Media); NO case study links, NO quantified results per client |
| **Blog / thought leadership** | VIA "Школа бізнесу" external link only |
| **AI-readiness (llms.txt, markdown mirror)** | NONE (see 04-ai-search.md) |

---

## 4. Gap Analysis — Queries NP Does NOT Target On-Page

These are **MTP Group opportunities** where NP's infrastructure-generalist positioning leaves white space:

### 4.1 Vertical specialization (huge gap — 0% coverage)
| Query | Why MTP can take it |
|---|---|
| `фулфілмент для інтернет-магазину одягу` | NP treats all verticals identically; MTP can build `/fulfillment-dlya-odyagu/` with clothing-specific WMS, hanging storage, size-labeling |
| `фулфілмент для косметики та парфумерії` | Cosmetics have temperature/expiry/tester requirements — NP ignores this |
| `фулфілмент БАД та харчові добавки` | Regulatory regime (ДСанПіН, permit tracking) — NP ignores |
| `фулфілмент для ювелірних виробів` | NP has `/export-of-jewellery` but no domestic fulfillment for jewelry |
| `фулфілмент для електроніки та гаджетів` | Serial-number tracking, anti-fraud — NP silent |
| `фулфілмент для дитячих товарів` | Certification-heavy vertical — gap |
| `фулфілмент для зоотоварів / корму для тварин` | Low-competition, high-intent B2B |
| `фулфілмент для меблів та габаритних товарів` | NP routes to `/freight` not fulfillment — content gap |

### 4.2 Price transparency & decision tools
| Query | Gap |
|---|---|
| `фулфілмент ціна за одиницю` | NP has ZERO numeric prices on-page; MTP can publish rate card |
| `калькулятор фулфілменту онлайн` | NP has no calculator tool; MTP `/calculator/` is a direct wedge |
| `порівняння цін фулфілмент Україна` | NP will never write "vs competitors"; MTP can |
| `фулфілмент з підключенням за 1 день` | NP's onboarding has 5 steps, implicitly slow |

### 4.3 Compliance / regulatory / certification
| Query | Gap |
|---|---|
| `УкрСЕПРО сертифікація для фулфілменту` | Zero coverage on NP |
| `фіскальний реєстратор ПРРО для інтернет-магазину` | NP doesn't touch — MTP has `/fiscal-register-requirements-ukraine/` blog post already |
| `митне оформлення для фулфілменту імпорт` | NP has `/customs-clearance` but not tied to fulfillment |
| `сертифікати відповідності для товарів у фулфілменті` | Niche B2B query |

### 4.4 AI search / agentic commerce
| Query | Gap |
|---|---|
| `fulfillment API Ukraine documentation` | NP has API but no public docs page |
| `AI-readable fulfillment pricing Ukraine` | MTP dual-md / llms.txt is unique — see 04-ai-search.md |
| `claude chatgpt fulfillment ukraine` | Zero presence from NP |

### 4.5 CIS / cross-border market entry (RU-language positioning)
| Query | Gap |
|---|---|
| `фулфілмент для експорту в ЄС з України` | Thin on NP; `/international-delivery` is courier, not fulfillment |
| `fulfillment for Ukraine based sellers Amazon` | NP doesn't address Amazon FBA prep |
| `prep center Amazon Ukraine` | Untouched — high-intent, low-competition EN query |
| `фулфілмент для продажу на Etsy з України` | Untouched |

### 4.6 Returns / reverse logistics depth
| Query | Gap |
|---|---|
| `повернення товарів інтернет-магазин фулфілмент` | NP has `/additional-services/return` but NOT linked from fulfillment page |
| `reverse logistics Ukraine ecommerce` | Thin |
| `зменшення відсотка повернень товарів` | MTP blog already covers — double down with service page |

### 4.7 Peak season / operational excellence
| Query | Gap |
|---|---|
| `фулфілмент для Чорної п'ятниці / Black Friday` | Untouched |
| `піковий сезон логістика помилки` | MTP already has blog post — convert into landing |
| `готовність складу до новорічного сезону` | Seasonal white space |

### 4.8 Long-tail informational / comparison
| Query | Gap |
|---|---|
| `фулфілмент vs 3PL відмінності` | NP doesn't distinguish |
| `коли переходити на фулфілмент` (threshold/decision) | Thin |
| `найкращий фулфілмент в Україні рейтинг 2026` | NP too big to write rankings; MTP already has "best fulfillment operators" post |
| `приклади успішного переходу на фулфілмент` (case studies) | NP has logos but no narrative case studies |

---

## 5. Domain-Authority Factor — Where NOT to Fight NP

NP has ~10+ years of brand equity, DR ~80+, millions of branded searches monthly. Some queries are unwinnable via content quality alone. **MTP should NOT invest in:**

### 5.1 Brand / navigational queries (unwinnable)
- `нова пошта фулфілмент` — user explicitly wants NP
- `нова пошта склад` — NAP query
- `нова пошта тарифи`
- `нова пошта доставка`
- Any query containing `нова пошта` or `novaposhta`

### 5.2 Generic head terms where NP wins on DA even with thin content
- `фулфілмент` (single-word head) — 3000-4000/mo in UA. NP + Rozetka + Prom-level brands will always rank top-3. **MTP fights from position 4-6 at best; volume is bait — transactional intent lives in long-tail.**
- `послуги фулфілменту` — same dynamic
- `склад для інтернет-магазину` — highly competitive; NP + Ukrposhta + commercial real-estate portals

### 5.3 Logistics-infrastructure queries
- `кур'єрська доставка Україна`
- `мережа відділень Україна`
- `міжнародна доставка з України`
- Any query where a courier network moat matters more than fulfillment expertise. **MTP is not a courier — don't pretend to be.**

### 5.4 "Same-day delivery" head term in big 4 cities
NP physically controls last-mile in Київ/Львів/Одеса/Дніпро. MTP can claim same-day but will never outrank NP on `доставка за 1 день Київ`. **Concede, position on B2B handoff instead.**

---

## 6. Priority Matrix for MTP Group

### 6.1 TIER 1 — Take now (high intent, NP zero coverage, MTP brief already exists or low effort)
1. **Vertical fulfillment landing pages** — `/fulfillment-dlya-odyagu/`, `/fulfillment-dlya-kosmetyky/`, `/fulfillment-dlya-bad/`, `/fulfillment-dlya-dytyachykh-tovariv/`, `/fulfillment-dlya-meblіv/` (5 pages × 3 langs = 15 assets)
2. **Price transparency / calculator** — `/tsiny/` with rate card + `/calculator/` tool
3. **Fulfillment vs own warehouse** comparison (MTP has blog → convert to service page; NP has H2 but thin)
4. **Returns / reverse logistics** service page — NP's huge gap, direct link from fulfillment landing
5. **Peak season / Black Friday** playbook landing — seasonal + evergreen

### 6.2 TIER 2 — Medium-term (informational authority plays)
6. `/shcho-take-fulfilment/` ultimate guide — 3000+ words, beats NP's thin "простими словами" H2
7. `/fulfillment-api-documentation/` — developer-ready docs (NP has API but no public docs)
8. `/fulfillment-marketplaces/` vertical (Rozetka + Prom + Kasta + Allo) with named integration guides
9. `/fulfillment-for-amazon-fba-prep/` — EN-only, targets Ukrainian sellers on Amazon
10. Case studies with quantified results (e.g., "JYSK equivalent — but with numbers")

### 6.3 TIER 3 — Do not fight
- Any `нова пошта` branded query
- `фулфілмент` single-word head (accept position 4-6)
- Same-day delivery head terms
- Courier network head terms

---

## 7. Summary for Cross-Report Synthesis

**NP's fulfillment keyword story in one sentence:**
> Brand-anchored generalist page that captures high-intent "нова пошта" branded traffic via title+H1, leaks local-SEO juice through 9 warehouse addresses in FAQ, owns "що таке фулфілмент" informational traffic via domain authority despite thin content, but has ZERO vertical specialization, ZERO price transparency, ZERO AI-readiness, and a siloed IA that under-links 40+ adjacent B2B pages.

**MTP's winning angle:**
> MTP cannot beat NP on brand or head terms. MTP can beat NP on **specificity** (vertical-specific landing pages), **transparency** (rate cards + calculator), **developer-friendliness** (API docs + llms.txt + dual-md), and **decision-support content** (comparison, case studies with numbers, threshold calculators).

---

## Appendix A — Raw H2/H3 dump

```
H1: Фулфілмент від Нової пошти

H2:
- Ще швидше, ніж ви звикли!
- Простими словами про фулфілмент
- Працюйте гнучко, масштабуйтеся швидко — з нами це просто:
- Переваги для вашого бізнесу
- Інтеграція з фулфілментом
- Як стати клієнтом?
- Для кого ця послуга
- Чому логістичні рішення саме від Нової пошти
- Готові спростити свій бізнес уже сьогодні?
- Як розпочати співпрацю
- Фулфілмент чи свій склад. Що вигідніше?
- Переваги послуги
- Недоліки власного складу
- Вибирайте фулфілмент від Нової пошти — розумне рішення для зростання вашого онлайн-бізнесу!
- Уже скористалися послугами фулфілменту
- Поширені запитання
- Документи для співпраці

H3:
- Бізнесу
- Повний цикл турботи про ваші онлайн-продажі

FAQ (only 2):
- Які документи потрібні для початку співпраці?
- Як відправити товари на склад фулфілменту Нової пошти?
```

## Appendix B — Related NP business URLs (47 total in sitemap)
See full list in data source — key fulfillment-adjacent: `/solutions/e-commerce`, `/solutions/b2b-customers`, `/freight`, `/additional-services/parcel-storage`, `/additional-services/return`, `/international-delivery/ioss`, `/international-delivery/export-of-jewellery`, `/cooperation/for-suppliers`, `/business-school`, `/partnership`.

**End of 06-keywords.md.**
