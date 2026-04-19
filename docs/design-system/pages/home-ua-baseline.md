---
slug: /ua/ (homepage)
file: src/pages/index.astro
archetype: Direct
mood: Direct
baseline_date: 2026-04-19
redesign_branch: redesign/ua-home-20260419
---

# Baseline — /ua/ home

## SEO-freeze (зберегти дослівно у редизайні)

- **URL:** `https://www.fulfillmentmtp.com.ua/`
- **Canonical:** `https://www.fulfillmentmtp.com.ua/`
- **Language:** `uk`
- **Title:** `Фулфілмент від 18 грн — MTP Group | 150+ клієнтів, 10 років` (60 симв)
- **Description:** `Фулфілмент від 18 грн/замовлення. Приймання, зберігання, пакування, доставка. 10 років, 150+ клієнтів, 2 склади, безперебійний 24/7.` (158 симв)
- **H1:** `Фулфілмент для інтернет-магазинів. Від 18 грн за відправку.`
- **Primary keywords у body:** фулфілмент, інтернет-магазин, від 18 грн, Київська область, 150 клієнтів, 10 років, склад, WMS, Нова Пошта
- **Hreflang:**
  - `uk` → `https://www.fulfillmentmtp.com.ua/`
  - `ru` → `https://www.fulfillmentmtp.com.ua/ru/`
  - `en` → `https://www.fulfillmentmtp.com.ua/en/`
  - `x-default` → `https://www.fulfillmentmtp.com.ua/`
- **Schema.org (перенести дослівно):**
  1. `LocalBusiness` (MTP Group Fulfillment, адреси, рейтинг 4.9, тел +380501444645)
  2. `WebSite` (Фулфілмент для інтернет-магазинів у Київській області)
  3. `FAQPage` — 7 питань (що таке фулфілмент, ціни, як почати, блекаути, маркетплейси, терміни доставки, мінімальний обсяг)

## Baseline метрики

### PageSpeed
- **Mobile / Desktop:** ❌ NOT CAPTURED — PageSpeed API daily quota exceeded (2026-04-19)
- **Дія:** повторно зняти baseline ДО деплою нового коду через 24 години (коли квота скинеться), або через локальний Lighthouse CLI

### GSC / GA4
- **GSC positions for primary keywords:** ⚠️ не знято через поточну сесію (потребує WebFetch авторизації)
- **GA4 form CR / bounce / scroll 75%:** ⚠️ не знято
- **Дія:** ручний snapshot у GSC → fulfillmentmtp.com.ua → Pages → "/" → позиції за останні 28 днів; залишити у коментарі до цього файлу ДО деплою

## Поточна структура сторінки (для reference)

1. HERO — full-width dark hero з background image + badge + H1 + sub + phone form + 4 статистики внизу (60 000+/міс, 10 років, 150+, 3 900 м²)
2. LOGOS — маркі клієнтів (Rozetka, Prom.ua, Horoshop, KeyCRM, WooCommerce, OpenCart, SalesDrive) + медіа (Europa Plus, Гроші Плюс, Top100)
3. PROBLEMS — "Ти впізнаєш себе?" 3 карти з italic питаннями в лапках
4. SERVICES — "Повний цикл фулфілменту" 6 кроків з номерами 01-06
5. CTA внутрішній — "Фулфілмент для важких товарів 50+ кг"
6. WAREHOUSE TOUR — чорний блок з YouTube thumbnail + CTA "Дивитись екскурсію"
7. TESTIMONIALS — 10 відгуків у slider
8. STEPS — "Почати за 1 день" 4 кроки
9. FAQ (details/summary) — 7 запитань
10. SEO TEXT — довгий SEO-артикль з h2/h3 + внутрішня перелінковка

## Redesign intent (Direct mood)

Підтримати всі 10 блоків, але:
- Перенести візуальну мову до **Direct** архетипу (`docs/design-system/archetypes/direct.md`):
  - повноекранний темний hero з overlay
  - червоний badge вгорі
  - form-in-hero (залишити)
  - warm tone CTA, мʼяка типографіка
- Shared компоненти з `src/components/stitch/`: `SplitHero` (або hero-варіант Direct), `StatsBar` для 4 KPI, `LabelChip` для badges, `DarkCTA` перед footer, `AccordionGroup` для FAQ
- Перенести testimonial slider + warehouse tour + marquee логотипів БЕЗ зміни даних
- Зберегти ВСІ внутрішні посилання (мінімум `/ua/fulfilment-ukraina/`, `/ua/fulfilment-kyiv/`, `/ua/fulfilment-dlya-marketpleysiv/`, `/ua/tsiny/`, `/ua/calculator/`, `/ua/fulfilment-vazhkykh-tovariv/`)

## Rollback trigger

Якщо за 7 днів після деплою:
- Form CR **-15%** vs baseline → **ROLLBACK**
- Google позиції по primary keyword "фулфілмент" впали на **-20%** → **ROLLBACK**
- LCP виріс на **+20%** проти попереднього заміру → дослідити і зафіксити за 48 годин, інакше rollback

## Links

- Stitch export: `docs/design-system/stitch-exports/2026-04-19_ua-home/`
- Archetype: `docs/design-system/archetypes/direct.md`
- ADR: (створити після деплою) `docs/design-system/pages/home-ua.md`
