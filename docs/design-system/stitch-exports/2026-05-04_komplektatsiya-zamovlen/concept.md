# Stitch concepts — `/komplektatsiya-zamovlen/` Pick & Pack spoke

**Date:** 2026-05-04
**Stitch project:** `18339893869506539502`
**Pipeline step:** 2.5 STITCH PREVIEW (HARD STOP — awaiting user approval)

---

## Concept A — UA Direct (Concept А)

- **Screen ID:** `07a5c7e1199e437ca2287af64e62e09a`
- **File:** `ua-direct-screenshot.png`
- **Archetype:** Direct (warm, conversion-first)
- **Hero:** Full-width dark image of warehouse picker with scanner. Red badge "PICK & PACK · УКРАЇНА" → H1 "Комплектація замовлень — 47 секунд, 99,5% точності" → hero CTA form (phone + red button) → 3 inline stats.
- **WOW element:** "Live Pick Speed Counter" — 3 huge red numbers on white: 47 / 99,5% / 18 грн.
- **Why:** UA buyer wants to act fast. Form above the fold. Warmth + immediacy.
- **Prompt rationale:** Mirrors `/fulfilment-knyzhok/` Direct mood and `/fulfilment-dlya-odyahu/` precedent.

## Concept B — RU Industrial (Концепт Б)

- **Screen ID:** `26921801d748467c9a546a7ec674e9ea`
- **File:** `ru-industrial-screenshot.png`
- **Archetype:** Industrial (data-driven, B2B confidence)
- **Hero:** Top red band "PICK & PACK / УКРАИНА 2026" → split 60/40: text-left ("Сборка заказов из Украины — 47 секунд, 99,5% точность, $0.41 за заказ") + warehouse picker photo right.
- **Stats bar:** 4-column dark `#0a0a0a` band — 47 / 99,5% / $0.41 / 60 000.
- **WOW element:** 8-step horizontal Process Flow (01 ПРИЁМ → 02 WMS-МАРШРУТ → 03 PICKER SCAN → 04 VERIFY → 05 УПАКОВКА → 06 QC → 07 ЯРЛЫК → 08 КУРЬЕР) on light grey.
- **Why:** CIS publisher buyer (Беларусь/Молдова/Казахстан) wants depth + process proof + formal tone. NO form in hero — depth-first conversion.
- **Prompt rationale:** Mirrors `/en/index.astro` Industrial archetype, applied with formal Russian for CIS-Ukraine outbound positioning.

## Concept C — EN Industrial (Concept C)

- **Screen ID:** `876ce711d0474297b729c2fbe572f38d`
- **File:** `en-industrial-screenshot.png`
- **Archetype:** Industrial (ROI-focused)
- **Hero:** Top red band "ORDER PICK & PACK · UKRAINE 3PL · 99.5% ACCURACY" → split 60/40: H1 "Order Pick and Pack Ukraine — 99.5% Accuracy at $0.41 per Order" + picker photo.
- **Stats bar:** 4-column dark — 47s / 99.5% / $0.41 / 60K.
- **WOW element:** Cost-vs-Accuracy 3-column comparison table — UKRAINE (MTP) | US 3PL | EU 3PL — with MTP column highlighted by red left-border. Rows: cost per order, pick accuracy, scan stages, QC checkpoint, turnaround time.
- **Why:** International B2B buyer wants cost-vs-quality framing. Table delivers the punchline ($0.41 vs $1.50 baseline).
- **Prompt rationale:** Same archetype as RU but DIFFERENT WOW (comparison table vs process flow) — proves "3 angles not translations" rule.

---

## Validation — "3 angles, not translations"

| Aspect | UA | RU | EN |
|---|---|---|---|
| Mood | Direct (warm) | Industrial (formal) | Industrial (ROI) |
| Hero form | YES (above fold) | NO (CTA button only) | NO (CTA button only) |
| Layout | Full-width overlay | Split 60/40 + top red band | Split 60/40 + top red band |
| WOW | Live Counter (3 numbers) | 8-step Flow Diagram | Cost Comparison Table |
| H1 hook | "47 секунд, 99,5%" (speed) | "47 секунд, 99,5%, $0.41" (data) | "99.5%, $0.41" (cost) |
| Closing angle | Conversion / 15-хв quote | Process transparency / CIS | Cost vs US/EU |

UA and RU/EN have fundamentally different hero structures (overlay vs split). RU and EN share archetype but DIFFERENT WOW elements (process flow vs comparison table).

---

## Approval status

**HARD STOP — awaiting user response:**
- "approved" → proceed to Step 4 WRITER
- "змінити X" → refine specific concept
- "повторити Y" → regenerate variant
