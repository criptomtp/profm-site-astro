# CSS Duplication Report

Generated: 2026-04-09

## Summary

The site has significant CSS duplication across page-level `<style is:inline>` blocks. The Base.astro layout contains core design-system CSS, but many page-specific styles are copy-pasted across multiple files.

---

## 1. FAQ Accordion CSS (40 files)

**Pattern**: `.faq-item`, `.faq-q`, `.faq-a`, `.faq-item.open` styles
**Occurrences**: 130 total across 40 files
**Variants**: `.faq-*`, `.sb-faq-*`, `.kv-faq-*`, `.ky-faq-*`, `.ek-faq-*`, `.faq-question/.faq-answer`

### Files with standard `.faq-*` CSS:
- src/pages/fulfilment-dlya-marketpleysov.astro
- src/pages/fulfilment-vazhkykh-tovariv.astro
- src/pages/fulfilment-dlya-internet-magazynu.astro
- src/pages/skladski-poslugy.astro
- src/pages/tsenu.astro
- src/pages/services.astro
- src/pages/en/heavy-goods.astro
- src/pages/en/prices.astro
- src/pages/en/fulfillment-for-online-stores.astro
- src/pages/en/warehouse-services.astro
- src/pages/en/fulfillment-for-marketplaces.astro
- src/pages/en/fulfillment-for-small-business.astro
- src/pages/en/services.astro
- src/pages/en/index.astro
- src/pages/ua/fulfilment-vazhkykh-tovariv.astro
- src/pages/ua/fulfilment-dlya-internet-magazynu.astro
- src/pages/ua/skladski-poslugy.astro
- src/pages/ua/fulfilment-dlya-marketpleysiv.astro
- src/pages/ua/tsiny.astro
- src/pages/ua/services.astro
- src/pages/ru/fulfilment-dlya-malogo-biznesa.astro
- src/pages/blog/index.astro
- src/pages/ua/blog/index.astro
- src/pages/en/blog/post/fulfillment-cost-guide.astro
- src/pages/en/blog/post/top-5-logistics-mistakes-ecommerce.astro
- src/pages/en/blog/post/fulfillment-vs-own-warehouse-2025.astro
- src/pages/en/blog/post/fulfillment-vs-own-warehouse.astro
- src/pages/en/blog/post/how-fulfillment-works-ukraine-2025.astro
- src/pages/en/blog/post/best-business-ideas-ukraine.astro
- src/pages/en/blog/post/how-to-choose-fulfillment-operator.astro
- src/pages/en/blog/post/product-business-ukraine-guide.astro
- src/pages/en/blog/post/what-is-fulfillment-7-services.astro
- src/pages/en/blog/post/expand-to-european-marketplaces.astro
- src/pages/en/blog/post/ecommerce-logistics-during-war.astro
- src/pages/en/blog/post/how-to-start-online-store-ukraine.astro
- src/pages/en/blog/post/what-is-sku-article-number.astro
- src/pages/en/blog/post/what-is-sla-in-logistics.astro

### Files with prefixed FAQ CSS (unique per page):
- src/pages/ua/fulfilment-dlya-maloho-biznesu.astro (`.sb-faq-*`)
- src/pages/fulfilment-kiev.astro (`.kv-faq-*`)
- src/pages/ua/fulfilment-kyiv.astro (`.ky-faq-*`)
- src/pages/en/fulfillment-kyiv.astro (`.ek-faq-*`)

### Recommendation:
Extract common FAQ CSS into `public/css/faq.css` or add to Base.astro `<style>` block. The prefixed variants (sb-, kv-, ky-, ek-) could be standardized to use the common `.faq-*` classes.

---

## 2. Hero Section CSS (33 files)

**Pattern**: `.hero`, `.hero-content`, `.hero h1`, `.hero-sub`, `.hero-form`, `.hero-stats`
**Occurrences**: 135 total across 33 files
**Note**: Already partially in Base.astro, but some pages redefine/override hero styles

### Files:
- src/pages/index.astro
- src/pages/ru/index.astro
- src/pages/en/index.astro
- src/pages/calculator.astro, ua/calculator.astro, en/calculator.astro
- src/pages/about.astro, ua/about.astro, en/about.astro
- src/pages/tsenu.astro, ua/tsiny.astro, en/prices.astro
- src/pages/services.astro, ua/services.astro, en/services.astro
- src/pages/skladski-poslugy.astro, ua/skladski-poslugy.astro, en/warehouse-services.astro
- src/pages/fulfilment-vazhkykh-tovariv.astro, ua/fulfilment-vazhkykh-tovariv.astro, en/heavy-goods.astro
- src/pages/fulfilment-dlya-internet-magazynu.astro, ua/fulfilment-dlya-internet-magazynu.astro, en/fulfillment-for-online-stores.astro
- src/pages/fulfilment-dlya-marketpleysov.astro, ua/fulfilment-dlya-marketpleysiv.astro, en/fulfillment-for-marketplaces.astro
- src/pages/recalls.astro, ua/recalls.astro, en/recalls.astro
- src/pages/blog/index.astro, ua/blog/index.astro

### Recommendation:
Hero styles are already in Base.astro. Pages that redefine them should only override what's different. Remove redundant hero CSS from individual pages.

---

## 3. Final CTA / Form CSS (19 files)

**Pattern**: `.final-cta`, `.final-form`, `.final-form input/button`
**Occurrences**: 45 total across 19 files
**Note**: Already in Base.astro but redefined in many pages

### Files:
- src/pages/fulfilment-vazhkykh-tovariv.astro, ua/fulfilment-vazhkykh-tovariv.astro
- src/pages/fulfilment-dlya-internet-magazynu.astro, ua/fulfilment-dlya-internet-magazynu.astro
- src/pages/skladski-poslugy.astro, ua/skladski-poslugy.astro
- src/pages/tsenu.astro
- src/pages/calculator.astro, en/calculator.astro
- src/pages/about.astro, en/about.astro
- src/pages/recalls.astro, en/recalls.astro
- src/pages/en/heavy-goods.astro, en/prices.astro, en/warehouse-services.astro
- src/pages/en/fulfillment-for-online-stores.astro, en/fulfillment-for-small-business.astro

### Recommendation:
Already in Base.astro. Remove duplicates from individual pages.

---

## 4. Anti-FOUC Overrides (30+ files)

**Pattern**: `.svc-card,.service-card,.num-card,...{opacity:1!important;transform:none!important}`
**Note**: Nearly every page has this line with slightly different class lists

### Recommendation:
Add a generic rule in Base.astro that targets common animated elements. Individual pages only need page-specific class overrides.

---

## 5. Fade-in / Reveal Animation CSS (6 files)

**Pattern**: `.fade-in`, `.reveal`, `opacity:0;transform:translateY()`
**Occurrences**: 6 files

### Recommendation:
Standardize on one animation approach (`.reveal` is already handled in Base.astro JS). Move CSS to Base.astro.

---

## Priority Order for Future CSS Cleanup

1. **FAQ CSS** -- highest duplication (40 files), most mechanical to extract
2. **Hero CSS overrides** -- remove redundant redefinitions from 33 pages
3. **Final CTA CSS** -- remove from 19 pages (already in Base.astro)
4. **Anti-FOUC overrides** -- normalize the pattern across 30+ pages
5. **Fade-in animations** -- standardize on `.reveal` pattern

## Estimated Savings

- FAQ CSS: ~120 lines removed across 40 files
- Hero CSS: ~200 lines removed across 33 files
- Final CTA CSS: ~90 lines removed across 19 files
- Anti-FOUC: ~30 lines removed across 30 files
- **Total**: ~440 duplicated CSS lines could be consolidated
