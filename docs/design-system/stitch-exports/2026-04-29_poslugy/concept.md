---
slug: poslugy
url: https://www.fulfillmentmtp.com.ua/poslugy/
archetype: Editorial
date: 2026-04-29
project_id: 13221574722902496783
---

# /poslugy/ — UA Editorial Services Hub

## Mood
Editorial / Digital Broadsheet — Bloomberg-meets-Stripe-Press for Ukrainian B2B fulfillment. Restricted palette (red #e63329, black, white, #fafafa, #eaeaea), serif Newsreader/DM Serif Display + sans Work Sans/DM Sans, sharp corners, large whitespace, no hero image — typography IS the hero.

## Stitch Outputs

### Base (recommended)
- **Screen ID:** `ebe5e022401843b2816bff4b3650ed45`
- **Screenshot:** `screenshot-base.png`
- **HTML:** `export-base.html`
- **Layout:** Centered hero (massive serif H1) → grey stats bar → 7 service category cards in 2-col grid → 6-step timeline → pricing table → FAQ → dark CTA band → footer.
- **Pros:** Clearest information hierarchy, content-first, 7 categories visible above-fold scroll, matches existing site patterns.
- **Cons:** Slightly conservative — leans on typography rather than visual surprise.

### Variant 1 — Asymmetric Ledger
- **Screen ID:** `577c1daedff44417b5b8f31ed6b24576`
- **Screenshot:** `screenshot-v1.png`
- **HTML:** `export-v1.html`
- **Layout:** Two-column hero (text left + numbered stats ledger right with check/list icons) → red full-bleed quote band ("12+ років") → image grid → pricing → FAQ → dark CTA.
- **Pros:** Stronger above-fold density, ledger evokes financial-grade trust, red quote band breaks rhythm.
- **Cons:** Three warehouse photos appear (we'd need to source/swap), service cards demoted vs. base.

### Variant 2 — Massive Numerals (Reimagine)
- **Screen ID:** `c397a4ad555b48dcb4b36be0a828efdb`
- **Screenshot:** `screenshot-v2.png`
- **HTML:** `export-v2.html`
- **Layout:** Centered "Логістичний хаб майбутнього" hero → 4-stat row → BIG hero image → world map "global network" panel → quote → footer image grid.
- **Pros:** Most ambitious visually.
- **Cons:** Drifts away from a services HUB into "about us" territory; loses the 7-category index that's the whole reason for /poslugy/.

## Recommendation
**Base** — it directly serves the user job: scan 7 service categories, click into the right one, see prices. Variant 1's ledger is a nice idea but I can borrow that idea inside Base (use a small ledger inside the hero CTA card rather than redesigning around it). Variant 2 is off-brief.

## WOW-element (one)
**Sticky category nav with anchor scroll** — when user scrolls past hero, the 7-chip nav (Зберігання / Комплектація / Доставка / Повернення / Інтеграції / Маркетплейси / Спецпослуги) sticks to top under the main header, highlighting the active section as user scrolls. Combined with `scroll-margin-top` and `prefers-reduced-motion: reduce` fallback. Implementation: `position: sticky; top: 64px;` + `IntersectionObserver` for active state.

## Shared components to reuse
- `src/components/Header.astro` (main nav)
- `src/components/Footer.astro`
- `src/components/HeroCTA.astro` (mandatory hero form per CLAUDE.md)
- `src/components/CTA.astro` (auto via Base.astro showCTA=true)
- `src/components/stitch/StatsBar.astro` (the 4-stat row)
- `src/components/stitch/AccordionGroup.astro` (FAQ)
- `src/components/stitch/LabelChip.astro` (uppercase red labels)
- Page-specific styles via `<style is:global>` with BEM prefix `poslugy__`.

## Page outline (13 sections, ~3000 words)
1. **Editorial Hero** — H1 + subhead + HeroCTA form (NOT decorative buttons — must be `<HeroCTA/>` per ironclad rule).
2. **Stats bar** — 5,500 m² / 17 операцій / 99.8% / 24h.
3. **TL;DR** (30-second answer for AI search) — 3-4 paragraphs.
4. **Sticky category nav** (7 chips, scroll spy).
5. **Зберігання** — палетне / поличне / холодне / великогабаритне → links to `/ua/skladski-poslugy/`, `/ua/paletne-zberigannya/`.
6. **Комплектація замовлень** — pick-pack, accuracy SLA, batch picking.
7. **Доставка** — Україна (Нова Пошта, Укрпошта, Justin) + міжнародна (DHL/UPS).
8. **Повернення** — обробка returns, refurb, утилізація.
9. **Інтеграції** — Horoshop / Prom / Rozetka / Allo / OpenCart / WooCommerce / 1C → cross-link `/ua/fulfilment-prom/`, `/ua/fulfilment-rozetka/`.
10. **Маркетплейси** — спеціалізація Rozetka/Prom/Allo.
11. **Спецпослуги** — копакінг, маркування, кросдокінг, інвентаризація, автодзвінок.
12. **Прайс знімок** — 8-row table з посиланням на `/ua/tsiny/`.
13. **FAQ** — 8 пар (FAQPage schema).
14. **Bottom CTA** (auto from Base.astro).

## Cross-links (deep internal linking)
Within service category sections — link to existing pages:
- `/ua/skladski-poslugy/`, `/ua/paletne-zberigannya/`, `/ua/fulfilment-ukraina/`, `/ua/fulfilment-kyiv/`
- `/ua/fulfilment-rozetka/`, `/ua/fulfilment-prom/`, `/ua/fulfilment-dlya-marketpleysiv/`
- `/ua/fulfilment-dlya-internet-magazynu/`, `/ua/fulfilment-dlya-kosmetyky/`, `/ua/fulfilment-dlya-maloho-biznesu/`, `/ua/fulfilment-vazhkykh-tovariv/`, `/ua/3pl-logistyka/`
- `/ua/calculator/`, `/ua/tsiny/`, `/ua/shcho-take-fulfilment/`, `/ua/about/`

## Hreflang siblings
- `uk` → `/poslugy/` (this page, root, no /ua/ prefix per UA URL Policy)
- `ru` → `/ru/services/` (existing)
- `en` → `/en/services/` (existing)
- `x-default` → `/poslugy/`

This closes the missing-UA-services-triad gap discovered in hreflang audit (2 incomplete cases).

## Approval status
Pending — awaiting "approved" before Writer/Code/Deploy.
