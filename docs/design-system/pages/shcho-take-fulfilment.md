# ADR — Pillar Hub "What Is Fulfillment"

- **Slugs**: `/ua/shcho-take-fulfilment/` · `/ru/chto-takoe-fulfilment/` · `/en/what-is-fulfillment/`
- **Archetype**: Editorial (long-form knowledge hub)
- **Approval**: 2026-04-21 (user approved "ок, роби як ти всі 5 рівнів")
- **Stitch artefacts**: `docs/design-system/stitch-exports/2026-04-21_shcho-take-fulfilment/`

## Per-language archetype variants

| Language | Variant | WOW element |
|---|---|---|
| UA | Variant A — Sticky TOC | Blackout Resilience Panel (3 generators + Starlink = 0 downtime days since 2022) |
| RU | Variant B — Split Diptych | Myth vs Reality CSS-flip grid (6 cards, hover flips myth→reality) |
| EN | Base — Data-first | Before/After ROI cards (6 metrics: pack time, error rate, cost, scale, setup, capex) with striked-before + red-arrow + after values |

## Content policy

Three distinct articles — not translations. UA targets Ukrainian ecommerce (hryvnia, Nova Poshta, Rozetka), RU targets CIS B2B (Kazakhstan, Moldova, Georgia entering Ukraine), EN targets Western DTC brands evaluating Ukraine as an EU-adjacent hub.

Word counts: UA 3,791 · RU 3,080 · EN 3,174 (all above the 2,500–3,500 target).

## Internal linking (5 levels, all implemented)

1. **Primary nav**: covered by mega-menu top entry with `GUIDE` / `ГІД` / `ГАЙД` badge
2. **Mega-menu**: added as first item in col1 ("By business type") across all 3 languages
3. **Footer**: new 4th column "Knowledge / Знання / Знания" with pillar + prices + calculator
4. **Home teasers**: inline "Newcomer to fulfillment?" lead line on `/`, `/ru/`, `/en/`; EN home adds a distinct red-gradient `en-article--pillar` card in the resources grid
5. **Upstream blog links**: contextual red callout box with pillar link inserted in:
   - `/ua/blog/scho-take-fulfilment/`
   - `/en/blog/post/what-is-fulfillment-complete-guide/`
   - `/en/blog/post/what-is-fulfillment-7-services/`
   - `/en/blog/post/fulfillment-vs-own-warehouse/`

## Coexistence with existing blog posts

Existing posts at `/ua/blog/scho-take-fulfilment/`, `/blog/chto-takoe-fulfilment/`, `/en/blog/post/what-is-fulfillment-complete-guide/` are **preserved** (no 301 redirects). Pillar lives at the top-level non-blog URL; blog posts remain as introductory pieces that upstream-link to the pillar for the full treatment.

## SEO

- Title: all under 60 chars
- Description: all within 150-160 chars
- H1: exactly one per page
- Schema.org: Article + FAQPage (6 UA / 12 RU / 12 EN Q&A) + BreadcrumbList
- Hreflang: uk/ru/en/x-default=uk, fully symmetric across 3 URLs
- Language-switcher: three-way slug mapping added in `Header.astro` map block

## CSS isolation

- UA: `.pillar-*` BEM prefix
- RU: `.ru-pil-*` BEM prefix
- EN: `.en-pil-*` BEM prefix

No class collisions; each page ships its own scoped inline `<style is:global>` block with the page-local palette (`#e63329`, `#000`, `#fff`).

## Verification

- `npm run build` — 173 pages, 0 errors
- Hreflang output verified via `grep hreflang dist/*/index.html` — symmetric
- Font loading via existing `/css/fonts.css` (DM Serif Display + DM Sans) inherited from `Base.astro`
