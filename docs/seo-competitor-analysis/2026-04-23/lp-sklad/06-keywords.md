# LP-Sklad Keyword Footprint Analysis

**Date**: 2026-04-23
**Target**: `lp-sklad.biz` (marketing domain; `lp-sklad.online` = SaaS login portal, excluded)
**Scope**: All sitemap-indexed URLs, with deep parse of 12 representative pages
**Source for our context**: `docs/seo-competitor-analysis/ai-search-audit` (LP-Sklad ranks MTP #9 in their listicle, drives AI citations)

---

## TL;DR — One-sentence strategy

LP-Sklad runs a **programmatic twin-page system**: each of 40 fulfillment verticals gets a `/fulfillment/uk/[slug]/` sales landing + a paired `/rating-fulfillment/uk/[top|rating|review]-[slug]/` "best operators" listicle — doubled across uk/ru/en/pl (164 + 164 URLs), then surrounded by a 1150+ post blog long-tail moat, giving them 1,486 total URLs vs MTP's ~110.

---

## 1. Sitemap Inventory

**robots.txt advertises 4 sitemaps**:
- `https://lp-sklad.biz/sitemap.xml` — only 3 URLs (home + ru/en homes), a decoy
- `https://lp-sklad.biz/fulfillment/sitemap-new.xml` — **164 URLs** (41 slugs × 4 langs: uk/ru/en/pl)
- `https://lp-sklad.biz/sitemap-top-sklad.xml` — **164 URLs** (41 slugs × 4 langs, the rating twins)
- `https://lp-sklad.biz/blog/sitemap_index.xml` → post-sitemap(2) + page-sitemap + category + tags — **~1,158 blog posts**

**Total unique URLs: 1,486** (confirms prior audit's ~1,485 estimate).

**Template counts, uk-only**:
| Template | UK URLs | Pattern | Word count |
|---|---|---|---|
| `/fulfillment/uk/[slug]/` | 41 | Sales landing, 11 H2 sections | ~480–495 words |
| `/rating-fulfillment/uk/[prefix]-[slug]/` | 41 | TOP/rating listicle | ~1,175–2,293 words |
| `/blog/[slug-ua-transliteration]/` | ~1,000+ | Long-form informational | ~635–700 words each |
| Homepage `/` (+ `/ru`, `/en`) | 1 | Navigation/portal | n/a |

**Language coverage**: uk, ru, en, pl (hreflang) — MTP only has uk/ru/en, so LP-Sklad already outflanks us on Polish market (relevant for Polish cross-border ecommerce querying Ukraine operators).

---

## 2. Programmatic Twin-Page System (the core weapon)

**The 40 keyword verticals** (1:1 pairing between `/fulfillment/uk/X/` seller page and `/rating-fulfillment/uk/Y-X/` listicle twin):

**Head-term / core**:
- `fulfilment` ↔ `rating-fulfilment`
- `fulfilment-servis` ↔ `top-fulfilment-servis`
- `fulfilment-operator` ↔ `top-fulfilment-operator`
- `fulfilment-posluhy` ↔ `top-fulfilment-posluhy`
- `fulfilment-tsentr` ↔ `rating-fulfilment-tsentr`
- `fulfilment-platforma` ↔ `rating-fulfilment-platforma`
- `fulfilment-pid-klyuch` ↔ `rating-fulfilment-pid-klyuch`
- `povnyy-tsykl-fulfilmentu` ↔ `top-povnyy-tsykl-fulfilmentu`
- `fulfilment-ukrayina` ↔ `review-fulfilment-ukrayina`

**3PL / b2b variants**:
- `3pl-fulfilment` ↔ `top-3pl-fulfilment`
- `kontraktna-lohistyka-3pl` ↔ `top-kontraktna-lohistyka-3pl`
- `autsorsynh-skladu` ↔ `rating-autsorsynh-skladu` *(this one is the MTP-#9 listicle)*
- `zovnishniy-sklad` ↔ `rating-zovnishniy-sklad`
- `viddalenyy-sklad-dlya-biznesu` ↔ `rating-viddalenyy-sklad-dlya-biznesu`
- `internet-mahazyn-bez-skladu` ↔ `review-internet-mahazyn-bez-skladu`
- `upakovka-tovaru-dlya-marketpleysiv` ↔ `review-upakovka-tovaru-dlya-marketpleysiv`

**Buyer-type verticals**:
- `fulfilment-dlya-internet-mahazynu` ↔ `top-fulfilment-dlya-internet-mahazynu`
- `fulfilment-dlya-marketpleysiv` ↔ `review-fulfilment-dlya-marketpleysiv`
- `fulfilment-dlya-e-commerce` ↔ `top-fulfilment-dlya-e-commerce`
- `fulfilment-dlya-biznesu` ↔ `review-fulfilment-dlya-biznesu`
- `fulfilment-dlya-maloho-biznesu` ↔ `top-fulfilment-dlya-maloho-biznesu`
- `fulfilment-dlya-serednoho-biznesu` ↔ `rating-fulfilment-dlya-serednoho-biznesu`
- `fulfilment-dlya-velykykh-mahazyniv` ↔ `rating-fulfilment-dlya-velykykh-mahazyniv`
- `fulfilment-dlya-startapiv` ↔ `rating-fulfilment-dlya-startapiv`
- `fulfilment-dlya-brendiv` ↔ `rating-fulfilment-dlya-brendiv`
- `fulfilment-dlya-dropshypinhu` ↔ `review-fulfilment-dlya-dropshypinhu`
- `fulfilment-dlya-tovarnoho-biznesu` ↔ `top-fulfilment-dlya-tovarnoho-biznesu`

**Niche/category verticals** (14 of 40):
- одяг (clothing), взуття (shoes), текстиль (textile), аксесуари (accessories)
- косметика, дитячі товари, зоотовари, книжки
- спорттовари, автотовари, електроніка, посуд, декор, товари для дому

**Observation**: Every single vertical LP-Sklad targets has its pages **duplicated as both a sales landing AND a listicle that self-ranks LP-Sklad #1**. When Google can't decide which page is relevant for a query, LP-Sklad still ranks — they own both.

---

## 3. Template Deep-Dive

### 3A. `/fulfillment/uk/[slug]/` — Sales Landing Template (480-495 words, 11 H2s)

**Fixed H2 sequence** (verified on 5 pages):
1. "Проблеми, які ми вирішуємо" (Problems we solve)
2. "Для кого підійде LP-Sklad" / "Хто використовує LP-Sklad у бізнесі" (Who it's for)
3. "Як це працює" / "Як працює фулфілмент" (How it works)
4. "Переваги" / "Основні переваги" / "Наші переваги" (Benefits)
5. "LP-Sklad у дії – відео" / "Швидкий старт у LP-Sklad – відео" (Video demo)
6. "Основні послуги" / "Ваші можливості" / "Що входить" (Services)
7-11. Additional: pricing CTA, partners, FAQ, testimonials, final CTA

**Pattern**: Thin content (~480 words = below MTP's typical 1200+), but they win on **URL inventory volume** not depth.

**Example titles**:
- `Фулфілмент в Україні: Швидка доставка товарів`
- `Фулфілмент для інтернет-магазину | Україна`
- `Фулфілмент для маркетплейсів в Україні`
- `3PL фулфілмент: Оптимізація для бізнесу`
- `Фулфілмент для одягу: швидка доставка по Україні`

**Meta descriptions**: All follow formula `[Service] для [audience]: зберігання, пакування, доставка замовлень. Оптимізуйте [logistics/business] з нами! Швидко, надійно, [benefit].` — templated to ~155 chars.

### 3B. `/rating-fulfillment/uk/[slug]/` — Listicle Template (1,175-2,293 words, 4 H2s + 11-18 H3s)

**Fixed H2 sequence**:
1. "Почніть співпрацю зі складом" / "Оберіть фулфілмент для свого бізнесу" (lead-in)
2. "Таблиця порівняння" (comparison table)
3. "FAQ"
4. "[CTA-closer]" e.g. "Автоматизуйте зберігання та відправку"

**H3s = ranked competitor list** (verified on `rating-autsorsynh-skladu/`, 18 competitors):
1. **Lp-Sklad** (self, always #1)
2. KolesoLogistics
3. TVL
4. Nova Poshta Fulfillment
5. Sender Ukraine
6. UB1
7. Upost
8. Diad Logistic
9. **MTP Group** ← we are ranked #9
10. Sea Way
11. Talman Logistics
12. GTAL Logistics
13. UniPost
14. Parkline Group
15. Global Unity Logistics
16. Cloud Commerce
17. Fast Lane Group
18. Zammler Fulfillment

**Variable competitor counts per listicle**: 11 operators (top-fulfilment-operator), 12 (rating-fulfilment), 15 (fulfilment-tsentr), 18 (rating-autsorsynh-skladu). Pattern: round number in title ("ТОП 11", "ТОП 15", "ТОП 18", "Найкращі 12").

**Example titles**:
- `ТОП 18 аутсорсинг складів. Огляд та рейтинг` (MTP appears here)
- `ТОП 15 фулфілмент центрів України: Рейтинг 2024`
- `ТОП 11 Фулфілмент Операторів в Україні`
- `Найкращі 12 фулфілмент: Порівняння та Вибір`

**This is the template MTP must clone.** Exact URL to reverse-engineer: `https://lp-sklad.biz/rating-fulfillment/uk/rating-autsorsynh-skladu/`

### 3C. Blog Long-Tail Moat (~1,158 posts)

**Topics observed**:
- Що таке фулфілмент / shcho-take-fulfilment — informational head-term
- Як замовити фулфілмент — transactional how-to
- Фулфілмент в Києві / в Україні — geo-modified
- Аутсорсинг персоналу складу — operational B2B
- Nova Poshta integration how-tos
- Instagram / Prom / Rozetka integration guides
- Ecommerce growth / arbitrage (off-topic but targets cheap long-tail)

**Quality**: 635-700 words per post. Titles transliterated UA (`shho-take-fulfilment-skladu-povnyj-oglyad`). **This is their long-tail search volume reservoir** — they don't need to rank #1, they just need to exist on every possible informational query.

---

## 4. Query Clusters Targeted

| Cluster | URL type | Examples | MTP coverage |
|---|---|---|---|
| (a) Informational head | `/blog/shho-take-fulfilment-*` | "що таке фулфілмент", "як замовити фулфілмент" | Partial |
| (b) Vertical-niche | `/fulfillment/uk/fulfilment-dlya-[niche]/` | "фулфілмент для одягу/косметики/взуття" | Partial (some verticals) |
| (c) Programmatic rating | `/rating-fulfillment/uk/top-*`, `/rating-*`, `/review-*` | "топ фулфілмент", "рейтинг фулфілмент Україна", "кращий аутсорсинг складу" | **Zero** — we have no listicle |
| (d) Buyer-type | `/fulfillment/uk/fulfilment-dlya-[audience]/` | "фулфілмент для інтернет-магазину", "...для дропшипінгу", "...для стартапу" | Partial |
| (e) Long-tail blog | `/blog/*` (1,158 URLs) | Every possible adjacent query | Partial (~40 posts) |
| (f) Geo | `/blog/fulfilment-v-kyyevi-*` | "фулфілмент Київ" | Zero |
| (g) Marketplace-specific | `/blog/*-rozetka`, `*-prom` | "фулфілмент для Розетки" | Zero |

---

## 5. Query-by-Query Reasoning: Which LP-Sklad page wins each test query?

| # | Query (UA) | Winning LP page | Why |
|---|---|---|---|
| 1 | "що таке фулфілмент" | `/blog/shho-take-fulfilment-skladu-povnyj-oglyad/` | H1 = exact match; 635 words; blog post format Google prefers for informational intent |
| 2 | "фулфілмент для інтернет-магазину" | `/fulfillment/uk/fulfilment-dlya-internet-mahazynu/` | Title+H1 exact match; paired listicle `/rating-fulfillment/uk/top-fulfilment-dlya-internet-mahazynu/` catches comparison intent |
| 3 | "3pl послуги Україна" | `/fulfillment/uk/3pl-fulfilment/` + `/fulfillment/uk/kontraktna-lohistyka-3pl/` | Two pages on the exact term; listicle `/top-3pl-fulfilment/` for "best 3PL" variant |
| 4 | "кращий фулфілмент Україна" | `/rating-fulfillment/uk/rating-fulfilment/` (title: "Найкращі 12 фулфілмент") | Superlative query → listicle page ranks; 1,263 words; comparison table |
| 5 | "рейтинг фулфілмент операторів" | `/rating-fulfillment/uk/top-fulfilment-operator/` (title: "ТОП 11 фулфілмент операторів") | Exact keyword match in URL + title; and secondary `/rating-autsorsynh-skladu/` |

**Pattern**: LP-Sklad wins **every commercial-investigation query in Ukrainian fulfillment** because they've built a URL for literally every phrasing. MTP currently relies on 1-2 pages to cover dozens of query phrasings.

---

## 6. LP-Sklad's Top 10 Ranking Query Targets (inferred from URL inventory + on-page priority signals)

Ranked by a composite of: sitemap priority, template depth, internal-link prominence, and number of twin pages serving the term.

1. **"фулфілмент"** / "fulfilment" — 2 pages: `/fulfillment/uk/fulfilment/` + `/rating-fulfillment/uk/rating-fulfilment/`
2. **"фулфілмент Україна"** — 2 pages: `/fulfilment-ukrayina/` + `/review-fulfilment-ukrayina/`
3. **"фулфілмент для інтернет-магазину"** — 2 pages + high-intent
4. **"фулфілмент для маркетплейсів"** — 2 pages, marketplace verticalization
5. **"3PL фулфілмент / контрактна логістика 3PL"** — 3 pages (both templates + variant)
6. **"аутсорсинг складу"** — 2 pages; `rating-autsorsynh-skladu/` is their #1 AI-citation driver
7. **"фулфілмент послуги"** / "послуги фулфілменту" — 2 pages
8. **"фулфілмент центр"** — 2 pages; listicle ranks ~1,625 words
9. **"фулфілмент оператор"** — 2 pages
10. **"фулфілмент під ключ / повний цикл"** — 4 pages: `/fulfilment-pid-klyuch/` + `/rating-fulfilment-pid-klyuch/` + `/povnyy-tsykl-fulfilmentu/` + `/top-povnyy-tsykl-fulfilmentu/`

---

## 7. MTP Counter-Attack: 10 Queries We Can Compete or Outrank On

**Selection criteria**: queries where (a) LP-Sklad's page is thin (<500 words), (b) we have a real operational advantage, or (c) query has commercial intent and the listicle format is cloneable.

| # | Target query | MTP action | Why winnable |
|---|---|---|---|
| 1 | **"рейтинг фулфілмент операторів Україна"** / "топ фулфілмент Україна 2026" | **Clone the listicle template**: `/reityng-fulfilment-ukraina/` (UA) + `/ru/` + `/en/` — rank ourselves #1, include honest competitor list | LP-Sklad's template is ~1,200 words, we can do 2,500+, fresher dated, include real data on competitors they skip (e.g. Hubber, iDeal Logistics). This is the single highest-leverage move. |
| 2 | **"фулфілмент для одягу"** | Expand existing page to 1,500 words with size-chart mgmt, return-rate handling, seasonal scaling | LP's page is 481 words — beat on depth |
| 3 | **"фулфілмент для косметики"** | Build dedicated UA page w/ SDS/shelf-life handling, tax docs for cosmetics imports | LP has 1 sales page; we have compliance angle they don't cover |
| 4 | **"фулфілмент для Розетки / Prom / Kasta"** | 3 dedicated marketplace-specific pages per language | LP has blog posts only, no dedicated LPs — easy win with proper LPs |
| 5 | **"фулфілмент ціни / тарифи / вартість"** | Publish real price calculator (we have `/calculator/`), add `/tsiny/` rich page with 10+ scenarios | LP hides pricing; transparent pricing = trust + featured snippets |
| 6 | **"3PL послуги для великого бізнесу"** / "контрактна логістика Україна" | Enterprise-tier page with SLA, 24/7, dedicated account mgmt, customs | LP's `/kontraktna-lohistyka-3pl/` is thin sales page; enterprise buyers want depth |
| 7 | **"фулфілмент Київ / Львів / Одеса"** (geo) | Create geo-LPs per city showing warehouse coverage | LP has only blog posts on "фулфілмент у Києві"; proper geo-LPs will outrank |
| 8 | **"що таке фулфілмент повний гайд 2026"** | Long-form 3,000-word guide w/ diagrams, video, schema HowTo | LP's blog post is 635 words; easy to beat with depth + freshness |
| 9 | **"фулфілмент для дропшипінгу"** | Dedicated UA/RU/EN page covering supplier integrations, dropship margins, no-stock model | LP has a single sales page; we can add real case studies |
| 10 | **"порівняння фулфілмент операторів Україна"** / "LP-Sklad vs MTP vs Nova Poshta" | Comparison page (our version of the listicle) — honest, data-driven, includes ourselves + 5-10 rivals with pros/cons | Cures the AI-citation gap. Clone + honest = AI engines prefer it. |

---

## 8. Template to Clone (exact URL)

**Primary target**: `https://lp-sklad.biz/rating-fulfillment/uk/rating-autsorsynh-skladu/`

**What to replicate**:
- URL structure: `/[top|rating|reityng]-[term]/` (UA root per our new URL policy → `/reityng-fulfilment-operatoriv/`)
- Word count: 2,000-2,500 (beat their 2,293)
- 4 H2 skeleton: Intro CTA → Comparison Table → FAQ → Closing CTA
- 12-18 H3 blocks, each = one competitor with: logo/name, 2-3 bullet strengths, 1-2 weaknesses, price band, specialization tag
- **We rank ourselves #1 honestly** (just like LP does) but with real differentiators; include LP-Sklad in the list as an honest #4-6 entry
- Comparison table with ~8 columns (price/min order/niches/integrations/SLA/locations/reviews/score)
- FAQ schema markup — 8-12 questions

**Secondary targets to clone (lower effort, still high-leverage)**:
- `/rating-fulfillment/uk/top-fulfilment-operator/` → our `/top-fulfilment-operatoriv-ukraina/`
- `/rating-fulfillment/uk/rating-fulfilment-tsentr/` → our `/top-fulfilment-tsentriv/`
- `/rating-fulfillment/uk/top-fulfilment-dlya-internet-mahazynu/` → our `/kraschi-fulfilment-dlya-internet-mahazynu/`

**Deploy priority**: Listicle first (cures the AI-citation crisis), then vertical expansion (fills cluster gaps).

---

## 9. Key Asymmetries to Exploit

| Dimension | LP-Sklad | MTP advantage |
|---|---|---|
| URL count | 1,486 | ~110 — **we need programmatic scale** |
| Avg words per sales LP | ~485 | We already ship 1,200+ — depth wins on head terms |
| Languages | uk/ru/en/pl | We lack PL — 4th language could be cheap win for cross-border |
| Homepage H1 | Missing (!) | Basic SEO hygiene advantage |
| Pricing transparency | Hidden | Our `/calculator/` already built |
| Listicle / comparison | 40 pages, self-ranked #1 | **Zero** — blocker on AI citations |
| Geo-LPs | Blog posts only | Opportunity for proper city LPs |
| Schema | Thin | Our Base.astro already has FAQPage/Article/Service — we serialize better |
| Marketplace-specific LPs | Blog only | Opportunity: proper Rozetka/Prom/Kasta LPs |

---

## 10. Raw Data Files

- `/tmp/lpsklad-ff-urls.txt` — 164 fulfillment sales URLs
- `/tmp/lpsklad-top-urls.txt` — 164 rating listicle URLs
- `/tmp/lpsklad-blog-urls.txt` — 1,159 blog URLs
- `/tmp/lpsklad-rating.html` — parsed source of `rating-autsorsynh-skladu` (MTP #9 listicle)
- `/tmp/lps-*.html` — 10 sampled page HTMLs

---

*Prepared for MTP SEO counter-strategy — analyst: Claude (task #77). Next step (task #78): synthesize with the other 3 competitor reports into `SYNTHESIS.md`.*
