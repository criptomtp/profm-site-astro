---
page: /ru/guide/
archetype: Direct (Playbook subtype)
stitch_project: 16366500142707399412
stitch_screen: f2605d62af3649c48e7f07667e58a166
approval_date: 2026-04-20
status: live
driver: GSC Coverage Drilldown 8 — "Копія. Google вибрав іншу канонічну" (3-й URL зі списку)
---

# ADR — `/ru/guide/` Operational Playbook redesign

## Причина
У GSC Drilldown 8 (2026-04-20) сторінка `https://www.fulfillmentmtp.com.ua/ru/guide/` позначена статусом "Копія. Google вибрав іншу канонічну" (останнє сканування 2026-04-15). Попередня RU-версія була ~95% перекладом UA (ідентичні "Глава 1-6", ідентична цитата засновника, ідентичний TOC, ідентична структура). Google вибрав UA як канонічну і виключив RU з індексації.

Мета редизайну: перепозиціонувати сторінку з "довгий blog-пост зі статтею" на "Operational Playbook / Decision Support Tool" — радикально інша структура, тон і формат.

## Archetype
**Direct (Playbook subtype)** — це третій archetype у циклі Drilldown 8 (після 2× Editorial для `/ru/recalls/` і `/ru/about/`). Варіанти використання tactical monolith aesthetic: zero-radius brutalism, Swiss International Style, numeric dominance (200px red DM Serif numerals 01-07 як tactical sign-posts), heavy uppercase labels, high-contrast binary palette, tables/checklists замість прози.

## Візуальний референс
- Stitch project: `16366500142707399412` ("MTP Manifesto")
- Approved screen: `f2605d62af3649c48e7f07667e58a166` ("v1-operational-playbook")
- Stitch-generated design system: "Tactical Grid"
- Локальний експорт: `docs/design-system/stitch-exports/2026-04-20_ru-guide/`
  - `concept.md` — ТЗ
  - `screenshot.png` — approved screen render

## Структура сторінки (10 секцій)

1. Top rule + label `ПЛЕЙБУК · OPERATIONAL DECISION GUIDE`
2. **Full-width hero** з warehouse photo + dark overlay 65-80%. Badge "ПЛЕЙБУК 2026", H1 "Переходить на фулфилмент или нет?", subhead "7 шагов, чтобы решить за 15 минут", red CTA button "Начать плейбук ↓", black stat strip 4×
3. **Шаг 01** — Big red "01". Cost calculator table 6 рядків з порожніми "_____" для self-fill + total bar. Bg `#fafafa`
4. **Шаг 02** — "02". Compare table 4 колонки ("Операция" / "Ваш склад" / "3PL" / "Где выигрыш") з red/green status dots
5. **Шаг 03** — "03". 5 white flag cards з red top-border (пропущенные заборы / потери SKU / ручная упаковка / возвраты / SLA маркетплейсов). Bg `#fafafa`
6. **Шаг 04** — "04". Checklist 2×5 з red square ✓ icons — 10 критеріїв оператора
7. **Шаг 05** — "05". Horizontal timeline 5 nodes з red connecting line — 14-day онбординг (аудит → договір → передача → тести → переход)
8. **Шаг 06** — "06". Vertical breakpoints 5 points (30/100/500/1000/5000 на день) — останній red-on-black accent. Bg `#fafafa`
9. **Шаг 07** — "07". Dark bg `#000`. 3 boxed warnings з red accents + red top-border (без SLA / товар дома / міграція перед піком)
10. **Closing CTA** — full-width red `#e63329`. H2 "Посчитайте свой месяц за 2 минуты", 2 white buttons (калькулятор + контакт), допоміжні links на recalls/about

## Відмінність від `/ua/guide/`

| Аспект | UA | RU (v1 Playbook) |
|---|---|---|
| Формат | Blog-стаття 6 глав H2/H3 | Operational Playbook 7 пронумерованих кроків |
| Тон | Educational monologue | Tactical decision-support |
| Hero | Small centered hero + TOC | Full-width photo + dark overlay + badge |
| Контент | Довгі параграфи прози | Tables, checklists, timeline, breakpoints |
| Архетип | Editorial (blog) | Direct (Playbook subtype) |
| H2 стиль | "Глава 1. Що таке фулфілмент" | "Шаг 01. Собери свою текущую стоимость логистики" |
| Author voice | Цитата засновника в тілі | Жодної цитати — лише метрики і структура |
| CTA | Розсіяні в тексті | Закриваючий red block + 2 white buttons |
| Tables | Немає | 2 великих + breakpoints + checklist grid |
| Interactive | Video embed | Cost calculator (self-fill) |
| Об'єм | ~2000 слів прози | ~1500 слів структури |

## Фіксовані токени
- Колір: `#e63329` (red 01-07 numerals, CTAs, accents, top-borders) / `#000` (stat strip, Шаг 07, tfoot) / `#fff` / `#fafafa` (alt sections 01/03/06) / `#e5e5e5` (dividers)
- Типографіка: `DM Serif Display` — тільки для 200px numerals 01-07 та breakpoint numbers. `DM Sans` — все інше (body, H2, labels, tables)
- CSS scope: префікс `.pb-` (playbook)
- **Zero-radius**: жодних `border-radius` — усі елементи прямокутні

## Shared компоненти
- `Base.astro` (layout + Header/Footer + skip-link + global tokens)
- Header + Footer — автоматично з Base, без змін
- Немає video modal (guide не містить відео — є посилання на `/ru/recalls/` в закриваючому блоці)

## Deviations from default Direct archetype
- Direct archetype зазвичай має hero form (CRO landing). Тут — ні: hero form проігноровано, оскільки guide це decision-support, а не conversion. CTA винесено в закриваючий block
- Використано question-form H1 ("Переходить на фулфилмент или нет?") — нестандартно для CRO-Direct, типово для playbook/SaaS comparison
- Чорні сегменти (Шаг 07 + stat strip) — нетипово для чистого Direct, але виправдано tactical monolith aesthetic
- Схема `HowTo` замість `Article` у JSON-LD — відображає playbook-природу сторінки

## Rollback criteria
- Якщо CR на `/ru/calculator/` з `/ru/guide/` падає >15% за 7 днів → revert
- Якщо GSC через 30 днів все ще показує "Копія, Google вибрав іншу канонічну" → переглянути hreflang або обʼєднати RU↔UA канонікли

## Реальні ресурси
- Hero image: `/images/mtp-fulfillment-warehouse-hero.webp` (warehouse photo)
- Closing links: `/ru/calculator/`, `/ru/contact/`, `/ru/recalls/`, `/ru/about/`
- Статистика в hero: 150+ клієнтів, 60 000+ відправок, OTIF 99.8%, 10 років — реальні дані
- Бенчмарки тарифів у Шаг 02 — ринкові ранжі на апрель 2026, відповідні реальним MTP-пропозиціям

## Next steps after deploy
1. GSC → Inspect URL `https://www.fulfillmentmtp.com.ua/ru/guide/` → Request Indexing
2. GSC → Coverage → "Копія, Google вибрав іншу канонічну" → Validate Fix для `/ru/guide/`
3. Monitor 7 днів (GSC recognition + CR на калькулятор)
4. **GSC Drilldown 8 завершено** — усі 3 URL переопрацьовано: `/ru/recalls/` (Editorial) + `/ru/about/` (Editorial Chronology) + `/ru/guide/` (Playbook)
