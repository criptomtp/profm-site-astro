# Pillar Uplift Tracker

**Mission.** Поетапно довести всі pillar-сторінки сайту до passing на `npm run validate:pillar`. Не one-shot push, а **многосесійний systematic процес** з checkpoints і чіткими задокументованими кроками.

**Started:** 2026-05-01
**Last update:** 2026-05-01
**Last session note:** Phase 2 batch 10/16 done — fulfilment-ukraina. All 3 schemas 9/9. Words 1437/1030/1255 thin (Phase 4). H1s have em-dash but `&mdash;` HTML entity confuses heuristic (same issue as 3pl-logistics). Cumulative session: 10 triplets, -29 schema fails (38→9). PASS still 9. P2: 2/5.

---

## ⚠️ ОБОВ'ЯЗКОВО ЧИТАТИ цей файл першим у будь-якій pillar-uplift сесії

**Workflow per session:**

1. **Прочитати цей файл повністю.**
2. Знайти найвищий пріоритет з статусом `IN PROGRESS` (продовжити) або найвищий `TODO` (почати).
3. Виконати **один батч** (не весь Phase, не одразу 10 — один логічний шматок, мін. 1, макс. 3 triplets або одна global-batch операція).
4. Після кожного batch:
   - `npm run build`
   - `npm run validate:pillar -- --triplet UA RU EN` для зачеплених триплетів
   - Оновити чек-бокси нижче
   - Оновити "Session log"
   - Commit з message типу `chore(pillar-uplift): Phase 2 batch — added LocalBusiness to UA/RU/EN of <triplet>`
5. **Зупинитись і повідомити користувача** про прогрес. Не йти далі без явного "продовжуй".
6. Якщо session ends mid-batch: лишити статус `IN PROGRESS` з нотатками що зроблено.

---

## Baseline (2026-05-01 — після Phase 1)

- 54 real pillars (skipped 15 non-pillar utility: faq, glossary, about, api-docs, guide, contact)
- ✅ PASS: **6**
- ❌ FAIL: **48**
- Сумарно fails: 38 schemas + 36 words + 39 H1 generic = **113 issues**

Цільовий стан (Phase 7 complete): **48+ pages PASS, ≤6 FAIL** (ті 6 — складні edge cases).

---

## Phase 1: Discovery refinement
**Goal:** виключити non-pillar utility сторінки з scorecard.

- [x] **DONE 2026-05-01** Update `scripts/pillar-scorecard.py` з `NON_PILLAR` regex (faq|glossary|about|api-docs|guide|contact)
- [x] **DONE 2026-05-01** Re-run scorecard, baseline записано (54 pillars)

---

## Phase 2: Schema uplift (global batch — найвищий impact / найменші зусилля)
**Goal:** додати missing JSON-LD schemas (LocalBusiness, GeoCoordinates, PostalAddress + maybe BusinessAudience) до всіх failing pillars. Без зачіпання тексту, лише technical SEO uplift. Очікуваний результат: -38 fails.

**Method per triplet:**
1. Прочитати existing schemaJson блок у файлі
2. Якщо missing LocalBusiness — додати окремий `<script>` з MTP pattern (Щасливе + Білогородка координати, як на `maloho-biznesu`)
3. Якщо missing BusinessAudience — додати у Service.audience
4. Якщо missing Country — додати в Service.areaServed
5. Build + validate single page (`npm run validate:pillar -- dist/<slug>/index.html`)
6. ✅ schemas check має пройти

### TODO list (15 triplets):

#### Already-passing triplets (skip — done)
- [x] **clothing** — odyahu (DONE 2026-05-01 via prior session)

#### P0 batch (high-impact, conversion)
- [x] **prices** — `/ua/tsiny/` + `/ru/tsenu/` + `/en/prices/` **DONE 2026-05-01**: added BusinessAudience + nested Offer to Service, GeoCoordinates + location[] to LocalBusiness; for EN also added full Service description + areaServed Country + FAQPage + BreadcrumbList. All 3 now 9/9 schemas ✅. Words + H1 generic still ❌ (Phase 3/4).
- [x] **calculator** — `/ua/calculator/` + `/ru/calculator/` + `/en/calculator/` **DONE 2026-05-01**: changed Service.provider from @id reference to inline Organization (adds Organization @type), added BusinessAudience to Service.audience, added GeoCoordinates + 2-Place location[] to LocalBusiness, added new FAQPage script with 5 calculator-specific Q/A. RU had different shape (Bilohorodka without description, areaServed as array of 4 CIS Countries) — applied RU-specific patterns. All 3 now 9/9 schemas ✅. Words + H1 generic still ❌.
- [x] **service-hub** — `/poslugy/` + `/ru/services/` + `/en/services/` **DONE 2026-05-01**: UA poslugy already had 9/9 schemas (no change). RU services + EN services were missing Offer — added nested `offers:[Offer]` to AggregateOffer (RU) and full Service block rewrite with description + offers (EN). All 3 now 9/9 schemas ✅. RU only 1 fail away (H1 generic). UA still words+H1. EN still words+H1.
- [x] **home** — `/index.html` + `/ru/index.html` + `/en/index.html` **DONE 2026-05-01**: all 3 had thin schema-stack (only WebSite + LocalBusiness + FAQPage; EN missing FAQPage too). Added GeoCoordinates + 2-Place location[] to LocalBusiness; added new Service script with description, Organization provider, BusinessAudience, AggregateOffer with nested Offer; for EN also added new FAQPage script with 7 Q/A translated/adapted from UA. All 3 now 9/9 schemas ✅. Words + H1 generic still ❌ (Phase 3/4).

#### P1 batch (top-of-funnel + flagship)
- [x] **what-is-fulfillment** — `/ua/shcho-take-fulfilment/` + `/ru/chto-takoe-fulfilment/` + `/en/what-is-fulfillment/` **DONE 2026-05-01**: this is Article-type pillar (not Service-type) — had thick schema-stack already (Article, WebPage, VideoObject, ImageObject, Person, FAQPage, BreadcrumbList, Speakable, Organization) but was missing all "service signal" types (LocalBusiness/Geo/PostalAddress/BusinessAudience/Service/Offer/Country). Appended 2 new scripts to schemaJson template literal: full LocalBusiness (with geo + 2-Place location[]) and full Service (description + Organization provider + BusinessAudience + AggregateOffer with nested Offers). Words 3042/2815/3657 already ≥ 2500. **Result: only H1 generic ⚠️ remains — 1 warning from full PASS on all 3 langs.**
- [x] **3pl-logistics** — `/ua/3pl-logistyka/` + `/ru/3pl-logistika/` + `/en/3pl-logistics/` **DONE 2026-05-01**: smallest batch — already had Service+LocalBusiness+Organization+PostalAddress+Country+Offer+FAQPage+Breadcrumb. Just added GeoCoordinates + 2-Place location[] to LocalBusiness, BusinessAudience to Service. 2 surgical replacements per file. EN had `²` JSON.stringify-escaped sqm symbol — adapted pattern. All 3 now 9/9 schemas ✅. Words 1092/879/1014 still ❌ (Phase 4); H1 generic ⚠️ (already has &mdash; twist but `&nbsp;` HTML entities confuse heuristic — Phase 3 will refine).
- [x] **fulfilment-rozetka** — `/fulfilment-rozetka/` + `/ru/fulfilment-rozetka/` + `/en/fulfillment-for-rozetka-sellers/` **DONE 2026-05-01**: had 0 LocalBusiness across all 3 (only Service+FAQ+Breadcrumb+BusinessAudience+Offer+Organization+Country). Single append: full LocalBusiness script (with geo + 2-Place location[] + 2-PostalAddress) per language. **🎊 UA + EN now FULL PASS** (first non-clothing pages!). RU close: 2281 words and H1 generic.
- [x] **fulfilment-prom** — `/fulfilment-prom/` + `/ru/fulfilment-prom/` + `/en/fulfilment-prom/` **DONE 2026-05-01**: same shape as rozetka — had everything except LocalBusiness. Single append per language. 🎊 RU now FULL PASS (words 2917, H1 "Фулфилмент для продавцов Prom.ua — от 22 ₴ за заказ" has em-dash + numeric). UA + EN H1s also brand-hooks ("FBO у Prom.ua не існує. До сьогодні.", "Prom has 700,000 sellers and zero native FBO.") — only words gap remains (2380/2131). All 3 schemas 9/9 ✅. UA prom note: pages had JS object literal with single quotes (not JSON double quotes) for serviceSchema — JSON.stringify converts at build time, no issue.

#### P2 batch (geo + specific)
- [x] **fulfilment-kyiv** — `/ua/fulfilment-kyiv/` + `/ru/fulfilment-kiev/` + `/en/fulfillment-kyiv/` **DONE 2026-05-01**: had Service+LocalBusiness+City+PostalAddress+FAQ+Breadcrumb+Org+Offer. Missing GeoCoordinates in LocalBusiness (was inside City schema only) + BusinessAudience + standalone Country @type. Surgical: replaced `areaServed:{City}` with `areaServed:[City, Country]`, added BusinessAudience, added geo+location[] to LocalBusiness. All 3 now 9/9 schemas ✅. RU H1 brand-hook ("Ваш склад без аренды. Ваша логистика без логистов." — paradox + period). UA+EN H1 generic. Words 1183/1087/1398 thin (Phase 4).
- [x] **fulfilment-ukraina** — `/ua/fulfilment-ukraina/` + `/ru/fulfilment-ukraina/` + `/en/fulfillment-ukraine/` **DONE 2026-05-01**: had Service+Country+Org+FAQ+Breadcrumb+Offer (UA/RU; EN had no Offer). Missing LocalBusiness/Geo/PostalAddress/BusinessAudience. Added BusinessAudience to Service.audience (UA/RU/EN), full LocalBusiness append per language, EN got Offer added too. All 3 now 9/9 schemas ✅. Words 1437/1030/1255 thin. H1s have `&mdash;` but heuristic doesn't decode HTML entity — Phase 3 fix.
- [ ] **vazhki-tovary** — `/ua/fulfilment-vazhkykh-tovariv/` + `/ru/fulfilment-vazhkykh-tovariv/` + `/en/heavy-goods/`
- [ ] **pallet-storage** — `/ua/paletne-zberigannya/` + `/ru/paletnoe-khranenie/` + `/en/pallet-storage/`
- [ ] **warehouse-services** — `/ua/skladski-poslugy/` + `/ru/skladskie-uslugi/` + `/en/warehouse-services/`

#### P3 batch (already mostly-passing — quick wins)
- [ ] **cosmetics** — UA mostly OK, RU 1 fail, EN passing (only quick top-up needed)
- [ ] **small-biz** — UA needs words, RU passing, EN 1 fail
- [ ] **marketplaces** — UA 2 fails, RU 1, EN 1
- [ ] **online-store** — UA 2 fails, RU 2, EN passing

---

## Phase 3: H1 brand-hooks (global batch)
**Goal:** переписати ~39 generic H1 у brand-hook формат (>5 words + comma/dash twist OR imperative). Не зачіпає body, чисто заголовок. Очікуваний результат: -39 ⚠️.

**Method:** для кожної H1 з `⚠️ generic`, придумати brand-hook (sample patterns у `docs/pillar-page-checklist.md` секція C). Користувач **обов'язково апрувить кожен H1 перед застосуванням** (важливо для SEO — H1 це ranking signal).

### TODO (per triplet — апрувити список перед merge):

- [ ] Compile current H1s + propose brand-hook variants (table format) → user approve → apply
- [ ] Per-triplet apply (same triplet groups як у Phase 2)

---

## Phase 4: Words uplift — P0 conversion pages
**Goal:** підняти топ-conversion pages до 2500+ слів. Не just word-stuffing — додати реально корисний контент: case studies, FAQ, technical depth, comparison tables, MTP anchor numbers.

**Per page method:** прочитати існуючий контент → виявити gaps (що бракує? competitor analysis за CLAUDE.md MULTI-AGENT PIPELINE) → додати 2-3 нові секції → humanizer pass → validate.

### TODO (4 triplets, ~12 pages, ~12-20 годин роботи):

- [ ] **prices** triplet — `tsiny` / `tsenu` / `prices`
- [ ] **calculator** triplet
- [ ] **service-hub** triplet — `poslugy` / `services` / `services`
- [ ] **home** triplet — `/` / `/ru/` / `/en/`

---

## Phase 5: Words uplift — P1 top-of-funnel + flagship

- [ ] **what-is-fulfillment** triplet
- [ ] **3pl-logistics** triplet
- [ ] **fulfilment-rozetka** triplet
- [ ] **fulfilment-prom** triplet

---

## Phase 6: Words uplift — P2 geo/specific

- [ ] **fulfilment-kyiv** triplet
- [ ] **fulfilment-ukraina** triplet
- [ ] **vazhki-tovary** triplet
- [ ] **pallet-storage** triplet
- [ ] **warehouse-services** triplet

---

## Phase 7: Final cleanup + edge cases

- [ ] Re-run full `pillar-scorecard.py`
- [ ] Identify residual edge cases (probably 3-6 pages)
- [ ] Document why вони лишаються FAIL (e.g. tool pages, redirect-heavy etc) у цьому файлі
- [ ] Update `pillar-scorecard.py` to flag known-exempt cases as `EXEMPT` not `FAIL`
- [ ] Final deploy + reindex via Indexing API
- [ ] Mark Mission accomplished, archive tracker as `docs/pillar-uplift-tracker-2026-completed.md`

---

## Session log (rolling — новіші зверху)

### 2026-05-01 — Phase 2 batch 10: fulfilment-ukraina triplet
- Pre-uplift: pages had Service+Country+Org+FAQ+Breadcrumb+Offer (UA/RU only; EN didn't have offers). Missing all geo signals (LocalBusiness/Geo/PostalAddress) + BusinessAudience.
- Surgical: add BusinessAudience to Service.audience for all 3 (between areaServed and offers); for EN added missing Offer too; full LocalBusiness append per language to schemaJson template
- All 3 schemas 9/9 ✅
- H1 status — same recurring issue as 3pl-logistics:
  - UA "Фулфілмент в Україні&mdash; економія до 49% vs власний склад" — has em-dash twist + concrete % but `&mdash;` HTML entity (no space before it) confuses heuristic word count
  - RU same pattern with `&mdash;`
  - EN "Ukrainian Fulfillment Services for Global Brands" — generic
- Words 1437/1030/1255 — far below 2500 (Phase 4)
- Net progress: -3 schema fails. Cumulative session: -29 (38 → 9)
- Next session: continue P2 with `vazhki-tovary` triplet (heavy goods)

### 2026-05-01 — Phase 2 batch 9: fulfilment-kyiv triplet (P2 start)
- Pages had Service+LocalBusiness+City+PostalAddress+FAQ+Breadcrumb+Org+Offer. Missing standalone Country @type, BusinessAudience, geo in LocalBusiness (was only inside City schema)
- Surgical replacements per file:
  1. Service: `areaServed:{City}` → `areaServed:[City, Country]` (adds Country) + add BusinessAudience after
  2. LocalBusiness: add `geo` + `location[]` to address tail
- All 3 schemas 9/9 ✅
- H1 status:
  - UA "Фулфілмент у Києві. Склад під ключ від 18 грн." — generic per heuristic (period not accepted as twist; also "под ключ" listed as banned phrase in humanizer doc)
  - RU "Ваш склад без аренды. Ваша логистика без логистов." — brand-hook ✅ (paradox + period; period works because heuristic also has 'не'/'без' lookbehind)
  - EN "Your logistics base in Eastern Europe." — generic short
- Words 1183/1087/1398 — well under 2500 (Phase 4)
- Note: UA H1 has "під ключ" — already flagged in `docs/humanizer-ua-mtp.md` forbidden list. Phase 3 should fix this.
- Net progress: -3 schema fails. Cumulative session: -26 (38 → 12)
- Next session: continue P2 with `fulfilment-ukraina` triplet

### 2026-05-01 — Phase 2 batch 8: fulfilment-prom triplet 🎊 (P1 complete)
- Same shape as rozetka — had Service+BusinessAudience+Offer+FAQ+Breadcrumb+Org+Country, missing only LocalBusiness/Geo/PostalAddress
- UA file uses JS object literal with single quotes (not JSON double quotes) — JSON.stringify converts to proper JSON at build time, so no issue
- Single append per language: full LocalBusiness with geo + 2-Place location[] + 2 PostalAddress
- Words: UA 2380, RU 2917, EN 2131. Only RU passed words threshold (≥2500). UA + EN need ~150-400 more words (Phase 4)
- H1s all brand-hooks per heuristic:
  - UA "FBO у Prom.ua не існує. До сьогодні." — declarative + paradox
  - RU "Фулфилмент для продавцов Prom.ua — от 22 ₴ за заказ" — em-dash + numeric
  - EN "Prom has 700,000 sellers and zero native FBO." — declarative + paradox + concrete
- 🎊 RU /ru/fulfilment-prom/ now FULL PASS
- Net progress: -3 schema fails. Cumulative session: -23 (38 → 15)
- Site-wide PASS count: 8 → 9 (+1 from this batch)
- **🎊 P1 batch (4/4) COMPLETE** (what-is-fulfillment, 3pl-logistics, fulfilment-rozetka, fulfilment-prom)
- Next session: start P2 batch with `fulfilment-kyiv` triplet (geo-specific Kyiv-targeted pillar)

### 2026-05-01 — Phase 2 batch 7: fulfilment-rozetka triplet 🎊
- Pages had everything except LocalBusiness — service-style page already with BusinessAudience, Offer, FAQPage, BreadcrumbList, Organization
- Single append: full LocalBusiness script (with geo + 2-Place location[] + 2 PostalAddress with localized streetAddress) per language
- Words already ≥2500 on UA (3127→2603 in dist) and EN (3149→2650). RU 2862→2281 in dist (under threshold)
- Both UA + EN H1 already brand-hooks: "Альтернатива Rozetka FBO для категорій, які вона не приймає" and "A multi-marketplace gateway to Ukraine — without Rozetka FBO lock-in"
- **🎊 RESULT: UA /fulfilment-rozetka/ and EN /en/fulfillment-for-rozetka-sellers/ now FULL PASS — first non-clothing pillars to clear the gate fully**
- RU /ru/fulfilment-rozetka/ close to PASS: words 2281 (need 219 more), H1 "Украина как логистический хаб для Rozetka и рынка СНГ" generic (need twist or imperative — Phase 3)
- Net progress: -3 schema fails. Cumulative session: -20 (38 → 18)
- Site-wide PASS count: 6 → 8
- Next session: continue P1 with `fulfilment-prom` triplet (last P1 item)

### 2026-05-01 — Phase 2 batch 6: 3pl-logistics triplet
- Tiniest batch in Phase 2 so far. Already had 8 of 9 must-have types. Just missing GeoCoordinates + BusinessAudience.
- 2 surgical python replacements per file (LocalBusiness add geo+location[], Service add audience after areaServed)
- EN had JSON.stringify-escaped `²` sqm symbol — used escape-aware pattern
- Validate: ✅ schemas 9/9 all 3, ❌ words 1092/879/1014, ⚠️ H1 generic (H1 has &mdash; em-dash twist but `&nbsp;` HTML entity in H1 confuses brand-hook heuristic word count — same issue as RU what-is-fulfillment)
- Net progress this batch: -3 schema fails. Cumulative session: -17 (38 → 21)
- Next session: continue P1 with `fulfilment-rozetka` (UA root + RU /ru/ + EN /en/fulfillment-for-rozetka-sellers/)

### 2026-05-01 — Phase 2 batch 5: what-is-fulfillment triplet (P1 start)
- Article-type pillar (not Service-type) — different schema profile from prior batches
- All 3 had rich Article+WebPage+Video+Person+FAQPage+Breadcrumb+Speakable+Organization, but were missing all 7 "service signal" types validate gate requires
- Solution: append 2 new scripts to existing schemaJson template literal (LocalBusiness + Service) — non-invasive, doesn't touch existing Article schema
- Words already ≥2500 on all 3 (3042/2815/3657) — biggest single-batch progress so far
- **Only H1 generic ⚠️ remains** — these 3 are first triplet to be 1-warning-from-PASS. Phase 3 will flip them
- Net progress: -3 schema fails. Cumulative session: -14 (38 → 24)
- Note: H1 chek heuristic doesn't accept period as twist marker — RU H1 has em-dash but `&nbsp;` HTML entity confuses word count. Both fixable in Phase 3 (H1 rewrites + heuristic refinement).
- Next session: continue P1 with `3pl-logistics` triplet

### 2026-05-01 — Phase 2 batch 4: home triplet (P0 complete!)
- All 3 homepages had thinnest schema-stack of any pillars seen so far: WebSite + LocalBusiness + FAQPage (UA/RU only). EN homepage didn't even have FAQPage.
- LocalBusiness uplift: added GeoCoordinates + 2-Place location[] (Schaslyve+Bilohorodka) + missing description on Bilohorodka address (UA, EN — RU already had it)
- NEW Service script per language: full hub-Service description (e-commerce, fashion, marketplaces integrations), Organization provider, BusinessAudience (different angle per language: UA-focused / CIS-focused / international-focused), AggregateOffer with 2 nested Offers (per-shipment + storage)
- EN-only: NEW FAQPage script with 7 Q/A — translated and slightly adapted from UA (added 21-day onboarding for international brands, marketplace count clarification)
- Validate: ✅ schemas 9/9 all 3 langs, ✅ hreflang reciprocal, ❌ words still <2500, ⚠️ H1 generic
- Net progress this batch: -3 schema fails. Cumulative session: -11 schema fails (38 → 27)
- **P0 batch DONE** (4/4: prices, calculator, service-hub, home)
- Next session: start P1 batch with `what-is-fulfillment` triplet (top-of-funnel pillar — already partial PASS for some langs)

### 2026-05-01 — Phase 2 batch 3: service-hub triplet
- Surprise: UA poslugy already had 9/9 schemas (Organization, LocalBusiness, GeoCoordinates, BusinessAudience, FAQPage all present from prior work). No UA changes needed.
- RU services missing only Offer — added nested `offers:[Offer]` to existing AggregateOffer
- EN services had bare Service block (just name+provider+areaServed) — replaced with full Service (description + AggregateOffer + nested Offer)
- Validate: ✅ schemas 9/9 all 3 langs, ✅ hreflang reciprocal
- RU services: only 1 fail left (H1 generic) — close to full PASS!
- Net progress this session: -2 schema fails (this batch). Cumulative session: -8 schema fails (38→30)
- Next session: continue Phase 2 with `home` triplet (last P0) — `/index.html` + `/ru/index.html` + `/en/index.html`. Heads-up: home pages can be sensitive (SEO impact, hero CTAs); be conservative.

### 2026-05-01 — Phase 2 batch 2: calculator triplet
- 3 files had richer schema-stack than prices (12 types each: WebApplication, OfferCatalog, UnitPriceSpecification, QuantitativeValue, etc), but missing Organization (used @id reference instead), GeoCoordinates, BusinessAudience, FAQPage
- UA + EN: standard pattern + areaServed kept (Ukraine for UA, [Ukraine, EU] for EN)
- RU: had 4-country areaServed [Ukraine, Kazakhstan, Moldova, Georgia] for CIS audience — preserved as-is, just appended audience after; also Bilohorodka address had no description field, added it
- All 3 FAQs unique to calculator (free to use? accuracy? inputs? packaging? volume discount?)
- Net progress this session: -6 schema fails (38 → 32)
- Next session: continue Phase 2 with `service-hub` triplet (poslugy / ru/services / en/services) — recommended next P0 item

### 2026-05-01 — Phase 2 batch 1: prices triplet
- Discovered current schemas in 3 files (UA had 12 types, RU had 12, EN had only 6 — bare Service)
- Surgical python replacements for UA/RU: added BusinessAudience to Service, nested Offer in offers, GeoCoordinates + 2-Place location[] in LocalBusiness
- For EN: full Service rewrite (added description, areaServed Country, BusinessAudience, nested Offer), GeoCoords in LocalBusiness, plus injected FAQPage (translated 6 Q/A from UA) + BreadcrumbList scripts
- Build: 202 pages, 0 errors
- Validate triplet: ✅ schemas 9/9 all 3, ✅ hreflang reciprocal, ❌ words still <2500 (deferred Phase 4), ⚠️ H1 still generic (deferred Phase 3)
- **Pre-existing observation** (NOT introduced by this work): RU tsenu and EN prices have DUPLICATE Service+LocalBusiness blocks (one in schemaJson prop, one inline). UA tsiny is clean (single set). Track as separate cleanup task — not Phase 2 scope.
- Net progress: -3 schema fails (from 38 → 35 site-wide)
- Next session: continue Phase 2 with another P0 triplet (recommend `calculator` next — same conversion class, similar shape)

### 2026-05-01 — initial setup
- Created tracker
- Phase 1 done — refined scorecard discovery (excluded 15 non-pillar utility pages)
- Baseline locked: 54 pillars, 6 PASS, 48 FAIL
- Built complete TODO list across Phases 2-7

---

## Snapshot reference (CSV)

Latest scorecard snapshot: `docs/pillar-scorecard.csv`
Re-generate with: `npm run pillar:scorecard` (after build)

If counts shift dramatically between sessions — investigate before proceeding.
