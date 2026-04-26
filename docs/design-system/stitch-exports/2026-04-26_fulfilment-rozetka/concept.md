---
date: 2026-04-26
slug: fulfilment-rozetka
archetype: industrial
status: pending-approval
stitch_project: 17546133288884555211
stitch_screens:
  base: ebd65713684649ada2275930829c0827
  variant_a: c81fb07b168a46e2a21ccfbc91959d01
  variant_b: 8c02ee817db14355917bdd6cdf9c839d
---

# Концепція: `/fulfilment-rozetka/` (UA + RU + EN)

## Архетип
**Industrial** (Swiss/Logistics Manifest) — high-contrast, sharp 0px corners,
typography-first, uppercase eyebrows. Reference: `/en/` home, EN pillar.

## Mood signals
- Eyebrow chip uppercase з letter-spacing 0.18em ("ФУЛФІЛМЕНТ ДЛЯ ROZETKA · СЕЛЕРАМ МАРКЕТПЛЕЙСУ")
- Display H1 з акцентом одного слова в червоному (`Альтернатива`)
- Тільки #e63329 / #000 / #fff — без сірого, тіней, заокруглень
- Stats bar з 4 KPI як основний візуальний якір (24 ГОД, 2-3 ДНІ, 0%, 4 СКЛАДИ)
- Marketplace logo strip під hero (Rozetka, Prom.ua, Kasta, Allo, Horoshop)

## WOW-елемент
Інтерактивна `<table class="rozetka-compare">` "Rozetka FBO vs MTP Group vs Власний склад" нижче по сторінці. 12 рядків:
категорії, комісія, multi-marketplace, контроль бренду, час підключення, мінімум,
SLA <30 хв, страхування, інтеграції, blackout-стійкість, прайс, повернення.
Червоні чекмарки в колонці MTP, чорні мінуси в колонці Rozetka FBO для
ексклюзивних позицій (меблі, габарит, вільне пакування etc).

## 3 варіанти hero (для approval)

### BASE — split 60/40 (текст + форма ліворуч, vertical stats bar праворуч)
- Hierarchy: eyebrow → H1 → sub → form → marketplace logos → "професійний фулфілмент..."
- ✓ Чітка ієрархія, форма у фокусі, stats — другий план
- ✓ Хороша мобільна адаптація (stack: text → form → stats)
- Ризик: 4 stats у вертикалі забирають правий простір — на мобайлі стане довгим скролом

### VARIANT A — full-width centered, stats у горизонтальній смузі під hero
- Hierarchy: eyebrow → centered H1 → sub → 4-col stats strip → form → logos
- ✓ Найбільш "монументальний" вигляд — H1 на повну ширину справляє враження
- ✓ Stats читаються як індустріальна стрічка (KPI dashboard)
- Ризик: форма далеко від hero — CR може просісти

### VARIANT B — split 60/40, форма ліворуч, 4 окремі картки stats праворуч
- Hierarchy: eyebrow → H1 → sub → form (left) | 4 white cards stack (right) → logos
- ✓ Stats виглядають як `<dl>` дата-модулі — кожен KPI самостійний блок
- ✓ Форма у тому ж horizontal lockup, що base
- Ризик: 4 картки стека — більше "boxiness" контр архетипу (No-Line rule)

## Рекомендація
**BASE** — найкраща збалансованість: форма видна одразу, stats читаються вертикально як warehouse dashboard, marketplace logos закривають hero як соціальне підтвердження. Industrial archetype забезпечений (uppercase, 0px, без тіней).

## Shared компоненти (Astro)
- `HeroCTA.astro` (lang/theme/sourceTag) — обов'язкова форма
- `LabelChip.astro` — uppercase eyebrows
- `StatsBar.astro` — 4 KPI
- `DarkCTA.astro` — bottom CTA
- `AccordionGroup.astro` — FAQ (12 пар)
- Custom: `.rozetka-compare__*` (BEM, page-specific) — comparison table

## Файли (URL Policy)
- UA: `src/pages/fulfilment-rozetka.astro` (root, без `/ua/` per H6 grandfather clause for new pages)
- RU: `src/pages/ru/fulfilment-rozetka.astro`
- EN: `src/pages/en/fulfillment-for-rozetka-sellers.astro`

## Hreflang quartet
```
uk → /fulfilment-rozetka/
ru → /ru/fulfilment-rozetka/
en → /en/fulfillment-for-rozetka-sellers/
x-default → /fulfilment-rozetka/
```

## Очікує approval від
@nikolay_mtp перед запуском АГЕНТА 3 (Writer).
