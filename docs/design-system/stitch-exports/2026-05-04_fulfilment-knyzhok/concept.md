# Stitch Concepts — `/fulfilment-knyzhok/` Books & Publishers Pillar

**Date:** 2026-05-04
**Stitch project:** `15311340617405209890`
**Pipeline step:** STITCH PREVIEW (3) — awaiting user approval
**ADR:** `docs/design-system/pages/fulfilment-knyzhok.md`
**Keyword strategy:** `.claude-flow/research/fulfilment-knyzhok-keywords.json`

---

## 3 archetypes generated — one per language

| Archetype | Lang | Screen ID | Files |
|---|---|---|---|
| **A — Editorial** | RU | `d948bff339c44503a64219305df4273c` | `concept-a-editorial.png/.html` |
| **B — Direct** | UA | `62e98615bfb848acb2c4736adfc395f2` | `concept-b-direct-ua.png/.html` |
| **C — Industrial** | EN | `24b2abc3945141e9a9fed9ac3a6e032b` | `concept-c-industrial-en.png/.html` |

---

## Concept A — EDITORIAL (RU version)

**Visual signature:** warm off-white paper background (#fff8f7), large DM Serif Display headlines, generous whitespace, drop-caps, sharp 1px black borders, no shadows, no hero image. Magazine/literary aesthetic.

**Що видно на screenshot:**
- Hero без зображення — pure typography
- Ledger-style pricing table (sharp borders, ink-on-paper feel)
- Vertical 8-step timeline з великими serif numerals (01, 02...)
- 6-card problem grid у білих картках на cream background
- Dark red CTA "Запустіть фулфілмент книг за 21 день" footer

**Чому RU:** СНД publishers оцінять серйозність, типографічне резонування з книгами. Editorial — найменш agressive, найбільше "respect the reader" feel, що матчить очікування CIS B2B аудиторії.

**WOW-element:** "Ledger Pricing Table" — стилізована як accounting book

---

## Concept B — DIRECT (UA version)

**Visual signature:** full-width hero with photo backdrop + dark overlay, bold sans-serif (Inter Display 800), prominent red CTAs, large red "ISBN Live Counter" stat, red number indicators on problem cards, conversion-focused.

**Що видно на screenshot:**
- Dark hero з red overlay, badge top-left, white H1
- **Велика червона цифра "47" на чорному фоні** — ISBN Live Counter WOW element
- 6-card problem grid з bold red numbers (ISBN, AOV, SEPT, BOX, FEFO, NP)
- Pricing section на black background з red highlighted minimum row
- Red CTA card в hero на right side
- Bold red footer CTA "Запустіть фулфілмент книг за 21 робочий день"

**Чому UA:** Ukrainian audience reacts to action-oriented, conversion-focused. Direct mood — workhorse pattern для UA pillars (clothing уже працює). Cyrillic warmth + immediate phone capture.

**WOW-element:** "ISBN Live Counter — 47 тиражів через MTP цього місяця"

---

## Concept C — INDUSTRIAL (EN version)

**Visual signature:** split hero (text left, dark image right), uppercase tracked-out labels (letterSpacing 0.15em), Inter Display 800 weight, sharp 1px black borders defining everything, stats-bar horizontal strips, no shadows, "Industrial Brutalism" aesthetic.

**Що видно на screenshot:**
- Split hero — left white з H1 + stats bar, right dark book warehouse image
- **Cost Comparison Table** на black background (UKRAINE / USA / EU columns) — WOW element clearly visible
- 6-card "OPERATIONAL DISCIPLINE" grid з 1px black borders
- Horizontal step timeline з red number squares
- Industrial pricing table
- Dark red footer "DEPLOY BOOK FULFILLMENT IN 21 BUSINESS DAYS"

**Чому EN:** International publishers expect data-driven, ROI-focused, machine-precision feel. Industrial Brutalism = anti-decorative, "we mean business". Best for cost-comparison angle (key differentiator vs US/EU 3PLs).

**WOW-element:** "Per-order cost: Ukraine $0.41 vs US $1.50 vs EU $2.20" comparison table

---

## Three angles validated

Each concept візуально передає різний кут атаки контенту, не тільки візуальну варіацію:

| Element | Concept A (RU/Editorial) | Concept B (UA/Direct) | Concept C (EN/Industrial) |
|---|---|---|---|
| **Hero** | Pure typography, no image | Photo with overlay + CTA card | Split (text + dark image) + stats bar |
| **WOW element** | Ledger pricing table | ISBN Live Counter "47" | Cost comparison US/EU vs UA |
| **Tone** | Scholarly, respectful | Energetic, conversion-pushing | Data-first, enterprise B2B |
| **Audience message** | "Ми поважаємо вашу справу" | "Заповніть форму — порахуємо" | "Per-order economics that work" |
| **Page background** | Warm off-white #fff8f7 | White + dark sections | White + black/red enforcement |
| **Typography spirit** | Serif (DM Serif Display) | Sans (Inter Display 800 — bold) | Sans (Inter Display 800 — uppercase) |

---

## Keyword strategy alignment (per `.claude-flow/research/fulfilment-knyzhok-keywords.json`)

Each design accommodates language-specific primary keywords:

**RU (Editorial):** "фулфилмент книг" + "для издательств" мають бути в hero typography (no image distracts), pricing table H2 = "Сколько стоит фулфилмент книг" (ledger headline)

**UA (Direct):** "фулфілмент книги" + "для видавництв" в hero badge + H1, ISBN counter WOW supports "ISBN облік склад" secondary keyword

**EN (Industrial):** "book fulfillment Ukraine" + "publisher fulfillment Ukraine" в hero H1, cost comparison table directly answers "how much does book fulfillment cost in Ukraine" (AI Overview target)

---

## Validation question for user

**Approve all 3?** Each archetype matched to its language audience per ADR analysis:
- ✅ A → RU (Editorial = scholarly tone for CIS publishers)
- ✅ B → UA (Direct = conversion focus for Ukrainian e-com)
- ✅ C → EN (Industrial = data/ROI focus for international)

**Or reassign?** Якщо хочеш Industrial для UA замість Direct, чи Editorial для EN — кажи, переграю.

**Or refine specific?** Якщо подобається загалом але треба змінити деталь (background tint, hero image style, WOW element execution) — кажи що саме.

---

## Hard stop until approval

Per pipeline create-page.md step 2.5 + memory `feedback_create_page_pipeline.md` — НЕ переходжу до WRITER (step 4) без явного "approved" string.

Можливі відповіді:
- "approve all 3" → переходжу до WRITER (3 окремі angles per language)
- "approve A/B/C only, regenerate X" → перегенерую конкретний concept
- "reassign A→EN, C→RU" → переключу archetype-language mapping
- "refine B: change WOW to Y" → modify specific concept then re-show
