---
page: /ru/recalls/
archetype: Editorial
stitch_project: 16366500142707399412
date: 2026-04-20
status: pending-approval
current_version: v2-with-videos
---

# RU /recalls/ — Editorial Data Cases

## Задача
RU `/ru/recalls/` був прямим перекладом UA. Google вибрав UA як канонічну — RU не індексувався окремо. Треба переписати з іншою структурою, іншим кутом, іншими текстами.

## Версії

### v1-data-only/
Базова Editorial концепція: data wall + long-form кейси без відео.
**Feedback від user:** "Виглядає непогано, але де відеовідгуки?"
→ Data-only формат не підходить для сторінки відгуків.

### v2-with-videos/ ← поточна
Editorial + відео інтегровані в кожен кейс + архівна смуга внизу.
- Stitch screen: `39207901ffb8479097100bf2240b05c1`
- Structure below ⬇

## Концепція v2
"Клиентские кейсы — цифры + видеодоказательство". Editorial archetype (Economist/FT/Monocle vibe) з відео як частиною кожного кейсу, НЕ як окремий grid.

## Відмінність від UA
| Аспект | UA `/ua/recalls/` | RU `/ru/recalls/` v2 |
|---|---|---|
| Формат відео | Grid з 6 однакових відео-плиток | Відео **вбудовані в кейси** (1 великий + 1 flipped + 1 центрований) |
| Архітектура | Hero-grid-first | Hero typography → featured case → data → flipped case → centered case → archive strip |
| Тон | Емоційний ("подивіться що кажуть") | Аналітичний + візуальний доказ ("посмотрите данные + видеоразбор") |
| Клієнти | 6 коротких відео | 3 deep-dive + таблиця на 8 + архівна смуга з 6 |
| Об'єм | ~600 слів | ~1500+ слів |
| H2/H3 | Перекладаються з UA | Різна структура |
| Hero | Відео-grid | Editorial typography "150 клиентов. 10 лет."

## Секції v2
1. Top rule + label "РАЗБОР / CLIENT CASE STUDIES"
2. Editorial hero: "150 клиентов. 10 лет. 60 000+ отправок в пик."
3. **Featured Case 1 Carter's** — split 55/45: VIDEO ліворуч + pull quote + text праворуч
4. Data wall — таблиця 8 клієнтів з метриками
5. **Case 2 Elemis** — flipped: text ліворуч + VIDEO праворуч
6. **Case 3 ORNER** — центроване VIDEO + pull quote + full-width text
7. Sector breakdown (black, bar chart)
8. 🆕 Archive strip — 6 малих відео-thumbnails горизонтальною смугою
9. Methodology: OTIF / Ошибки / Время цикла
10. Dark CTA: "Получите разбор своего магазина"

## Артефакти
- `v1-data-only/screenshot.png` + `design.html` — базова без відео (rejected)
- `v2-with-videos/screenshot.png` + `design.html` — з відео (current, pending approval)

## Наступні кроки
1. User → approved для v2
2. Content writing (~1500 слів RU, не переклад UA)
3. Astro implementation + токени з `src/styles/stitch-tokens.css`
4. Оновлення hreflang cross-links UA ↔ RU ↔ EN
5. Build + deploy + ADR в `docs/design-system/pages/ru-recalls.md`
6. GSC "Validate fix"
