---
slug: fulfilment-for-small-business
language: EN
target_url: /en/fulfilment-for-small-business/
archetype: Industrial
date: 2026-04-29
stitch_project: projects/1536735774681646973
status: pending_approval
---

# Concept — Small Business EN landing page

## Target audience
International DTC SMB founders running 50–3,000 orders/month: Shopify Lite,
Etsy Plus, Kickstarter creators, Faire wholesale, indie Amazon EU sellers.
Currently ship from a garage, a co-working desk, or a Brooklyn/Berlin/London
apartment. Priced out of US 3PL platform fees ($150–$1,995/mo + per-order),
priced out of EU contract fulfillment (€500/mo minimums). Want a real WMS
and EU/UA shipping rates, not a side-hustle.

## Why Industrial archetype
This buyer is mid-procurement evaluation, not brand discovery. They have
ShipBob, ShipMonk, ShipHero, Red Stag, ShipHero spreadsheet open. They want
hard numbers, not warmth. Industrial archetype's monospace data-table aesthetic
maps to "I am evaluating fulfillment vendors against my P&L" — same mental
model as Red Stag and ShipMonk reviews on Reddit r/ecommerce.

We do NOT use the Direct archetype here — that's for UA/RU domestic CRO
landings where warmth and hero photo of warehouse converts. International
SMB buyers shopping for a 3PL want operating data first.

## WOW element
**"GROWTH_LADDER" same-partner narrative** — a monospace 4-step ladder showing
that one Ukrainian warehouse covers the entire SMB-to-mid-market journey:
- 01 CROWDFUND — 50–300 backers · Kickstarter + Indiegogo
- 02 SHOPIFY_LITE — 50–300 orders/mo · Etsy + Faire
- 03 SHOPIFY_PLUS — 300–3,000 orders/mo · native API
- 04 MARKETPLACE_EXPANSION — 1,000–30,000 orders/mo · 7 channels

The decision-relevant insight in three seconds: you do not need to migrate
3PLs at every brand-maturity stage. The global SMB pain is "outgrowing" a
fulfillment partner — switching from a basement to ShipBob, switching from
ShipBob to a contract 3PL, switching again at marketplace expansion. We
collapse all four stages into one pricing table, one WMS, one warehouse.

This avoids head-on collision with `/en/fulfilment-for-online-store/` (which
already owns the cost-anatomy comparison angle vs ShipBob/ShipMonk per
llms.txt). Different angle, different page.

## Stitch prompt (verbatim)
> Industrial brutalist landing-page hero for B2B small-business fulfillment.
> Pure black background. Single red accent #E63329. Editorial DM Serif Display
> headline: "Don't outgrow your 3PL. Outgrow your competitors." Monospace
> data table (JetBrains Mono UPPERCASE) titled GROWTH_LADDER on the right
> with 4 rows: 01 CROWDFUND (50-300 BACKERS · KICKSTARTER + INDIEGOGO),
> 02 SHOPIFY_LITE (50-300 ORDERS/MO · ETSY + FAIRE), 03 SHOPIFY_PLUS
> (300-3,000 ORDERS/MO · NATIVE API), 04 MARKETPLACE_EXPANSION (1,000-30,000
> ORDERS/MO · 7 CHANNELS). Sub-paragraph in DM Sans about same warehouse,
> same WMS, same partner across all four brand-maturity stages. Primary CTA
> "GET A QUOTE" red button (only rounded element). Below: 4-tile sticky
> manifest — $0 SETUP / $0 MONTHLY MIN / 14 DAYS CANCEL / $0.55→$0.42 PER
> ORDER. 2px red horizontal rules. No shadows. 90-degree edges.

## Variants

### Base — GROWTH_LADDER (default Industrial)
Editorial hero on the left ("Don't outgrow your 3PL. Outgrow your
competitors."), monospace GROWTH_LADDER table on the right with 4 brand-
maturity rows. 4-tile manifest below: $0 SETUP / $0 MONTHLY MIN / 14 DAYS
CANCEL / $0.55→$0.42 per order. Most balanced — closest to ShipBob and
ShipMonk editorial energy. **Lowest conversion friction** because the
ladder makes the value prop obvious in 3 seconds without any math from
the visitor. Risk: less aggressive than Variant B at undercutting
incumbents on price.

### Variant A — FOUNDER_LETTER (Editorial Memo)
Sidebar nav (LIVE_TIME_TRACK / MANIFEST_LOG / SHIPMENTS / FLEET_LOG /
TERMINAL) frames a typewritten memo aesthetic. The hero IS a letter:
"FROM: M. LIASHCHUK, TO: INTERNATIONAL DTC FOUNDERS, RE: WHY YOUR 3PL WILL
BREAK AT 1,500 ORDERS/MO." Body text reads like a McKinsey diagnostic —
"the standard fulfillment model is a house of cards built on shared
warehouses and legacy ERP systems." Right column has STAGED_ORDERS_PROTOCOL
table identical to GROWTH_LADDER but smaller. Sticky data manifest at
bottom + recent SHIPMENT_DATA_TX log table. **Highest authority signal**
because the page reads like a position paper, not a sales pitch. Risk:
slower to scan, higher reading-time bar, weaker for cold visitors who
need conversion in 8 seconds.

### Variant B — COST_PARITY_TABLE (Direct attack)
Same OPERATOR_042 chrome, but the right-side hero is a 5-row monospace
comparison table:
- MTP KYIV / UA — $0.58 per order + $0 platform = $58/mo
- RED STAG / TN — $3.45 per order + $0 platform = $345/mo
- SHIPBOB / IL — $3.85 per order + $0 platform = $480/mo
- SHIPMONK / FL — $3.45 per order + $150 platform = $495/mo
- SHIPHERO / NC — $2.95 per order + $1,995 platform = $2,290/mo

Headline: "Same fulfillment. 10× lower at the entry tier." Editorial
sub-paragraph explains the cost base — same WMS, same warehouse-management
discipline, lower input costs because we operate in Ukraine. **Highest
conversion bias for cost-sensitive comparison shoppers**, especially DTC
founders coming off Reddit r/shopify or r/ecommerce threads asking "why
is ShipBob so expensive at 100 orders/mo." Risk: invites a price-only
positioning, which can backfire if quality-conscious buyers assume cheap
= low quality.

## Recommendation
**Base — GROWTH_LADDER** — best balance of editorial clarity, conversion
focus, and unique angle that is structurally different from
`/en/fulfilment-for-online-store/` (cost-anatomy) and
`/en/fulfilment-for-marketplaces/` (single inventory pool). The
"don't-outgrow-your-3PL" narrative is proprietary — no US 3PL competitor
markets this way because most can't honestly claim coverage from
Kickstarter to marketplace expansion on the same pricing curve.

If the user wants to bias for **higher form-fill on cold paid traffic**,
fall back to **Variant B (COST_PARITY_TABLE)** — direct price attack
converts better at the top of the funnel.

If the user wants **brand authority and SEO depth for organic queries
like "best fulfillment for small business"**, fall back to **Variant A
(FOUNDER_LETTER)** — long-form memo style ranks better for
position-paper queries.

## Tri-color enforcement check
All three variants — strict #000 / #fff / #e63329. No gray fills, no
shadows, no rounded corners except primary CTA button. Pass.

## Avoiding collision with existing EN service hub

| EN page | Angle | Audience |
|---------|-------|----------|
| `/en/fulfillment-ukraine/` | EU access via Ukraine warehouse | Mid-market international |
| `/en/fulfilment-for-online-store/` | Cost-anatomy vs ShipBob/ShipMonk | Mid-market DTC |
| `/en/fulfilment-for-marketplaces/` | Single inventory pool, 5 channels | Multi-channel mid-market |
| `/en/fulfilment-for-small-business/` (NEW) | Same partner across 4 brand-maturity stages | SMB / DTC indie / Kickstarter |

Each page owns ONE angle. Small-business owns the growth-ladder narrative.

## Shared components map (when coding)
- `<HeroCTA>` — required (canonical hero form, lang="en", theme="dark",
  sourceTag="hero /en/fulfilment-for-small-business/")
- `<StatsBar>` for the 4-tile sticky manifest
- `<LabelChip>` for "FULFILLMENT FOR SMALL BUSINESS · ENGLISH-SPEAKING TEAM
  · UKRAINE" hero eyebrow
- `<AccordionGroup>` for FAQ section (12 Q/A targeting common SMB founder
  objections — minimum order, currency, returns, peak-season cancel
  windows, integration onboarding)
- `<DarkCTA>` for bottom inquiry section
- Custom: monospace GROWTH_LADDER block (page-specific .sb-ladder)
- Custom: 4-tier pricing table (page-specific) — reuse marketplaces tier
  patterns but rebuild with brand-maturity columns instead of channel
  columns

## Files
- `base.png` — default Industrial GROWTH_LADDER concept
- `variantA.png` — FOUNDER_LETTER editorial memo
- `variantB.png` — COST_PARITY_TABLE direct attack
- `concept.md` — this file

## Approval gate
Awaiting user choice: BASE / VARIANT A / VARIANT B / change something.
