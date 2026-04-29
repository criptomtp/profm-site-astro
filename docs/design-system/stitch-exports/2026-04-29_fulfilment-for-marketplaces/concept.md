---
slug: fulfilment-for-marketplaces
language: EN
target_url: /en/fulfilment-for-marketplaces/
archetype: Industrial
date: 2026-04-29
stitch_project: projects/3159947887984056947
status: pending_approval
---

# Concept — Marketplaces EN landing page

## Target audience
International B2B brands (US/UK/EU/AU DTC and SMB) entering Eastern European
markets via multiple Ukrainian marketplaces (Rozetka, Prom.ua, Kasta) plus
Shopify EU and Amazon EU on a single Ukrainian inventory pool.

## Why Industrial archetype
Western buyers comparing 3PLs are running a procurement evaluation, not a
brand discovery. The page must communicate operational rigor (WMS, real-time
inventory pool, integrations) more than warmth. Industrial archetype's
aesthetic — uppercase JetBrains Mono labels, 2px red rules, dark void
background, monospace data tables — matches the "logistics control room"
mental model these buyers expect from sites like ShipBob, ShipMonk and
Red Stag Fulfillment.

## WOW element
**"Single Inventory Pool" live ticker** — a monospace table that displays the
exact same SKU count across all five sales channels (ROZETKA, PROM.UA, KASTA,
SHOPIFY EU, AMAZON EU). The visual makes one decision-relevant fact obvious
in three seconds: a brand does not need to split inventory by channel; one
warehouse, one pool, five storefronts. This is the structural advantage of
Ukraine as a multi-marketplace hub vs single-channel-only fulfillment.

## Stitch prompt (verbatim)
> Industrial brutalist landing-page hero for B2B marketplace fulfillment SaaS.
> Pure black background. Single red accent color #E63329. Editorial DM Serif
> Display headline: "One inventory. Five marketplaces. Zero duplicate stock."
> Monospace data ticker (JetBrains Mono UPPERCASE) showing 5 rows: ROZETKA.UA,
> PROM.UA, KASTA, SHOPIFY EU, AMAZON EU — each with the SAME SKU count to
> visualize "single inventory pool". 2px red horizontal rules. Sub-paragraph
> in DM Sans about real-time stock reconciliation across all channels.
> Primary CTA "GET A QUOTE" red button (only rounded element). Sticky data
> manifest below with 4 KPI tiles. No shadows. 90-degree edges.

## Variants

### Base (default Industrial brutalism)
Editorial hero on the left ("One inventory. Five marketplaces. Zero duplicate
stock."), monospace LIVE_INVENTORY_POOL ticker on the right showing all 5
channels at the SAME SKU count. Stats strip below: # operators, # SKUs, # avg
sync time, # uptime. Three feature cards (DYNAMIC INTEGRATION, ERROR
ISOLATION, UNIFIED API). Warehouse photo strip at the bottom. Most balanced,
closest to ShipBob editorial energy.

### Variant A — Structural Flip ("FULFILLMENT_OS" Control Room)
Sidebar nav (COMMAND / MANIFEST / INVENTORY / NODES / REPORTS) frames a
SaaS-dashboard-style hero. Inventory manifest table is horizontal across the
top with 5 marketplace cells. OPERATIONAL_INQUIRY form is centered and big —
it dominates the conversion zone. NODE_NETWORK card on the right.
KPI tiles 99.4% / 45m / 24H at the bottom. Reads like the brand IS a
software product, not a service vendor. **Higher conversion bias** because
the form is enormous and the CTA is unmissable. Risk: looks more like a
SaaS marketing page than a 3PL landing.

### Variant B — Logistics Map (Network Topology)
Same FULFILLMENT_OS chrome, but the right-side hero is a network diagram:
KYIV WAREHOUSE as the central red dot, with red dashed lines branching to
ROZETKA, PROM, KASTA, AMAZON EU, SHOPIFY EU nodes. Each node shows its stock
count. Form is INITIALIZE_SYNC. **Highest information density**, most
"Ukraine as a hub" visualization. Risk: form is smaller and less
conversion-optimized than Variant A.

## Recommendation
**Base** — best balance of editorial clarity, conversion focus and
proprietary "single inventory pool" WOW. Variant A is more aggressive on
conversion but reads SaaS, not 3PL. Variant B has the strongest hub
visualization but underperforms on the form.

If the user wants to bias for higher form-fill, fall back to Variant A.
If the user wants to lean into "Ukraine as a marketplace hub" narrative,
fall back to Variant B.

## Tri-color enforcement check
All three variants — strict #000 / #fff / #e63329. No gray fills, no shadows,
no rounded corners except primary CTA. Pass.

## Shared components map (when coding)
- `<HeroCTA>` — required (canonical hero form, lang="en", theme="dark",
  sourceTag="hero /en/fulfilment-for-marketplaces/")
- `<StatsBar>` for the 4-tile KPI strip
- `<LabelChip>` for "STEP / SECTION" uppercase tags
- `<AccordionGroup>` for FAQ section
- `<DarkCTA>` for bottom inquiry section
- Custom: monospace inventory pool ticker (page-specific .mp-pool block)
- Custom: marketplaces grid with logos + features (page-specific)

## Files
- `base.png` — default Industrial concept
- `variantA.png` — Structural Flip / Control Room form-led
- `variantB.png` — Logistics Map / network topology
- `concept.md` — this file

## Approval gate
Awaiting user choice: BASE / VARIANT A / VARIANT B / change something.
