# Stitch concepts — `/fulfilment-dnipro/` Geo Stealth Landing

**Date:** 2026-05-05
**Stitch project:** `6907697812680848603`
**Pipeline step:** 3 STITCH PREVIEW (HARD STOP — awaiting user approval)
**Special class:** Geo-modifier landing — стелс (NOT in Header/Footer), funnel-out architecture

---

## Concept А — UA Direct (Map+Route signature)

- **Screen ID:** `5e9ef79435a94b1097fcf56278ca4870`
- **File:** `ua-direct-screenshot.png`
- **Audience:** Українські підприємці у Дніпрі (1М місто, 4-те за розміром UA)
- **Hero:** Темна мапа України з червоною лінією маршруту Київ→Дніпро. Бейдж "ФУЛФІЛМЕНТ · ДНІПРО · ДНІПРОПЕТРОВСЬКА ОБЛАСТЬ" → H1 "Фулфілмент для бізнесу з Дніпра — 1-2 дні через Нову Пошту" → HeroCTA форма (телефон + кнопка) → 3 inline stats.
- **WOW element:** **Route Timeline** — 5 пронумерованих червоних кружечків на тонкій чорній лінії: 14:00 (замовлення в WMS) → 17:00 (забір НП) → 22:00 (Полтава sortcenter) → 08:00 (Дніпро) → 10:00 (клієнт забирає).
- **Why Direct:** Geo-аудиторія хоче конкретну обіцянку часу + ціну швидко. Form above the fold.

## Concept Б — RU Direct (Cost-vs-Self Calculator signature)

- **Screen ID:** `2484769ff5f14701bf88fc9d69d25298`
- **File:** `ru-direct-screenshot.png`
- **Audience:** Російськомовні підприємці у Дніпрі (велика двомовна база)
- **Hero:** Centered text-first, БЕЗ split, БЕЗ мапи. Червоний chip → H1 "Когда выгодно закрыть склад в Днепре и перейти на Киев" → subline про 100+ замовлень/день threshold → CTA "Получить расчёт под мой объём →".
- **WOW element:** **Cost Comparison Block** — 2 колонки side-by-side на сірому: ліворуч "Свой склад в Днепре" (50,000₴ фіксовано + ризики), праворуч "Наш склад в Києве" (54,000₴ змінні, генератори+Starlink). Внизу червона смуга з точкою беззбитковості ~150-200 замовлень/міс.
- **Why DIFFERENT:** ROI-decision frame замість route promise. Фото warehouse worker на банері.

## Concept C — EN Industrial (Region Profile signature)

- **Screen ID:** `4c949c1550df4c75bbfd3fb73fc69cfc`
- **File:** `en-industrial-screenshot.png`
- **Audience:** International brands evaluating Eastern Ukraine market entry
- **Hero:** Split 60/40. Текст ліворуч ("Eastern Ukraine fulfillment from Kyiv hub — Dnipro region 3PL coverage"), industrial map праворуч (Dnipropetrovsk Oblast highlighted in red). Красна смуга-чип "FULFILLMENT · DNIPRO REGION · UA". CTA "Get pricing for Ukraine 3PL →".
- **Stats bar (4-col dark):** "3M" (population) / "1-2 days" (transit) / "$0.41" (cost) / "0 days" (downtime).
- **WOW element:** **Eastern Ukraine Industrial Profile** — 3-column data card grid:
  - DEMOGRAPHICS (Dnipro 1.0M / Kryvyi Rih 640K / Kamianske 240K, $720/month median)
  - E-COMMERCE PROFILE (4th largest e-com region, 24% NP preference, B2B distribution hub)
  - LOGISTICS COVERAGE (120+ NP branches, 250+ pick-up lockers, same-day pickup)

---

## Validation — "3 angles, not translations"

| Aspect | UA | RU | EN |
|---|---|---|---|
| Mood | Direct (warm route promise) | Direct (ROI decision) | Industrial (B2B regional context) |
| Hero comp | Full-width overlay + map | Centered text-first | Split 60/40 + map |
| Hero form | YES (phone+CTA) | NO (only CTA button) | NO (only CTA button) |
| Primary visual hook | Route Timeline (5 timestamps) | Cost Comparison (₴) | Region Profile cards |
| H1 angle | "1-2 дні через НП" (speed) | "Когда выгодно закрыть склад" (decision) | "Eastern Ukraine fulfillment" (regional context) |
| Section bg pattern | white→white→light gray | white→light gray→dark photo | white→dark stats→white cards |

UA, RU, EN мають **3 різні візуальні точки опори** (Route, Cost, Profile), хоча всі Direct/Industrial. Не translations.

---

## Geo-rules applied (per memory)

✅ **NOT in Header/Footer** (стелс)
✅ **Title contains "Дніпро/Днепр/Dnipro"** in all 3 langs (anti-cannibalization)
✅ **Hub-and-spoke from /ua/fulfilment-ukraina/** (NOT /poslugy/)
✅ **Funnel-out CTAs** to /ua/calculator/, /ua/tsiny/, /poslugy/, /komplektatsiya-zamovlen/
✅ **Word target lower** (1800-2000 vs 2700+ service pillars)
✅ **LocalBusiness address = Київський склад** (не вигадуємо Дніпровську адресу)

---

## Approval status

**HARD STOP — awaiting user response:**
- "approved" → proceed to Step 4 WRITER
- "змінити А|Б|C: [що саме]" → refine specific concept
- "повторити А|Б|C з іншим [layout/WOW]" → regenerate variant
