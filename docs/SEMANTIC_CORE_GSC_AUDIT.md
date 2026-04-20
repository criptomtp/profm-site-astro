# Semantic Core Audit — GSC-Driven (90 днів)

**Період**: 2026-01-20 → 2026-04-20 (90d)
**Джерело**: Google Search Console API через `scripts/gsc-full-audit.py` + `gsc-opportunities.py`
**Сирі дані**: `docs/gsc/full-pages.json`, `full-queries.json`, `opportunities.json`

---

## 🚨 Головне відкриття

**Сайт зараз генерує лише 29 кліків / 4329 impressions / CTR 0.67% за 90 днів.**

Це приблизно **10 кліків на місяць** з органіки. Для B2B-бізнесу зі 170 сторінок і 3 мовами — **катастрофічно мало**. Але це означає також — там **величезний upside**, бо GSC фіксує 4329 impressions = Google нас ПОКАЗУЄ, просто не за тими запитами/сторінками, де є конверсія.

---

## 📊 Breakdown по мовам

| Мова | Pages | Impr 90d | Clicks 90d | CTR |
|------|-------|----------|------------|-----|
| **UA** | 53 | 1,547 | 16 | **1.03%** |
| **RU** | 13 | 590 | 2 | 0.34% |
| **EN** | 52 | 591 | 1 | **0.17%** ⚠️ |
| **root (legacy)** | 60 | 1,601 | 10 | 0.62% |

**Insight**: 52 англомовні сторінки дають 1 клік за 90 днів. Це **відсутність топіка/інтенту**, не обсягу контенту. Треба закрити EN-сегмент (тимчасово зупинити створення), поки не розберемось з UA/RU.

**legacy root** (Tilda-епоха) все ще дає 1601 impressions = **37% всіх показів**. Ми щойно перерозподілили це через 301-редіректи — Google покарбує ранжування протягом 2-4 тижнів. Важливо не втратити цей трафік через відсутність цільових UA/RU сторінок.

---

## 🔥 Top Opportunities — "Striking Distance" (pos 4-20, imp ≥ 30)

Запити де ми **майже** на page 1 і 0 кліків. Це найшвидші виграші — треба **тільки поправити CTR / переписати сторінку**, а не створювати новий контент.

| Query | Pos | Impr | Current page | Дія |
|-------|-----|------|--------------|-----|
| **артикул** | 5.5 | 119 | Tilda `/ua/blog/tpost/2fz7njsgn1-*` | **P0** → створити `/ua/blog/post/scho-take-artykul-sku/` |
| **sla** | 8.2 | 151 | Tilda `/ua/blog/tpost/s7non1f0y1-*` | **P0** → `/ua/blog/post/scho-take-sla-v-logistici/` |
| **sla це** | 6.5 | 95 | ^^ той самий Tilda | ^^ той самий UA post |
| **мтп** (UA lang) | 6.4 | 191 | `/ru/` homepage | **P0** → виправити RU title/snippet щоб brand search конвертив |
| **мтп** | 8.2 | 72 | `/` homepage | ^^ те саме на hardware рівні |
| **товарний бізнес** | 9.2 | 65 | Tilda `/ua/blog/tpost/xz8vfk1jg1-*` | **P1** → `/ua/blog/post/tovarnyi-biznes-v-ukraini/` |
| **товарный бизнес** (RU) | 8.9 | 51 | Tilda root `/blog/tpost/8emi42xu61-*` | **P1** → `/ru/blog/post/tovarnyi-biznes/` |
| **sla** (RU duplicate) | 10.3 | 36 | Tilda root `/blog/tpost/pdjm77ogc1-*` | **P1** → `/ru/blog/post/chto-takoe-sla/` |
| **фулфілмент** | 16.0 | 42 | `/` homepage (pos 13) | **P0** → homepage SEO rewrite (див. секцію нижче) |

---

## 🚨 Catastrophic zero-CTR на топ-3 позиціях

Це **не про контент** — це про **snippet / title / SERP features**. Ми ранжуємося на pos 1-4 і отримуємо **0 кліків**:

| Query | Pos | Impr | Clicks | Diagnosis |
|-------|-----|------|--------|-----------|
| **фулфилмент заказать** | 1.7 | 11 | 0 | 🔴 критично: ми #1-2, 0 CTR → title не матчить інтент "заказати" |
| **артикул це** | 2.2 | 61 | 0 | 🔴 snippet показує не відповідь, а блог з Tilda |
| **що таке артикул** | 2.3 | 21 | 1 | 4.76% CTR — краще, але могло б бути 20%+ |
| **скільки коштує складське зберігання для e-commerce** | 2.3 | 15 | 0 | 🔴 зросли, але без ціни в snippet клацати нікому |
| **фулфилмент цены** | 2.5 | 13 | 0 | 🔴 **КРИТИЧНО** — нет публічного прайсу, люди йдуть до конкурентів |
| **prom.ua** | 2.9 | 68 | 0 | Неочікуваний трафік. Snippet не залучає — ми для них не відповідь |
| **mtp** | 3.8 | 56 | 0 | Brand search, ймовірно SERP заслоняє Google Business |
| **фулфилмент украина** | 4.6 | 13 | 1 | Майже OK |

**Гіпотеза №1**: на запити з ціновим інтентом ("цены", "заказать", "скільки коштує") нас показують на pos 1-3, але ми **ховаємо ціни в калькулятор**. Конкуренти показують публічний прайс в snippet → отримують клік.

**Гіпотеза №2**: "мтп/mtp" бренд pos 3.8-6.9, 319 impr, 0 clicks — у SERP виходить Google Business profile з номером телефону. Люди **дзвонять не переходячи** (ми не бачимо цих конверсій в GSC, але побачимо в Ads conversion tracking через `tel:` click).

**Рекомендація**:
- **Fix C** — додати публічні базові ціни в meta description `/ua/tsiny/`, `/ru/tsenu/`, `/en/pricing/` (або створити якщо немає) + структурувати Organization schema зі Service + PriceSpecification
- **Fix D** — переписати title homepage: замість "MTP Group — Фулфілмент..." → "Фулфілмент в Україні від 16 грн — MTP Group" (ціна в title = +30-50% CTR)

---

## ❌ Ми НЕ на першій сторінці за основним ключем

| Ключовий запит | Поточна позиція | Impr 90d | Очікуваний top 3 |
|----------------|-----------------|----------|-------------------|
| **фулфілмент** | 16.0 | 42 | 300-500 impr/місяць |
| **фулфилмент** | 16.6 | 34 | 400-600 impr/місяць |
| **склад фулфилмент** | 16.5 | 31 | 150-250 impr/місяць |
| **фулфилмент интернет магазина** | 15.7 | 30 | 200-300 impr/місяць |
| **услуги фулфилмента** | 8.7 | 24 | 80-150 imp/місяць |

**Це AAA-пріоритет**. Сайт у назві має "fulfillment" але не ранжується в топ-10 за своє ядро. Це питання:
1. **Homepage H1/title** — чи точно "фулфілмент" там є у стратегічних місцях?
2. **Топікальна авторитетність** — недостатньо pillar + cluster pages
3. **Backlinks** — ймовірно нуль/мало сигналів на релевантні сторінки

---

## 🗺️ Географічні gap (Дніпро)

| Query | Pos | Impr | Dedicated page? |
|-------|-----|------|-----------------|
| фулфилмент днепр | 42.8 | 12 | ❌ |
| фулфілмент дніпро | 49.8 | 12 | ❌ |
| склад фулфілмент дніпро | 51.1 | 14 | ❌ |
| фулфилмент для интернет магазинов днепр | 50.8 | 12 | ❌ |
| **фулфілмент для маркетплейсов дніпро** | 58.3 | 22 | ❌ |

Загалом **72 impressions на місяць** за Дніпро-запитами. Немає ні однієї dedicated сторінки. Маємо `/ua/fulfilment-kyiv/` але не `/ua/fulfilment-dnipro/`.

**Рекомендація P1**: створити `/ua/fulfilment-dnipro/` + `/ru/fulfilment-dnepr/`. Якщо експансія географічна ще де-факто тільки Київ — писати як "фулфілмент для Дніпра з відправкою з Київського складу, 1-2 доби НП".

---

## 📦 Кластери товарних вертикалей — де трафік?

GSC показує **мінімальний трафік на існуючі `/ua/fulfilment-dlya-*` сторінки**:
- Лише `/ua/fulfilment-dlya-internet-magazynu/` — 72 impr, pos 26.9, 0 clicks
- Інші 21 vertical сторінок — НЕ засвітилися в 90d даних взагалі

**Висновок**: Наші 22 vertical сторінки або:
- Не проіндексовані (перевірити в GSC Coverage)
- Мають ідентичний контент — Google їх вважає doorway/thin
- Занадто нішеві запити які ще не були в жодному SERP

**Gap-запити що ми НЕ показуємося**:
- "фулфилмент для магазинов" — 19 impr pos 10.1 (так, показуємо) — але якась інша сторінка, не vertical
- "фулфилмент в товарном бизнесе" — 26 impr pos 13.3
- "фулфилмент для интернет магазина" — 26 impr pos 10.3

**Рекомендація**: замість нових 20 сторінок, **консолідувати 22 `/fulfilment-dlya-*` у 6-8 глибоких pillar-сторінок** (косметика, одяг, електроніка, marketplace, hazmat, small biz). 301 з тих що зникли → на pillar.

---

## 🏁 RU сегмент — найвища маржа upside

RU-сторінки: 13 pages / 590 impr / 2 clicks = **CTR 0.34%** (UA 1.03%).

RU запити які **НЕ захоплені взагалі**:
- "открыть интернет магазин" (17 impr pos 10.5)
- "как открыть интернет магазин" (15 impr pos 9.6)  
- "как создать интернет магазин" (15 impr pos 36.3)
- "как открыть интернет магазин в украине" (11 impr pos 12.1)
- "открыть свой интернет магазин" (13 impr pos 14.1)
- "что нужно чтобы открыть интернет магазин" (10 impr pos 10.2)

**Cумарно 81 impressions** за RU-запитами "як відкрити інтернет-магазин" — але ми ведемо їх на Tilda-блоги (яка тепер 301 на /ru/). **Треба створити `/ru/blog/` з першим постом саме за цим кластером**.

---

## 🌍 EN сегмент — треба пауза

EN: 52 сторінок, 591 impressions, **1 клік за 90 днів**.

Запити EN де ми показуємось але не конвертуємо:
- "packaging fulfillment" (16 impr pos 5.3, 0 CTR) — **виграшна позиція, треба title fix**
- "fulfilment service" (16 impr pos 20.3) — не dedicated page
- "how to calculate fulfillment cost per order" (24 impr pos 39.6) — блоговий інтент
- "fulfilment" / "fulfilment services" (16+14 = 30 impr)

**Рекомендація**: призупинити створення нових EN сторінок до того, як розбудемо UA/RU. Натомість:
1. Переписати existing `/en/fulfillment-for-marketplaces/` (139 impr pos 4.8, 0 CTR — найкраща EN сторінка за потенціалом)
2. Фікс title на `/en/` home (pos 10.5)
3. Амер-EU аудиторію домінувати **пізніше** — після того як UA/RU вивелися в топ по своєму ядру

---

## 🎯 PRIORITY MATRIX — що робити і в якому порядку

### P0 — Week 1-2 (маленький ефорт, великий ефект)

1. **UA blog post: `scho-take-artykul-sku`** (pos 5.5 → очікуємо pos 3, +50 clicks/mo)
2. **UA blog post: `scho-take-sla-v-logistici`** (pos 8.2 → очікуємо pos 5, +30 clicks/mo)
3. **Homepage UA/RU SEO rewrite**: додати "фулфілмент" в title/H1, додати ціну у meta description
4. **MTP brand snippet fix**: Organization schema + Google Business claim перевірка
5. **Analytics cleanup**: Fix A (en/thanks duplicate events) + Fix B (23 noscript iframes)
6. **Pricing page**: `/ua/tsiny/` / `/ru/tsenu/` з публічною базовою таблицею цін (від XXX грн/паллета, від XXX грн/заказ)

### P1 — Week 3-6 (середній ефорт)

1. **RU blog infrastructure** + 3 пости: "как открыть интернет магазин в украине", "что такое SLA", "товарный бизнес в украине"
2. **Dnipro geo-page**: `/ua/fulfilment-dnipro/` + `/ru/fulfilment-dnepr/`
3. **Pillar consolidation**: 22 `/fulfilment-dlya-*` → 8 глибоких сторінок з внутрішньою лінковкою
4. **Homepage перепис** з топіком: pillar + 8 cluster links для topic authority
5. **EN fix**: переписати `/en/fulfillment-for-marketplaces/` (pos 4.8 потенціал) + `/en/` home title

### P2 — Month 2-3 (великий ефорт, довгий горизонт)

1. **Blog content velocity**: 2 UA пости/тиждень на "striking distance" запити (opportunities.json має список)
2. **Featured snippet capture**: на всі "що таке X" запити додати структуровані визначення з FAQPage schema
3. **Backlink outreach** — без authority сайт не вийде в топ-3 за "фулфілмент" навіть з ідеальним контентом
4. **Amazon FBA Prep EN сторінка** (вже approved у Q2 drilldown)

---

## 🔮 Прогноз по cohorts

Якщо виконати P0+P1 (без backlink campaign):
- **Baseline**: 29 clicks/90d = 10/month
- **+P0 (6 тижнів)**: 50-80 clicks/month (5-8x)
- **+P1 (3 місяці)**: 150-250 clicks/month (15-25x)
- **+P2 без backlinks (6 місяців)**: 400-700 clicks/month
- **+P2 з backlinks (9-12 місяців)**: 1500-3000 clicks/month (топ-3 за "фулфілмент" = ~500 clicks/month один запит)

**Нагадую ваш ultimate goal**: "забрати повністю весь трафік на перших сторінках показу". Він реальний, але потребує **6-9 місяців** безперервної роботи + backlink investment.

---

## 📁 Додаткові дані

- `docs/gsc/full-pages.json` — всі 178 сторінок з impr/pos/queries
- `docs/gsc/full-queries.json` — всі 334 запити з position
- `docs/gsc/opportunities.json` — 9 striking-distance запитів
- `docs/gsc/tilda-audit.json` — 59 Tilda URLs (уже 301)
- `docs/gsc/tilda-301-mapping-proposal.md` — план редіректів
- `docs/gsc/competitor-gap-research.md` — **pending** (researcher agent ще працює)

---

## 🚦 Наступні рішення від вас

Чекаю approved по:

- **Fix A+B+C+D** (analytics cleanup + homepage/pricing snippet rewrite) — можу виконати зараз, 1 година роботи
- **P0.1 + P0.2** — починаю писати UA posts (SLA + артикул) після того як ви затвердите archetype (я рекомендую **Editorial** mood для both — educational intent)
- **P1.3 pillar consolidation** — це reorg з 22 сторінок у 8, ризик 301-chain і втрати тих що ранжуються. Обговорити?

Скажіть що в пріоритеті, або просто "роби P0" — і я запускаю все по черзі з деплоєм після кожного кроку.
