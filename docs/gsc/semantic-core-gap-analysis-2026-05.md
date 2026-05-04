# Semantic Core × GSC — Gap Analysis & Refined Tier 1
**Дата:** 2026-05-04
**Інпут:** `docs/MTP_SEMANTIC_CORE_FULL.md` (121 цільових сторінок) + GSC дані за квітень 2026

---

## 1. Поточний стан семантичного ядра

| Категорія | Цільових сторінок | Done ✅ | Покриття |
|---|---:|---:|---:|
| За товаром (вісь 1) | 26 | 2 | 12% |
| За бізнесом (вісь 2) | 16 | 3 | 19% |
| За каналом (вісь 3) | 12 | 2 | 17% |
| За послугою (вісь 4) | 17 | 4 | 24% |
| За географією (вісь 5) | 8 | 2 | 25% |
| Інформаційні (вісь 6) | 24 | 11 | 46% |
| EN версії (вісь 7) | 18 | 8 | 44% |
| **ВСЬОГО** | **121** | **32** | **27%** |

**88 сторінок ще треба зробити.** Питання — у якому порядку. Старий план базувався на гіпотезах, тепер маємо реальні GSC сигнали.

---

## 2. КРИТИЧНІ ВІДКРИТТЯ — що GSC показав про "приховані можливості"

### 🔥 GAP №1 — `доставка в Молдову з України` (РЕЗОНАНСНА сторінка)

**Семантичне ядро:** покрите слабко, тільки `/ua/mizhnarodna-dostavka/` (#70, 🔵 backlog)

**GSC:** 
- "prom ua доставка в молдову" — **989 imp, pos 7.7, 0 кліків** (квітень)
- "rozetka com ua доставка в молдову" — 120 imp pos 11.7
- **Combined: 1,109 imp у топ-10 БЕЗ dedicated landing**

**Що відбувається:** Користувачі шукають як отримати товар з Prom/Rozetka в Молдову. Ми ранкуємо випадково (через сторінки fulfilment-prom і chto-takoe-fulfilment), але CTR = 0% бо запитувач не бачить релевантного відповіді.

**Дія:** Створити `/ru/dostavka-v-moldovu-iz-ukrainy/` ASAP. Це **найвищий ROI з усіх існуючих gaps**.

---

### 🔥 GAP №2 — `B2B фулфілмент` (РЕАЛЬНА аудиторія, semantic core 🟠 у Tier 1)

**Семантичне ядро:** `/ua/b2b-fulfilment/` (#30) — 🟠 priority, не зроблено

**GSC сигнали (квітень):**
- "b2b фулфілмент в україні" — 3 imp pos 50.3
- "послуги фулфілменту для b2b" — 3 imp pos 71.0
- "b2b фулфілмент" — 1 imp pos 55
- "b2b fulfillment in ukraine" — 1 imp pos 20.0

**Аналіз:** Маленький volume в квітні, АЛЕ pos 20-71 показує що Google нас бачить за цими queries — просто на дальніх сторінках. Зробити dedicated landing → з pos 50 в pos 10-15 за 2-4 тижні.

**Дія:** `/b2b-fulfilment/` (UA + RU + EN) — Tier 1 пріоритет, відповідає семантичному ядру.

---

### 🔥 GAP №3 — `Геолокація: Дніпро, Харків, Запоріжжя`

**Семантичне ядро:** МАЄ ПРОБЛЕМУ. У вісі 5 (География) тільки Київ, Бориспіль, Білогородка, Київська область (#72-77), а Lviv #78 і Odesa #79 описані як "інформаційні: чому Київ краще".

**GSC показує реальну (недопокриту) демандну картину:**

| Запит | Imp | Pos | Має landing? |
|---|---:|---:|---|
| фулфилмент киев | 145 | 37.5 | / (home) — не геолендинг |
| фулфилмент днепр | 29 | 41.1 | ❌ |
| фулфілмент дніпро | 19 | 43.5 | ❌ |
| склад фулфілмент дніпро | 33 | 48.2 | ❌ |
| фулфілмент для маркетплейсов дніпро | 46 | 56.5 | ❌ |
| фулфилмент для интернет магазинов днепр | 29 | 47.9 | ❌ |
| склад фулфилмент днепр | 16 | 36.5 | ❌ |
| фулфілмент логістика дніпро | 17 | 43.4 | ❌ |
| фулфилмент запорожье | 17 | 51.9 | ❌ |
| фулфілмент запоріжжя | 3 | 12.0 | ❌ |
| фулфилмент харьков | (long-tail) | — | ❌ |

**Реальний стан:** ~370 imp/місяць по Дніпру + Запоріжжю + Харкову у pos 30-100 без жодного dedicated landing.

**Дія:** Оновити семантичне ядро — додати `/fulfilment-dnipro/`, `/fulfilment-kharkiv/`, `/fulfilment-zaporizhzhia/` як commercial landings (не просто "інформаційні чому Київ краще"). Lviv і Odesa теж потребують реальних landings, а не редиректів-приманок.

---

### 🔥 GAP №4 — `Packaging fulfillment` (EN, semantic core 🟡)

**Семантичне ядро:** `/ua/pakuvannya/` (#64) — 🟡

**GSC:** 
- "packaging fulfillment" — **216 imp, pos 32.6** (EN)

**Аналіз:** Сильний international intent. Ми ранкуємо на /en/guide/ — generic guide, не targeted. Створити `/en/packaging-fulfilment-ukraine/` + UA+RU equivalents.

---

### 🟡 GAP №5 — `ФОП фулфілмент`

**Семантичне ядро:** `/ua/fulfilment-dlya-fop/` (#34) — 🟠 в Tier 1 (Apr 30)

**GSC:** Прямих кліків у квітні мало, АЛЕ:
- "рро для фоп что это" 22 imp pos 46.7 (РРО для ФОП — adjacent intent)
- "як легально вести онлайн бізнес" 8 imp pos 13.1

**Аналіз:** 70% UA e-commerce = ФОП. Запит ще не визрів через свіжість домену в GSC, але буде. Створити landing зараз як preemptive move.

---

### 🟡 GAP №6 — `Електроніка фулфілмент`

**Семантичне ядро:** `/ua/fulfilment-dlya-elektroniky/` (#3) — 🟠 в Tier 1

**GSC:** Прямих сигналів мало в квітні, АЛЕ висока коммерційна цінність ніші. Aspirational запит — створити для майбутнього SEO-equity.

---

### 🟢 ГОТОВІ КЛАСТЕРИ — де ми вже добре стоїмо

| Кластер | Best pos | Сторінок | Дія |
|---|---:|---|---|
| Бренд (`mtp`, `мтп`, `mtp group`) | 1.3-7.5 | / (home) | Тримати, не псувати |
| `товарний бізнес` (UA+RU) | 6.4-9.6 | 2 blogs | CTR rescue зробили |
| `артикул товару` (UA+RU) | 4.3-6.2 | 2 blogs | CTR rescue зробили |
| `що таке SLA` | 6.2-7.9 | 2 blogs | CTR rescue зробили |
| `доставка в Молдову` (через NP) | 7.7 | 0 dedicated | СТВОРИТИ landing! |
| `kasta.ua international` | 9.7 | 0 dedicated | СТВОРИТИ landing |
| `prom.ua api` | 7.7 | EN guide | wrong-intent, окреме рішення |

---

## 3. РЕВІЗОВАНИЙ TIER 1 (наступні 30 днів) — data-driven

Поєднання: оригінальний Tier 1 (Apr 30) + GSC сигнали + стратегічна вага

| # | Сторінка | Aize | GSC сигнал | Очікуваний impact | Estim години |
|---|---|---|---|---|---:|
| **1** | `/ru/dostavka-v-moldovu-iz-ukrainy/` (RU primary, UA equiv) | новий, оновлення ядра | **989 imp pos 7.7 без landing** = найбільший immediate ROI | +50-100 кліків/тиждень за 14 днів | 3-4 |
| **2** | `/b2b-fulfilment/` cluster (UA+RU+EN) | вісь 2 #30 🟠 | "b2b фулфілмент в україні" pos 50 + 4 variants | +30-50 imp/тиждень за 30 днів | 5-6 |
| **3** | `/fulfilment-dnipro/` cluster (UA+RU+EN) | додати в ядро | 188 imp combined geo Дніпро | +200-300 imp/тиждень за 30 днів | 4-5 |
| **4** | `/fulfilment-dlya-fop/` (UA+RU) | вісь 2 #34 🟠 | preemptive (70% e-com=ФОП) | +50-100 imp/міс через 60 днів | 3-4 |
| **5** | `/fulfilment-kharkiv/` cluster (UA+RU+EN) | додати в ядро | 80 imp combined geo Харків | +50-100 imp/тиждень за 30 днів | 4-5 |
| **6** | `/komplektatsiya-zamovlen/` (UA+RU) | вісь 4 #59 🟠 | базова послуга, semantic gap | +30-50 imp/міс | 3 |
| **7** | `/3pl-boryspil/` (UA+RU+EN) | вісь 5 #73 🟠 | unique USP angle "склад біля аеропорту" | +20-40 imp/міс | 3-4 |
| **8** | `/fulfilment-dlya-elektroniky/` (UA+RU) | вісь 1 #3 🟠 | high-value niche | +30-50 imp/міс | 3-4 |
| **9** | `/fulfilment-zaporizhzhia/` cluster (UA+RU) | додати в ядро | 50+ imp prefronlinе region | +30 imp/міс + резонансний angle "війна" | 3-4 |
| **10** | `/en/packaging-fulfilment-ukraine/` (+UA+RU) | вісь 4 #64 🟡 | "packaging fulfillment" 216 imp pos 32.6 (EN) | +50-100 imp/тиждень за 30 днів | 3-4 |

**Загалом:** ~10 кластерів × 2-3 мови = 25-30 нових сторінок за 30 днів. Час: ~35-45 годин роботи.

**Прогноз impact:** +600-1000 imp/тиждень baseline + 100-200 кліків/тиждень за 60 днів.

---

## 4. ЗМІНИ ДО СЕМАНТИЧНОГО ЯДРА (треба внести)

### 4.1 Вісь 5 (Географія) — додати реальні landings:

**Зараз:** Lviv #78 і Odesa #79 описані як "(інформаційна: чому Київ краще)" — це слабка стратегія.

**Замінити на:**
- `/fulfilment-dnipro/` 🟠 (commercial landing, не інформаційна)
- `/fulfilment-kharkiv/` 🟠
- `/fulfilment-zaporizhzhia/` 🟡 (унікальний angle "прифронтовий регіон → київський хаб")
- `/fulfilment-lviv/` 🟡 (REWRITE: commercial, не "чому Київ краще")
- `/fulfilment-odesa/` 🟡 (те саме)

**Логіка:** GSC показав ~370 imp/місяць по геомодифікаторах. Робити "інформаційну сторінку чому Київ краще" — це втрата 100% commercial intent. Краще робити повноцінні commercial landings з explicit geo-targeting.

### 4.2 Вісь 4 (Послуги) — додати:

- `/dostavka-v-moldovu-iz-ukrainy/` 🟠 (new — окремо, не лише як підрозділ "міжнародна доставка")
- `/dostavka-v-kazakhstan-iz-ukrainy/` 🟡 (CIS expansion)
- `/dostavka-v-belarus-iz-ukrainy/` 🟡

### 4.3 Вісь 7 (EN) — додати:

- `/en/fulfilment-for-cis-brands/` 🟠 (consolidated landing для брендів СНГ що йдуть в UA — зараз розкидано по pages)
- `/en/packaging-fulfilment-ukraine/` 🟡 (під "packaging fulfillment" 216 imp signal)
- `/en/kasta-international-shipping/` 🟡 (під 127 imp signal)

---

## 5. ШВИДКІ HIGH-VOLUME WINS (паралельно з новими landings)

Окрім нових сторінок, ці switch-on changes можна зробити за 1-2 години на наступному тижні:

1. **CTR Rescue для додаткових 5 striking-distance pages** з GSC аналізу:
   - "склад фулфилмент" pos 10.8 на UA home → секція "Склад фулфілмент"
   - "услуги фулфилмента" pos 12.3 на /ru/services/ → CTR-driving title (вже зроблено)
   - "fulfilment services" pos 14.1 EN home → CTR title (вже зроблено)
2. **Внутрішнє лінкування під ці striking distance** — додати посилання з 5+ authority pages з anchor text "склад фулфілмент", "услуги фулфилмента" тощо.

---

## 6. ЩО НЕ РОБИТИ (semantic core є але GSC показує що не варто зараз)

| Сторінка | Чому skip | Альтернатива |
|---|---|---|
| `/ua/fulfilment-supplement/` (#21 🟡) | ризикова ніша, низький search volume | Включити в /ua/fulfilment-dlya-kosmetyky/ як секцію "БАДи" |
| `/ua/fulfilment-knyzhok/` (#9 🔵) | вже видалили в Apr (cannibalisation) | Не повертати |
| `/ua/fulfilment-budmaterialiv/` (#12 🔵) | дуже специфічна ніша | Wait for organic demand signals |
| `/ua/fulfilment-amazon/` (#51 🔵) | реалістично не можемо обслуговувати FBA | Включити в /en/fulfillment-ukraine/ як FAQ |
| `/ua/fulfilment-tiktok-shop/` (#47 🟡) | TikTok Shop ще не запущено в UA | Wait for TikTok Shop UA launch |

---

## 7. РЕЗЮМЕ — що змінилось з Tier 1 (Apr 30)

**Стара Tier 1 (10 пунктів, hypothesis-driven):**
1. /fulfilment-dlya-odyahu/ ✅ Done
2. /fulfilment-dlya-elektroniky/ — все ще в плані (зараз #8)
3. /fulfilment-sonyachni-paneli/ — DEPRIORITIZED (тільки 1 кейс EcoDrive, не масовий запит)
4. /b2b-fulfilment/ — зараз #2 (підтверджено GSC)
5. /fulfilment-dlya-fop/ — зараз #4 (підтверджено)
6. /komplektatsiya-zamovlen/ — зараз #6
7. /3pl-boryspil/ — зараз #7
8. /fulfilment-dlya-startapiv/ — DEPRIORITIZED (низькі сигнали)
9. /blog/case-kosmetyka/ — DEPRIORITIZED (blog vs commercial landing)
10. /en/blog/ukraine-3pl-hub-europe/ — DEPRIORITIZED (Blog AI-magnet, але не immediate ROI)

**Нова Tier 1 (data-driven):**
- Молдова landing — REPLACED #1 (immediate massive ROI)
- B2B — REPRIORITIZED #2 (GSC validated)
- Geo cluster Dnipro/Kharkiv/Zaporizhia — NEW additions (real demand)
- ФОП — REPRIORITIZED #4
- Електроніка — REPRIORITIZED to #8 (hypothetical, не GSC-validated yet)
- Packaging EN — NEW addition (216 imp pos 32.6)

---

## 8. РЕКОМЕНДАЦІЯ — ритм виконання

**Тиждень 1 (5-11 травня):** 
- Молдова landing (Tier 1 #1) — вже в попередньому memo
- Dnipro cluster start — UA версія
- 2026-05-09 GSC delta аналіз

**Тиждень 2 (12-18 травня):**
- Dnipro RU + EN
- B2B-fulfilment UA + RU
- Kharkiv cluster start

**Тиждень 3 (19-25 травня):**
- B2B EN + ФОП UA + RU
- Запоріжжя cluster
- Komplektatsiya zamovlen UA + RU

**Тиждень 4 (26 травня - 1 червня):**
- 3PL Boryspil cluster
- Електроніка UA + RU
- Packaging EN
- Monthly trend analysis re-run (`gsc-trend-analysis.py` + `gsc-excel-export.py`)

**Cycle exit (~1 червня):** ~25 нових сторінок, очікуваний загальний impact +500-800 imp/тиждень baseline + +200 кліків/тиждень.
