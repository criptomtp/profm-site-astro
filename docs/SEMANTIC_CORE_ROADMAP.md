# СЕМАНТИЧНЕ ЯДРО MTP — ROADMAP v2
## Єдиний документ: що є / що бракує / що змінилось vs план v1

**Дата**: 2026-04-20
**Джерела даних**: GSC 90d (178 сторінок, 334 запити, 29 кліків, 4,329 показів) + competitor research (20+ конкурентів) + фактичний інвентар сайту (170 pages deployed)

**Пов'язані файли** (не дублюю — читати разом):
- `docs/MTP_SEMANTIC_CORE_FULL.md` — план v1 від 2026-03-27 (121 сторінка)
- `docs/SEMANTIC_CORE_GSC_AUDIT.md` — детальний GSC-аудит з пріоритетами P0/P1/P2
- `docs/gsc/competitor-gap-research.md` — аналіз 20+ конкурентів
- `docs/gsc/full-pages.csv` + `opportunities.csv` — сирі дані GSC
- `docs/gsc/tilda-301-mapping-proposal.md` — 59 Tilda URLs, всі 301-закриті

---

## 1. ЩО У НАС ВЖЕ Є (фактичний стан)

### 1.1 Інвентар за мовами (170 pages deployed)

| Мова | Root | Blog posts | Разом | GSC 90d clicks | CTR |
|------|------|-----------|-------|---------------|-----|
| UA | 19 | 4 (+ tpost legacy) | 23 | 16 | 1.03% |
| RU | 19 | 0 | 19 | 2 | 0.34% |
| EN | 17 | 38 | 55 | 1 | **0.17%** ⚠️ |
| Root (neutral) | ~70 | — | ~70 | 10 | 0.62% |

**Критичний висновок**: EN має НАЙБІЛЬШЕ сторінок (55), але НАЙМЕНШЕ трафіку (1 клік за 90 днів). Це семантична, а не технічна проблема — EN таргетує непотрібні queries.

### 1.2 Сторінки які реально працюють (GSC 90d top-10)

| # | URL | Clicks | Imp | Pos | Топ query |
|---|-----|--------|-----|-----|-----------|
| 1 | /ua/ | ~8 | ~700 | ~6 | фулфілмент |
| 2 | / (root) | ~7 | ~900 | — | brand queries |
| 3 | /ua/fulfilment-dlya-internet-magazynu/ | ~4 | ~200 | ~8 | фулфілмент для інтернет-магазину |
| 4 | /ua/calculator/ | ~2 | ~150 | ~9 | калькулятор фулфілменту |
| 5 | /en/ | 1 | ~300 | — | fulfillment ukraine |
| 6 | /ua/faq/ | 1 | ~80 | — | (FAQ snippets) |

Всі інші 164 сторінки сумарно дали **<6 кліків** за 90 днів.

### 1.3 Що вже покрито з плану v1 (121 сторінок)

**ВИСНОВОК: ~30% плану v1 реалізовано** (38 з 121), але переважно в EN блозі — де немає трафіку.

| Ось плану v1 | План | Зроблено | Працює в GSC |
|-------------|------|----------|--------------|
| За товаром (26) | 26 | 6 | 0 (UA косметика/одяг ще не проіндексовані) |
| За бізнесом (16) | 16 | 2 | 1 (інтернет-магазин) |
| За каналом (12) | 12 | 0 | — |
| За послугою (17) | 17 | 4 | 1 (калькулятор) |
| За географією (8) | 8 | 1 | 0 (Київ) |
| Інфо (24) | 24 | 3 (UA blog) | 0 |
| EN (18) | 18 | 22 (більше ніж в плані!) | 0 (НІ, таргетять не ті queries) |

---

## 2. ЩО ТРЕБА ПОКРАЩИТИ (на основі GSC даних)

### 2.1 🔴 КРИТИЧНІ ПРОБЛЕМИ (P0, тижні 1-2)

#### A. Zero-CTR paradox на top-3 positions
**Проблема**: 5 queries в pos 1-3 показують **0 кліків** при 200+ показах:
- `фулфилмент цены` pos 2.5, 13 imp → гіпотеза: сніпет не показує ціни
- `фулфилмент заказать` pos 1.7, 11 imp
- `артикул це` pos 2.2, 61 imp → сніпет не відповідає на питання
- `prom.ua` pos 2.9, 68 imp → нерелевантний intent
- `mtp` pos 3.8, 56 imp → **власний бренд не генерує клік!**

**Фікс**: переписати title + meta-description з **конкретними цифрами** ("Фулфілмент від 9 грн/замовлення") + додати Organization schema на головну для brand query.

#### B. Головний keyword "фулфілмент" — pos 16 (не на 1-й сторінці)
**Проблема**: при 4,329 імпресіях за 90 днів, MTP має pos 16 на головному запиті галузі — це pos 2 Google сторінки.

**Competitor research підтверджує**: MTP не в топ-10 за `фулфілмент для інтернет-магазину` (buyer intent). Топ-5 займають: Unipost, Novapost, 4erdak, zammler, PTL.

**Фікс**: створити pillar hub `/ua/shcho-take-fulfilment/` 3-4K слів з cross-link у всі 22 вертикальні сторінки. **Це #1 пріоритет** — одночасно б'є "що таке" (1-2K/mo) і topic authority для всіх дочірніх.

#### C. Striking distance (pos 4-20, можна в топ-3 за 4-8 тижнів)

9 opportunities з GSC analysis (`docs/gsc/opportunities.csv`):

| Query | Pos | Imp/90d | Score | Action |
|-------|-----|---------|-------|--------|
| `артикул це` | 5.5 | 336 | 61.1 | Створити /ua/blog/scho-take-artykul-sku/ |
| `sla логістика` | 8.2 | 365 | 44.5 | Створити /ua/blog/scho-take-sla-v-logistici/ |
| `фулфілмент україна` | 7.3 | 180 | 24.6 | Оптимізувати /ua/fulfilment-ukraina/ |
| `ecommerce fulfillment ukraine` | 12.1 | 145 | 12.0 | Оптимізувати /en/ecommerce-fulfillment-ukraine/ |
| `3pl україна` | 9.8 | 98 | 10.0 | Створити /ua/3pl-ukraina/ |
| `фулфілмент київ` | 11.3 | 84 | 7.4 | Оптимізувати /ua/fulfilment-kyiv/ |
| `дніпро фулфілмент` | 14.2 | 72 | 5.1 | **НОВА** /ua/fulfilment-dnipro/ |
| `калькулятор фулфілменту` | 6.1 | 62 | 10.2 | Оптимізувати /ua/calculator/ |
| `комплектація замовлень` | 15.3 | 58 | 3.8 | Створити /ua/komplektatsiya-zamovlen/ |

### 2.2 🟠 ВАЖЛИВЕ (P1, тижні 3-6)

#### D. RU blog = 0 posts, 0 impressions
План v1 передбачав UA-first. Зараз RU має **19 root pages** але **жодного блогового поста**. В Україні RU-пошук ~30% трафіку, і `что такое фулфилмент`, `цены на фулфилмент` — окремі keywords.

**Фікс**:
- `/ru/blog/` інфраструктура (index + tpost legacy)
- `/ru/blog/chto-takoye-fulfilment/`
- `/ru/blog/kak-otkryt-internet-magazin/`
- `/ru/blog/sla-v-logistike/`

#### E. Географічні gaps (нова вісь, якої не було в v1)
GSC показує реальні гео-queries які план v1 ігнорував:
- `дніпро фулфілмент` 72 imp/mo — окрема сторінка
- `одеса логістика` 45 imp/mo — була в v1 тільки як "інформаційна, чому Київ кращий" → **помилка**, треба повноцінна landing
- `харків фулфілмент` 38 imp/mo — план v1 не мав взагалі
- `львів фулфілмент` 55 imp/mo — план v1 мав як "чому Київ кращий" → треба повноцінну

**Фікс**: 4 нові гео-landings UA + RU (8 сторінок).

#### F. Pillar consolidation: 22 `/fulfilment-dlya-*` → 8 deep pages
План v1 хотів 26 тонких вертикальних сторінок. Реалізовано 6. GSC показує що **жодна з них не отримує трафіку** (< 5 imp/90d кожна).

**Гіпотеза**: тонкий контент (800 слів) не ранжується. Треба 8 deep hubs по 2-3K слів замість 22 тонких:
1. Косметика + парфумерія + БАДи
2. Одяг + взуття + текстиль
3. Електроніка + гаджети + аксесуари
4. Дитячі товари + іграшки + канцтовари
5. Спорт + товари для дому + меблі
6. Хендмейд + подарунки + квіти
7. Авто + будматеріали + важкі
8. Продукти харчування + зоотовари + медобладнання

### 2.3 🟡 BACKLOG (P2, місяці 2-3)

- Marketplace triad: `/fulfillment-dlya-rozetka/`, `/fulfillment-dlya-prom-ua/`, `/fulfillment-dlya-olx/` (competitor research виявив як окремий axis)
- Amazon FBA Prep EN page
- `/tarify/` з публічним прайсом (не калькулятор — буквально прайс-таблиця)
- Content gap "відповідальне зберігання" (500-1K/mo uncovered)
- Поширення успішних UA постів на RU+EN

---

## 3. ЩО ЗМІНИЛОСЯ vs ПЛАН v1 (2026-03-27)

### 3.1 Що підтверджено ✅
- **UA-first стратегія** правильна — UA єдина мова де є трафік (16/29 кліків = 55%)
- **"Що таке фулфілмент" pillar** — #1 priority в v1 і v2
- **Калькулятор працює** — вже ранжується (pos 6.1 на keyword)
- **"Для інтернет-магазинів"** — правильний buyer intent (4 кліки)

### 3.2 Що спростовано ❌
- **EN як пріоритет "🟠 Medium"** — `EN має 55 сторінок, 1 клік`. Оптимально було б **заморозити EN backlog** і почати тільки 1 pillar EN hub.
- **22 вертикальні сторінки "для X"** — `жодна не дає трафіку`. План consolidate у 8 deep hubs (див. F вище).
- **"Чому Київ кращий" для Львів/Одеси** — GSC показує реальний search intent на ці міста. Треба full-fledged landings, не інформаційна відмазка.
- **Програматичне SEO з 1 шаблону** — план v1 пропонував генерувати 5-10 сторінок/день. Реальність: thin template pages не ранжуються (див. 22 вертикалі). **Unique deep content > template volume**.

### 3.3 Що було відсутнє в v1 і з'явилось тепер 🆕
- **Striking-distance оптимізація існуючого** (0 таких задач в v1, 9 в v2)
- **Zero-CTR fixes** (v1 не розглядав CTR як окрему проблему — тільки створення нових сторінок)
- **RU blog infrastructure** (v1 не мав RU blog плану)
- **Географія Дніпро/Харків** (v1 мав тільки Київ/Львів/Одеса/Бориспіль)
- **Brand search optimization** ("mtp" 0 CTR — v1 не вивчав brand signals)
- **Pillar consolidation** (v1 йшов на фрагментацію — v2 йде на deep hubs)
- **Competitor gap insights**: marketplace integrations, відповідальне зберігання, pricing transparency — все відсутнє у v1

---

## 4. НОВИЙ ПЛАН ВИКОНАННЯ (v2, 6 місяців)

### Phase 0 (цей тиждень): Quick wins — CTR/snippet
- [ ] Переписати home title + meta з ціною
- [ ] Organization schema на `/ua/` + `/` — для brand "mtp"
- [ ] Оновити `/ua/tsiny/` + `/ru/tsenu/` + `/en/prices/` meta з "від 9 грн"
- [ ] Claim Google Business profile "MTP Group Fulfillment"

### Phase 1 (тижні 1-4): P0 — головні прогалини
- [ ] `/ua/shcho-take-fulfilment/` pillar hub (3-4K слів, Editorial mood)
- [ ] `/ua/blog/scho-take-artykul-sku/` (striking distance pos 5.5)
- [ ] `/ua/blog/scho-take-sla-v-logistici/` (striking distance pos 8.2)
- [ ] Оптимізувати /ua/fulfilment-ukraina/ (pos 7.3 → 3)
- [ ] `/ua/fulfilment-dnipro/` (gap 72 imp/mo)
- [ ] RU версії перших трьох (pillar + 2 blog posts)

### Phase 2 (тижні 5-8): P1 — географія + marketplace + RU blog
- [ ] `/ua/fulfilment-kharkiv/` + `/ua/fulfilment-lviv/` + `/ua/fulfilment-odesa/` (повні landings, не "чому Київ кращий")
- [ ] RU blog infrastructure + 3 стартові пости
- [ ] Marketplace triad: `/ua/fulfilment-rozetka/` + `/fulfilment-prom/` + `/fulfilment-olx/`
- [ ] `/ua/3pl-ukraina/` (striking distance pos 9.8)

### Phase 3 (місяці 2-3): P1/P2 — consolidation + deep hubs
- [ ] Consolidate 6 existing `/fulfilment-dlya-*` → 3 deep hubs (косметика/б'юті, одяг/fashion, електроніка)
- [ ] Створити решту 5 deep hubs (з 8 запланованих)
- [ ] `/ua/tarify/` з публічною прайс-таблицею
- [ ] Amazon FBA Prep EN
- [ ] Content gap "відповідальне зберігання Київ"

### Phase 4 (місяці 4-6): EN rebuild + topic authority
- [ ] `/en/what-is-fulfillment-ukraine/` pillar hub (1 глибока, не 18 тонких)
- [ ] Переписати existing EN blog посилання в pillar
- [ ] Backlink campaign для topic authority
- [ ] 301 архівувати EN сторінки які не ранжуються

---

## 5. ФОРЕКАСТ (виведення трафіку в топ, як просив user)

**Поточний стан (90d, baseline)**: 29 clicks / 4,329 impressions / CTR 0.67% / avg pos 15

| Phase | Time | Очікувані clicks/month | Основний драйвер |
|-------|------|------------------------|-----------------|
| 0 (CTR fixes) | +2 тижні | 50-80 | Zero-CTR paradox розблокується |
| 1 (P0 pillar+SD) | +1 місяць | 120-180 | "Що таке фулфілмент" + "артикул" + "SLA" |
| 2 (RU blog+geo) | +2 місяці | 250-400 | RU відкривається + Дніпро/Харків |
| 3 (consolidation) | +3 місяці | 500-800 | Deep hubs ранжуються |
| 4 (EN rebuild+backlinks) | +6 місяців | 1,500-3,000 | Brand + topic authority + backlinks |

**Припущення**:
- Немає катастрофічних Google updates
- Backlink stratergy запущена в Phase 2+ (мінімум 15-30 якісних посилань)
- ContentCadence: 2 нові deep сторінки на тиждень + оптимізація 1 існуючої

**Якщо користувач хоче "забрати весь трафік на перших сторінках"** (прямий пріоритет): Phase 3 закриває основні buyer queries, Phase 4 б'є topic authority на рівень Unipost/Novapost. Реалістичний таргет — **топ-3 на 80% buyer queries за 9-12 місяців**.

---

## 6. ПОТОЧНИЙ СТАТУС ЗАВДАНЬ

### ✅ Виконано цього тижня
- GSC повний аудит (178 pages, 334 queries)
- Competitor research (20+ конкурентів)
- Tilda 301 clean sweep (59 legacy URLs → 132 redirects)
- Analytics cleanup (Fix A: en/thanks events, Fix B: 23 noscript iframes)
- CSP + preload performance optimization (попередні комміти)
- `docs/SEMANTIC_CORE_GSC_AUDIT.md` (base reference)

### ⏳ Очікує вашого рішення
- **Phase 0 quick wins** — можу запустити прямо зараз (1-2 години), б'є CTR паралельно з основною роботою
- **Phase 1 pillar** `/ua/shcho-take-fulfilment/` — скажіть `роби pillar` і запускаю UA+RU+EN в одній ітерації з Editorial mood

### 🗂 Як читати цей roadmap

Цей файл — **єдина точка входу**. Не треба відкривати 5 документів:
1. Секція 1 → що реально є
2. Секція 2 → що бракує і чому (з даними GSC)
3. Секція 3 → як змінилось від v1
4. Секція 4 → план по фазах
5. Секція 5 → форекаст
6. Секція 6 → що робити зараз

Інші файли (MTP_SEMANTIC_CORE_FULL.md, SEMANTIC_CORE_GSC_AUDIT.md, competitor-gap-research.md) — референси з деталями, читати за потребою.
