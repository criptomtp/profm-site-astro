---
slug: fulfilment-rozetka
created: 2026-04-26
archetype: industrial
mood: industrial
status: shipped
languages:
  - uk
  - ru
  - en
urls:
  uk: https://www.fulfillmentmtp.com.ua/fulfilment-rozetka/
  ru: https://www.fulfillmentmtp.com.ua/ru/fulfilment-rozetka/
  en: https://www.fulfillmentmtp.com.ua/en/fulfillment-for-rozetka-sellers/
stitch_export: docs/design-system/stitch-exports/2026-04-26_fulfilment-rozetka/
approval_date: 2026-04-26
semantic_core_id: 43
---

# /fulfilment-rozetka/ — Rozetka multi-marketplace landing

## Archetype: Industrial

Three-language launch where each language receives a different layout VARIANT
inside the Industrial archetype. This is intentional — same archetype keeps
typography / spacing / palette consistent, but hero composition and stat
placement vary per audience.

## Per-language variant mapping

| Lang | Variant      | Hero layout                                         | Audience angle                                                 |
|------|--------------|-----------------------------------------------------|----------------------------------------------------------------|
| UA   | BASE 60/40   | Split: text+form left, vertical stats column right  | Альтернатива Rozetka FBO для excluded categories               |
| RU   | VARIANT A    | Full-width centered H1 + horizontal stats strip + form below | Україна як CIS-хаб, ИМ-71, KZ/MD/GE distribution      |
| EN   | VARIANT B    | Split 60/40 + 4 white-bordered stat cards stacking right | Multi-marketplace gateway to Ukraine without lock-in     |

## Why three different angles (not translations)

- **UA**: Rozetka сама blocks excluded categories (furniture, large
  appliances, fragile glass, cold-chain). UA seller already knows Rozetka FBO
  exists — selling proposition is "we do what FBO refuses".
- **RU**: CIS seller (KZ/MD/GE) needs **entry into Ukraine**. Rozetka is
  a destination, not a problem. ИМ-71 customs warehouse + 4 100 m² is the
  hook.
- **EN**: international seller wants Ukraine without picking one marketplace.
  EU hub comparison (PL/CZ) and EUR pricing matter more than Rozetka's
  category list.

## Shared vs divergent

**Shared (single source of truth):**
- `<HeroCTA/>` canonical form (`id="heroLeadForm"` → window.mtpSubmitLead)
- `<StatsBar/>`, `<DarkCTA/>`, `<AccordionGroup/>`, `<LabelChip/>` from `src/components/stitch/`
- Tokens: `#e63329` / `#000` / `#fff` only — no other colors
- Industrial archetype rules: 0px corners, no shadows, uppercase eyebrows
- Schema.org: Service + FAQPage + BreadcrumbList per page (3 schemas concatenated in head)

**Divergent (per language):**
- BEM namespace per page: `.rzh-*` (UA), `.rzr-*` (RU), `.rze-*` (EN)
- Hero composition (BASE / Variant A / Variant B as described above)
- Comparison table content (UA: vs FBO; RU: vs CIS routing; EN: vs FBO + EU hub)
- Stats: UA shows OTIF/categories; RU shows ИМ-71/4 countries; EN shows ETA/EUR price/APIs

## Mood deviations

None. All three pages stay strictly inside Industrial archetype:
- Uppercase eyebrow labels (`<LabelChip/>`)
- Statbar with bordered cells, no rounded corners
- Black DarkCTA before footer
- No decorative gradients, no glass effects, no shadows

## Word counts

- UA: 2 571 words
- RU: 2 274 words
- EN: 2 598 words

All comfortably above the 1 200-word minimum from the create-page checklist.

## Hero CTA wiring

Each page uses `<HeroCTA/>` with a unique `sourceTag`:

- UA: `sourceTag="hero /fulfilment-rozetka/"`
- RU: `sourceTag="hero /ru/fulfilment-rozetka/"`
- EN: `sourceTag="hero /en/fulfillment-for-rozetka-sellers/"`

This lets us segment Telegram leads by language and page in `@nikolay_mtp`
inbox.

## Cross-language wiring

- Hreflang quartet on every page (uk / ru / en / x-default → UA root URL)
- Header.astro language-switcher map updated with two keys
  (`fulfilment-rozetka` for UA+RU and `fulfillment-for-rozetka-sellers` for EN slug)
- `public/llms.txt` updated with all 3 URLs in **Services** section

## Internal linking

Each page links to:
- `/3pl-logistyka/` (or `/ru/3pl-logistyka/` / `/en/3pl-logistics/`)
- `/calculator/` (or localized)
- Pricing page in target language
- About / contact

## Rollback trigger

If Rozetka FBO sellers convert at materially worse rate than other landings
(CR -15%) OR organic positions for "fulfillment rozetka" drop -20% within
7 days post-launch — git revert and rethink.

## Related decisions

- Three-language launch enforced by user feedback rule
  (no single-language deploys when 3 languages are already drafted).
- New UA URL policy applied: `/fulfilment-rozetka/` at root, no `/ua/` prefix.
- llms.txt sync rule applied: phantom URLs would break AI agent ingestion.
