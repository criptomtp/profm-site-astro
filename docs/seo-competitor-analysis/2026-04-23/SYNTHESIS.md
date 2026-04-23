# SYNTHESIS — конкурентний SEO-аудит MTP Group

**Дата:** 2026-04-23
**Об'єкт:** fulfillmentmtp.com.ua (MTP Group)
**Бенчмарки:** novaposhta.ua, senderukraine.com, lp-sklad.biz
**Джерела:** 24 тематичні звіти в `docs/seo-competitor-analysis/2026-04-23/[mtp|novaposhta|senderukraine|lp-sklad]/01..06.md`
**Синтезатор:** Claude (task #78)

---

## 1. TL;DR

MTP **технічно найсильніший** серед чотирьох сайтів (Lighthouse mobile 74-88 vs NP 24, Sender 56, LP-Sklad 93 на одній сторінці), має **унікальний dual-md + llms.txt моат**, найякіснішу Schema (LocalBusiness + FAQPage + AggregateRating + DefinedTermSet). Але LP-Sklad перемагає нас у AI-цитуванні **не завдяки техніці чи AI-доступу** (вони навпаки блокують GPTBot/ClaudeBot/Google-Extended), а завдяки **масштабу класичного SEO**: 1 486 URL проти наших 110, програмна система 41 "sales landing + rating listicle" × 4 мови (включно з польською), і одна killer-сторінка `/rating-autsorsynh-skladu/` з Schema `SoftwareApplication` на 18 конкурентів, де LP-Sklad сам себе ставить №1, а MTP — №9. Nova Poshta тримається лише на бренді + Wikipedia-ентиті, але технічно розвалена (LCP 19.7s мобільний, canonical відсутній, `<html lang="undefined-ua">`). Sender Ukraine — слабка у всіх вимірах (34/100 контент, LCP 31.5s, тільки FAQPage Microdata, 6 URL). **Стратегія 90 днів:** скопіювати LP-Sklad listicle-шаблон (ми #1 чесно), побудувати 15 вертикальних LP (одяг/косметика/Розетка/Київ), додати Polish /pl/, запустити YouTube-канал + Wikipedia-драфт, полагодити P0 fonts perf — і MTP виграє і в AI, і в SERP.

---

## 2. Comparative Matrix (4 × 6)

| Вимір | MTP | Nova Poshta | Sender UA | LP-Sklad |
|---|---|---|---|---|
| **1. Technical** | 86/100 — dual-md, www+301, hreflang×4, HSTS/CSP | 58/100 — no canonical, `<html lang="undefined-ua">`, broken BreadcrumbList | 58/100 — canonical-leak /uk→/, sitemap stale 2024-02-08, no CDN | 34/100 (.online gated) / .biz mid — Cloudflare, WP+Yoast, без llms.txt |
| **2. Content** | 81/100 — pillar 2 778 слів, E-E-A-T Experience 88 | 58/100 — одна FF-сторінка, нема verticals, 404 на RU | 34/100 — 5 блог-постів, 605w cornerstone, RU як default | mid — 1 154 блог-постів AI-generated, 164 sales + 164 listicle pages, 4 мови (uk/ru/en/pl) |
| **3. Schema** | **найкращий** — LocalBusiness+FAQPage+AggregateRating+DefinedTermSet+Article+BreadcrumbList | Тільки Organization (542B stub) + зламаний BreadcrumbList на кожному URL | **Нуль JSON-LD** сайтово, тільки FAQPage Microdata на home | Organization + FAQPage на home, per-item `SoftwareApplication` на listicle — структурно найслабший з конкурентів, але listicle-схема = AI-magnet |
| **4. AI Search / GEO** | 82/100 — dual-md унікальний, llms.txt, crawlers allow | 66/100 — 80% бренд + 20% структура, Wikipedia UK+EN = моат | 38/100 — **GPTBot + OAI-SearchBot 403-блок на WAF** | 46/100 — БЛОКУЄ всі AI-бoти, але виграє через SERP-retrieval (Bing/Google index → LLM RAG) |
| **5. Performance (mobile)** | Lighthouse 74-88, LCP home 4.98s (**FAIL — P0 fonts**) | **24/100**, LCP 19.7s, CLS 0.62 POOR, Nuxt SPA hydration, 10 third-party scripts | 56, LCP 31.5s, 9.6MB (Wistia video blocker), CLS 0.00 | 93 на home /, LCP 2.88s (needs improvement), 6 render-blocking CSS, HTTP/1.1 only |
| **6. Keywords / URL count** | 109 URL; 5/26 вертикалей (19%); 3 UA блог vs 30 EN (інверсія) | Бренд-якорений генераліст, 0 верт., 0 ціни, 9 адрес у FAQ | 6 URL тільки; "платформа"-позиціювання; 1-місяць-free CRO | **1 486 URL**; 41 sales × 4 мови + 41 listicle × 4 мови + 1 158 блог-постів; 4 мови вкл. PL |

**Одна теза на конкурента:**
- **MTP** — найсильніший технічно і за Schema, але критично малий за URL-масштабом і не має жодної listicle-сторінки.
- **Nova Poshta** — бренд + Wikipedia перекривають технічний бардак; копіювати можна лише passage-first текстовий патерн.
- **Sender Ukraine** — не загроза за жодним виміром; RU як / на українському ринку = політичний ризик.
- **LP-Sklad** — AI-дoмінує через обсяг + listicle-ентіті-граф, а не через AI-оптимізацію файлів. Блокують crawlers — це **баг, а не фіча**.

---

## 3. Who Wins at What — 4 Profiles

### MTP Group (наш профіль)
- **Виграє:** технічна архітектура (dual-md twin — унікально в UA fulfillment), Schema density (найкращий LocalBusiness + AggregateRating + DefinedTermSet в ніші), E-E-A-T Experience 88/100, URL policy (2-кластерна UA: нові без `/ua/`), font-preload commit 095da3d, HSTS/CSP, hreflang×4 консистентний, CTA-Telegram воронка.
- **Програє:** обсяг (109 vs 1 486 URL у LP-Sklad), 5/26 вертикалей, інверсія блог-інвестицій (3 UA vs 30 EN — хоча 80% трафіку українського), відсутність listicle/comparison сторінки, відсутність YouTube-каналу, відсутність Wikipedia-ентіті, 34 мертвих blog-tpost редиректи, home LCP 4.98s мобільний (FAILS через DM Sans + DM Serif Display swap з fonts.gstatic.com).

### Nova Poshta
- **Виграє:** бренд (8-річне домінування, 92-98% brand share), Wikipedia UK+EN (величезний AI-моат), passage-first стиль написання який LLM легко цитує, 9 фізичних адрес у FAQ (пасивне local-SEO), 10 000 unmarked відділень (потенційна мета-schema goldmine).
- **Програє:** технічний борг (немає canonical, `<html lang="undefined-ua">`, зламаний BreadcrumbList з `https:/` і `undefined`), Nuxt SPA-hydration руйнує LCP до 19.7s, 839KB HTML, CLS 0.62, CrUX origin POOR, єдина фулфілмент-сторінка без вертикалей, 404 на RU-версії, нуль прозорості цін, 10 third-party scripts (GTM/Typeform/Plerdy/Clarity/YouTube/TikTok), тільки Organization stub 542B sitewide.

### Sender Ukraine
- **Виграє:** "платформа"-позиціювання (особистий кабінет + mobile app + 20+ інтеграцій), first-month-free CRO weapon, динамічний price slider, FAQPage Microdata на home (цитоване в LLM).
- **Програє:** майже все — 6 URL тільки, контент-скор 34/100, LCP 31.5s (Wistia video stack — блокер #1), 9.6MB сторінка, canonical-leak (/uk та /en self-canonical на RU /), sitemap stale 2024-02-08, нуль JSON-LD sitewide, GPTBot + OAI-SearchBot 403-WAF-блок (жорсткий), Hosting Ukraine без CDN, без modern image formats, RU-як-default на українському ринку (політичний ризик), 605-слово cornerstone, 5-постовий блог.

### LP-Sklad (.biz, не .online)
- **Виграє:** програмний URL-масштаб (1 486 vs наших 110), 41 "fulfillment/[slug]/" sales LP × 4 мови + 41 "rating-fulfillment/[prefix]-[slug]/" listicle × 4 мови + 1 158 WordPress/Yoast постів, 4-мовний покрив включно з **польським** (яку ми не маємо), killer-сторінка `/rating-autsorsynh-skladu/` з `SoftwareApplication` per-item × 18 конкурентів (MTP = №9), title-exact-match патерн, home `/` Lighthouse 93 мобільний, кожна вертикаль покрита twin-сторінкою (sales + listicle).
- **Програє:** технічна гігієна (розбитий Organization-стаб через мутацію, relative-URL logos, self-referencing sameAs, відсутній H1 на home, 6 render-blocking CSS, HTTP/1.1 only, нема HTTP/2/3, нема CDN на origin), E-E-A-T майже нуль (нуль author bios, нуль Wikipedia, sameAs тільки Instagram+Telegram, нуль LinkedIn/Facebook/YouTube у schema), контент якість низька (~485w sales LP, AI-generated блог без citations), **БЛОКУЄ всі AI crawlers** (GPTBot/ClaudeBot/Google-Extended/Bytespider/Applebot-Extended/meta-externalagent — всі 403 на Cloudflare), нема llms.txt/dual-md/`.well-known/ai-plugin.json`, .online домен повністю gated (1 публічна URL).

---

## 4. Why LP-Sklad Dominates AI Search — Root Cause

**Парадокс:** LP-Sklad блокує КОЖНОГО AI-crawler на WAF-рівні (Cloudflare 403 для GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot, Bytespider, Applebot-Extended, meta-externalagent, CloudflareBrowserRenderingCrawler), не має жодного AI-файлу (llms.txt, llms-full.txt, dual-md, ai.txt, .well-known/ai-plugin.json, Content-Signal ai-train=no) — але **стабільно з'являється в AI-відповідях** ChatGPT Search, Perplexity, Google AI Overviews, Gemini.

**Механізм (підтверджено логами):**

1. **SERP-as-RAG.** Сучасні AI-пошукові інтеграції (Perplexity Sonar, ChatGPT SearchGPT, Google AI Overviews, Gemini Search) не покладаються на власних crawlers як основне джерело. Вони **запитують Bing/Google indices** у момент запиту користувача, отримують top-10 SERP, парсять SERP-snippet + (якщо є доступ) fetch-ять сторінку. Cloudflare 403 на AI user-agent блокує **лише live re-crawl**, але не блокує:
   - Bing/Google традиційні crawlers (Googlebot, Bingbot) — вони пропущені як "search=yes" у Content-Signal
   - кеш Bing/Google index з уже засвоєним контентом LP-Sklad
   - SERP-snippets які формуються з того cache
2. **Training-data residue.** Перший live probe на robots.txt-блок датується після 2024 WP-Yoast оновлень. До 2022-2024 LP-Sklad.biz був відкритий для всіх crawlers. GPT-4, Claude 3/4, Gemini training snapshots вже мають їхній контент в ваговій матриці. Блок зупиняє оновлення, не знищує згадки.
3. **Killer listicle matches exact AI-answer shape.** Сторінка `/rating-fulfillment/uk/rating-autsorsynh-skladu/` має:
   - Title "ТОП 18 аутсорсинг складів. Огляд та рейтинг" = exact-match для `"найкращі фулфілмент компанії Україна"`
   - 18 конкурентів розмічені `itemtype="https://schema.org/SoftwareApplication"` з `id="warehouse-1"..."warehouse-18"`
   - Ranked format з H3 per конкурент = ідеальна форма для AI-відповіді (ranked list + explanations)
   - 1 986 слів глибини + comparison table + FAQ
   - LP-Sklad сам себе ставить №1 (MTP — №9), TVL №3, Nova Poshta №4, Sender №5
4. **Volume at scale.** 1 486 URL проти наших 110 = 13× більше поверхні для SERP-exposure. Коли Google/Bing обробляють query "фулфілмент для [будь-якої ніші]", одна з twin-сторінок LP-Sklad майже гарантовано матиме title-exact-match.

**Що ЦЕ НЕ:** це **не** Wikipedia (нуль статей LP-Sklad), **не** YouTube 0.737 correlation (канал не в sameAs), **не** Reddit/forums (0 присутність), **не** превалідна Schema (їхня розбита), **не** llms.txt (нема), **не** швидкість (home LCP 2.88s needs improvement).

**Висновок для MTP:** щоб побити LP-Sklad в AI-цитуванні ми НЕ копіюємо їхні AI-файли (вони не існують) і НЕ копіюємо блокування (це баг). Ми копіюємо їхній **листикл-шаблон + URL-масштаб + title-exact-match патерн**, тримаючи наші переваги (dual-md, Schema, allow-AI crawlers, швидкість).

---

## 5. 10 Breakthrough Actions (ranked by ROI = impact × 1/effort)

Ефорт у годинах, impact 1-10 (10 = зміна ніші), ROI-tier 🟢/🟡/🔴.

| # | Дія | Ефорт | Impact | ROI | Чому саме так |
|---|---|---|---|---|---|
| 1 | **Fix fonts P0 — self-host DM Sans + DM Serif Display WOFF2, preload з `type="font/woff2"` crossorigin, зняти fonts.gstatic.com swap** | 3h | 9 | 🟢 | Home LCP 4.98s FAIL → очікувано 2.5-3.0s. Прямий CWV/AI-crawler сигнал. Commit 095da3d вже напрямку |
| 2 | **Build `/top-fulfilment-ukraine-2026/` listicle UA/RU/EN** (3 сторінки, 2 500+ слів, ItemList + SoftwareApplication per-item × 15 операторів, MTP чесно №1, включно з LP-Sklad як #4-6) | 16h | 10 | 🟢 | Єдиний механізм якого LP-Sklad виграє AI. 60-90 днів до перших цитувань. Жоден інший конкурент цього не має (NP, Sender — нуль). |
| 3 | **Expand UA blog 3 → 20 постів** (long-tail informational: "як замовити фулфілмент", "фулфілмент Київ", "ФОП vs ТОВ для ecommerce", "фулфілмент для Розетки/Prom/Kasta") + **fix 34 мертвих tpost-редиректів** | 40h | 8 | 🟢 | Ринок UA — 80% трафіку, у нас 3 пости vs LP-Sklad 1 154. Кожен пост = вхід для long-tail. Dead redirects крадуть PageRank. |
| 4 | **Build 15 vertical LPs** (одяг, взуття, косметика, дитячі товари, електроніка, спорт, авто, зоо, текстиль, аксесуари, посуд, декор, дім, книжки, добавки) × UA з 1 200+ словами + Service schema | 30h | 9 | 🟢 | Покриваємо 19% → 75% верт. LP-Sklad має по 4 langs × 14 ніш; ми поки 0. Кожна вертикаль = 4-7 SERP-входів. |
| 5 | **YouTube канал + 3-5 відео** (warehouse tour 3-5min, як працює фулфілмент, MTP vs Nova Poshta comparison) + embed на home + about, додати у Organization `sameAs` | 20h | 7 | 🟡 | 0.737 correlation з AI-цитуванням (canonical GEO research). Конкуренти: LP-Sklad embed-ає але не linkає, NP має TikTok не YouTube, Sender нуль. |
| 6 | **Add Polish `/pl/` layer** для home + 5 top-service pages + listicle | 24h | 6 | 🟡 | LP-Sklad вже таргетить PL sellers що шиплять в UA. MTP має 0. Cheap win — переклад + hreflang. |
| 7 | **Pursue Wikipedia entity "MTP Group / ПП МТП Груп"** — зібрати 3-5 незалежних press citations (Forbes.ua, AIN, MC.today, Business UA) → потім draft UK Wikipedia | 80h (2-4 тижні) | 8 | 🟡 | Єдиний durable entity-graph моат якого NP має, а LP-Sklad/Sender не мають. Тривалий path, але ефект на 5+ років. |
| 8 | **Fix Schema residue:** EN blog Article `datePublished`/`dateModified` (template bug), уніфікувати `addressLocality`, перекласти `knowsAbout` на UA/RU на localized сторінках | 6h | 5 | 🟢 | Вже найкраща Schema в ніші — чистимо залишкові баги щоб забрати 95+/100. |
| 9 | **Expand `sameAs` в Organization** — додати LinkedIn Company Page, Facebook, YouTube channel, Crunchbase, Trustpilot, G2, Google Business Profile CID URLs | 4h (після #5, #7) | 5 | 🟢 | E-E-A-T close gap. LP-Sklad має тільки Instagram+Telegram — ми закриваємо в 2× більше. |
| 10 | **Programmatic geo-LPs** — `/fulfillment-kyiv/`, `/fulfillment-lviv/`, `/fulfillment-odesa/`, `/fulfillment-dnipro/`, `/fulfillment-kharkiv/`, `/fulfillment-boryspil/` × UA з warehouse-coverage, GeoCoordinates + LocalBusiness schema | 24h | 6 | 🟡 | NP має 9 адрес у FAQ-залитті, LP-Sklad тільки blog-пости. Proper geo-LP = featured snippet + Maps pack. |

**Sum:** ~247h роботи, 10 дій, 73 impact points.

**Skip / Do-Not-Do list (Section 8 розгорне):** не блокувати AI crawlers, не копіювати 1 154 AI-generated блог-постів, не мігрувати на Nuxt/React SPA, не дропати RU-версію.

---

## 6. 30-Day Roadmap (week-by-week)

### Week 1 (Day 1-7) — Unlock CWV + AI-citation foundation
- **Day 1:** Fix fonts P0 (Action #1). Deploy, measure LCP в PSI лабі. Експект: home mobile LCP 4.98s → ~2.8s.
- **Day 2:** Write + deploy `/top-fulfilment-ukraine-2026/` UA (Action #2 частина 1). 2 500 слів, ItemList + SoftwareApplication×15. HeroCTA + Base.astro (dual-md генерує .md twin автоматично).
- **Day 3:** Write + deploy `/ru/top-fulfilment-ukraine-2026/` + `/en/top-fulfillment-companies-ukraine-2026/` (різний кут атаки, не переклад). Hreflang×4 на всіх трьох.
- **Day 4:** Fix Schema residue (Action #8). EN blog Article template `datePublished`, `knowsAbout` localization, `addressLocality` consistency.
- **Day 5:** Fix 34 dead tpost redirects (Action #3 частина 1). Або 301→канонічні живі, або 410 для остаточного видалення.
- **Day 6:** Write 3 vertical LPs UA (Action #4 batch 1): одяг, косметика, електроніка. 1 200+ слів кожен, Service schema.
- **Day 7:** Write 3 vertical LPs UA (batch 2): дитячі товари, Розетка-фулфілмент, Київ-геo-LP. Submit всі new URLs в GSC + Bing Webmaster.

### Week 2 (Day 8-14) — Scale verticals + YouTube prep
- **Day 8-10:** Write 6 more UA vertical LPs: взуття, спорт, авто, зоо, текстиль, аксесуари.
- **Day 11-12:** Write 3 UA geo-LPs: Львів, Одеса, Дніпро + 3 UA blog posts (how-to "як замовити фулфілмент", "ФОП vs ТОВ", "фулфілмент для маркетплейсів").
- **Day 13:** Запис YouTube warehouse tour 3-5min. Редагування.
- **Day 14:** Upload YT + embed на home + about + `/shcho-take-fulfilment/`. Додати YT channel URL в Organization `sameAs`.

### Week 3 (Day 15-21) — RU+EN expansion + Polish pilot
- **Day 15-17:** Translate + adapt (різний кут!) 9 vertical LPs на RU (/ru/fulfilment-dlya-[slug]/).
- **Day 18-20:** Translate + adapt 9 vertical LPs на EN.
- **Day 21:** Start Polish pilot — translate home + `/fulfilment/` + `/tsiny/` + `/top-fulfilment-ukraine-2026/` на PL. Hreflang expand до `pl`.

### Week 4 (Day 22-30) — Blog velocity + press outreach + monitoring
- **Day 22-26:** Write 10 UA blog posts (long-tail: "фулфілмент Боярка", "ФОП для ecommerce", "пакування для маркетплейсів", etc.).
- **Day 27-28:** Press outreach — надіслати 5 pitches на Forbes.ua / AIN / MC.today / Business UA / Retailers про "як український fulfillment оператор виграє AI search проти LP-Sklad" (meta-story + data).
- **Day 29:** Mid-sprint audit — GSC impressions per new URL, first LLM citations test (ChatGPT "найкращі фулфілмент Україна"), CWV re-check.
- **Day 30:** Publish 3 EN blog posts + finalize YouTube video #2 (how fulfillment works).

**Day 30 deliverable:** 15 нових vertical LPs UA + 9 RU + 9 EN = 33 LPs, 3 listicle LPs (UA/RU/EN), 6 geo-LPs UA, 13 нових блог-постів, YouTube канал з 1-2 відео + embeds, Polish pilot на 4 URL, Schema 95+/100, home LCP <3s mobile.

---

## 7. 90-Day Quarter Plan

**Q-theme:** "From 110 URLs to 300+, from 0 listicles to 5, from invisible in AI to cited in top-3 AI answers for UA fulfillment."

### Month 1 (Day 1-30): Foundation (див. Section 6)
- 33 vertical LPs (UA+RU+EN)
- 3 listicle pages (TOP-15 Ukraine)
- 6 geo-LPs UA
- 13 blog posts
- YouTube channel + 2 videos
- Polish pilot 4 URL
- Fonts P0 fix + Schema cleanup

### Month 2 (Day 31-60): Depth + authority
- **Wikipedia pursuit:** секюрити 3-5 press citations з Forbes.ua/AIN/MC.today/Retailers/Business UA. Coordinate через PR agency або cold outreach. Draft UK Wikipedia article "МТП Груп" з secondary sources.
- **Expand listicles:** 2 нові listicle LPs — `/top-fulfilment-dlya-marketpleysiv-ukraina/` + `/top-3pl-ukraina-2026/` (UA/RU/EN).
- **15 more UA blog posts** — topic clusters: "pre-fulfilment" (ФОП setup, перший склад), "scaling" (перевозка між провайдерами, SLA), "crisis" (воєнні risks, страхування).
- **3 more YouTube videos:** warehouse tour part 2, MTP vs Nova Poshta (data-driven comparison), Calculator walkthrough.
- **Expand Polish:** +10 PL URLs (всі vertical LPs).
- **Add LinkedIn company content** — 3 posts/тиждень. Додати LinkedIn до `sameAs`.
- **Comparison hub launch:** `/mtp-vs-nova-poshta/`, `/mtp-vs-lp-sklad/`, `/mtp-vs-sender-ukraine/` (honest data, ItemList schema).

### Month 3 (Day 61-90): Compounding + consolidation
- **Publish Wikipedia article** — UK first, потім EN translation (якщо notable пройде AfD).
- **10 more vertical LPs** покриваючи 25/26 верт.: книжки, добавки, decor, посуд, продукти, алкоголь (B2B), лайт-промисл., Б2Б contract manufacturing, FBS Amazon-style, cross-docking.
- **5 case study pages** — 5 конкретних клієнтів-кейсів з цифрами (% growth, SLA, ROI). Review schema + CaseStudy markup.
- **Content hub launch:** `/knowledge/` — структуровані guide clusters (DefinedTermSet glossary, calculator, checklist downloads).
- **Monitor + iterate:** weekly GSC + AI-citation pulse (manual ChatGPT/Perplexity query testing на 20 queries), PageSpeed quarterly audit, rollback trigger check (CR -15% / positions -20%).

**90-day success criteria:**
- GSC impressions +300% (ніша-level)
- GSC UA clicks +150%
- Top-10 Google positions на 50+ нових UA/RU queries
- 5+ AI-citation captures (ChatGPT/Perplexity/Google AIO/Gemini) на queries "фулфілмент Україна", "найкращий фулфілмент", "3PL Київ"
- Wikipedia UK entity live
- YouTube channel 500+ subscribers
- Polish /pl/ live з 15+ URLs
- Home LCP <2.5s mobile

---

## 8. Don't-Do List

Усвідомлено **НЕ** робити (уникнути конкурентних пасток):

1. **Не блокувати AI crawlers.** LP-Sklad блокує — це їх **обмеження**, не перевага. Наш dual-md + llms.txt + allow-GPTBot — стратегічна перевага. Не змінювати.
2. **Не копіювати 1 154 AI-generated блог-пости.** Волюм без якості зараз спрацьовує, але QRG Sept 2025 + 2026 E-E-A-T tightening зробить такий контент fragile. Ми пишемо 40-60/quarter якісних постів з author byline + citations, не 1 000 AI-thin.
3. **Не мігрувати на Nuxt/React SPA для marketing.** Nova Poshta = живий доказ чому це невірно (LCP 19.7s, CLS 0.62). Astro SSG + dual-md залишається.
4. **Не дропати RU-версію.** NP дропнув і втратив ~15% impressions з RU-queries. Sender тримає RU як default на UA-ринку — політичний ризик. Наш стан (тримовний divergent-angle) — правильний середній шлях.
5. **Не створювати UA сторінки з префіксом `/ua/`.** 2026-04-22 URL policy: нові UA = root `/slug/`. Старі `/ua/*` лишаємо (audit C-1 perebиl'shиl ризик). Порушення policy зламає hreflang.
6. **Не мігрувати з Vercel.** CF Pages cutover branch є як backup (cf-pages-migration), але Vercel edge + Cloudflare DNS наразі дає найнижчий TTFB у ніші.
7. **Не писати fake reviews / fake AggregateRating.** AggregateRating має бути на реальних даних (Google Business reviews, Trustpilot). Фейк = manual action.
8. **Не дублювати форму 3× на сторінці.** Hero HeroCTA + bottom CTA — дві форми максимум. HeroCTA має `id="heroLeadForm"`, CTA має `id="finalForm"`. Не copy-paste інлайн-handler'и (вже був випадок з broken Telegram delivery на 3 pillars).
9. **Не використовувати Wistia / embed video без facade.** Sender = -30 Lighthouse на Wistia stack. YouTube embed через lite-youtube-embed facade або клік-to-load pattern.
10. **Не забувати оновлювати `public/llms.txt` + `public/.well-known/api-catalog` після кожної нової сторінки.** Phantom URLs ламають AI-citation trust.

---

## 9. Success Metrics (GSC + GA4 over 90 days)

### Leading indicators (weekly pulse)
| Metric | Source | Baseline (2026-04-23) | Day 30 target | Day 90 target |
|---|---|---|---|---|
| Indexed URLs | GSC Coverage | ~110 | 150 | 250+ |
| Total impressions | GSC Performance | baseline | +100% | +300% |
| UA impressions | GSC filter country:UA | baseline | +120% | +350% |
| Avg position (ніша-queries) | GSC filter "фулфілмент" | baseline | -3 positions | -10 positions |
| CTR home | GSC | baseline | +15% | +40% |
| LCP mobile home (CrUX 75p) | PSI/CrUX | 4.98s | <3.0s | <2.5s |
| CLS mobile home | PSI/CrUX | ok | ok | <0.1 |

### Lagging indicators (monthly review)
| Metric | Source | Day 30 target | Day 90 target |
|---|---|---|---|
| Organic sessions | GA4 | +50% | +200% |
| New leads (Telegram `window.mtpSubmitLead`) | GA4 event `form_submit` | +30% | +100% |
| Conversion rate (lead / session) | GA4 | baseline +10% | baseline +25% |
| Brand search volume | GSC "MTP" / "МТП Груп" | +20% | +80% |
| AI-citation captures (manual test × 20 queries) | Monthly manual | 2/20 | 8/20 |

### Moat indicators (one-time milestones)
- Wikipedia UK article for "МТП Груп" live — target Day 75
- YouTube channel ≥500 subscribers — target Day 90
- Polish /pl/ section indexed 15+ URLs — target Day 60
- 5+ listicle LPs deployed (UA+RU+EN) — target Day 45
- 25/26 vertical niches covered by dedicated LPs — target Day 90

### Rollback triggers (per memory note `redesign_rollback_triggers.md`)
- **Any redesign:** CR -15% OR positions -20% within 7 days → `git revert` immediately.
- **Schema/Indexation:** Coverage errors >5% of sitemap → pause new URLs + audit.
- **Performance:** LCP mobile >4s на 3 pillar pages після fonts fix → investigate (likely new font/script regression).
- **AI-citation:** якщо після Day 60 manual test = 0/20 captures → звернутися до `seo-ai-audit` SKILL для diagnostics.

---

## Приписка для наступної сесії

- Task #78 → `completed`
- Next up: запуск Action #1 (fonts fix) та Action #2 (listicle UA).
- Pipeline: `multi-agent create-page` (RESEARCHER → ANALYZER → STITCH PREVIEW → WRITER → IMAGE-GEN → DESIGN → QA → DEPLOY).
- Stitch mood для listicle — **Editorial** (велика типографіка, comparison table, category nav).
- ADR для listicle у `docs/design-system/pages/top-fulfilment-ukraine-2026.md`.
- Post-deploy: Submit to GSC/Bing + update `public/llms.txt` + `public/.well-known/api-catalog`.

**Report ends.**
