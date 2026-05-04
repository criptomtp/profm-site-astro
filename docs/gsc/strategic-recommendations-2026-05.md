# Стратегічні рекомендації на основі GSC аналізу
**Дата:** 2026-05-04
**Дані:** Apr 1 - May 2 2026 (1973 page-query pairs, 928 unique queries)
**Контекст:** GSC property верифікований ~Apr 1 2026, дані тільки за 1 місяць

---

## 1. Поточна картина — де ми стоїмо

| Категорія | Кількість запитів | Imp | Що це означає |
|---|---:|---:|---|
| 🏆 Won (pos 1-5) | 28 | 1,408 | Бренд + нішеві перемоги |
| 🎯 Striking distance (pos 6-15) | 105 | **3,853** | **Найбільший CTR-резерв** |
| ⚠️ Page 2 (pos 16-30) | 89 | 3,039 | Words/depth uplift |
| 🌑 Long-tail far (pos 31-100) | 207 | 3,704 | Content gaps |
| 👻 Wrong-intent (top-15, 0 clicks) | 43 | 19,239 | Ghost ranking |
| 🥷 Competitor brand (rozetka, prom etc) | 18 | 15,962 | Не наш бій |

**Висновок:** **24,000 imp** з потенціалом конверсії в кліки знаходяться на pos 6-30 — це наш main battlefield для квітня-травня.

---

## 2. ⚡ ШВИДКІ WINS (1-2 дні роботи) — title/H1/snippet rewrite на 12 сторінках

Це сторінки де ми ВЖЕ в топ-10 але не отримуємо кліків (CTR 0%). Простий title rewrite може дати 5-10x кліків миттєво.

### CTR Rescue Tier 1 (>200 imp, pos top-10, 0 clicks):

| Query | Imp | Pos | Page | Дія |
|---|---:|---:|---|---|
| `sla це` | 463 | 7.9 | UA blog "Що таке SLA" | Title: "Що таке SLA в логістиці — простими словами + приклад калькуляції" |
| `артикул` | 301 | 6.2 | UA blog "Що таке артикул" | Title: "Артикул товару — що це, чим відрізняється від SKU" |
| `склад фулфилмент` | 196 | 10.8 | / (UA home) | Add H2 секція явно "Склад фулфілмент" + redirect signal |
| `артикул це` | 172 | 4.3 | UA blog | Title: "Артикул — це унікальний код товару (визначення + 3 формати)" |
| `мтп` | 414 | 7.5 | / (UA home) | Title brand-strengthen: "MTP Group — фулфілмент в Україні" |
| `товарний бізнес україна` | 110 | 7.4 | UA blog "Товарний бізнес" | Title: "Товарний бізнес в Україні 2026 — з чого почати без $1000 капіталу" |
| `склад фулфилмент` | 196 | 10.8 | / | Hero subtitle включити "склад фулфілмент" |
| `услуги фулфилмента` | 98 | 12.3 | /services/ | Title: "Услуги фулфилмента — приёмка, хранение, упаковка от 18 грн" |
| `fulfilment services` | 123 | 14.1 | / EN | Title rewrite з фокусом на "fulfilment services" |

**Очікуваний результат:** 50-100 додаткових кліків на тиждень тільки з цих 9 рядків.

---

## 3. 📈 PAGE 2 BREAKTHROUGH (~1 тиждень) — words/depth uplift

Ці сторінки на pos 16-30 — треба прорватися в топ-10. Потребують:
- Більше контенту (semantic depth)
- Більше внутрішніх посилань
- Більш targeted H2-секцій під query

| Query | Imp | Pos | Top page | Що робити |
|---|---:|---:|---|---|
| `фулфилмент для интернет магазина` | 273 | 22.1 | /ru/fulfilment-dlya-internet-magazynu/ | Вже зробили Phase B сьогодні — спостерігати |
| `фулфілмент` | 266 | 24.8 | / (UA home) | Brand-pillar на home — додати H1 secondary "Фулфілмент в Україні" + збагатити лендінг |
| `фулфилмент` | 243 | 21.6 | https://fulfillmentmtp.com.ua/ | Те саме але /ru/ home потребує |
| `фулфилмент в товарном бизнесе` | 156 | 17.4 | RU blog | Перенести/доповнити окрему сторінку /ru/fulfilment-dlya-tovarnogo-biznesa/ |
| `складські послуги` | 126 | 15.7 | /ua/skladski-poslugy/ | Words uplift на pillar (вже в нашому 24-fail списку) |
| `что такое фулфилмент` | 72 | 19.4 | /ru/chto-takoe-fulfilment/ | Phase B candidate — додати H2 з прикладами |

---

## 4. 🆕 НОВІ СТОРІНКИ ДЛЯ СТВОРЕННЯ (priority queue)

### Priority 1: GEO-LANDING PAGES (12-15 годин роботи, +500+ imp потенціал)

Поточний стан: запити з географічними модифікаторами стирчать на pos 31-100 без dedicated landing.

**Створити 4 нові сторінки:**

#### 1.1 `/fulfilment-dnipro/` (UA + RU + EN cluster) — найбільший imp pool
**Запити (combined 188 imp):**
- "фулфилмент днепр" 29 imp pos 41
- "фулфілмент дніпро" 19 imp pos 43.5
- "склад фулфілмент дніпро" 33 imp pos 48.2
- "фулфілмент для маркетплейсов дніпро" 46 imp pos 56.5
- "фулфилмент для интернет магазинов днепр" 29 imp pos 47.9
- "склад фулфилмент днепр" 16 imp pos 36.5
- "фулфілмент логістика дніпро" 17 imp pos 43.4

**Структура:** Hero "Фулфілмент для бізнесу з Дніпра" → "Чому з Дніпра обирають київський фулфілмент" → "Що NP робить за 1 добу" → Економічна модель → CTA. ~2500 слів × 3 мови.

#### 1.2 `/fulfilment-kharkiv/` (UA + RU + EN)
**Запити (combined ~80 imp):**
- "фулфилмент харьков", "склад харьков", "фулфілмент харків"
- "фулфилмент для интернет магазинов харьков"

#### 1.3 `/fulfilment-zaporizhzhia/` (UA + RU)
**Запити (combined ~50 imp):**
- "фулфилмент запорожье" 17 imp pos 51.9
- "фулфилмент для маркетплейсов запорожье" 5 imp pos 15.2 (вже близько top-15!)
- "склад фулфілмент запоріжжя" 5 imp pos 28.2

**Особливий angle:** прифронтовий регіон → київський хаб як стабільне рішення.

#### 1.4 `/fulfilment-lviv/` (UA + RU + EN)
**Запити (combined ~30 imp):** "фулфилмент львов", "фулфілмент львів", western Ukraine focus.

**ROI прогноз для 4 геолендингів:** 600-1000 додаткових imp/міс, ~5-10 кліків/тиждень коли індексація стабілізується.

---

### Priority 2: BIG CONTENT GAP — "Доставка в Молдову/СНД" (~3-4 години)

**Дані:** 1,109 imp combined, avg pos 7.7 — **МИ ВЖЕ в топ-10** але без dedicated landing.
- "prom ua доставка в молдову" 989 imp pos 7.7 (!) — 0 clicks
- "rozetka com ua доставка в молдову" 120 imp pos 11.7

**Створити:** `/ru/dostavka-v-moldovu-iz-ukrainy/` (RU primary, оскільки pos з RU SERP) — landing про cross-border доставку Nova Poshta International, ціни, терміни, документи. Один landing закриє цілий cluster з ВЕЛИЧЕЗНИМ потенціалом конверсії (молдавські e-com бренди шукають саме це).

---

### Priority 3: PRRO/РРО Hub — інформаційний pillar (~3 години)

**Дані:** 35 queries, 379 imp, avg pos 43.8 — розкидано по 6 blog-постах.

**Створити:** `/ua/prro-dlya-internet-magazynu/` + RU equivalent — повноцінний pillar (не blog) з:
- Що таке РРО/ПРРО, різниця
- Хто зобов'язаний
- Як підключити
- Інтеграція з касовим софтом
- Роль фулфілмент-провайдера у РРО compliance

**Це конвертить ваш бренд у "експерта legal compliance для e-com" — серйозний trust signal.**

---

### Priority 4: COSMETICS EN PAGE — full rewrite (~2 години)

**Дані:** Pages exists at pos 80-98 — **майже невидимий**.
- "fulfillment cosmetics" 33 imp pos 81.5
- "cosmetics fulfilment" 43 imp pos 89.3
- "fulfillment of cosmetics" 43 imp pos 80.8

Сторінка `/en/fulfillment-for-cosmetics/` потребує великого contentual rewrite з конкурентним аналізом топ-3 EN ranking (US/UK 3PL operators в beauty-сегменті).

---

### Priority 5: NEW DEDICATED LANDINGS for already-ranking clusters

#### 5.1 `/ru/fulfilment-dlya-tovarnogo-biznesa/` (~2-3 години)
**Дані:** "фулфилмент в товарном бизнесе" 156 imp pos 17.4, "фулфилмент в товарке" 127 imp pos 20.1.

Це слово "товарка" — RU slang який не охоплено окремою сторінкою. Зараз веде на /ru/fulfilment-dlya-marketpleysov/ — зробити свій landing.

#### 5.2 `/en/kasta-international-shipping/` (~2 години)
**Дані:** 127 imp combined, avg pos 9.7 — ми РАНКУЄМО на сторінці яка про Україну!
- "kasta.ua international delivery" 96 imp pos 9.9
- "kasta.ua international shipping" 31 imp pos 9.4

Зробити focused landing для Kasta cross-border — буквально нішевий high-converting traffic.

#### 5.3 `/en/horoshop-fulfilment-integration/` (~2 години)
Horoshop — найпопулярніша SaaS storefront в UA, але не маємо dedicated landing з integration guide. Запити "horoshop" приходять на блог пост.

---

## 5. 🚫 WRONG-INTENT — рішення треба

### `/en/guide/how-to-integrate-prom/` — 14,436 imp / 0 clicks
**Запит:** "prom.ua api" pos 7.7
**Реальність:** Користувачі шукають **офіційну API документацію Prom.ua**, не нашу інтеграційну гайд.
**3 опції:**
- (a) **Accept as ghost SEO** — нічого не робимо, але це 14K marketing imp проходить мимо
- (b) **Title pivot:** змінити з "How to integrate Prom" на щось що справді матчить наше пропозиція ("Prom.ua fulfillment partner — automated order sync") — ризик втратити ranking
- (c) **noindex** — звільнити SEO budget для інших сторінок

**Моя рекомендація:** опція (b) — title rewrite з збереженням URL. Маленький A/B експеримент.

---

## 6. 📋 TOP RIGHT-NOW ACTION LIST (наступні 7 днів)

| Дія | Час | Очікуваний impact |
|---|---:|---|
| **CTR Rescue 9 titles** (Section 2) | 1 год | +50-100 кліків/тиждень |
| **Створити /ru/dostavka-v-moldovu/** | 3-4 год | +50 imp/тиждень, потенціал на cross-border conversion |
| **Створити /fulfilment-dnipro/ cluster (UA+RU)** | 4-6 год | +200 imp/тиждень |
| **CONTENT REWRITE /en/fulfillment-for-cosmetics/** | 2 год | вирвати з pos 80 в pos 30-40 |
| **Re-write title `/en/guide/how-to-integrate-prom/`** | 30 хв | спробувати конвертувати ghost imp |

**Total: ~12-15 годин** на наступний тиждень → potential **+300-400 imp/тиждень + 100-150 кліків/тиждень gain**.

---

## 7. 📅 КАЛЕНДАРНИЙ ПЛАН — травень 2026

**Тиждень 1 (5-11 травня):** CTR Rescue batch + спостереження за 2026-05-09 GSC delta + dnipro cluster start
**Тиждень 2 (12-18 травня):** kharkiv + zaporizhzhia geo-landings + Молдова landing
**Тиждень 3 (19-25 травня):** lviv + cosmetics rewrite + товарна бізнес RU landing
**Тиждень 4 (26 травня - 1 червня):** PRRO hub + Kasta + Horoshop landings + monthly trend analysis re-run

**Цикл закінчується ~1 червня з:**
- 8-10 нових landing pages
- 9 CTR-optimized titles
- 1 wrong-intent experiment
- Pillar scorecard target 30 → 40+ PASS
- GSC clicks ціль: 60-80/тиждень → 150-200/тиждень

---

## 8. 🏆 ЩО ЦЕ ВСЕ РАЗОМ ОЗНАЧАЄ

**Ти зараз у фазі "discovery / breadth" — Google знаходить нас за десятками нових queries (519 нових за тиждень).** Це здоровий сигнал — site індексується, semantic relevance росте.

**Дві "стіни" які треба пробити:**
1. **CTR wall** — багато pos 6-15 рангів з 0 кліків. Title-level робота.
2. **Page-2 wall** — багато pos 16-30 рангів. Content depth + internal linking робота.

**Один "ghost" які треба вирішити:**
- `prom.ua api` — 14K imp без конверсії. Думати: pivot чи accept.

**Один "blue ocean" який майже ніхто не зайняв:**
- Geo-modifier фулфілмент queries (Дніпро, Харків, Запоріжжя). Конкурентам в UA лінь робити city-level landings → swift entry для нас.

**Якщо виконати весь Tier 1 + новi landings за травень,** прогноз:
- Травень: ~70K imp / 250-400 кліків (vs квітень 32K / 127)
- Червень: 100K+ imp / 500+ кліків якщо CTR утримається
- Брендові queries (`mtp`, `мтп`) ростуть органічно — в червні очікую 300-500 brand-search imp
