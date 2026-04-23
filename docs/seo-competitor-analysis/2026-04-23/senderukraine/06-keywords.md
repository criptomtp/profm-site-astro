# Sender Ukraine — Keyword Footprint Analysis

**Competitor:** https://senderukraine.com
**Analyzed:** 2026-04-23
**Analyst context:** MTP Group (fulfillmentmtp.com.ua) — direct 3PL fulfillment competitor in Ukraine
**Method:** curl homepage + /prices + /how-it-works + /faq + /contacts + /blog + /sitemap.xml; extract `<title>`, `<meta description>`, `<h1>`, `<h2>`, `<h3>`, integration-block alts, FAQ labels, blog post titles

---

## 1. Sitemap Reality Check

Sender Ukraine's `/sitemap.xml` exposes **only 6 URLs**:

```
https://senderukraine.com/                (priority 1.0, lastmod 2024-02-08)
https://senderukraine.com/how-it-works    (0.5, 2024-02-08)
https://senderukraine.com/prices          (0.5, 2024-02-08)
https://senderukraine.com/faq             (0.4, 2024-02-08)
https://senderukraine.com/contacts        (0.5, 2024-02-08)
https://senderukraine.com/blog            (0.3, 2024-02-08)
```

**Key observations:**
- No individual blog-post URLs in sitemap (blog posts exist on `/blog/{slug}` but not declared — indexability suffers)
- No service sub-pages (no `/fulfillment-dlya-marketpleysov`, no city pages, no industry pages)
- `/tarify` returns 404 — only `/prices` exists; RU speakers searching "тарифы" may land on 404
- `lastmod` frozen at Feb 2024 — site is effectively static, not actively SEO-maintained
- No hreflang split in sitemap (they have `/uk/` `/ru/` `/en/` variants hardcoded in `<link rel="alternate">`, but the root URLs default to Russian-language content)

**Verdict:** Sender's SEO surface area is ~6× smaller than MTP's. They compete primarily on brand + platform differentiation, not on keyword breadth.

---

## 2. Page-by-Page Metadata

### Homepage `/`
- **Title:** `Фулфилмент для интернет-магазинов в Украине - Sender Fulfillment`
- **Description:** `Более 5 лет предоставляем услуги фулфилмента для интернет-магазинов. Легкий старт работы и доступные тарифы ☎ +38(063)595-32-32 ✔ Хранение товаров ✔ Комплектация ✔ Отправка ✔ Доставка`
- **H1:** `Фулфилмент в Украине`
- **Key H2/H3:** `Личный кабинет Sender Fulfillment`, `Заказы`, `Товарные остатки`, `Статистика`, `Интеграции`, `Мобильное приложение`, `Галерея`, `Сравнение с другими фулфилмент компаниями`, `Преимущества Sender`, `Отзывы наших клиентов`, `Основные вопросы и ответы`
- **Entities named:** Nova Poshta, Ukrposhta, Rozetka, Prom UA, Shopify, Horoshop, Salesdrive, Key CRM, Sitnix CRM, Checkbox, Turbo SMS, Telegram, KeepinCRM, Lp CRM, SMS-fly, Мій Дроп — **16 integration logos**, claim of "более 20 интеграций"
- **Mobile app:** iOS (App Store id6744337675) + Android (Google Play `com.senderfulfillment.sender_fulfillment_app`)
- **Comparison table row:** "Мобильное приложение" — Sender YES vs competitors NO

### `/prices`
- **Title:** `Тарифы и цены на фулфилмент - Sender Fulfillment`
- **Description:** `Фулфилмент - цены. Сколько стоят услуги фулфилмента? Фулфилмент в Украине...`
- **H1:** `Тарифы и цены`
- **Pricing transparency:** 23 грн/обработка заказа, 20 грн/м³/день хранение, 2 грн/приемка, 350 грн курьер по Киеву, min payment 2600 грн при <99 заказов/мес
- **Unique hook:** "Первый месяц бесплатный" (1 м³ storage + 10 orders комплектация)
- **Range slider** dynamic pricing calculator embedded on page (JS-driven)

### `/how-it-works`
- **Title:** `Как работает Фулфилмент - Sender Fulfillment`
- **H1:** `Как это работает`
- **H2:** `Наши услуги`, **H3:** `Шаг 1/2/3` — classic 3-step explainer

### `/faq`
- **Title:** `Вопросы и ответы - Sender Fulfillment`
- **H1:** `Основные вопросы`
- **9 FAQ items (all Russian):**
  1. Как происходит отправка заказов?
  2. Когда отправляются заказы?
  3. В какую упаковку комплектуется заказ?
  4. Какое количество заказов в месяц нужно иметь?
  5. Какие услуги нужно оплачивать кроме обработки заказов?
  6. Как происходит оплата услуг?
  7. Как рассчитывается тариф за обработку заказов и хранение?
  8. Как контролировать списание средств?
  9. Есть ли минимальный ежемесячный платеж?

### `/contacts`
- **Title:** `Контактная информация - Sender Fulfillment`
- **H1:** `Контактная информация`
- Phone: +38(063)595-32-32 only (no address/directions block extracted)

### `/blog`
- **Title:** `Блог - Sender Fulfillment`
- **H1:** `Блог`
- **5 posts visible on listing page:**
  1. ТОП-5 лучших сервисов для создания интернет-магазина
  2. CRM-система для интернет-магазина: контроль за заказами, клиентами и ростом
  3. Сочетание Sender Fulfillment с SITNIKS CRM: Оптимизация бизнеса в два клика
  4. Автоматизация интернет-магазина: ТОП украинских CRM-систем
  5. Что такое фулфилмент? Преимущества, недостатки, кому подойдет

---

## 3. Ranking Intents Sender Targets

Mapped by page:

| Page | Primary intent | Secondary intent |
|---|---|---|
| `/` | `фулфилмент украина`, `фулфилмент для интернет-магазинов` | брендинг "Sender Fulfillment", личный кабинет, мобильное приложение |
| `/prices` | `фулфилмент цены`, `фулфилмент тарифы`, `сколько стоит фулфилмент` | первый месяц бесплатно, расчёт стоимости |
| `/how-it-works` | `как работает фулфилмент`, `что такое фулфилмент` | шаги подключения |
| `/faq` | длиннохвостые вопросы по процессу (упаковка, отправка, оплата) | — |
| `/contacts` | brand-только | локация Киев |
| `/blog` | информационные запросы: "crm для интернет-магазина", "топ сервисов для интернет-магазина", "что такое фулфилмент", "автоматизация интернет-магазина" | интеграционные (Sitnix + Sender) |

**Primary keyword cluster:** `фулфилмент` (Russian transliteration) + Ukraine/Kyiv + "для интернет-магазинов" + "цены/тарифы".

**Secondary cluster (unique to Sender):** platform/SaaS-side — `личный кабинет фулфилмент`, `мобильное приложение фулфилмент`, `интеграция Horoshop фулфилмент`, `API фулфилмент`, `CRM интеграция фулфилмент`.

**Tertiary cluster (blog):** intent = "research before choosing vendor" → CRM/platform comparisons + fulfillment explainers. They are NOT blogging about industries, geography, or seasonal logistics.

---

## 4. MTP vs Sender — Coverage Comparison

### MTP Group has — Sender doesn't (inventory of MTP's moat)

MTP's UA page set:
```
/              (home UA)
/about/         /api-docs/      /calculator/
/chto-takoe-fulfilment/         /fulfilment-dlya-internet-magazynu/
/fulfilment-dlya-kosmetiki/     /fulfilment-dlya-malogo-biznesa/
/fulfilment-dlya-marketpleysov/ /fulfilment-kiev/
/fulfilment-ukraina/            /fulfilment-vazhkykh-tovariv/
/paletnoe-khranenie/            /3pl-logistika/
/skladskie-uslugi/              /tsenu/
/services/                      /faq/                /guide/
/glossariy/                     /recalls/            /privacy/
```
Plus `/ua/*` mirrors (UA-language), `/ru/*`, `/en/*` — full tri-lingual, ~22+ service/landing pages per locale.

**What MTP covers that Sender doesn't:**
- **Industry verticals:** cosmetics, heavy goods, small business, marketplaces (Sender = none)
- **Service types:** 3PL logistics, pallet storage, warehouse services, recalls (отзыв товара) (Sender = none)
- **Geo:** Kyiv city landing page (Sender mentions Kyiv only in contact info)
- **Dedicated calculator page** with persistent URL (Sender has embedded JS on /prices only)
- **Glossary / guide content** (Sender has none)
- **API/developer docs** as standalone page (Sender mentions API inline, no dedicated page)
- **Trilingual coverage** with hreflang policy (Sender's /uk/ /ru/ /en/ are cosmetic language switchers on the same 6 pages)
- **Blog depth:** MTP has 15+ English blog posts alone (fiscal register, peak season, fraud protection, returns reduction, reviews, Russian service replacement, marketplaces); Sender has 5 posts on listing page total
- **Schema/markup depth** (based on prior audit reports)

### Sender has — MTP doesn't (where Sender wins)

- **Explicit "platform/SaaS" positioning:** `Личный кабинет Sender Fulfillment` as an H2 branded product with screenshots of "Заказы", "Товарные остатки", "Статистика" tabs
- **Mobile app for clients:** iOS + Android downloads, "Мобильное приложение" as a comparison-table advantage
- **Integration logos showcase:** 16+ named platforms on homepage (Horoshop, Shopify, Prom, Rozetka, Salesdrive, Key CRM, Sitnix CRM, KeepinCRM, Lp CRM, Checkbox POS, Turbo SMS, SMS-fly, Telegram, Мій Дроп, Nova Poshta, Ukrposhta)
- **"Сравнение с другими фулфилмент компаниями"** comparison table — direct-attack SEO page targeting "фулфилмент сравнение" intent
- **"Первый месяц бесплатно"** offer — direct-response angle
- **CRM-integration blog content** — capturing "CRM для интернет-магазина" informational traffic
- **Dynamic price-slider calculator** embedded inline (no separate URL, but better UX)
- **Gallery / warehouse photos** (Sender has `<h3>Галерея</h3>` section)

---

## 5. Sender's Unique Positioning → Keyword Angle

Sender's brand is **"fulfillment-as-a-platform"** — they market the client dashboard, mobile app, and 20+ integrations as the product, with warehouse ops as backend. This implies they rank (or should rank) on **platform-side queries** that MTP under-serves:

- `личный кабинет фулфилмент` / `особистий кабінет фулфілмент` / `fulfillment dashboard Ukraine`
- `мобильное приложение для фулфилмента` / `fulfillment mobile app`
- `фулфилмент интеграция horoshop` / `horoshop фулфилмент api`
- `фулфилмент с prom.ua интеграцией` / `фулфілмент prom`
- `фулфилмент keycrm интеграция` / `keycrm фулфилмент`
- `фулфилмент salesdrive интеграция`
- `фулфилмент api`
- `автоматизация интернет-магазина фулфилмент`
- `фулфилмент с crm интеграцией`

This is the "tech-forward SaaS" angle MTP has not explicitly claimed in URL/title structure. MTP's `/api-docs/` page exists but doesn't rank for integration-name queries.

---

## 6. Queries Sender Likely Ranks For (MTP Should Also Target)

Prioritized by commercial intent × MTP's realistic ability to outrank:

1. **`фулфилмент цены`** / `фулфилмент тарифы` / `сколько стоит фулфилмент` — Sender has a dedicated /prices page with visible numbers (23 грн, 20 грн/м³); MTP has `/tsenu/` and `/calculator/` but Sender's transparent-pricing page format wins the snippet game. **MTP action:** enrich `/tsiny/` with an H2 price table matching Sender's structure (order processing / storage / acceptance / courier) + "первый месяц бесплатно"-type hook if commercially viable.
2. **`первый месяц фулфилмент бесплатно`** (long-tail, high intent) — Sender owns this pattern. **MTP action:** if free-trial offer possible, create `/besplatnyj-mesyats/` or embed a similar promo block in `/tsiny/`.
3. **`фулфилмент сравнение`** / `фулфилмент компании сравнение` — Sender has an on-page comparison table. **MTP action:** build `/porivnannia-fulfilment-kompaniy/` (UA) + RU/EN versions — a neutral-looking comparison page (Sender does this exact move).
4. **`личный кабинет фулфилмент`** — Sender explicitly H2s this. **MTP action:** add client-portal screenshot section with "Особистий кабінет MTP" on home + consider dedicated landing if MTP has a client portal.
5. **`мобильное приложение фулфилмент Украина`** — Sender's unique moat (iOS + Android). **MTP action:** if MTP has or can ship a PWA/app, own this keyword; otherwise counter-position with "не нужно приложение — веб-кабинет работает с телефона".
6. **`CRM для интернет-магазина ТОП`** / `автоматизация интернет-магазина CRM` (informational blog) — Sender's blog covers this; MTP's blog doesn't have CRM-comparison content in UA/RU. **MTP action:** add blog post `/blog/top-crm-dlya-internet-magazynu/` in UA + RU.
7. **`что такое фулфилмент преимущества недостатки`** — Sender has blog post with this exact phrasing. MTP has `/chto-takoe-fulfilment/` (RU) and `/shcho-take-fulfilment/` (UA/legacy) — check title match and add "преимущества и недостатки" / "переваги та недоліки" as H2s.
8. **`фулфилмент Horoshop интеграция`** — Sender puts Horoshop logo front-and-center. **MTP action:** create integration-focused landing `/integraciya-horoshop/` or strengthen mentions on `/fulfilment-dlya-internet-magazynu/`.
9. **`фулфилмент KeyCRM`** / `фулфилмент Salesdrive` / `фулфилмент Sitnix` — platform-name long-tails. **MTP action:** if MTP integrates with these, add a "Підтримувані CRM/платформи" block on home + `/api-docs/` with each name as H3.
10. **`топ сервисов для создания интернет-магазина`** (informational) — Sender's top blog post. **MTP action:** write a competing long-form post with MTP perspective.

---

## 7. Queries Where MTP Is Better Positioned to Win

MTP has existing URL/content advantage — Sender has no competing page:

1. **`фулфилмент для маркетплейсов`** / `фулфілмент для маркетплейсів` — MTP has `/fulfilment-dlya-marketpleysov/` per locale; Sender has zero marketplace-specific content.
2. **`фулфилмент для косметики`** / `фулфілмент для косметики` — MTP has `/fulfilment-dlya-kosmetyky/`; Sender silent.
3. **`фулфилмент тяжёлых товаров`** / `фулфілмент важких товарів` (appliances, furniture, heavy SKUs) — MTP has `/fulfilment-vazhkykh-tovariv/`; Sender has no heavy-goods page.
4. **`фулфилмент для малого бизнеса`** / `фулфілмент для малого бізнесу` — MTP has `/fulfilment-dlya-maloho-biznesu/`; Sender has only "min 99 orders/month" pricing note which actively excludes small business from their page.
5. **`паллетное хранение Киев`** / `палетне зберігання` / `pallet storage Ukraine` — MTP has `/paletne-zberigannya/`; Sender has no warehouse-service pages.
6. **`3PL логистика Украина`** / `3PL Ukraine` — MTP has `/3pl-logistyka/`; Sender never uses the term "3PL" on their site.
7. **`складские услуги Киев`** / `складські послуги` — MTP has `/skladski-poslugy/`; Sender has no warehouse-as-service angle.
8. **`фулфилмент Киев`** (geo-modifier) — MTP has `/fulfilment-kyiv/`; Sender mentions Kyiv only in contact info with no dedicated landing.
9. **`английский фулфилмент Украина`** / `fulfillment Ukraine English`** / `3PL Ukraine` (EN queries from international D2C brands) — MTP has full `/en/*` section with blog; Sender's `/en/` is a cosmetic language switcher over the same 6 Russian-origin pages, thin English content.
10. **`возврат товаров фулфилмент`** / `зниження повернень`, `отзыв товара` (recalls) — MTP has `/recalls/` + blog posts on returns reduction; Sender silent.
11. **`фискальный регистратор фулфилмент Украина`** — MTP EN blog has post on this; Sender silent. (Head-to-head in UA/RU would require MTP to translate the post.)
12. **`глоссарий фулфилмент`** / `fulfillment glossary Ukraine` — MTP has `/glossariy/` + `/glosariy.astro`; Sender has no glossary. Long-tail authority play.

---

## 8. Strategic Takeaways

**Sender's moat is narrow but deep:** they win on brand + platform/integration/mobile-app positioning, with aggressive "first month free" bait. Their SEO is a 6-URL surface with no sustained content investment (lastmod frozen Feb 2024).

**MTP's moat is wide but under-optimized:** 22+ pages per locale × 3 locales = ~66 pages vs Sender's 6, but MTP does not explicitly brand its client portal or integrations on the homepage, letting Sender own "platform" keyword space uncontested.

**Priority moves for MTP:**
1. **Ship a `/porivnannia/` or `/сравнение/` comparison page** — direct attack on Sender's comparison-table traffic.
2. **Add platform/integration keyword density** on home and `/api-docs/` — name KeyCRM, Horoshop, Sitnix, Salesdrive, Checkbox explicitly if MTP supports them.
3. **Create `/integraciyi/` hub page** listing every supported platform as H3s — captures long-tail "фулфилмент [platform]" queries.
4. **Strengthen `/tsiny/`** with a Sender-style transparent price table (numbers visible on page, not behind a calculator).
5. **Publish CRM-comparison blog content** in UA/RU (currently MTP's UA/RU blogs are thinner than Sender's on this topic).
6. **Exploit Sender's gaps** — double-down SEO investment on industry verticals (cosmetics, heavy goods, marketplaces, small business) and warehouse-services pages (3PL, pallet, skladski) where Sender cannot respond without months of content work.

**Defense priority:** Sender's "first month free" + transparent /prices + mobile app is their CRO/conversion weapon. MTP should not chase feature-for-feature but counter with stronger industry-expertise positioning (case studies per vertical, geographic reach beyond Kyiv).

---

*End of report. Raw HTML artifacts retained in `/tmp/sender-*.html` during analysis.*
