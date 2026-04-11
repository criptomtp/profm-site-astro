# MTP Group -- Design, Usability & Content Uniqueness Audit

**Date:** 2026-04-09
**Scope:** 13 UA service/landing pages
**Auditor:** Claude (automated deep analysis)

---

## PART 1: CONTENT SIMILARITY ANALYSIS

### 1.1 Duplicate Text Blocks -- Repeated Stats & Claims

The following stats/claims appear on **6+ pages** (near-identical wording):

| Repeated Stat / Claim | Pages Where It Appears |
|---|---|
| "від 18 грн за відправлення" | ALL 13 pages |
| "3 генератори, 2 оптоволоконних провайдери, Starlink" | services, internet-magazynu, marketpleysiv, vazhkykh, kyiv, ukraina, maloho-biznesu, skladski-poslugy |
| "Жодного дня простою з 2022 року" | services, internet-magazynu, marketpleysiv, vazhkykh, kyiv, ukraina, maloho-biznesu |
| "150+ клієнтів" | internet-magazynu, kyiv, ukraina, maloho-biznesu, about |
| "6 000 відправлень на день" | internet-magazynu, marketpleysiv, kyiv, ukraina, maloho-biznesu, about, guide |
| "30 секунд збір замовлення" | services, internet-magazynu, marketpleysiv, kyiv, maloho-biznesu, skladski-poslugy |
| "Зберігання від 650 грн/м3/міс" | ALL service pages |
| "Мінімальний платіж 5 000 грн/міс" | internet-magazynu, marketpleysiv, kyiv, ukraina, maloho-biznesu, tsiny, calculator |
| "Підключення 1-3 дні" | internet-magazynu, marketpleysiv, vazhkykh, kyiv, ukraina, maloho-biznesu |
| "4 рази на день забори НП" | services, internet-magazynu, kyiv, ukraina, maloho-biznesu |
| "KeyCRM, SalesDrive, Horoshop, WooCommerce, OpenCart, Shopify, Prom.ua, Rozetka" | internet-magazynu, marketpleysiv, maloho-biznesu, guide |
| "99.5% точність замовлень" | internet-magazynu, maloho-biznesu |

**Verdict:** Every service page repeats the same 8-10 core stats. Google may see this as thin/duplicate content.

### 1.2 Duplicate Case Studies & Testimonials

| Case Study | Pages Where It Appears |
|---|---|
| **Carter's: 12 -> 72 замовлень/день** | internet-magazynu (as "80 -> 400 cosmetics case"), ukraina, recalls |
| **ORNER: 50 -> 500+ замовлень/день** | marketpleysiv (mentioned), kyiv (full case), ukraina (mentioned) |
| **EcoDrive: 50 важких відправлень/день** | vazhkykh-tovariv (full case + SEO article re-tells it) |
| **Cosmetics store: 80 -> 400** | internet-magazynu (full case study) |
| **Accessories store: 3200 SKU** | skladski-poslugy (full case study) |

The Carter's case appears on 3 pages with slightly different numbers (10->72, 12->72, 80->400 "cosmetics"). ORNER is mentioned on 3 pages.

### 1.3 Duplicate FAQ Questions

| FAQ Question (paraphrased) | Pages |
|---|---|
| "Скільки коштує фулфілмент?" | services, internet-magazynu, marketpleysiv, kyiv, maloho-biznesu, tsiny |
| "Як швидко можна почати/підключитися?" | services, internet-magazynu, marketpleysiv, kyiv, ukraina, maloho-biznesu |
| "Що під час блекауту/відключень?" | services, internet-magazynu, marketpleysiv, vazhkykh, kyiv, ukraina, maloho-biznesu |
| "Як відстежувати замовлення/залишки?" | services, internet-magazynu, maloho-biznesu |
| "Чи є офіційний договір?" | services |
| "Які служби доставки?" | services |

**6 out of 8 FAQ sections share 3+ identical questions** with only slightly different wording of the answers.

### 1.4 Duplicate CTA Text

| CTA Button Text | Pages |
|---|---|
| "Отримати розрахунок" | services, internet-magazynu, vazhkykh, kyiv, calculator, about, recalls |
| "Розрахувати вартість" | marketpleysiv, maloho-biznesu, tsiny |
| "Безкоштовна консультація / Передзвонимо за 15 хвилин" | ALL pages |

### 1.5 Duplicate Pricing Tables

The same pricing table (18/20/22/23/25/26 grn dynamic scale) appears **identically** on:
- services (condensed)
- internet-magazynu (3-column table)
- marketpleysiv (3-column table -- nearly pixel-perfect duplicate)
- maloho-biznesu (card-based)
- kyiv (card-based)
- ukraina (card-based with scale)
- tsiny (full table -- this is the canonical source)

### 1.6 Duplicate Comparison Tables ("MTP vs Власний склад")

| Page | Comparison Details |
|---|---|
| services | 50 orders/day, total 55k vs 28k |
| marketpleysiv | 100 orders/day, total 55k+ vs 50.5k |
| ukraina | 50 orders/day, total 55k vs ~28k |
| tsiny | 50 orders/day, total 55k vs ~28k |
| maloho-biznesu | 10/50/100/200 orders (4 scenarios!) |

**services** and **tsiny** have virtually identical tables. **ukraina** has the same data.

### 1.7 Similarity Matrix (High/Medium/Low overlap)

Scale: HIGH = 70%+ shared content structure, MED = 40-70%, LOW = <40%

|  | services | internet-mag | marketpl | vazhkykh | kyiv | ukraina | maloho | skladski | about | guide | recalls | calc | tsiny |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **services** | -- | HIGH | MED | MED | MED | HIGH | MED | MED | LOW | LOW | LOW | MED | HIGH |
| **internet-mag** | HIGH | -- | HIGH | MED | MED | HIGH | MED | MED | LOW | LOW | LOW | LOW | HIGH |
| **marketpl** | MED | HIGH | -- | LOW | MED | HIGH | MED | LOW | LOW | LOW | LOW | LOW | HIGH |
| **vazhkykh** | MED | MED | LOW | -- | MED | MED | LOW | MED | LOW | LOW | LOW | LOW | MED |
| **kyiv** | MED | MED | MED | MED | -- | HIGH | MED | MED | LOW | LOW | LOW | LOW | HIGH |
| **ukraina** | HIGH | HIGH | HIGH | MED | HIGH | -- | HIGH | MED | LOW | LOW | LOW | LOW | HIGH |
| **maloho** | MED | MED | MED | LOW | MED | HIGH | -- | LOW | LOW | LOW | LOW | LOW | HIGH |
| **skladski** | MED | MED | LOW | MED | MED | MED | LOW | -- | LOW | LOW | LOW | LOW | MED |
| **about** | LOW | LOW | LOW | LOW | LOW | LOW | LOW | LOW | -- | LOW | LOW | LOW | LOW |
| **guide** | LOW | LOW | LOW | LOW | LOW | LOW | LOW | LOW | LOW | -- | LOW | LOW | LOW |
| **recalls** | LOW | LOW | LOW | LOW | LOW | LOW | LOW | LOW | LOW | LOW | -- | LOW | LOW |
| **calc** | MED | LOW | LOW | LOW | LOW | LOW | LOW | LOW | LOW | LOW | LOW | -- | HIGH |
| **tsiny** | HIGH | HIGH | HIGH | MED | HIGH | HIGH | HIGH | MED | LOW | LOW | LOW | HIGH | -- |

**Worst offenders (highest overlap):**
1. **services <-> tsiny** -- pricing and comparison tables nearly identical
2. **services <-> ukraina** -- same comparison table, same FAQ, same stats
3. **internet-magazynu <-> marketpleysiv** -- same hero structure, same pricing table, same FAQ pattern
4. **ukraina <-> kyiv** -- same stats, same case studies (ORNER, Carter's), same pricing
5. **maloho-biznesu <-> internet-magazynu** -- same value proposition, same FAQ topics

---

## PART 2: HERO SECTION ANALYSIS

| Page | Hero Style | H1 | Subtitle | Form? | Stats? | Background |
|---|---|---|---|---|---|---|
| services | Dark BG, centered, red underline | "Фулфілмент послуги для інтернет-магазинів" | "...допоможуть вам заробляти більше" | YES (phone) | NO | Solid #111 |
| internet-mag | Dark BG with YouTube thumbnail overlay, left-aligned | "Фулфілмент для інтернет-магазину" | "Ти продаєш -- ми відправляємо..." | YES (phone) | YES (6000, 150+, 30 sec) | YouTube video thumbnail gradient |
| marketpl | Dark BG with warehouse hero image overlay, left-aligned | "Фулфілмент для маркетплейсів. Rozetka, Prom, Kasta..." | "Ти завантажуєш товар..." | YES (phone) | YES (60000+, 30 sec, 10+ years) | /images/mtp-fulfillment-warehouse-hero.webp |
| vazhkykh | Dark BG with YouTube thumbnail overlay, left-aligned | "Фулфілмент важких товарів. Великий габарит." | "Сонячні панелі, будматеріали..." | YES (phone) | YES (50+ kg, До 1 т, 2 складі) | YouTube video thumbnail gradient |
| kyiv | Dark centered, radial gradient dots | "Фулфілмент у Києві. Склад під ключ від 18 грн." | "Два склади в 20 хв від Києва..." | YES (phone) | NO (pins instead) | Black with radial gradients |
| ukraina | Dark with actual image overlay | "Фулфілмент в Україні--працюємо навіть під час блекаутів" | "Два склади в Київській області..." | YES (phone) | YES (150, 60000, 10) | /images/fulfilment-ukraina-hero-ua.webp |
| maloho | Split-screen pain/solution | "Фулфілмент для малого бізнесу" | (no subtitle -- pain lines instead) | YES (phone) | NO (price badge instead) | Split black/dark |
| skladski | Dark with warehouse image overlay | "Складські послуги для інтернет-магазинів у Києві" | "Зберігання, комплектація та відправка..." | YES (phone) | YES (3900m2, 2, 60000+) | /images/mtp-fulfillment-warehouse-hero.webp |
| about | Dark with gradient overlay | "Як працює фулфілмент склад MTP Group" | "Від маленького складу у 2015..." | YES (phone) | NO | Gradient overlay |
| guide | Light minimal, no BG image | "Повний гайд по фулфілменту для інтернет-магазинів" | "Все що потрібно знати..." | NO | NO | None (editorial style) |
| recalls | Dark with gradient overlay | "Відгуки задоволених клієнтів MTP Group" | "Реальні історії від 150+..." | YES (phone) | NO | Gradient overlay |
| calculator | Dark with gradient overlay | "Калькулятор вартості фулфілменту" | "Розрахуйте вартість за 30 секунд..." | YES (phone) | YES (18 grn, 650 grn, 5000 grn) | Gradient overlay |
| tsiny | Dark minimal | "Ціни на фулфілмент для інтернет-магазинів" | "Прозоре ціноутворення..." | YES (phone) | YES (18, 650, 5000) | None |

### HERO DUPLICATES FLAGGED:

1. **internet-magazynu, vazhkykh-tovariv** -- SAME background image (YouTube thumbnail of bHY3cFF9SlI), same layout (left-aligned, red vertical line, badge + h1 + sub + form + stats)
2. **marketpleysiv** -- Same layout pattern as above but uses warehouse .webp instead
3. **skladski-poslugy** -- SAME background image as marketpleysiv (/images/mtp-fulfillment-warehouse-hero.webp)
4. **calculator, tsiny** -- Same hero stats (18 grn, 650, 5000) -- nearly identical hero
5. **about, recalls, calculator** -- All use same gradient-overlay dark hero with badge + h1 + sub + form pattern

**Only truly unique heroes:** guide (editorial), maloho-biznesu (split-screen), kyiv (map-style pins)

---

## PART 3: SECTION STRUCTURE COMPARISON

| Page | Section Order |
|---|---|
| **services** | Hero -> Services Grid -> Video Tour -> Pricing Table -> Integrations -> Comparison Table -> FAQ |
| **internet-mag** | Hero -> Benefits Grid -> Video Tour -> Case Study -> Pricing Table -> FAQ -> SEO Article |
| **marketpl** | Hero -> Pain Points -> Case Study -> Marketplaces Grid -> Comparison Table -> Timeline -> Pricing Table -> FAQ -> SEO Article |
| **vazhkykh** | Hero -> Categories Grid -> Case Study -> Advantages Grid -> Pricing Table -> FAQ -> SEO Article |
| **kyiv** | Hero -> Delivery Map -> Warehouse Gallery -> Video Tour -> Seasonality -> Pricing Cards -> FAQ -> SEO Article |
| **ukraina** | Hero -> Proof Grid (3 cards) -> Pricing Cards -> Case Study -> Comparison Table -> FAQ -> SEO Text |
| **maloho** | Hero -> Threshold Scale -> Economics Table -> Pain/Solution Cards -> Video Tour -> Timeline -> Pricing Cards -> FAQ -> SEO Article |
| **skladski** | Hero -> Benefits Grid -> Warehouses Grid -> Pricing Table -> Case Study -> ... |
| **about** | Hero -> Story (photo + text) -> Video Tour -> Warehouses Grid -> Technology Grid -> ... |
| **guide** | Hero -> Table of Contents -> Long-form Article (6 chapters) |
| **recalls** | Hero -> Video Grid -> Case Studies Grid -> ... |
| **calculator** | Hero -> Calculator Widget -> Pricing Table -> FAQ |
| **tsiny** | Hero -> Dynamic Scale Table -> Storage Table -> Extras Grid -> Comparison Table -> FAQ |

### IDENTICAL SECTION ORDER FLAGS:

- **internet-mag and vazhkykh** share: Hero -> Grid -> Case Study -> Pricing -> FAQ -> SEO Article
- **services, tsiny, ukraina** all have: Pricing Table + Comparison Table + FAQ as final sections
- **Video Tour section (same YouTube ID bHY3cFF9SlI)** appears on 8 pages with near-identical markup

### UNIQUE SECTIONS (good differentiation):

- marketpleysiv: Marketplace cards with external links
- maloho-biznesu: Split-screen hero, threshold scale, 4-tier economics table
- kyiv: Delivery speed map, warehouse gallery with icons
- guide: Long-form editorial content with TOC
- recalls: Video grid with multiple YouTube videos
- calculator: Interactive calculator widget

---

## PART 4: DESIGN ISSUES

### 4.1 Color Violations

**CRITICAL: Green color (#22c55e) used on 9 pages**

Files: services, internet-magazynu, marketpleysiv, vazhkykh, skladski, tsiny, calculator, about, recalls

Usage: Form success message `color:#22c55e` and comparison table `.comp-yes{color:#22c55e}` in marketpleysiv.

This directly violates the rule: "Колір: ТІЛЬКИ #e63329 + #000 + #fff -- ніякого зеленого"

**MEDIUM: #ed2121 used instead of #e63329**

Files: services.astro, blog/index.astro

The services page uses `#ed2121` throughout its styles while other pages use `var(--red)` which resolves to `#e63329`. This creates inconsistency.

### 4.2 CSS Duplication and Inconsistency

**CRITICAL: fulfilment-ukraina.astro is a STANDALONE page**

This page does NOT use `Base.astro` layout. It has its own header, footer, fonts, styles, and Google Analytics implementation. This means:
- Different font loading strategy (Google Fonts CDN instead of local fonts)
- Different header markup and behavior
- No shared CSS variables
- Potential SEO issues (different structured data format)

**HIGH: Hero CSS duplicated across files**

The following CSS block is copy-pasted (with minor tweaks) across internet-magazynu, vazhkykh, marketpleysiv:

```css
.hero{position:relative;min-height:90vh;background:var(--black);...}
.hero-bg{position:absolute;inset:0;background:linear-gradient(105deg,...}
.hero-content{position:relative;z-index:2;padding:0 8vw;width:100%}
.hero-content::before{content:'';position:absolute;left:calc(8vw - 40px)...}
```

Same CSS repeated ~3-4 times across files instead of being in a shared stylesheet.

**HIGH: FAQ CSS duplicated with different class names**

- services.astro: `.faq-question`, `.faq-answer`
- internet-magazynu.astro: `.faq-q`, `.faq-a`
- kyiv.astro: `.ky-faq-q`, `.ky-faq-a`
- maloho-biznesu.astro: `.sb-faq-q`, `.sb-faq-a`

All functionally identical but with 4 different class naming schemes.

### 4.3 Badge Style Inconsistency

- services.astro: No `.badge` class used (section headings only)
- internet-magazynu: `.badge` with `border:1px solid var(--red)` + `border-radius:2px`
- ukraina: `.badge` with `border:1.5px solid #e63329` + `border-radius:100px` (pill shape!)
- Other pages: `.badge` with `border-radius:2px` (rectangle)

**ukraina page uses completely different badge styling (pill vs rectangle)**

### 4.4 Mobile Layout Issues

- **marketpleysiv mp-grid**: `grid-template-columns:repeat(2,1fr)` has no mobile breakpoint in the visible CSS -- 2-column grid persists on mobile
- **vazhkykh adv-grid**: `grid-template-columns:repeat(4,1fr)` collapses to 1fr on mobile (good)
- **services integrations-row**: `flex-wrap:wrap` works but logos are 140px fixed width -- may overflow on very small screens
- **ukraina**: Has its own responsive breakpoints that differ from Base.astro pages

### 4.5 Video Section Consistency

The warehouse tour (YouTube ID: bHY3cFF9SlI) appears on 8 pages. The section markup is consistent across pages using Base.astro, but:
- Different H2 titles ("Наш склад -- ваша логістика", "Ваші замовлення -- наша справа", "Склад у Києві -- відправка за годину", etc.)
- Different button text ("Подивитись відео", "Побачити процес", "Переглянути відео", "Дивитись екскурсію", "Оглянути склад")
- This is actually OK for SEO variety, but the SAME VIDEO on 8+ pages is excessive

---

## PART 5: CONCRETE RECOMMENDATIONS -- TOP 15

### 1. [CRITICAL] Remove green color (#22c55e) from all pages

**Severity:** Critical
**Files:** 9 files (see list in 4.1)
**What:** Replace `color:#22c55e` with `color:#e63329` or `color:var(--red)` in form success messages and comparison table highlights
**Example:**
```css
/* BEFORE */ .comp-yes{color:#22c55e}
/* AFTER  */ .comp-yes{color:#e63329;font-weight:600}
```

### 2. [CRITICAL] Migrate fulfilment-ukraina.astro to Base.astro layout

**Severity:** Critical
**File:** `src/pages/ua/fulfilment-ukraina.astro`
**What:** This standalone page has its own header, footer, font loading, analytics. Convert to use `import Base from '../../layouts/Base.astro'` like all other pages. This eliminates ~160 lines of duplicated infrastructure code and ensures consistent header/footer/font behavior.

### 3. [HIGH] Deduplicate pricing tables -- use a shared component

**Severity:** High
**Files:** services, internet-magazynu, marketpleysiv, kyiv, ukraina, maloho-biznesu, skladski-poslugy
**What:** Create `src/components/PricingTable.astro` that accepts props (variant: 'full' | 'compact' | 'cards'). Replace 7 copy-pasted pricing sections with component references. The canonical pricing data lives in tsiny.astro; other pages should link to it instead of duplicating.

### 4. [HIGH] Deduplicate comparison tables -- use a shared component

**Severity:** High
**Files:** services, marketpleysiv, ukraina, tsiny
**What:** Create `src/components/ComparisonTable.astro`. The "Свій склад vs MTP" table appears 4+ times with nearly identical data. Each page should either (a) use the component, or (b) link to `/ua/tsiny/` with an anchor instead.

### 5. [HIGH] Make FAQ questions unique per page

**Severity:** High
**What:** Currently 6 pages share 3+ identical FAQ questions. Each page should have FAQs specific to its topic:
- **internet-magazynu**: Focus on e-commerce specific questions (returns, SKU limits, seasonal scaling)
- **marketpleysiv**: Focus on multi-marketplace questions (FBO vs 3PL, API specifics per platform, rating protection)
- **kyiv**: Focus on geography (delivery speed by district, how close to NP hub, warehouse visit scheduling)
- **maloho-biznesu**: Focus on small business concerns (contract flexibility, branding options, Instagram/Telegram integration)
- Remove generic "how much does it cost" and "what about blackouts" from pages where tsiny/calculator already answer these

### 6. [HIGH] Reduce video tour repetition -- use it on max 3 pages

**Severity:** High
**Files:** 8+ files embed YouTube ID bHY3cFF9SlI
**What:** Keep the warehouse tour video on: about, services, and recalls. Remove from other landing pages and replace with page-specific visual content (e.g., photo carousel for skladski, process diagram for internet-magazynu, marketplace logos grid for marketpleysiv).

### 7. [HIGH] Standardize hero background images

**Severity:** High
**What:** Currently 3 pages use the SAME YouTube thumbnail, 2 use the same warehouse .webp. Each landing page should have a unique hero visual:
- **internet-magazynu**: Packing station close-up or Shopify dashboard screenshot
- **marketpleysiv**: Rozetka/Prom logos collage or marketplace seller dashboard
- **vazhkykh**: Forklift/pallet operation photo
- **skladski-poslugy**: Warehouse aisle/shelving photo (different angle from hero)

### 8. [HIGH] Fix #ed2121 vs #e63329 color inconsistency

**Severity:** High
**File:** `src/pages/ua/services.astro`
**What:** Replace all instances of `#ed2121` with `var(--red)` to match the site-wide brand color.

### 9. [MEDIUM] Create unique SEO articles instead of rehashing the same points

**Severity:** Medium
**Files:** internet-magazynu, marketpleysiv, vazhkykh, kyiv, maloho-biznesu
**What:** Each page has a "КОРИСНО ЗНАТИ" article section that covers "what is fulfillment + how much it costs + how to choose operator." These overlap 60-80%. Recommendations:
- **internet-magazynu**: Deep dive on CRM integration workflows, order automation, return handling
- **marketpleysiv**: Platform-specific guides (Rozetka seller requirements, Prom API setup, Kasta ranking algorithm)
- **vazhkykh**: Logistics of oversized goods, packaging requirements, carrier comparison for 50kg+ items
- **kyiv**: Geographic analysis of Kyiv logistics infrastructure, district-level delivery speeds
- **maloho-biznesu**: Step-by-step "from garage to fulfillment" transition guide, real cost breakdown for 10/day

### 10. [MEDIUM] Deduplicate "блекаут" claims into a single dedicated section/page

**Severity:** Medium
**What:** The "3 generators, Starlink, 2 providers, zero downtime since 2022" claim appears on 8+ pages. Create a dedicated "Reliability" section as a component, or a standalone page like `/ua/nadijnist/`, and link to it from other pages. This avoids repetition while keeping the SEO value.

### 11. [MEDIUM] Fix badge border-radius inconsistency

**Severity:** Medium
**Files:** ukraina.astro vs all other pages
**What:** ukraina uses `border-radius:100px` (pill) while all others use `border-radius:2px` (rectangle). Standardize to one style site-wide via Base.astro or a shared component.

### 12. [MEDIUM] Unify FAQ CSS class names

**Severity:** Medium
**Files:** All pages with FAQs
**What:** Currently 4 different naming schemes: `.faq-question/.faq-answer`, `.faq-q/.faq-a`, `.ky-faq-q/.ky-faq-a`, `.sb-faq-q/.sb-faq-a`. Create a single `FAQ.astro` component with consistent class names, or move FAQ styles to a shared stylesheet.

### 13. [MEDIUM] Add unique case studies to pages that lack them

**Severity:** Medium
**What:** 
- **kyiv**: Has ORNER case but could add a Kyiv-specific local business case
- **skladski**: Has a unique case (3200 SKU) -- good
- **maloho-biznesu**: Needs its own case study of a small business (e.g., an Instagram seller growing from 10 to 50 orders/day)
- Avoid reusing Carter's case on more than 2 pages

### 14. [LOW] Differentiate hero form CTA button text

**Severity:** Low
**What:** 10 out of 13 pages use "Отримати розрахунок" as the CTA. Tailor to page context:
- services: "Обрати послугу"
- marketpleysiv: "Підключити маркетплейс"
- vazhkykh: "Отримати умови для важких товарів"
- maloho-biznesu: "Спробувати безкоштовно"
- calculator: "Порахувати зараз" (remove form, scroll to calculator)

### 15. [LOW] Add mobile breakpoint for marketpleysiv marketplace grid

**Severity:** Low
**File:** `src/pages/ua/fulfilment-dlya-marketpleysiv.astro`
**What:** The `.mp-grid{grid-template-columns:repeat(2,1fr)}` has no mobile override visible in the CSS excerpt. Add:
```css
@media(max-width:768px){.mp-grid{grid-template-columns:1fr}}
```

---

## SUMMARY SCORECARD

| Category | Score | Notes |
|---|---|---|
| **Content Uniqueness** | 3/10 | Massive overlap in stats, FAQs, pricing tables, case studies |
| **Hero Differentiation** | 5/10 | 3 pages truly unique (guide, maloho, kyiv), 10 follow same pattern |
| **Section Structure Variety** | 5/10 | Some unique sections exist but pricing+FAQ+SEO article pattern dominates |
| **Design Consistency** | 4/10 | Green color violation, #ed2121 vs #e63329, badge inconsistency, standalone page |
| **Component Reuse** | 2/10 | Zero shared components -- everything is copy-pasted inline |
| **Mobile Readiness** | 6/10 | Most pages have breakpoints but some grids miss mobile rules |

### Priority Order for Fixes:

1. Remove green color (#22c55e) -- **1 hour**
2. Migrate ukraina.astro to Base.astro -- **2-3 hours**
3. Fix #ed2121 in services.astro -- **15 minutes**
4. Create shared PricingTable component -- **2 hours**
5. Create shared ComparisonTable component -- **1 hour**
6. Make FAQs unique per page -- **3-4 hours**
7. Reduce video tour to 3 pages -- **1 hour**
8. Create unique hero images/backgrounds -- **2 hours (design) + 1 hour (code)**
9. Rewrite SEO articles for uniqueness -- **4-6 hours**
10. Fix badge inconsistency -- **15 minutes**

**Total estimated effort for critical + high items: ~12-15 hours**
