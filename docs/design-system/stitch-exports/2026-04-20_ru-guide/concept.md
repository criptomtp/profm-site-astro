---
page: /ru/guide/
archetype: Direct (Playbook subtype)
stitch_project: 16366500142707399412
stitch_screen: f2605d62af3649c48e7f07667e58a166
date: 2026-04-20
status: pending-approval
driver: GSC Coverage Drilldown 8 — "Копія. Google вибрав іншу канонічну" (3-й URL зі списку)
---

# RU /guide/ — Operational Playbook

## Задача
RU `/ru/guide/` — майже дослівний переклад UA `/ua/guide/` (однакові "Глава 1-6", однакова цитата засновника, однакова структура). Google вибрав UA як канонічну → RU не індексується. Треба перепозиціонувати з "довгий blog-пост зі статтею" на "Operational Playbook / Decision Support Tool".

## Концепція
**"Переходить на фулфилмент или нет? Плейбук из 7 шагов"** — переосмислити guide як **інструмент прийняття рішення**, а не як статтю для читання. Direct archetype (Playbook subtype): full-width hero з overlay, badge, великі червоні цифри 01-07 як тактичні sign-posts, таблиці й чекліст замість прози, закриваючий CTA на червоному.

## Tactical Monolith aesthetic
- Zero-radius (немає border-radius взагалі)
- Strong numbering — кожен крок з 200px DM Serif Display red numeral
- Heavy uppercase labels, бінарний high-contrast
- Tables > prose (формули, не narrative)
- Decision-support vibe — як чекліст пілота, не як колонка журналіста

## Відмінність від `/ua/guide/`

| Аспект | UA | RU (v1 Playbook) |
|---|---|---|
| Формат | Blog-стаття 6 глав H2/H3 | Operational Playbook 7 пронумерованих кроків |
| Структура | Author monologue | Decision framework з таблицями |
| Hero | Small hero + TOC | Full-width photo з dark overlay + badge "ПЛЕЙБУК 2026" |
| Контент | Довгі параграфи прози | Таблиці (cost calculator), checklists, timeline, breakpoints |
| Архетип | Editorial (blog) | Direct (Playbook subtype) |
| Тон | Educational narrative | Tactical decision-support |
| CTA | Розсіяні в тексті | Закриваючий red CTA block |
| H2 | "Глава 1. Що таке фулфілмент" | "Шаг 01. Собери свою текущую стоимость логистики" |
| Об'єм | ~2000 слів прози | ~1500 слів структури + таблиці |

## Структура v1 (10 секцій)

1. **Top rule + label** `ПЛЕЙБУК · OPERATIONAL DECISION GUIDE`
2. **Full-width hero** — warehouse photo з dark overlay 60%. Badge "ПЛЕЙБУК 2026". H1 80px "Переходить на фулфилмент или нет?". Subhead "7 шагов, чтобы решить за 15 минут". Black stat strip 4 col: "150+ магазинов" / "60 000+ отправок в пик" / "OTIF 99.8%" / "10 лет с 2015". Red button "Начать плейбук ↓"
3. **Шаг 01** — Big red "01" 200px. "Собери свою текущую стоимость логистики". Bg `#fafafa`. Таблиця 6 рядків: Аренда / Упаковочные материалы / Зарплата упаковщика / Печать ТТН / Ваше время × ставка / Прочие. Колонка "В месяц грн" + grey total bar
4. **Шаг 02** — "02". "Сравни с бенчмарком 3PL в Украине 2026". Білий bg. 2-колонкова таблиця "Ваш склад" vs "Фулфилмент 3PL", 6 рядків з red/green dots, totals
5. **Шаг 03** — "03". "Проверь красные флаги". Bg `#fafafa`. 5 white cards з red top-border: пропущенные заборы / потери SKU / ручная упаковка 3+ часов / накопившиеся возвраты / провал marketplace SLA
6. **Шаг 04** — "04". "10 критериев правильного оператора". 2×5 checklist grid з red ✓. Критерії: 5+ років досвіду / власна WMS / штрихкодовий контроль / генератор+UPS+Starlink / інтеграції (Rozetka/Prom/Horoshop) / преміум-партнер НП / прозорі тарифи / візит на склад / SLA в договорі / кейси з цифрами
7. **Шаг 05** — "05". "Процесс онбординга — таймлайн 14 дней". Horizontal timeline 5 nodes з red connecting line: День 1-3 Аудит / 4-6 Договор+тарифы / 7-9 Передача товара / 10-12 Тестовые отправки / 13-14 Полный переход
8. **Шаг 06** — "06". "Точки масштабирования — где ломается DIY". Bg `#fafafa`. Vertical breakpoints з red progress markers: 30/день DIY / 100/день упаковщик / 500/день WMS / 1000/день генератор / 5000+/день тільки 3PL
9. **Шаг 07** — "07". "Типичные ошибки миграции на 3PL". Black bg `#000`. 3 boxed warnings з red accents: без SLA / товар дома / міграція перед піком
10. **Closing CTA** — red bg `#e63329` full-width. "Плейбук пройден. Посчитайте свой месяц за 2 минуты." + 2 white outline buttons: "Открыть калькулятор" / "Написать Николаю"

## Фіксовані токени
- Колір: `#e63329` (red numerals 01-07, CTAs, accents) / `#000` (чорні текст, dark сегменти) / `#fff` (основний bg) / `#fafafa` (alt sections) / `#e5e5e5` (dividers + ghost borders)
- Типографіка: `DM Serif Display` (тільки для 200px numerals 01-07), `DM Sans` (body + headlines + labels), uppercase labels із letter-spacing 0.22em
- CSS scope: усі класи з префіксом `.pb-` (playbook)
- **Zero-radius**: жодних `border-radius` — усе прямокутне

## Shared компоненти
- `Base.astro` (layout + Header/Footer + skip-link)
- Header + Footer без змін
- Немає video modal (guide не містить відео всередині — є посилання на `/ru/recalls/` для відео-кейсів)

## Deviations from default Direct archetype
- Direct archetype зазвичай має hero form (CRO landing). Тут — ні: hero form проігноровано навмисно, оскільки guide це decision-support, а не conversion-landing. CTA винесено в закриваючий блок.
- Використано Full-width hero з overlay (як у Direct), але H1 — питальна форма (нестандартно для CRO-Direct, типово для playbook).
- Чорні секції (Шаг 07 + stat strip у hero) — нетипово для "чистого" Direct, але виправдано tactical monolith aesthetic.

## Rollback criteria
- Якщо CR на калькулятор з `/ru/guide/` падає >15% за 7 днів → revert
- Якщо GSC через 30 днів все ще показує "Копія, Google вибрав іншу канонічну" → переглянути hreflang або об'єднати RU↔UA канонікли

## Stitch артефакти
- Project: `16366500142707399412` ("MTP Manifesto")
- Screen: `f2605d62af3649c48e7f07667e58a166` ("v1-operational-playbook")
- Generated design system: "Tactical Grid" (Zero-Radius Brutalism, Swiss International Style)
- Локальний експорт: `docs/design-system/stitch-exports/2026-04-20_ru-guide/`
  - `concept.md` — цей файл
  - `screenshot.png` — approved screen render

## Наступні кроки
1. User → "approved" для v1
2. Content writing (~1500 слів RU, не переклад UA; таблиці + формули + checklists)
3. Astro implementation з токенами та CSS-префіксом `.pb-`
4. Оновлення hreflang cross-links UA ↔ RU ↔ EN на всіх 3 guide-сторінках
5. Build + deploy (vercel --prod) + ADR `docs/design-system/pages/ru-guide.md`
6. GSC → Inspect URL `/ru/guide/` → Request Indexing → Validate Fix
7. Monitor 7 днів — завершення GSC Drilldown 8
