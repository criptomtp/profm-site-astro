# CRITIC REPORT -- Quality Audit

**Date:** 2026-04-11
**Auditor:** Quality Critic Agent
**Build:** npm run build -- PASS (159 pages, 2.12s)

---

## 1. BUILD TEST

**Result: PASS with 2 CSS warnings**

The build completes successfully, generating 159 pages in ~2 seconds. However, there are **2 CSS syntax warnings** from esbuild CSS minifier:

### CRITICAL: Unbalanced CSS braces

| File | Line | Issue |
|------|------|-------|
| `src/pages/blog/index.astro` | 454 | `.footer-bottom{...` missing closing `}` |
| `src/pages/ua/blog/index.astro` | 478 | `.footer-bottom{...` missing closing `}` |

Both files have a `.footer-bottom` rule that ends abruptly without a closing brace. This causes the CSS minifier to produce a warning and could cause downstream styling corruption in production (any CSS rules after this line may be silently discarded by some browsers).

**Fix:** Add `}` at the end of line 454 in `blog/index.astro` and line 478 in `ua/blog/index.astro`.

---

## 2. DESIGN CONSISTENCY CHECK

### 2a. Prohibited colors -- PASS (no green)

No instances of green (#22c55e, #4caf50, #2e7d32, #00c853, etc.) found anywhere in `src/pages/`.

### 2b. Non-standard accent colors -- MINOR

The following non-brand colors are used. While not "green," they deviate from the strict `#e63329 + #000 + #fff + grays` palette:

| Color | Usage | Files |
|-------|-------|-------|
| `#e6a829` | Warning indicator (amber) | `ua/fulfilment-dlya-maloho-biznesu.astro` |
| `#f9a825` | Callout box borders (yellow-amber) | `ua/blog/top-marketpleysiv-ukrayiny.astro`, `blog/top-marketplejsov-ukrainy.astro` |
| `#fff8e1`, `#fffde7` | Callout box backgrounds (light yellow) | Same blog posts |
| `#fff0f0` | Negative highlight background (light red) | Same blog posts |
| `#c62828` | Negative text emphasis (dark red) | Same blog posts |
| `#8b0000` | Gradient endpoint (dark red) | `ua/fulfilment-dlya-maloho-biznesu.astro` |
| `#767676` | Label text (medium gray) | `index.astro`, `ru/index.astro` |

**Assessment:** The amber/yellow colors (`#f9a825`, `#fff8e1`, `#fffde7`) in the marketplace comparison blog posts are functional (pro/con callout boxes) and acceptable for editorial content. The dark red variants (#c62828, #8b0000, #c42b22, #c42a22, #c4271e, #d41c1c) are all hover states or gradients of the primary red -- acceptable.

### 2c. Video sections -- PASS

All video sections use the consistent `video-thumb` pattern with play overlay buttons. No broken patterns found.

---

## 3. MOBILE LAYOUT CHECK

### CRITICAL: Blog posts with inline 4-column grids and NO media queries

The following blog posts use `grid-template-columns:repeat(4,1fr)` as inline styles with **zero `@media` queries** on the entire page:

| File | Line | Issue |
|------|------|-------|
| `src/pages/ua/blog/top-marketpleysiv-ukrayiny.astro` | 32 | Inline 4-col grid, no `@media` at all |
| `src/pages/blog/top-marketplejsov-ukrainy.astro` | 30 | Same issue |
| `src/pages/en/blog/post/top-marketplaces-ukraine.astro` | 49 | Same issue |

**Impact:** On 375px screens, each column is ~80px wide. The "200+ mlrd" / "2-27%" stats block will overflow or compress text illegibly.

**Fix:** Add `@media(max-width:768px){ ... }` to convert these to 2-column or single-column layouts. Since these are inline styles, they need to be moved to a `<style>` block to be made responsive.

### MAJOR: Tables without overflow-x wrapper

The following EN blog posts have `<table>` elements without any `overflow-x:auto` wrapper:

| File | Tables |
|------|--------|
| `en/blog/post/fulfillment-cost-guide.astro` | 2 tables |
| `en/blog/post/where-online-store-loses-money.astro` | 1 table |
| `en/blog/post/reduce-product-returns-ecommerce.astro` | 1 table |
| `en/blog/post/fulfillment-vs-own-warehouse-2025.astro` | 1 table |
| `en/blog/post/what-is-sla-in-logistics.astro` | 1 table |
| `en/blog/post/fulfillment-for-clothing-shoes.astro` | 1 table |

The CSS sets `article table{width:100%}` but on narrow screens with 4+ columns, tables will overflow the viewport horizontally with no scrollbar.

**Fix:** Wrap each `<table>` in `<div style="overflow-x:auto">`.

### Other multi-column grids -- PASS

All other `repeat(4,1fr)` and `repeat(5,1fr)` grids across service pages, about pages, and pricing pages have proper `@media` breakpoints that reduce to 2 or 1 column on mobile.

---

## 4. FAQ SCHEMA CONSISTENCY

### CRITICAL: ua/fulfilment-ukraina.astro -- Schema/HTML mismatch

**Schema FAQPage has 8 questions. HTML FAQ has 11 questions. The questions themselves are DIFFERENT.**

Schema questions (not in HTML):
- "Скільки фулфілмент-операторів працює в Україні і чим MTP відрізняється?"
- "Чи є доукомплектація замовлень і скільки вона коштує?"
- "Як порівняти вартість фулфілменту з власним складом в Україні?"
- "Чи є реферальна програма для клієнтів MTP?"

HTML questions (not in Schema):
- "Скільки коштує фулфілмент в Україні?"
- "Як швидко можна підключитися?"
- "Які маркетплейси підтримуєте?"
- "Чи можна почати з малих обсягів?"
- "Що входить у вартість відправки?"
- "Чому два склади -- не один?"

**Impact:** Google may flag "Mismatch between structured data and page content" in Search Console, potentially losing rich FAQ snippets.

**Fix:** Synchronize Schema.org JSON with the actual HTML FAQ items.

### MINOR: index.astro (UA homepage) -- wording mismatches

Schema Q5: "Які маркетплейси підтримуєте?" vs HTML: "Які маркетплейси та CRM підтримуєте?"
Schema Q7: "Чи є мінімальний обсяг?" vs HTML: "Чи є мінімальний обсяг замовлень?"

### MINOR: ru/index.astro -- wording mismatches

Schema Q4: "Работает ли склад при блэкаутах?" vs HTML: "Работает ли склад при отключениях света?"
Schema Q5: "Какие маркетплейсы поддерживаете?" vs HTML: "Какие маркетплейсы и CRM поддерживаете?"

### PASS: Other FAQ pages checked

- `ua/services.astro` -- 6 Schema questions match 6 HTML FAQ items (OK)
- `en/fulfillment-for-small-business.astro` -- 6 Schema questions match 6 HTML FAQ items (OK)

---

## 5. INTERNAL LINKS

### Broken link patterns -- PASS

- `/ua/vidhuky/` -- 0 occurrences (correct, was renamed to /ua/recalls/)
- `/ua/kalkulyator-fulfillment/` -- 0 occurrences (correct, was renamed to /ua/calculator/)

### Internal links in SEO articles -- PASS

Spot-checked links in:
- `ua/fulfilment-ukraina.astro` -- all links point to existing pages (/ua/tsiny/, /ua/calculator/, /ua/services/, etc.)
- `ua/fulfilment-dlya-maloho-biznesu.astro` -- all links valid
- `ua/blog/scho-take-fulfilment.astro` -- all links valid
- `ua/blog/top-marketpleysiv-ukrayiny.astro` -- all links valid

---

## 6. HREFLANG

### Spot-check results (3 pages) -- PASS

| Page | uk | ru | en | x-default |
|------|----|----|----|-----------|
| `ua/fulfilment-dlya-maloho-biznesu.astro` | OK | OK | OK | OK |
| `en/fulfillment-for-marketplaces.astro` | OK | OK | OK | OK |
| `ua/about.astro` | OK | OK | OK | OK |

### MINOR: 3 blog posts missing hreflang="ru"

These 3 UA blog posts (and their EN equivalents) have hreflang for uk, en, x-default but are **missing hreflang="ru"**:

| UA file | EN file |
|---------|---------|
| `ua/blog/tpost/2fz7njsgn1-scho-take-artikul-yak-pravilno-iogo-stvo.astro` | `en/blog/post/what-is-sku-article-number.astro` |
| `ua/blog/tpost/2lpu5l5sa1-mtp-group-dinii-v-ukran-servs-z-shvidko.astro` | `en/blog/post/mtp-group-fast-product-liquidation.astro` |
| `ua/blog/tpost/hmh91dbl11-mtp-group-fulfillment-naikrasch-fulflmen.astro` | `en/blog/post/mtp-group-best-fulfillment-operators.astro` |

These are newer posts that may not have RU counterparts. If RU versions do not exist, the missing hreflang="ru" is acceptable but inconsistent with all other blog posts that have it.

---

## SUMMARY TABLE

| # | Category | Severity | Count | Status |
|---|----------|----------|-------|--------|
| 1 | CSS unbalanced braces (blog index) | CRITICAL | 2 files | NEEDS FIX |
| 2 | FAQ Schema/HTML mismatch (fulfilment-ukraina) | CRITICAL | 1 file | NEEDS FIX |
| 3 | Inline 4-col grid without mobile breakpoints (blog) | CRITICAL | 3 files | NEEDS FIX |
| 4 | Tables without overflow-x wrapper (EN blog) | MAJOR | 6 files | NEEDS FIX |
| 5 | FAQ Schema wording mismatches (homepage UA/RU) | MINOR | 2 files | SHOULD FIX |
| 6 | Missing hreflang="ru" on 3 blog post sets | MINOR | 6 files | LOW PRIORITY |
| 7 | Non-brand amber/yellow in blog callouts | MINOR | 3 files | ACCEPTABLE |
| 8 | Prohibited green colors | -- | 0 | PASS |
| 9 | Broken internal links | -- | 0 | PASS |
| 10 | Video sections consistency | -- | 0 issues | PASS |
| 11 | Hreflang completeness (main pages) | -- | 0 issues | PASS |
| 12 | Build errors | -- | 0 | PASS |

**Total critical issues: 3 (affecting 6 files)**
**Total major issues: 1 (affecting 6 files)**
**Total minor issues: 3 (affecting 11 files)**
