---
page: /ru/about/
archetype: Editorial
stitch_project: 16366500142707399412
stitch_screen: 88e73faec3774b7eaff893a1b9824577
date: 2026-04-20
status: pending-approval
driver: GSC Coverage Drilldown 8 — "Копія. Google вибрав іншу канонічну" (2-й URL зі списку)
---

# RU /about/ — Editorial Chronology

## Задача
RU `/ru/about/` — майже дослівний переклад UA `/ua/about/`. Google вибрав UA як канонічну → RU не індексується як самостійна сторінка. Треба переписати з іншим кутом атаки (хронологія), іншим тоном (журналістський), іншими H2.

## Концепція
**"Фулфилмент, который рос вместе с украинским e-commerce"** — хронологічна подача історії MTP Group як журналістського матеріалу від першої особи бренду. Editorial archetype (FT/Economist/Monocle vibe): велика типографіка DM Serif Display, без hero image, без форми над фолдом, один CTA у фінальній editorial-нотці.

## Відмінність від `/ua/about/`

| Аспект | UA | RU (v1 Editorial) |
|---|---|---|
| Структура | Topical: OUR STORY → технології → blackout → цифри | Chronological: 2015 → 2018-2020 → 2022 → 2026 |
| Hero | Split hero з фото складу | Editorial typography, eyebrow "2015 → 2026", H1 без зображення |
| Тон | Корпоративний "ми" | Журналістський наратив від першої особи |
| Blackout-розділ | Окремі 3 картки "виклик" | Окрема Chapter III з графіком uptime та інсайтом про дизельку |
| Технології | 4 картки у grid | Вбудовані в chronological chapters + окремий специфікейшн складу |
| Форма | Hero form | Без форми; закриття editorial-нотою + 3 текстові посилання |
| H2 | "Наша історія", "Наші технології", "Блекаут" | "Глава I. 2015: старт в одной комнате", "Глава II. 2018-2020: когда маркетплейсы стали главным каналом", "Глава III. 2022: война, блэкауты, дизель" |
| Об'єм | ~1400 слів | ~1700 слів оригінального RU (не переклад) |

## Структура v1 (10 секцій)

1. **Top rule + label** `О КОМПАНИИ · FOUNDER'S NOTE`
2. **Editorial hero** — eyebrow "2015 → 2026", H1 `Фулфилмент, который рос вместе с украинским e-commerce`, dek-параграф (2-3 речення), без зображення
3. **Chapter I. 2015: старт в одной комнате** — split 7/5: архівне фото (1 room warehouse, palette, boxes) ліворуч + drop-cap text праворуч. Метрики тих років (2 клієнта / 80 м² / 40 відправок на день)
4. **Chapter II. 2018-2020: маркетплейсы и масштабирование** — flipped split 1/1: text ліворуч + photo (modern racks, barcode scanning) праворуч. Pull quote "Rozetka стала нашей школой дисциплины"
5. **Data strip** — 6 year-pill cards з ключовими цифрами по роках: 2015 / 2017 / 2019 / 2021 / 2023 / 2026. Сірий бекграунд #fafafa, divider lines
6. **Chapter III. 2022: война, блэкауты, дизель** — full-width black bg з uptime chart (99.8% OTIF утримано навіть при blackout). Pull quote "Дизель-генератор и UPS оказались такой же частью SLA, как WMS"
7. **Warehouse specsheet** — два склади SHCHASLYVE / BILOGORODKA у двох колонках. Технічні характеристики: площа, висота стелажів, потужність приймання, WMS версія, генератор kVA, UPS час автономії
8. **Methodology** — 3 cards: OTIF 99.8% / Pick Accuracy 99.98% / Cycle 1.5 h. Такий самий стиль як в `/ru/recalls/` для візуальної консистентності
9. **Warehouse video tour** — embed відео `bHY3cFF9SlI` (Ekskursia po skladu) з коротким підписом
10. **Closing editorial note** — без форми. Pull quote від засновника + 3 текстові посилання: "Ознакомиться с клиентскими кейсами" → `/ru/recalls/`, "Рассчитать стоимость фулфилмента" → `/ru/calculator/`, "Написать нам напрямую" → `/ru/contact/`

## Фіксовані токени
- Колір: `#e63329` (red accent, year labels, drop caps) / `#000` / `#fff` + `#fafafa` (data strip bg) + `#e5e5e5` (divider lines)
- Типографіка: `DM Serif Display` (H1, Chapter titles, pull quotes, years), `DM Sans` (body, metrics, labels)
- CSS scope: усі класи з префіксом `.ab-` (about) щоб уникнути конфліктів з `.ed-` (recalls) та глобальними

## Shared компоненти
- `Base.astro` (layout + Header/Footer + skip-link + глобальні токени)
- Header + Footer без змін
- Відеомодал для warehouse tour — inline script як в `/ru/recalls/`

## Deviations from default Editorial archetype
- `src/pages/en/faq.astro` референс рекомендує StatsBar + AccordionGroup. Тут не використовуються, бо це не Q&A.
- Використано dark chart на чорному тлі (Chapter III uptime) — нетипово для Editorial, але необхідно для візуального відокремлення "кризового" розділу.
- Немає CTA form взагалі (навіть наприкінці) — editorial closing note з текстовими посиланнями замість форми. Рішення: `/ru/about/` це не конверсійна сторінка, це trust-building; CTA перенесена до суміжних сторінок.

## Rollback criteria
- Якщо CR на суміжні сторінки з `/ru/about/` (calculator, contact, recalls) падає >15% за 7 днів → revert.
- Якщо GSC Coverage через 30 днів все ще показує "Копія, Google вибрав іншу канонічну" → переглянути hreflang або об'єднати RU↔UA канонікли.

## Stitch артефакти
- Project: `16366500142707399412` ("MTP Manifesto")
- Screen: `88e73faec3774b7eaff893a1b9824577` ("v1-editorial-chronology")
- Локальний експорт: `docs/design-system/stitch-exports/2026-04-20_ru-about/`
  - `concept.md` — цей файл (ТЗ)
  - `screenshot.png` — approved screen render

## Наступні кроки
1. User → "approved" для v1
2. Content writing (~1700 слів RU, не переклад UA)
3. Astro implementation з токенами `src/styles/stitch-tokens.css` + класи `.ab-`
4. Оновлення hreflang cross-links UA ↔ RU ↔ EN на всіх 3 about-сторінках
5. Build + deploy (vercel --prod) + ADR `docs/design-system/pages/ru-about.md`
6. GSC → Inspect URL `/ru/about/` → Request Indexing → Validate Fix
7. Monitor 7 днів, потім наступний URL зі списку Drilldown 8: `/ru/guide/`
