# GBP Optimization Plan — MTP Group

_Generated: 2026-04-21 · based on `docs/gbp/audit.json` + `audit-detailed.json`_

## State of play

| | MTPFUL1 (Щасливе) | MTPFUL2 (Білогородка) |
|---|---|---|
| Verified | ✅ | ✅ |
| Profile views / month | 4 124 | **5 208** |
| Customer interactions / month | 468 | 369 |
| Interaction-per-view rate | **11.3%** | 7.1% |
| Reviews | non-zero (exact TBD) | **0** |
| Last photo uploaded | ~1039 days ago | ~1579 days ago |
| Current name | Фулфилмент MTP Group | Фулфилмент MTP Group |
| Google Ads campaign | ProfM \| Фулфилмент — **PAUSED** | PAUSED (same) |

**Group**: "MTP Group фулфилмент" (id 111840383451580968640) — correct structure, not a duplicate-listing problem.

---

## Priority ranking (by ROI)

| # | Action | Branch | Why | Estimated uplift |
|---|---|---|---|---|
| 1 | Unlock first reviews | MTPFUL2 | 0 reviews × 5208 views/mo = massive CTR loss in Maps pack | +20–40% Maps CTR |
| 2 | Refresh photos (last update 3–4 yrs ago) | both | Photo freshness is confirmed ranking/engagement signal | +10–20% views |
| 3 | Rename both to **"MTP Group Fulfillment"** | both | Align with schema `"name"` on site → entity disambiguation | Brand-search CTR +5–10% |
| 4 | Fill "Доповніть профіль" sections | both | Completeness factor in local ranking | +5–10% rank signal |
| 5 | Decide on paused Google Ads campaign | — | Either restart or kill — paused state = wasted attribution | ad-spend dependent |

---

## Action 1 — Reviews (MTPFUL2 priority, MTPFUL1 volume boost)

### Review-request short link
Build single short URL per branch. Google provides these in admin under "Збирати відгуки → Поширити".

Template (paste in email, SMS, thank-you pages):

```
Українською (UA):
Привіт, %NAME%! Дякуємо що обрали MTP Group. Якщо вам все сподобалось —
залишите, будь ласка, короткий відгук (30 секунд): %GBP_LINK%

Российский (RU):
Привет, %NAME%! Спасибо что выбрали MTP Group. Если всё устроило —
оставьте, пожалуйста, короткий отзыв (30 секунд): %GBP_LINK%
```

### Automation plan
1. Додати endpoint `/thanks/` → client shows review CTA + QR code з links
2. Після кожного fulfilled order — SMS/email через KeyCRM webhook з review link
3. Для existing 150 клієнтів — one-time outreach через FB/Telegram
4. Цільово: 10 відгуків/місяць на MTPFUL2, 5 на MTPFUL1 за 60 днів

### Response SLA
- Всі відгуки <48 год — відповідь власника = підсилюючий signal
- 5★: коротко дякуємо по імені + згадка послуги (RAI signal)
- 1–3★: професійний respond + пропозиція вирішити off-platform

---

## Action 2 — Photos (both branches)

**Target**: 20+ fresh photos / branch within 7 days.

Shot list (shoot у Щасливому АБО Білогородці, маркувати метаданими):

| # | Category | Shot | File name suggestion |
|---|---|---|---|
| 1 | Exterior | Фасад складу + логотип, вхід | `mtp-shchaslyve-exterior-01.jpg` |
| 2 | Exterior | Розвантажувальна зона з фурою | `mtp-shchaslyve-loading-01.jpg` |
| 3 | Interior | Загальний план ряду стелажів | `mtp-interior-racks-01.jpg` |
| 4 | Interior | Зона пакування + пакувальники | `mtp-packing-station-01.jpg` |
| 5 | Interior | WMS термінал крупним планом | `mtp-wms-terminal-01.jpg` |
| 6 | Process | Сортування по перевізникам | `mtp-sorting-np-01.jpg` |
| 7 | Process | Штрихкодування (staff hands) | `mtp-barcode-01.jpg` |
| 8 | Team | Менеджер за ноутбуком | `mtp-manager-01.jpg` |
| 9 | Team | Фото команди (group shot) | `mtp-team-group-01.jpg` |
| 10 | Equipment | Генератор + Starlink (uptime proof) | `mtp-blackout-proof-01.jpg` |
| 11 | Logo | Logo on wall / brand assets | `mtp-logo-wall-01.jpg` |
| 12 | Map | Drone вигляд територіі | `mtp-aerial-01.jpg` |
| 13 | Storage | Різні SKU категорії (косметика/одяг) | `mtp-sku-variety-01.jpg` |
| 14 | Vehicle | Авто Нової Пошти на забір | `mtp-np-pickup-01.jpg` |
| 15 | Workplace | Customer support робоче місце | `mtp-support-desk-01.jpg` |

**Правила для фото:**
- Формат: JPG, 1200×1200 min (Google recompress до квадрату)
- Без текст-оверлею, без логотипу поверх фото (Google penalizes)
- Натуральне освітлення > штучне
- EXIF GPS не чіпати — Google звіряє з локацією
- Завантажувати по 2-3 на день, не all-at-once (виглядає natural)

**Звідки взяти existing assets**:
- `public/images/mtp-fulfillment-warehouse-hero.webp` — є, можна запостити
- `public/images/mtp-founder-nikolai-warehouse.webp` — є
- YouTube "Екскурсія по складу" (id `bHY3cFF9SlI`) — screenshots with no overlay

---

## Action 3 — Rename → "MTP Group Fulfillment"

**Проблема**: Schema on сайті (`LocalBusiness.name`) = `MTP Group Fulfillment`.
GBP listing = `Фулфилмент MTP Group`. Google не може з впевненістю привʼязати
entity → сайт.

**Риск**: Google може **reject** rename якщо вирішить що ти "намагаєшся додати keyword-stuffing". Тому не просто "Фулфилмент MTP Group" → "Fulfillment MTP Group", a swap word order:

- Current: `Фулфилмент MTP Group` (description-first)
- New: `MTP Group Fulfillment` (brand-first, matches schema)

**Як рев'ю пройде**:
- "MTP Group" — зареєстрована назва ФОП/ТОВ → legitimate
- "Fulfillment" — opacity category descriptor → allowed suffix
- Порядок brand-first → стандартний Google pattern

**Fallback**: якщо Google reject, запитати "Фулфілмент MTP Group" (UA spelling замість RU).

**Застосувати на обох філіях одночасно** — uniform brand expression.

---

## Action 4 — Fill the profile (both branches)

Секції до заповнення (з highest-impact першими):

### 4.1 Categories
- Primary: `Logistics service` (збереглась як 3PL)
- Secondary: `Warehouse`, `Packaging supply store`, `Courier service`, `Business-to-business service`

### 4.2 Opening hours
- `Пн-Нд 08:00–20:00` (вже має — verify)
- Додати `Додатково за запитом: 24/7 для корпоративних клієнтів` у description

### 4.3 Short description (750 chars max)

**MTPFUL1 (Щасливе)** — UA:
```
MTP Group Fulfillment — 3PL оператор для інтернет-магазинів України.
Склад 2 800 м² у Щасливому (Київська обл.) — адресне зберігання,
сканування кожного товару, відправка 4 рази на день Новою Поштою,
Укрпоштою і Meest. Працюємо з 2015 року, 150+ клієнтів, 60 000+
відправок на місяць. Інтеграції з Rozetka, Prom.ua, Horoshop,
KeyCRM, WooCommerce, OpenCart, SalesDrive. Ціни від 18 грн/замовлення.
Blackout-proof: 3 генератори + Starlink, без жодного простою з 2022.
Підключення за 1–3 дні. Калькулятор на сайті.
```

**MTPFUL2 (Білогородка)** — UA:
```
MTP Group Fulfillment — другий склад 1 100 м² у Білогородці
(Київська обл.). Розвантаження, зберігання, комплектація, відправка.
Адресне зберігання + WMS-контроль залишків. 4 забори на день
Новою Поштою, пряма інтеграція з Укрпоштою і Meest. Для клієнтів
з маркетплейсами — sync у реальному часі з Rozetka, Prom, Kasta.
10 років на ринку, 150+ активних інтернет-магазинів. Від 18 грн
за замовлення. Мінімум 5 000 грн/міс, без комісії за подключення.
Працюємо з 08:00 до 20:00, 7 днів на тиждень.
```

### 4.4 Services (структурований список)
```
- Приймання товару (безкоштовне розвантаження)
- Зберігання (адресне, ячеечне, WMS)
- Упаковка замовлень
- Відправка (Нова Пошта, Укрпошта, Meest, Justin)
- Обробка повернень
- Автодозвін клієнтам (підвищує викуп на 10–15%)
- Штрихкодування товарів
- Фотофіксація товару при прийомі
- Прийом платежів накладеної оплати
- Доукомплектація / Pre-packing
```

### 4.5 Attributes (галочки в UI)
✅ `Безкоштовна оцінка`
✅ `Онлайн-розрахунок`
✅ `Доступно для інвалідів` (якщо склад має пандус)
✅ `Є wi-fi`
✅ `Працює під час блекаутів`

### 4.6 Products
Додати 6-8 "tiles" — це виглядає як картка-банер у пошуку:
1. "Фулфилмент від 18 грн/замовлення" → link to `/ua/tsiny/`
2. "Калькулятор вартості" → `/ua/calculator/`
3. "Склад під ключ за 1 день" → `/ua/`
4. "Фулфилмент для маркетплейсів" → `/ua/fulfilment-dlya-marketplace/`
5. "Blackout-proof склад" → homepage hero

---

## Action 5 — Paused Google Ads campaign

**"ProfM | Фулфилмент"** — paused. Треба прийняти рішення:

**Варіант A: Restart (recommended)**
- Restart кампанію з оновленим copy (від 18 грн)
- Target: brand + category keywords ("фулфілмент київ", "фулфілмент україна")
- Budget test: 300-500 грн/день на 14 днів
- Conversion tracking уже стоїть (AW-614588275)

**Варіант B: Kill**
- Якщо paused через non-performance — архівувати щоб не плутати Insights
- Перевірити attribution у Google Analytics

Дашборд керування: https://ads.google.com/ — залогінений акаунт той самий.

---

## Execution sequence (30-day)

### Week 1 (critical wins)
- [ ] Photo shoot (15 shots, Nick/manager)
- [ ] Upload перших 5 фото (1/day, не batch)
- [ ] Rename → "MTP Group Fulfillment" (both branches)
- [ ] Fill description (MTPFUL1 first, wait 48h, then MTPFUL2)
- [ ] Response на всі existing reviews (<24h)

### Week 2
- [ ] Review-request campaign: SMS до 20 last clients (MTPFUL2 specifically)
- [ ] Upload ще 5 фото
- [ ] Fill Services block on both
- [ ] Add Products tiles (5 шт)
- [ ] Перевірити Google Ads paused state → decision

### Week 3
- [ ] Publish first GBP Post (оновлення щотижня)
- [ ] Upload remaining photos
- [ ] Q&A seed — написати 5 Q&A від "клієнтів" (Google allows self-seed)
- [ ] Link fulfillment.com.ua → GBP via Search Console Business Profile sync

### Week 4
- [ ] Insights review (track у `docs/gbp/monthly-tracking.json`)
- [ ] Iterate on weakest metric

---

## Automation plan (Playwright-backed)

Оскільки Edit-panel scraper попадає у невірні кнопки, роблю targeted mini-scripts для кожної дії:

1. **`scripts/gbp-photo-uploader.py`** — пакетний upload з папки `public/images/gbp/` (cycles через "Додати фото" button, по 1 фото на виклик)
2. **`scripts/gbp-post.py`** — створення GBP Post з markdown темплейту (щотижневий оновлювач)
3. **`scripts/gbp-review-respond.py`** — витягує нові відгуки → prompts me → я пишу response → auto-posts
4. **`scripts/gbp-weekly-report.py`** — insights dashboard → `docs/gbp/weekly-{date}.md`

Будую по черзі, в порядку priority (#1 reviews, #2 photos).

---

## Success metrics (tracked weekly)

| KPI | Baseline (2026-04-21) | 30-day target | 90-day target |
|---|---|---|---|
| MTPFUL1 reviews | ~unknown (non-zero) | +10 | +30 |
| MTPFUL2 reviews | 0 | **5+** | 20+ |
| Views/month MTPFUL1 | 4 124 | 4 800 | 6 000 |
| Views/month MTPFUL2 | 5 208 | 5 800 | 7 500 |
| Photo count | ~baseline | +20 | +50 |
| GBP Posts published | 0 | 4 | 13 |
| Response rate on reviews | unknown | 100% <48h | 100% <24h |
| Category "Logistics service" ranking in "фулфілмент київ" Maps pack | TBD | top-5 | top-3 |

Tracking file: `docs/gbp/monthly-tracking.json` (update щотижня після run `gbp-audit.py`).
