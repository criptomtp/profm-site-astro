# Tilda URL 301 Mapping Proposal — Drilldown Q6

**Джерело**: `docs/gsc/tilda-audit.json` — 90d GSC дані (20.01.2026 – 20.04.2026)
**Всього Tilda URLs**: 59 | **Клики**: 13 | **Покази**: 1910
**Статус**: **PENDING APPROVAL** — не пишемо redirects, доки юзер не скаже "approved".

---

## Принцип

GSC показує, **за якими запитами** Google досі індексує Tilda-URLs. Замість сліпого редіректу на `/blog/` hub, ми:

1. **301 SPECIFIC** (5 URLs, 1213 impr = 63% усього impr) → на **топічно-точну** сторінку, яка збереже рейтинг.
2. **301 HUB** (19 URLs, 542 impr = 28%) → на `/ua/blog/` або `/blog/` hub (хай Google сам перерозподілить).
3. **410** (35 URLs, 155 impr = 8%) → відразу gone, бо на них **0 кліків** і позиції 10+ (Google так і так викидає).

**Чому не всі просто 301 на hub**: 301 без топічної відповідності — це dilution. Google бачить hub без ключового слова "sla" і просто ігнорує сигнал. Специфічний редірект передає auth.

---

## 🔥 Tier 1 — SPECIFIC (5 URLs, критичні)

### 1. SLA в логістиці — **365 impr / 2 clk / pos 7.1** ⭐
- **From**: `/ua/blog/tpost/s7non1f0y1-scho-take-sla-v-logstits-chomu-tse-klyuc/`
- **Top queries**: sla, sla це, що таке sla, sla що це
- **Target**: `/ua/blog/post/scho-take-sla-v-logistici/` **(⚠️ TO BE CREATED — Week 1)**
- **EN source**: `/en/blog/post/what-is-sla-in-logistics.astro` (вже є) — писати UA з нуля, не переклад
- **Temp redirect (до створення UA post)**: `/ua/blog/` hub
- **Priority**: P0 — позиція 7.1 на 365 impr = реальний shot at page 1 топ-5

### 2. Артикул / SKU — **336 impr / 1 clk / pos 5.0** ⭐⭐
- **From**: `/ua/blog/tpost/2fz7njsgn1-scho-take-artikul-yak-pravilno-iogo-stvo/`
- **Top queries**: що таке артикул, артикул товару, артикул це
- **Target**: `/ua/blog/post/scho-take-artykul-sku/` **(⚠️ TO BE CREATED — Week 1)**
- **EN source**: `/en/blog/post/what-is-sku-article-number.astro` (вже є)
- **Priority**: **P0 ТОП** — pos 5.0 на 336 impr = якщо відновимо — page 1 гарантовано

### 3. Як відкрити інтернет-магазин (RU) — **295 impr / 1 clk / pos 24.1**
- **From**: `/blog/tpost/yzhv774pa1-kak-otkrit-internet-magazin-v-ukraine-os/`
- **Top queries**: как открыть интернет магазин, запуск интернет магазина
- **Target**: `/ru/blog/post/kak-otkrit-internet-magazin-v-ukraine/` **(⚠️ TO BE CREATED — Week 2, з RU blog)**
- **Temp redirect**: `/ru/` homepage
- **Priority**: P1 — pos 24.1 низька але impressions 295. Варто створити.

### 4. Товарний бізнес — **164 impr / 0 clk / pos 8.5**
- **From**: `/ua/blog/tpost/xz8vfk1jg1-tovarnii-bznes-v-ukran-osoblivost-ta-per/`
- **Top queries**: товарний бізнес в україні, що таке товарний бізнес
- **Target**: `/ua/blog/post/tovarnyi-biznes-v-ukraini/` **(⚠️ TO BE CREATED — Week 2)**
- **EN source**: `/en/blog/post/product-business-ukraine-guide.astro` (вже є)
- **Temp redirect**: `/ua/blog/` hub
- **Priority**: P1 — 0 кліків за 90д попри pos 8.5 означає поганий title/snippet. Переписуємо з нуля.

### 5. MTP Group бренд — **53 impr / 6 clk / pos 8.5 / CTR 11.32%** ⭐
- **From**: `/ua/blog/tpost/2lpu5l5sa1-mtp-group-dinii-v-ukran-servs-z-shvidko/`
- **Top queries**: mtp group (brand)
- **Target**: `/ua/about/` (вже існує)
- **Priority**: P0 — brand search, 6 кліків реальних, редіректимо одразу

---

## 🔵 Tier 2 — HUB (19 URLs, 542 impr)

Все на `/ua/blog/` або `/blog/` (зараз це 404) — **ми створюємо `/blog/` як UA hub** і спрямовуємо туди і root-legacy і ru-legacy (бо на старому сайті /blog/ була російська).

Але для чистоти: **всі `/ua/blog/tpost/*` → `/ua/blog/`**, **всі `/blog/tpost/*` → `/ua/blog/`** (тимчасово, з подальшою міграцією в RU blog).

Список 19 URLs у Tier 2 — див. `tilda-audit.json` (action=301_HUB). Серед них цікаві:

- `pdjm77ogc1-chto-takoe-sla-v-logistike` (RU, 98 impr) — дубль SLA, RU-версія. Target: **`/ru/blog/post/chto-takoe-sla/` (Week 2)**, до того — `/ru/`.
- `iyjgnyrmx1-rro-prro-dlya-bznesu` (56 impr, pos 36) — UA RRO topic. Маємо `/en/blog/post/fiscal-register-requirements-ukraine.astro`. Target UA версія — **P2**, hub until.
- `8emi42xu61-tovarnii-biznes...` (67 impr, RU) — дубль #4 в RU, target `/ru/` hub.
- `rjmgtrmvb1-fulflment-scho-tse` (15 impr, UA) — fulfillment UA. Target: `/ua/blog/post/scho-take-fulfilment/` (вже є!).

---

## ⚫ Tier 3 — KILL (35 URLs, 155 impr, 0 cumulative clicks)

Усі pos 20+ або impr < 10 без кліків. 301 на `/ua/blog/` все одно нічого не передасть — Google їх дедалі знижує. 

**Варіант A (recommended)**: bulk 301 → `/ua/blog/` (безпечно, нічого не втратимо, але і не виграємо).
**Варіант B (aggressive)**: 410 Gone → Google викидає з індексу за тиждень, звільняємо crawl budget.

Рекомендую **A** — redirect дешевий, ризик нульовий.

---

## 📋 Що потрібно від вас (approve/edit)

### ✅ Approve чи edit мапінг P0:

| # | From | → To | Status |
|---|------|------|--------|
| 1 | `/ua/blog/tpost/s7non1f0y1-scho-take-sla-v-logstits-chomu-tse-klyuc/` | `/ua/blog/post/scho-take-sla-v-logistici/` | **Створити UA post Week 1, temp → /ua/blog/** |
| 2 | `/ua/blog/tpost/2fz7njsgn1-scho-take-artikul-yak-pravilno-iogo-stvo/` | `/ua/blog/post/scho-take-artykul-sku/` | **Створити UA post Week 1, temp → /ua/blog/** |
| 3 | `/blog/tpost/yzhv774pa1-kak-otkrit-internet-magazin-v-ukraine-os/` | `/ru/blog/post/kak-otkrit-internet-magazin-v-ukraine/` | **Створити RU post Week 2, temp → /ru/** |
| 4 | `/ua/blog/tpost/xz8vfk1jg1-tovarnii-bznes-v-ukran-osoblivost-ta-per/` | `/ua/blog/post/tovarnyi-biznes-v-ukraini/` | **Створити UA post Week 2, temp → /ua/blog/** |
| 5 | `/ua/blog/tpost/2lpu5l5sa1-mtp-group-dinii-v-ukran-servs-z-shvidko/` | `/ua/about/` | **Одразу деплой** |

### ✅ Approve Tier 2 (19 bulk hub redirects)?

Всі → `/ua/blog/` (тимчасово, далі розподілимо як будуть UA/RU posts).

### ✅ Approve Tier 3 варіант A (35 bulk → /ua/blog/)?

Або варіант B (410 Gone)?

---

## Чому це важливо (TL;DR)

- **1910 imp / 13 clk** — це СПАДЩИНА з Tilda часів. Тобто навіть через 3+ роки 59 старих URL ще в індексі Google і дають трафік.
- Якщо ми зараз НЕ редіректимо → Google поступово викине їх з індексу → ми втратимо impressions разом з можливістю побороти за ці ж запити чистими URL.
- **Top 2 queries з вашої CS-семантики**: "sla" (365 impr, pos 7) і "артикул" (336 impr, pos 5) — це базові терміни логістики, і ми вже на першій сторінці з Tilda-URL. Забираємо їх на чисту URL → topic authority росте.
- Це відкриває шлях до домінування по всій семантиці фулфілменту — бо ми будемо тримати топ не лише по commercial, а й по informational queries.

---

**Очікую "approved"** для виконання:
- (A) тільки Tier 1 зараз (safe)
- (B) Tier 1 + Tier 2 (recommended)
- (C) все 3 tiers одразу (clean sweep, варіант A для Tier 3)
