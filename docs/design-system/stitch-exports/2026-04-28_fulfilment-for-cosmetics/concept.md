---
page: /en/fulfilment-for-cosmetics/
archetype: Industrial
date: 2026-04-28
status: awaiting_approval
stitch_project_id: 12510886995608715072
---

# Cosmetics EN — Stitch Preview Concept

## Archetype: Industrial

International B2B audience (DTC beauty brands, indie lines, EU exporters). Same mood as `/en/` home and `/en/fulfilment-for-online-store/`. Authority + data + discipline — not a softer/feminine route.

## Mood signals

- Palette: `#000` background, `#fff` foreground, `#e63329` single-accent (3px vertical rules, ticker dots)
- Typography: DM Serif Display (display), DM Sans (body), JetBrains Mono (data ticker)
- Geometry: 0px radius, no gradients, no drop shadows, sharp corner stats grid divided by 1px hairlines
- Density: stats bar with 4 metrics, monospace data row, uppercase micro-labels

## WOW element

**FEFO ticker** — a thin monospace strip just below hero stats, scrolling batch-rotation data:

```
BATCH 2024-11-A · EXP 2026-05 · LANE 14 · QTY 3,420  →  BATCH 2024-12-B · EXP 2026-08 · LANE 22 · QTY 1,860  →
```

Signals operational discipline at a glance — the only thing that matters to a cosmetics brand owner: "do they actually rotate stock or just promise it." No competitor in UA does this.

## Stitch prompt (verbatim, base screen)

> Industrial archetype hero for "Fulfilment for Cosmetics" — international B2B beauty fulfillment landing. Dark monochrome (#000 background, #fff text, #e63329 single accent). Headline: "Stop guessing your batch dates. Start shipping cosmetics fresh." 3px red vertical rule left of headline. Subhead: "FEFO discipline, 18-22°C, 30-second pick. EU + Ukraine fulfillment for skincare, fragrance, and color brands." Stats bar 4 columns: "10+ YEARS" / "150+ CLIENTS" / "30 SEC PICK" / "18-22°C". Below stats: monospace FEFO ticker strip ("BATCH 2024-11-A · EXP 2026-05 · LANE 14 · QTY 3,420 →"). Below ticker: small "Technical Compliance" section with 4 chips — EU GMP-aligned / Lot tracking / Cold chain / Returns triage. Sharp corners, no gradients, no shadows. DM Serif Display + DM Sans + JetBrains Mono.

## 3 variants generated

1. **Base** (`screenshot-base.png`) — Full hero + stats + FEFO ticker + Technical Compliance chip row directly below. Most information-dense.
2. **Variant A** (`screenshot-variant-A.png`) — 50/50 split: headline + sub left, warehouse photo right. Stats moved to a separate row below the split. More photographic.
3. **Variant B** (`screenshot-variant-B.png`) — Magazine cover: massive "30 SEC" left as numeric anchor, headline right, full-bleed photo below, thin stats strip at the bottom. Most editorial of the three but still Industrial mood.

## Rationale

Industrial chosen over Direct because: (a) audience is international DTC/wholesale buyers who already know what fulfillment is — they want proof of discipline, not a calculator; (b) sibling EN pages (`/en/`, `/en/fulfilment-for-online-store/`) are Industrial — keeps the EN section coherent; (c) cosmetics is regulated category — Industrial conveys compliance better than Direct's hero-form pattern.

## Stitch IDs (for reference)

- Project: `12510886995608715072` — "MTP — Fulfilment for Cosmetics EN (Industrial archetype)"
- Base screen: `10eaecdef0404b9fb08958e963b2140d`
- Variant A: `33edc017c3f94652a17623700ae7adbf`
- Variant B: `640f4b06edbc472f8032f80c3b11e0a0`

## Decision needed

Which option proceeds to Writer + Design?
- **Base** — densest, ticker is the WOW
- **Variant A** — more photographic, splits attention with imagery
- **Variant B** — most editorial, "30 SEC" is the anchor

Reply with `approved base` / `approved A` / `approved B` (or describe changes).
