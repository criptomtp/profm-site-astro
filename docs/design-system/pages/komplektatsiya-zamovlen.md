# ADR — `/komplektatsiya-zamovlen/` Pick & Pack Service Spoke

**Date:** 2026-05-04
**Status:** ANALYZER complete, awaiting STITCH approval
**Pipeline trigger:** `/create-page комплектація замовлень` (first test of formal /create-page pipeline)

---

## Strategic context — Hub-and-Spoke architecture

This is the **FIRST of 13 service-detail spokes** spoking from `/poslugy/` services hub.

- **Hub:** `/poslugy/` — lists 17 services briefly
- **Spoke (this page):** `/komplektatsiya-zamovlen/` — deep-dive on pick & pack as standalone service
- **Future spokes (12 more, prioritized in research file):** `/pakuvannya/`, `/markuvannya-tovaru/`, `/povernennya-tovariv/`, `/pryom-tovaru/`, `/intehratsii-api/`, `/avtodzvonok/`, `/kopaking/`, `/dostavka-po-ukraini/`, `/inventaryzatsiya/`, `/kros-doking/`, `/obsluhovuvannya-zamovlen/`, `/mizhnarodna-dostavka/`

**SEO logic:** spoke wins long-tail + head terms hub can't compete on; inbound link from authority hub passes equity; outbound link back to hub keeps user in funnel. **Hub MUST be updated post-deploy** to add clickable card linking to spoke (step 9 WIRE-UP).

---

## Inputs (from Steps 1 + 1.5)

- Competitor research: `.claude-flow/research/komplektatsiya-zamovlen.json`
- Keyword strategy: `.claude-flow/research/komplektatsiya-zamovlen-keywords.json`

---

## Word count targets

- UA competitor avg: ~1500 (only Pakline Logistics has dedicated page) → **target ≥ 2700 words** (+80% to dominate uncompeted UA niche)
- RU competitor avg: ~1200 (BOX 69 Belarus benchmark) → **target ≥ 2700 words** (over-deliver in CIS-Ukraine niche)
- EN competitor avg: ~2500 (RushOrder, Boxzooka, ArgoSoftware well-developed) → **target ≥ 2900 words** (+15%, must beat developed competitors with Ukraine-specific angle)

---

## Archetype decision — DIFFERENT per language (intentional)

Same pattern as `/fulfilment-knyzhok/`. Each audience has different cognitive/buying frame; visual language must match.

### 🇺🇦 UA — DIRECT mood

- **Audience:** Ukrainian e-com operators evaluating outsourced pick & pack vs in-house
- **Buyer behaviour:** wants to see speed numbers + accuracy + price quickly, action-oriented
- **Hero:** full-width with overlay (warehouse picker with scanner photo), badge "PICK & PACK · УКРАЇНА", H1, prominent HeroCTA form
- **Reference:** `/fulfilment-knyzhok/` (Direct mood, recently shipped)
- **WOW-element:** **"Live Pick Speed Counter"** — animated stat block "47 секунд → 99,5% точності → 18 грн" що оживає при scroll into view (CSS-only animation, no JS lib)

### 🇷🇺 RU — INDUSTRIAL mood

- **Audience:** CIS publishers/sellers (Belarus, Moldova, Kazakhstan) using Ukraine warehouse for outbound to UA + neighbouring CIS
- **Buyer behaviour:** wants operational proof (process diagrams, scan-flow, accuracy metrics), formal tone, depth
- **Hero:** split (text left, dark warehouse image right), uppercase tracked-out label "PICK & PACK / УКРАИНА 2026", H1, stats bar immediately below
- **Reference:** `/en/fulfilment-for-clothing/` (Industrial archetype signature)
- **WOW-element:** **"Process Flow Diagram"** — 8-step pick-flow rendered as numbered horizontal flow with icons (1. Прием → 2. WMS-маршрут → 3. Picker scan → 4. Verify → 5. Упаковка → 6. QC → 7. Ярлык → 8. Курьер). CSS grid + numbered circles, no SVG library.

### 🇬🇧 EN — INDUSTRIAL mood (different angle from RU)

- **Audience:** International e-com brands evaluating Ukraine 3PL for cross-border fulfilment
- **Buyer behaviour:** data-driven, ROI-focused, wants cost-vs-accuracy comparison vs US/EU baseline
- **Hero:** split (text left, dark hero image right), uppercase label "ORDER PICK & PACK · UKRAINE 3PL", H1, stats bar below
- **Reference:** `/en/fulfilment-for-clothing/` + `/en/fulfilment-for-books-and-publishers/`
- **WOW-element:** **"Cost-vs-Accuracy Matrix"** — 3-column table comparing UA/US/EU 3PL on per-order cost, accuracy %, scan stages, QC step. Industrial styling with sharp borders + uppercase headers.

---

## Validation test for "3 angles, not translations"

After WRITER step, verify:
- Translate UA H1 to RU via Google Translate → must NOT match RU H1 word-for-word (target overlap <50%)
- Each language has 2-3 sections that DO NOT exist in other languages:
  - **UA:** "Помилка комплектації — хто платить і як ми компенсуємо" (UA-specific accountability)
  - **RU:** "Сборка заказов из Украины в Беларусь, Молдову, Казахстан" (CIS outbound from UA warehouse)
  - **EN:** "Why Ukraine pick & pack costs $0.41 vs $1.50 US baseline" (cost structure breakdown)

---

## Shared stitch components to use

- `<LabelChip>` (3/3 languages, variants: red UA / dark RU / dark EN)
- `<StatsBar>` — 3/3 languages (Direct + Industrial both allow)
- `<SplitHero>` — RU + EN only (Industrial archetype signature)
- `<HeroCTA>` — 3/3 languages above-the-fold form
- `<DarkCTA>` — 3/3 languages footer conversion
- `<AccordionGroup>` — 3/3 languages for FAQ sections

---

## Keyword strategy enforcement (from Step 1.5)

**UA:**
- URL: `/komplektatsiya-zamovlen/` (exact match primary #1: "комплектація замовлень")
- Title: "Комплектація замовлень — pick & pack за 47 секунд від 18 грн"
- H1: includes "комплектація замовлень" + brand-hook (em-dash + 47 секунд / 99,5% точність)
- ≥2 H2s mention "збір замовлень" / "точність комплектації"
- Lede: "комплектація замовлень" + "47 секунд" in first 50 words

**RU:**
- URL: `/ru/komplektaciya-zakazov/`
- Title: "Комплектация заказов — pick & pack 47 секунд, 99,5% точность"
- H1: includes "комплектация заказов" + Industrial brand-hook
- ≥2 H2s mention "сборка заказов" / "точность комплектации"
- Lede: "комплектация заказов" + "47 секунд" in first 50 words

**EN:**
- URL: `/en/order-pick-and-pack-ukraine/`
- Title: "Order Pick and Pack Ukraine — 99.5% Accuracy, $0.41 per Order"
- H1: includes "pick and pack Ukraine" + cost-vs-US hook
- ≥2 H2s mention "scan-based picking" / "Ukrainian warehouse"
- Lede: "pick and pack Ukraine" in first 50 words
- Cost-comparison block must exist

---

## Negative keywords critical to filter

Job-search intents must be aggressively negated (UA: "комплектувальник", "пакувальник вакансія"; RU: "комплектовщик", "вакансия упаковщик"; EN: "picker job", "warehouse worker job"). High volume but wrong intent — would attract job-seekers, not B2B buyers.

---

## Next step

STITCH PREVIEW — generate base concept for each of 3 archetypes. Save all to `docs/design-system/stitch-exports/2026-05-04_komplektatsiya-zamovlen/`. Show user. **HARD STOP** until "approved all 3" or refinement requests.
