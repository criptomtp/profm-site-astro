---
slug: fulfilment-for-online-store (EN-only)
date: 2026-04-28
archetype: Industrial
language: EN (no UA/RU triplet — UA + RU already exist as siblings at /ua/fulfilment-dlya-internet-magazynu/ + /ru/...)
target audience: International DTC ecommerce founders, Shopify/WooCommerce store owners, EU/US brands entering Ukraine
target keyword: "fulfillment for online store" / "ecommerce fulfillment Ukraine"
hreflang siblings:
  - uk: /ua/fulfilment-dlya-internet-magazynu/ (UPDATE pointing here)
  - ru: /ru/fulfilment-dlya-internet-magazynu/ (UPDATE pointing here)
  - en: /en/fulfilment-for-online-store/ (NEW)
  - x-default: /ua/fulfilment-dlya-internet-magazynu/
---

# Concept — `/en/fulfilment-for-online-store/`

## Strategic angle

This is **NOT** the same as `/en/fulfillment-ukraine/` (geo-anchored, "why Ukraine?") or `/en/fulfilment-prom/` (marketplace-vertical, Prom.ua-specific) or `/en/fulfillment-for-rozetka-sellers/` (marketplace-vertical, Rozetka).

The angle here is **store-vertical**: "you run a Shopify/WooCommerce/OpenCart store, here's why MTP fits". The differentiator is **price as the lead**: $0.41/order vs ShipBob $1.50, Red Stag $2.50, US average $5+.

## Competitor research summary

| Provider | Per-order rate | Storage | Notes |
|----------|----------------|---------|-------|
| ShipBob | $0.99-1.50 + line items | $8-12/cu ft/yr | Most popular DTC 3PL, US-based |
| Red Stag | $2-3 + line items | negotiable | Heavy/bulky specialist |
| ShipMonk | $4-6 base | tiered | DTC-focused, growing fast |
| US average | $5-8 all-in | $0.45-0.75/cu ft/mo | Multi-line bills typical |
| **MTP Group** | **$0.41 all-in** | **~$15/m³/mo** | Single-line all-in pricing |

Source: bettamax, redstagfulfillment.com, fulfillrite.com, ecomautoprep, ShipBob direct.

EU 2026 changes: €150 duty de minimis is being phased out — 5.8B low-value parcels affected. This creates tailwind for **local-fulfillment-in-target-market** plays (the angle MTP can lean on for EU brands selling INTO Ukraine).

## WOW element — "COST ANATOMY"

Hero shock: massive typographic price treatment of **$0.41** rendered in DM Serif Display at ~16-22vw, dominating left half. Tiny superscript "$" sign + huge "0.41" in tight tracking.

Below hero: **"What's NOT in your $0.41"** comparison — strips line items US/EU 3PLs charge separately:
- Pick fee · Pack fee · Each-additional-item · Box · Storage tier upgrade · Returns · Account fee → totals $5.05+
- vs MTP: single line, "Pick + pack + box + label + Nova Poshta dropoff" → $0.41

This pattern is **distinct** from already-shipped EN pages:
- `/en/fulfilment-prom/` Variant N (newspaper manifesto)
- `/en/fulfillment-for-rozetka-sellers/` (split-hero workflow)
- `/en/fulfillment-ukraine/` (dark-hero stats)

## Stitch options generated

All 4 screens use the project "MTP Fulfillment Redesign" (id 17546133288884555211) which is already locked to:
- Primary #e63329 (red), neutrals #000/#fff/#f3f3f3
- DM Serif Display + DM Sans
- Industrial archetype tokens (sharp 90deg corners, no shadows, tonal layering)

### `screen-base.png` — **MASSIVE $0.41 (RECOMMENDED)**
- Hero: huge serif "$0.41" left, form + headline right
- Stats bar after hero
- Cost-anatomy comparison block
- Most direct execution of the brief

### `variant-A-tabular.png` — TABULAR MANIFEST
- Hero: small "lowest per-order rate in Europe" headline
- Provider comparison table is the hero centerpiece (ShipBob, Red Stag, ShipMonk, MTP rows)
- MTP row in red
- Form on right
- More understated, more "data-table-as-hero"

### `variant-B-monolith.png` — BLACK MONOLITH
- Full black background hero, white "$0.41"
- B&W warehouse motion-blur image with subtle red tint
- White form floating over black
- Highest visual contrast — most cinematic

### `variant-C-receipt.png` — SPLIT ORDER RECEIPT
- Hero left half is a stylized "shipping label / order receipt"
- Right half: "Engineering-grade fulfillment" headline + form
- Receipt has dotted-leader line items, status: PENDING/SHIPPED, etc.
- Most editorial-feeling, but $0.41 price not the visual lead

## Recommendation

**`screen-base.png`** is the strongest because:
1. The $0.41 price IS the value proposition — it deserves to be the visual hero
2. International audiences scan first, read second — a typographic price is instant cognitive hook
3. Cost-anatomy section below pays off the hero promise (how can it be that low?)
4. Differentiated from Prom (red 0 letter as decorative element) and Rozetka (workflow-split) and Ukraine page (dark stats)

**Variant A** is fallback if user feels the giant $0.41 is "too aggressive" — table is more polite.

**Variant B** could be reserved for a future `/en/enterprise/` or B2B page (too heavy for ecommerce SMB audience).

**Variant C** is editorial-fun but buries the price — ditch.

## Approval needed before writing code

User must say "approved" + which option (base / variant-A / variant-B / variant-C) before AGENT 3 (Writer) starts. Default = base.

## File locations

- `screen-base.png` — recommended option
- `screen-base.html` — Stitch raw HTML (reference only — DO NOT copy into .astro)
- `variant-A-tabular.png` — alternative
- `variant-B-monolith.png` — alternative
- `variant-C-receipt.png` — alternative
