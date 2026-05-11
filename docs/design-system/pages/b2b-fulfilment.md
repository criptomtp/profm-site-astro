# ADR — `/b2b-fulfilment/` B2B Fulfillment Pillar

**Date:** 2026-05-11
**Status:** ANALYZER complete, awaiting STITCH approval
**Type:** Service pillar (semantic core #30, 🟠 priority)
**Pipeline trigger:** `/create-page b2b фулфілмент`

---

## Strategic context

**Different buyer persona from B2C pillars.** B2B audience = wholesaler / distributor / brand-to-retailer. AOV 5,000-50,000₴ (vs B2C 300-1500₴). Multi-SKU pallet pick. Document flow (рахунок-фактура, видаткова, ЕДО). 1С/BAS integration critical.

GSC signal: page already has temp redirect `/b2b-fulfilment/` → `/ua/fulfilment-ukraina/` (commit `edbabae`) because Google was hitting 404 — demand confirmed.

---

## Word count targets

- UA competitor avg: ~1500 (1 of 6 has dedicated B2B page) → **target ≥2700**
- RU avg: thin (CIS market entry niche uncontested) → **target ≥2700**
- EN avg: 2000-2500 (US ShipBob/Red Stag well-developed) → **target ≥2900**

---

## Archetype decision — DIFFERENT per language

### 🇺🇦 UA — Industrial mood (B2B is data-driven, decision-framework)

- **Audience:** UA дистриб'ютори, оптовики, бренди з виробництвом
- **Hero:** Split 60/40 — text left, photo of pallet storage row + 1С dashboard mockup right
- **WOW-element:** **"B2B vs B2C comparison matrix"** — taxonomy table показуючи різниці (AOV, pick unit, document flow, integration, delivery)
- **Reference:** `/komplektatsiya-zamovlen/` UA Direct + Industrial elements

### 🇷🇺 RU — Direct mood (CIS brand entry, ROI decision)

- **Audience:** CIS-бренди з косметики/одягу/харчування що виходять на UA через дистриб'юторів
- **Hero:** Centered text-first — "Из Казахстана/Молдовы/Грузии в украинскую розницу через наш склад"
- **WOW-element:** **"4 CIS country flows"** — KZ cosmetics → AS-IS UA retail, MD wine → Silpo, GE fashion → INTERTOP, UZ textile → ATB
- **Reference:** `/ru/fulfilment-dnipro/` Direct with CIS focus

### 🇬🇧 EN — Industrial mood (international brand B2B)

- **Audience:** US/EU brands selling wholesale into Ukraine via distributors
- **Hero:** Split + industrial map of Ukrainian retail chain coverage
- **WOW-element:** **"Cost matrix"** — Ukraine 3PL B2B vs US/EU baseline per pallet/month
- **Reference:** `/en/order-pick-and-pack-ukraine/` Industrial

---

## Anti-cannibalization plan

5 potential conflict pages — see `b2b-fulfilment.json` for details. Key rule: **"B2B" keyword in first 30 chars of title/H1/lede.** Bare "фулфілмент" without B2B context = negative keyword.

---

## Schema requirements

- Service.serviceType: "B2B Wholesale Fulfillment Ukraine"
- audience.BusinessAudience.name: explicit B2B (distributors, wholesalers, brand-to-retailer)
- Standard 9 must-have @types
- 1C/BAS integration mention in description

---

## Hub-and-spoke wiring

- **Hub:** `/poslugy/` (services hub) — add B2B card
- **Sibling spokes:** `/komplektatsiya-zamovlen/`, `/ua/skladski-poslugy/`, `/ua/fulfilment-vazhkykh-tovariv/`
- **Critical post-deploy:** **REMOVE temp redirect** `/b2b-fulfilment/ → /ua/fulfilment-ukraina/` from `_redirects` (lines 578-580)
- Header mega-menu: ADD to col1 "По типу бізнесу"

---

## Next step

STITCH PREVIEW — 3 concepts. **HARD STOP** until user approval.
