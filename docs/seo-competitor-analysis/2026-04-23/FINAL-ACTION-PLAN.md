# FINAL ACTION PLAN — MTP Group SEO/GEO 2026-Q2

**Дата:** 2026-04-23
**Джерела:** два незалежні аудити, проведені паралельно
- **Звіт A** (цей репо): 24 агенти × 4 сайти → `SYNTHESIS.md` — архітектура, технічна гігієна, Schema, AI-search механіка
- **Звіт B** (google-ads репо): `COMPETITIVE-ANALYSIS-FINAL-2026-04-23.md` — GSC positions, keyword volumes, existing-page surgery

Обидва аудити **сходяться на діагнозі**: MTP технічно найсильніший, але програє за content mass + listicle-шаблоном LP-Sklad. Розходяться в рівні деталізації (A = архітектура, B = операції на вже існуючих сторінках).

---

## 1. CONSENSUS — що підтверджено обома аудитами

1. **MTP технічно сильніший за всіх трьох** (A: 86/100, B: 80/100 — different scales, both top)
2. **LP-Sklad виграє AI через content scale, не через AI-оптимізацію**
   - A: SERP-as-RAG mechanism (блокують GPTBot, але Bing/Google indices живлять LLM)
   - B: 3 own rating sites cross-cite → feedback loop + 150 блог-постів
3. **Єдина наша зброя проти LP-Sklad — свій власний unbiased listicle** (обидва)
4. **Вертикальні LP критично не покриті** — 19%→75% треба закрити
5. **UA blog інвертовано** — 3 пости UA vs 30 EN на ринку де 80% трафіку UA
6. **Wikipedia entity потрібен** (durable moat що є в NP, відсутній у MTP/Sender/LP)
7. **YouTube канал потрібен** (0.737 correlation з AI-цитуванням, нема у жодного з 3 конкурентів)
8. **Sender бере "платформним" positioning + transparent pricing** — контратака через калькулятор + `/integrations/` hub
9. **Nova Poshta — бренд only**, не бити в контент-battle, тільки CAP pages + negative keyword
10. **Проза ризику:** дропати RU не можна (NP втратив 15% impressions), копіювати 1000+ AI-generated блогів не можна (E-E-A-T fragile)

---

## 2. UNIQUE — що бачив тільки один з аудитів

### Знайшов тільки Звіт A (архітектурний shift)
- **P0 fonts fix** — DM Sans/Serif з Google Fonts ламає LCP (4.98s mobile home). Self-host WOFF2 + preload = -1.5 до -2s. **Найдешевший великий win.**
- **34 dead `blog/tpost/*` редирект-лупи** — крадуть crawl budget + PageRank
- **Polish /pl/ ринок** — LP-Sklad вже таргетить PL sellers що шиплять в UA (їх 4-та мова); у нас 0
- **Schema residue**: EN blog Article без `datePublished`/`dateModified` (template bug — вимикає Article rich results на всьому EN блозі)
- **lp-sklad.biz ≠ lp-sklad.online** — .online лише SaaS login gateway; весь SEO-масив на .biz (1,486 URL точно)
- **Programmatic twin-pattern:** 41 sales LP × 4 мови + 41 listicle × 4 мови — ось точна формула масштабу
- **DefinedTermSet glossary** на `/glosariy/` — унікальний AI-моат якого ніхто не має
- **dual-md + Content-Signal** — унікальний UA fulfillment stack; не зламати

### Знайшов тільки Звіт B (operational GSC data)
- **ProfM у top-10 лише 3/20 keywords (15%)** — конкретна SERP-діагностика якої нема в Звіті A
- **`/ua/skladski-poslugy/` — позиція 59** при 800+ impressions/міс у GSC. Критично. 1,200 слів thin, H1 generic, keyword exact phrase відсутня
- **`/ua/about/` 4.8/10 E-E-A-T** — відсутні ЄДРПОУ, team photos, address → site-wide trust leak
- **Існуючий listicle `/ua/blog/top-fulfilment-operatoriv-2026/` має "MTP 9.5/10" bias** — AI devalue через очевидну упередженість. Треба додати disclosure + honest ranking
- **Sender володіє "фулфілмент послуги" (880-1,300/міс)** як #1. Конкретний target з volume
- **Чердак (4-й конкурент)** ранжує pos #4 "фулфілмент для інтернет магазину", #6 "фулфілмент Київ" — small-biz angle + "від 19 грн" price hook
- **`/ua/services/` duplicates `/ua/3pl-logistyka/`** — 301-редиректити
- **gtag form conversion tracking broken** — 3 конкретних fix-и вже визначені
- **CAP-сторінки** — `/alternatyva-nova-poshta-fulfillment/`, `/alternatyva-sender/` (бренд-паразит)
- **`/ua/integrations/` hub** — контрзахід Sender moat "20+ integrations"
- **Flagship case studies 3 deep-dive** — Carter's, Elemis, ORNER з цифрами before/after

---

## 3. STATUS TRACKER — прогрес по 34 діях

**Легенда:** ⬜ не розпочато · 🟡 в роботі · ✅ зроблено · ❌ відкладено/скасовано

### Horizon 1 — Emergency Week
- ⬜ **#1** Fonts P0 fix (self-host WOFF2)
- ⬜ **#2** Un-bias existing listicle `/ua/blog/top-fulfilment-operatoriv-2026/`
- ⬜ **#3** Rewrite `/ua/skladski-poslugy/` → 2,500+ слів
- ⬜ **#4** Rewrite `/ua/about/` — ЄДРПОУ + team + Person schema
- ⬜ **#5** 301 `/ua/services/` → `/ua/3pl-logistyka/`
- ⬜ **#6** Fix 34 dead `blog/tpost/*` redirects
- ⬜ **#7** Fix gtag form conversions (3 fixes)
- ⬜ **#8** Full calculator на `/ua/3pl-logistyka/` + `/ua/paletne-zberigannya/`
- ⬜ **#9** GSC URL Inspection + Request Reindex (8 pillar URLs)
- ⬜ **#10** Schema residue fix — EN blog Article datePublished template

### Horizon 2 — Competitive Moves
- ⬜ **#11** NEW `/top-fulfilment-ukraine-2026/` listicle UA/RU/EN
- ⬜ **#12** `/ua/rating-fulfillment-2026/` rating micro-sub (buyer focus)
- ⬜ **#13** 15 vertical LPs UA
- ⬜ **#14** CAP `/ua/alternatyva-nova-poshta-fulfilment/`
- ⬜ **#15** CAP `/ua/alternatyva-sender/`
- ⬜ **#16** CAP `/ua/alternatyva-lp-sklad/`
- ⬜ **#17** 15-post Nova Poshta cluster
- ⬜ **#18** `/ua/integrations/` hub — 20+ інтеграцій
- ⬜ **#19** 3 flagship case studies (Carter's, Elemis, ORNER)
- ⬜ **#20** Person schema Микола Лящук + author byline
- ⬜ **#21** YouTube канал + 3 відео
- ⬜ **#22** llms.txt rewrite to llmstxt.org spec
- ⬜ **#23** Expand Organization sameAs (LinkedIn/FB/YT/Crunchbase/GBP)
- ⬜ **#24** 10 UA blog posts batch 1

### Horizon 3 — Structural Moat
- ⬜ **#25** Wikipedia entity "МТП Груп" UK + EN
- ⬜ **#26** 1-2 press reportage (AIN/MC.today/Forbes)
- ⬜ **#27** Blog cadence 2-3/тиждень UA (60+ постів за 3 міс)
- ⬜ **#28** Polish /pl/ layer
- ⬜ **#29** YouTube 3-5 more відео
- ⬜ **#30** GBP Бориспіль + 20+ real reviews
- ⬜ **#31** 10 more vertical LPs + 6 geo-LPs
- ⬜ **#32** 5 more case study pages
- ⬜ **#33** Content hub `/knowledge/`
- ⬜ **#34** Monitor + iterate (weekly GSC + AI pulse)

**Прогрес:** 0/34 (0%) · H1: 0/10 · H2: 0/14 · H3: 0/10
**Last updated:** 2026-04-23

---

## 4. MERGED ACTION PLAN — зведена пріоритизація

### 🔥 HORIZON 1 — EMERGENCY WEEK (Day 1-7)

Комбінація P0 з обох звітів. Виконавець: site-chat (це я).

| # | Дія | Джерело | Ефорт | Impact |
|---|---|---|---|---|
| 1 | **Fonts P0 fix** — self-host DM Sans + DM Serif Display WOFF2, preload crossorigin, зняти fonts.gstatic.com swap | A | 3h | 9/10 |
| 2 | **Un-bias existing listicle** `/ua/blog/top-fulfilment-operatoriv-2026/` — додати disclosure "MTP рейтинг базується на criteria X/Y/Z", чесне порівняння, не "9.5/10 MTP vs все інше". Додати ItemList + SoftwareApplication schema на кожен пункт | B | 4h | 8/10 |
| 3 | **Rewrite `/ua/skladski-poslugy/`** → 2,500+ слів, keyword exact phrase в H1/title/URL, Service schema, internal links | B | 6h | 8/10 (pos 59→15) |
| 4 | **Rewrite `/ua/about/`** — ЄДРПОУ, team photos, address, founder bio, Person schema, +E-E-A-T site-wide | B | 4h | 7/10 |
| 5 | **301 `/ua/services/` → `/ua/3pl-logistyka/`** — stop duplication + consolidate link equity | B | 1h | 6/10 |
| 6 | **Fix 34 dead `blog/tpost/*` redirects** — або 301 на живі канонічні, або 410 Gone | A | 3h | 6/10 |
| 7 | **Fix gtag form conversions** (3 fixes вже задокументовано) — enable Ads attribution | B | 2h | 7/10 |
| 8 | **Full calculator на `/ua/3pl-logistyka/` + `/ua/paletne-zberigannya/`** — neutralize Sender pricing moat | B | 4h | 6/10 |
| 9 | **GSC URL Inspection + Request Reindex** для 8 pillar URLs після всіх правок | B | 1h | 5/10 |
| 10 | **Schema residue fix** — EN blog Article `datePublished`/`dateModified` template, `addressLocality` consistency, `knowsAbout` localized | A | 2h | 5/10 |

**Week 1 total:** ~30h, 10 дій. Deliverable: P0 тех.борг закритий, 2 існуючі сторінки з GSC-пріоритету виправлені, трекінг відновлений.

### 🎯 HORIZON 2 — COMPETITIVE MOVES (Day 8-30)

| # | Дія | Джерело | Ефорт | Проти кого |
|---|---|---|---|---|
| 11 | **NEW `/top-fulfilment-ukraine-2026/` listicle UA/RU/EN** (окремо від існуючого біасного, на корені, Editorial archetype, 2,500+ слів, ItemList + SoftwareApplication×15 operators, MTP чесно #1, LP-Sklad #4-6) | A+B | 16h | LP-Sklad |
| 12 | **`/ua/rating-fulfillment-2026/` rating micro-sub** — додаткова сторінка в ranking cluster, відрізняється від #11 фокусом (focus: "as buyer — які критерії обрати") | B | 8h | LP-Sklad parasite |
| 13 | **15 vertical LPs UA** — одяг, взуття, косметика, дитячі, електроніка, спорт, авто, зоо, текстиль, аксесуари, посуд, декор, дім, книжки, добавки × 1,200+ слів | A | 30h | LP-Sklad + Sender |
| 14 | **CAP: `/ua/alternatyva-nova-poshta-fulfilment/`** — honest comparison landing, ItemList schema | B | 6h | NP brand hijack |
| 15 | **CAP: `/ua/alternatyva-sender/`** — direct counter pricing table | B | 6h | Sender |
| 16 | **CAP: `/ua/alternatyva-lp-sklad/`** — NEW (не було в жодному) — честна відповідь на їх listicle | merged | 6h | LP-Sklad |
| 17 | **15-post Nova Poshta cluster** — блог-пости про NP fulfillment (порівняння, альтернативи, відмінності) | B | 20h | NP brand trafic |
| 18 | **`/ua/integrations/` hub** — 20+ інтеграцій (KeyCRM, SalesDrive, Rozetka, Prom, Horoshop, Shopify, WooCommerce, OpenCart, Kaspi, Checkbox, SitniX, Poshta, Ukrposhta, Meest, DHL, Justin, Epicentr, OLX, Kasta, Allo, Intertop) з Service schema | B | 8h | Sender |
| 19 | **3 flagship case studies** — Carter's, Elemis, ORNER з цифрами before/after, Review + CaseStudy schema | B | 12h | LP-Sklad 0 named |
| 20 | **Person schema Микола Лящук** на всіх pillar + blog, author byline, LinkedIn sameAs | B | 4h | E-E-A-T |
| 21 | **YouTube канал + 3 відео** — warehouse tour 3-5min, how fulfillment works, MTP vs NP. Embed на home + about + shcho-take. Додати у Organization sameAs | A+B | 20h | AI citation |
| 22 | **llms.txt rewrite to llmstxt.org spec** | B | 2h | GEO first-mover |
| 23 | **Expand Organization sameAs** — LinkedIn, Facebook, YouTube, Crunchbase, GBP CID | A+B | 3h | E-E-A-T |
| 24 | **10 UA blog posts batch 1** — long-tail: "як замовити фулфілмент", "ФОП vs ТОВ для ecommerce", "фулфілмент для Розетки крок за кроком", "пакування для маркетплейсів", "що таке SLA в фулфілменті" | A+B | 30h | LP-Sklad content scale |

**Month 1 total:** ~171h, 14 дій. Deliverable: 15 vertical LPs + 3 listicles + 3 CAP pages + integrations hub + 3 case studies + YouTube live + 10 blog posts + Person schema everywhere.

### 🏗️ HORIZON 3 — STRUCTURAL MOAT (Day 31-90)

| # | Дія | Джерело | Тип моату |
|---|---|---|---|
| 25 | **Wikipedia entity "МТП Груп" UK + EN** — зібрати 3-5 незалежних press citations (Forbes.ua, AIN, MC.today, Business UA, Retailers), draft, submit | A+B | Brand authority |
| 26 | **1-2 press reportage** — "MTP Group — 0 днів простою з 24.02.2022" в AIN/MC.today/Forbes | B | Media authority |
| 27 | **Blog cadence 2-3/тиждень UA** — 60+ постів за 3 міс | A+B | Content moat |
| 28 | **Polish /pl/ layer** — home + 5 top-service pages + listicle + 10 vertical LPs | A | Geographic moat |
| 29 | **YouTube 3-5 more відео** — warehouse tour part 2, calculator walkthrough, Carter's case study interview | A+B | Visual + AI |
| 30 | **GBP Бориспіль + 20+ real reviews** | B | Local pack |
| 31 | **10 more vertical LPs + 6 geo-LPs** — закрити 25/26 верт., Київ/Львів/Одеса/Дніпро/Харків/Бориспіль | A | Keyword coverage |
| 32 | **5 more case study pages** — Б2Б contract manufacturing, FBS Amazon-style, cross-docking | A+B | Experience moat |
| 33 | **Content hub `/knowledge/`** — structured guide clusters + DefinedTermSet expansion | A | Semantic moat |
| 34 | **Monitor + iterate** — weekly GSC + AI-citation pulse (manual test 20 queries), rollback trigger watch | A+B | Quality gate |

---

## 5. KEY KPI — злиті цілі обох звітів

| Metric | Baseline 2026-04-23 | Day 30 | Day 90 |
|---|---|---|---|
| Top-10 Google positions (з 20 ключових) | **3/20** (B) | 6/20 | **10/20** |
| GSC impressions total | baseline | +100% | +300% |
| GSC UA clicks | baseline | +80% | +200% |
| Indexed URLs | ~110 | 150 | 250+ |
| `/ua/skladski-poslugy/` position | **59** (B) | 20-25 | **10-15** |
| Home mobile LCP | **4.98s** (A) | <3.0s | **<2.5s** |
| AI citations (manual test × 20) | **2/20** (A) | 5/20 | **10/20** |
| Organic sessions (GA4) | baseline | +50% | +200% |
| Leads (window.mtpSubmitLead) | baseline | +30% | +100% |
| Wikipedia UK entity | ❌ | ❌ | ✅ |
| YouTube subscribers | 0 | 100 | 500+ |
| Polish /pl/ URLs indexed | 0 | 0 | 15+ |
| Vertical coverage (26 ніш) | 5/26 (19%) | 20/26 | 25/26 (96%) |

---

## 6. STOP-LIST (не робити — уникнути конкурентних пасток)

Злито з обох звітів:

1. **Не блокувати AI crawlers** (як LP-Sklad) — це баг, не фіча. Наш dual-md + llms.txt + allow-GPTBot — стратегічна перевага.
2. **Не копіювати 1,154 AI-generated блог-пости LP-Sklad** — QRG Sept 2025 + E-E-A-T tightening зробить такий контент fragile. Писати 40-60/quarter якісних з author byline + citations.
3. **Не мігрувати на Nuxt/React SPA** — NP = живий доказ (LCP 19.7s, CLS 0.62). Astro SSG + dual-md залишається.
4. **Не дропати RU-версію** — NP втратив 15% impressions з RU-queries. Sender має RU-as-default на UA-ринку = політичний ризик. Наш тримовний divergent-angle підхід правильний.
5. **Не створювати UA сторінки з префіксом `/ua/`** — policy 2026-04-22: нові UA = root `/slug/`. Старі `/ua/*` як є.
6. **Не писати fake reviews / fake AggregateRating** — reviews мають бути real (Google Business + Trustpilot). Фейк = manual action.
7. **Не дублювати форму 3× на сторінці** — `<HeroCTA>` hero + `<CTA>` bottom максимум.
8. **Не використовувати Wistia / embed video без facade** (Sender -30 Lighthouse доказ).
9. **Не забувати оновлювати `public/llms.txt` + `public/.well-known/api-catalog`** після кожної нової/видаленої сторінки.
10. **Не писати UA та RU як переклади** — різний кут атаки обов'язково (CIS-entry на RU як приклад).

---

## 7. РОЗПОДІЛ ПО ЧАТАХ

**Site-chat (ця сесія)** — виконує: #1-3, #5-6, #10, #11-13, #18, #21, #24, #27-29, #31-33.
**Google-ads chat** — виконує: #4 (about rewrite), #7 (gtag), #14-17 (CAP + NP cluster + bias-fix), #19-20 (case studies + Person schema), #22-23 (llms.txt + sameAs), #25-26 (Wikipedia + PR).

**GSC robota (nikolaj)** — виконує: #9, моніторинг KPI, request reindex після кожного merge.

---

## 8. ПЕРШИЙ КРОК (now)

**Action #1 — Fonts P0 fix.** 3h роботи, +~2s LCP на home mobile, feeds into AI crawler bandwidth signals. Після нього → Action #2 (un-bias existing listicle). Після нього → Action #11 (NEW unbiased listicle). Цей sequence закриває найдорожчий архітектурний + контент-борг за 1-2 дні.

**Трегер commit + push after each action.** CF Pages auto-deploy. Rollback trigger: CR -15% або positions -20% за 7 днів → `git revert`.

**Report ends.** Next session: start Action #1.
