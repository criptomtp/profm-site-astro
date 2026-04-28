---
slug: fulfilment-prom
date: 2026-04-28
archetype: Editorial-Brutalist (нова варіація — НЕ повтор Rozetka)
status: pending-approval
stitch_project: 17546133288884555211
stitch_screens:
  base: e952b58a4901401d8a21e21a62c01b81
  variant_newspaper: c96ff4cd9d4f42e280cb527809ce8cab
  variant_calc_first: e783d6f4341e45a99e22547fb93cfb94
---

# /fulfilment-prom/ — Stitch concept (V2 — переробка після зворотного зв'язку)

## Чому переробляємо
Перша ітерація (Base + Contrarian + Live/Dark) = той самий шаблон що Rozetka:
**stats bar + lead-form справа + порівняння + pricing cards + dark CTA**.
Користувач справедливо помітив одноманітність останніх Stitch-сторінок.

## Що зламано в V2
1. **Прибрано stats bar з hero** — він уже на Rozetka, /en/, pillar.
2. **Прибрано форму справа в hero** — інша архетипова логіка кожному варіанту.
3. **Калькулятор-як-WOW** замість generic "діаграми потоку".
4. Усі варіанти мають принципово різну hero-DNA, не просто перефарбовані.

## WOW-елемент: Live FBO Calculator
Інтерактивний інструмент: користувач вводить кількість замовлень/міс → бачить:
- Скільки коштує робити самому (оренда + персонал + пакування + помилки)
- Скільки коштує MTP (фіксована тарифікація 18-27 ₴/замовлення)
- **Економія**: різниця у грошах + час, який звільняється
Це єдина сторінка в нашій лінійці з калькулятором-як-hero.

## Палітра
#e63329 / #000 / #fff. Без сірих градієнтів, без зайвих тонів.

---

## 3 варіанти на вибір

### Base — "Кінетичний маніфест" (Calculator + Massive 0)
- **Hero**: гігантський червоний "**0**" + "**FBO У PROM.UA / ...не існує. До сьогодні.**". Праворуч компактний калькулятор-картка з результатами економії.
- **Sections**: Cinematic warehouse photo з заголовком "РЕАЛЬНІ ЦИФРИ" (case study) → "ТАРИФІКАЦІЯ PRECISION" (порівняльна таблиця, не картки) → FAQ accordion → темний bottom CTA.
- **Tone**: Industrial-editorial. Цифри + типографіка + ритм.
- **Risk**: композиція "великий 0 + калькулятор" може здатися щільною на mobile.

### Variant N — "Newspaper Manifesto" ⭐
- **Hero**: повноекранна **чорна стрічка** з гігантським headline "**PROM МАЄ 700 000 ПРОДАВЦІВ І ЖОДНОГО ВЛАСНОГО FBO.**" — без зображень, без форми. Один тезис.
- **Sections**: окрема секція "FBO CALCULATOR" з widget'ом по центру на білому → "**THE CASE FOR DISRUPTION**" 3-колонкова газетна верстка з pull-quote → "PRICING TIERS" як 4 колонки tariff-картки (0 ₴ / 1.2k / 4.8k / TALK).
- **Tone**: серйозний op-ed, манифест-стайл. Близько до Stripe Atlas / NYT Opinion.
- **Risk**: "холодна" подача — хтось хоче CTA вище.

### Variant C — "Calculator-First / Tool" (з'явилася саме тому що сильно ламає шаблон)
- **Hero**: **КАЛЬКУЛЯТОР НА ВЕСЬ ЕКРАН** (без headline зверху) — слайдер обсягу, гігантський результат "**₴284,200.00**" (закреслений сірим) + червоний %22.4% економії%". Headline "**Scale with the Kinetic Force of Precision Logistics**" з'являється ПІД калькулятором.
- **Sections**: 3 нумеровані chapters (01 / 02 / 03) з гігантськими номерами → "**Case Study**" як інфографіка з 3-х панелей (warehouse photo + +240% / 0.002% defects / 99.8%) → мінімалістичний червоний CTA-band з одним рядком "**Підключити склад →**".
- **Tone**: tool-first, utility, "calculator before copy".
- **Risk**: відсутність emotional headline у hero — для холодного трафіку з SEO може бути недостатньо контексту.

---

## ✅ ФІНАЛЬНЕ РІШЕННЯ — три варіанти на три мови (approved 2026-04-28)

Користувач запропонував елегантне рішення: оскільки CLAUDE.md вимагає що UA/RU/EN мусять
бути різними кутами атаки (а не перекладами), використовуємо **різний дизайн на кожну мову**.
Це автоматично гарантує що сторінки не виглядають одна як одна, і дизайн відображає психологію
кожної аудиторії.

| Мова | Варіант | Архетип | Кут атаки |
|------|---------|---------|-----------|
| **UA** | **Base** "Кінетичний маніфест" (масивний 0) | Editorial-Brutalist provocative | Емоційно-провокативний. Українські підприємці у Prom добре реагують на bold-заяви. Calculator як інструмент-картка. Cinematic warehouse photo. |
| **RU** | **Variant C** "Calculator-First / Tool" | Utility / tool-first | Раціональний СНД-бізнес (Казахстан/Молдова/Грузія + рускомовні в Україні). Цифри-цифри-цифри, мінімум маркетингу. Калькулятор НА ВЕСЬ ЕКРАН — для тих хто рахує гроші перш за все. |
| **EN** | **Variant N** "Newspaper Manifesto" | Editorial / op-ed | Західна аудиторія, серйозний бізнес-tone. "Ukraine has 700K Prom sellers and zero native FBO." Газетна верстка, pull-quotes, 4-колонкові tariffs — vibe Stripe Atlas / NYT Opinion. Data-driven, ROI-focused. |

## Why this mapping
- **UA = Base**: український ринок Prom — імпульсивний, mobile-first, провокаційні headlines працюють (див. наш досвід з Rozetka).
- **RU = Variant C**: рускомовний СНД ринок дуже tool-orientovaniy — калькулятор як hero має конверсійну перевагу. Меньше "чому" і більше "скільки".
- **EN = Variant N**: міжнародні бренди шукають вагомий контентний виклад. Op-ed формат + газетна верстка створює "publication-grade" довіру.

Це створює унікальну ситуацію — **на кожній мові сторінка виглядає принципово інакше**, що, окрім UX-переваги, є SEO-знахідкою (різні візуальні entity, різна структурна семантика на DOM рівні → диференціація hreflang-кластера).

---

## Наступні кроки (Agent 3 → Writer)
1. UA: `src/pages/fulfilment-prom.astro` — Base дизайн (масивний 0 + калькулятор), 1500+ слів, провокативний UA tone
2. RU: `src/pages/ru/fulfilment-prom.astro` — Variant C дизайн (calculator-as-hero), 1500+ слів, утилітарний RU tone
3. EN: `src/pages/en/fulfilment-prom.astro` — Variant N дизайн (manifesto headline + 3-col newspaper), 1500+ слів, editorial EN tone
