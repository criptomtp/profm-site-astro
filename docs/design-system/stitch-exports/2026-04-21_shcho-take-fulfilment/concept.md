---
page: Pillar — What is Fulfillment
url_ua: /ua/shcho-take-fulfilment/
url_ru: /ru/chto-takoe-fulfilment/
url_en: /en/what-is-fulfillment/
archetype: Editorial
stitch_project: 568924337125736683
generated: 2026-04-21
status: awaiting-approval
---

# Pillar page: "Що таке фулфілмент"

## Archetype
**Editorial** — long-form knowledge hub with category nav, no traditional hero image on base version, big typography, deep internal linking to all service/industry/geo subpages.

## Color palette (strict)
- `#e63329` — red accent
- `#000000` — black
- `#ffffff` — white
- Нічого іншого.

## Typography
- Headlines: **DM Serif Display** (editorial serif)
- Body / labels: **DM Sans** (geometric sans)

---

## Три варіанти для вибору

### Option 1 — BASE (`screenshot-base.png`)
**Що це**: стандартний editorial layout — великий headline, одна колонка контенту, блок "Як працює фулфілмент" з нумерованими кроками, calculator-preview блок, FAQ accordion, темний CTA в кінці.

**Плюси**: чистий, класичний FAQ-стиль (як `/en/faq/`), легко читається на мобілі.
**Мінуси**: нічого WOW — звичайний блог, не pillar.

---

### Option 2 — VARIANT A: "Sticky Sidebar TOC" (`variant-A-sticky-toc.png`)
**Що це**: hero з масивним editorial headline ліворуч + червоний chip `PILLAR GUIDE` над ним; праворуч — вертикальний sticky зміст з 8 розділами (01–08), який залишається видимим при скролі. Одразу під hero — **Blackout Resilience Panel**: чорна стрічка на всю ширину з білим написом `3 generators + Starlink = 0 downtime`. Нижче — блок "Тактика роботи" з нумерованими картками.

**WOW-елемент**: **Blackout Resilience Panel** — єдиний в своїй ніші blackout-proof claim, жирно винесений у hero зоні.

**Плюси**:
- Sticky TOC перетворює довгу статтю на навігаційний hub (ключова user потреба для pillar page).
- Blackout panel — унікальна конкурентна перевага, якої нема в 8/10 конкурентів.
- 8 categories TOC = 8 гачків для internal links на service/industry сторінки.

**Мінуси**: на мобілі TOC треба тримати як горизонтальний pill-bar зверху (зайвий код).

---

### Option 3 — VARIANT B: "Split Diptych" (`variant-B-diptych.png`)
**Що це**: hero розділений на дві рівні колонки — ліва чорна з білим серифним заголовком `Фулфілмент — це`, права біла з фото складу і накладеними data-картками (сканування, WMS, 4 забори/день). Під hero — горизонтальний sticky pill-bar з 8 категоріями. В середині сторінки — **Myth vs Reality grid**: 4 червоні картки міфів перевертаються на hover у чорні картки з реальністю.

**WOW-елемент**: **Myth vs Reality** interactive grid — усуває 4 основні заперечення (ціна, втрата контролю, складна інтеграція, для великих only) у візуальній формі.

**Плюси**:
- Дуже кінематографічний hero з фото складу = моментальний visual proof.
- Myth vs Reality — ідеальний CRO-хід у середині довгого тексту (утримує scroll).
- Horizontal pill-bar добре адаптується на мобілі.

**Мінуси**: складніший код (hover flip + sticky pill + overlay cards), +20% часу на реалізацію.

---

## Моя рекомендація: **Variant A — Sticky Sidebar TOC**

**Чому**:
1. **Sticky TOC** — це найпотужніший UX-патерн для pillar page (він буквально комунікує "це hub з розділами", а не блог).
2. **Blackout Resilience Panel** — унікальна перевага MTP, яку ніхто з конкурентів не підсвічує. Ставимо її ODRAZU в hero зону, а не на page 3.
3. Технічно простіше: sticky position + chapters linkable через `id=` anchors. Жодних hover flip магій.
4. SEO: TOC з 8 anchor links = готова структура для Google sitelinks в SERP.

**Fallback**: якщо тобі не зайде sticky TOC — беремо Variant B з Myth vs Reality (теж сильний CRO-хід).

---

## Structure (для всіх 3 опцій однакова — міняється тільки hero):

1. **Hero** (варіює A/B/Base)
2. **Stats bar**: 150+ клієнтів · 60 000 відправок/міс · 0 простоїв з 2022 · 10 років
3. **Розділ 01 — Що таке фулфілмент простими словами** (визначення, 3PL vs own warehouse у 2-3 реченнях, коли потрібен)
4. **Розділ 02 — Як працює фулфілмент: 8 кроків** (приймання → сканування → зберігання → комплектація → упаковка → маркування → передача → обробка повернень)
5. **Розділ 03 — Хто наш клієнт** (інтернет-магазини від 100 замовлень/міс, маркетплейс-продавці, D2C бренди; cross-link на industry pages)
6. **Розділ 04 — Скільки коштує** (структура тарифу: зберігання + комплектація + повернення; живий приклад 500 замов/міс; cross-link на `/calculator/`)
7. **Розділ 05 — Фулфілмент vs власний склад** (таблиця: інвестиція, час запуску, масштабованість, ризик; cross-link на `/fulfillment-vs-own-warehouse/`)
8. **Розділ 06 — Як обрати оператора** (7 критеріїв, cross-link на порівняння операторів)
9. **Розділ 07 — Типові помилки при переході** (5 помилок, cross-link на `/peak-season-logistics-mistakes/`)
10. **Розділ 08 — FAQ** (12 питань, accordion, schema.org FAQPage)
11. **Dark CTA**: "Готові перевести логістику на автопілот?" → розрахунок + контакт

## Internal links (мінімум 15 з pillar)
Services: `/ua/service/`, `/ua/fulfillment-for-marketplaces/`, `/ua/bulk-fulfillment/`
Industries: `/ua/fulfillment-for-clothing/`, `/ua/fulfillment-for-cosmetics/`, `/ua/fulfillment-for-baby-products/`
Tools: `/ua/calculator/`, `/ua/price/`, `/ua/contact/`
Content: `/ua/blog/fulfillment-vs-own-warehouse/`, `/ua/blog/what-is-fulfillment-7-services/`, `/ua/blog/peak-season-logistics-mistakes/`

## 301 redirects (обов'язково)
- `/ua/blog/scho-take-fulfilment/` → `/ua/shcho-take-fulfilment/`
- `/blog/chto-takoe-fulfilment/` → `/ru/chto-takoe-fulfilment/`
- `/en/blog/post/what-is-fulfillment-complete-guide/` → `/en/what-is-fulfillment/`

## Очікується від тебе
Скажи одне з трьох:
- **"approved A"** (Sticky Sidebar TOC — моя рекомендація)
- **"approved B"** (Split Diptych з Myth vs Reality)
- **"approved base"** (класичний editorial без WOW)

Або: опиши що поміняти — згенерую нові варіанти.
