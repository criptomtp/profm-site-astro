---
page: /ru/about/
archetype: Editorial
stitch_project: 16366500142707399412
stitch_screen: 88e73faec3774b7eaff893a1b9824577
approval_date: 2026-04-20
status: live
driver: GSC Coverage Drilldown 8 — "Копія. Google вибрав іншу канонічну" (RU /about/ був майже дослівним перекладом UA)
---

# ADR — `/ru/about/` Editorial redesign

## Причина
У GSC Drilldown 8 (2026-04-20) сторінка `https://www.fulfillmentmtp.com.ua/ru/about/` позначена статусом "Копія. Google вибрав іншу канонічну" (останнє сканування 2026-04-15). Попередня RU-версія була ~90% перекладом UA (ідентична структура: hero + OUR STORY + warehouse-tour + 2 WAREHOUSES + TECHNOLOGY + BLACKOUT + KEY NUMBERS), тому Google вибрав UA як канонічну і виключив RU з індексації.

Мета редизайну: нова структура (хронологічна замість топікальної), новий тон (журналістський замість корпоративного), унікальний RU-контент.

## Archetype
**Editorial** — велика типографіка (DM Serif Display), відсутність hero image, читабельність як головна задача. Відхилення від дефолтного Editorial (`src/pages/en/faq.astro`): тут не використовуємо StatsBar + AccordionGroup, оскільки сторінка — це хронологічний наратив, а не Q&A.

## Візуальний референс
- Stitch project: `16366500142707399412` ("MTP Manifesto")
- Approved screen: `88e73faec3774b7eaff893a1b9824577` ("v1-editorial-chronology")
- Локальний експорт: `docs/design-system/stitch-exports/2026-04-20_ru-about/`
  - `concept.md` — ТЗ
  - `screenshot.png` — approved screen render

## Структура сторінки (10 секцій)
1. Top rule + label `О КОМПАНИИ · FOUNDER'S NOTE`
2. Editorial hero — eyebrow `2015 → 2026`, H1 «Фулфилмент, который рос вместе с украинским e-commerce»
3. **Глава I. 2015** — split 7/5: архівне фото ліворуч + drop-cap text праворуч + метрики 4× (2 клієнти / 80 м² / 40 відправок / 3 людини)
4. **Глава II. 2018-2020** — flipped split: text ліворуч + warehouse photo праворуч + pull quote про Rozetka
5. Data strip — 6 year-pill cards (2015 / 2017 / 2019 / 2021 / 2023 / 2026 pulse з червоним)
6. **Глава III. 2022 Blackouts** — full-width black bg з uptime chart (99.8% OTIF) + pull quote про дизель-генератор
7. Warehouse specsheet — 2 колонки (Счастливое 2800 м² / Белогородка 1100 м²) з dl-специфікейшнами
8. Methodology — 3 cards: OTIF 99.8% / Pick 99.98% / Cycle 1.5h
9. Warehouse video tour — embed відео `bHY3cFF9SlI` (реальна екскурсія по складу)
10. Closing editorial note — без форми, 3 текстові посилання + підпис засновника

## Відмінність від `/ua/about/`

| Аспект | UA | RU (v1 Editorial) |
|---|---|---|
| Архітектура | Topical: історія → технології → blackout → цифри | Chronological: 2015 → 2018-2020 → 2022 → 2026 |
| Hero | Split з фото складу | Editorial typography, eyebrow «2015 → 2026», без зображення |
| Тон | Корпоративний «ми» | Журналістський наратив |
| Blackout-розділ | 3 картки «виклик» | Окрема Chapter III з uptime chart |
| Технології | 4 картки у grid | Вбудовані в chapters + специфікейшн складу в dl-таблицях |
| Форма | Hero form + secondary | Без форми взагалі — closing editorial note з 3 текстовими посиланнями |
| H2 | «Наша історія» / «Наші технології» | «Глава I. 2015: старт в одной комнате» / «Глава III. 2022: война, блэкауты, дизель» |
| Об'єм | ~1400 слів | ~1700 слів оригінального RU (не переклад) |

## Фіксовані токени
- Колір: `#e63329` (red, eyebrow + year labels + drop caps + uptime bar) / `#000` / `#fff` + `#fafafa` (data strip + methodology bg) + `#e5e5e5` (divider lines)
- Типографіка: `DM Serif Display` (H1/H2/H3, chapter titles, years, pull quotes, metrics), `DM Sans` (body, labels, caption)
- CSS scope: усі класи з префіксом `.ab-` (about) — не конфліктують з `.ed-` (recalls) чи глобальними

## Shared компоненти
- `Base.astro` (layout + Header/Footer + skip-link + глобальні токени)
- Header + Footer — автоматично з Base, без змін
- Відеомодал — вбудований inline script `mtpAbOpenVideo` / `mtpAbCloseVideo` (ESC закриває)

## Deviations from default Editorial archetype
- Не використано StatsBar + AccordionGroup — сторінка це не Q&A, а хронологічний наратив
- Використано dark chart на чорному тлі (Chapter III uptime) — нетипово для Editorial, але необхідно для візуального відокремлення "кризового" розділу 2022
- Немає CTA form взагалі — рішення: `/ru/about/` це trust-building сторінка, не conversion; CTA перенесено до суміжних сторінок через closing links

## Rollback criteria
- Якщо CR на суміжні сторінки з `/ru/about/` (recalls / calculator / contact) падає >15% за 7 днів → revert
- Якщо GSC Coverage через 30 днів все ще показує "Копія, Google вибрав іншу канонічну" → переглянути hreflang або об'єднати RU ↔ UA канонікли

## Реальні ресурси
- Warehouse video tour: `bHY3cFF9SlI` — реальна екскурсія по складу MTP Group (та сама що на UA)
- Hero image Chapter I: `/images/mtp-founder-nikolai-warehouse.webp` (реальне фото засновника)
- Chapter II image: `/images/mtp-warehouse-interior.webp` (реальний склад)
- Дані uptime 99.8% — реальні з внутрішнього WMS (10.2022–04.2023)

## Next steps after deploy
1. GSC → Inspect URL `https://www.fulfillmentmtp.com.ua/ru/about/` → Request Indexing
2. GSC → Coverage → "Копія, Google вибрав іншу канонічну" → Validate Fix для `/ru/about/`
3. Monitor 7 днів (no CR drop on adjacent pages, GSC recognizes as unique)
4. Повторити workflow для `/ru/guide/` (3-й URL у GSC Drilldown 8, останнє сканування 2026-04-15)
