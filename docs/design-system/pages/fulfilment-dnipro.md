# ADR — `/fulfilment-dnipro/` Geo-modifier Stealth Landing

**Date:** 2026-05-05
**Status:** ANALYZER complete, awaiting STITCH approval
**Special class:** First geo-modifier landing — different rules than service pillars

---

## Strategic context — Stealth + Funnel architecture

Per memory rule `feedback_geo_landing_rules.md` (locked 2026-05-05 by user feedback):

- **NOT in Header navigation** — page exists, gets indexed, but isn't part of primary IA
- **NOT in Footer navigation**
- **Hub-and-spoke from `/ua/fulfilment-ukraina/`** (NOT from `/poslugy/`)
- **Body funnels OUT** to `/ua/calculator/`, `/ua/tsiny/`, `/poslugy/`, `/komplektatsiya-zamovlen/`
- **Anti-cannibalization** — bare "фулфілмент" / "фулфілмент Київ" / "фулфілмент Україна" are NEGATIVE keywords (NEVER in title/H1)

---

## Inputs

- Competitor + GSC research: `.claude-flow/research/fulfilment-dnipro.json`
- Keyword strategy: `.claude-flow/research/fulfilment-dnipro-keywords.json`
- GSC signal: 189 imp combined / pos 36-56 (page 4-6) / **0 dedicated competitor pages**

---

## Word count targets (lower than service pillars)

- UA: 1800-2000 words (vs 2700+ for service pillars)
- RU: 1800-2000
- EN: 1500-1800
- **Rationale:** funnel architecture — depth less critical than direct CTAs to converters

---

## Archetype decision — DIRECT mood (all 3 langs same archetype, but differentiated)

Geo-pages need warmth + speed signal — Direct mood matches. But each language gets DIFFERENT visual hook to avoid "translation template" trap (per memory `feedback_template_differentiation.md`):

### 🇺🇦 UA — Direct mood, **Map+Route hero** signature

- **Audience:** Ukrainian business owners in Dnipro (1M city, 4th largest UA)
- **Buyer behaviour:** wants concrete shipping promise + cost
- **Hero:** Map of Ukraine with Kyiv→Dnipro route line, badge "ФУЛФІЛМЕНТ ДЛЯ БІЗНЕСУ З ДНІПРА", H1 with route timing, HeroCTA form
- **Reference:** `/ua/fulfilment-kyiv/` Direct mood
- **WOW-element:** **"Route Timeline"** — visual horizontal strip showing pickup 14:00 → НП Київ → НП Полтава (overnight) → НП Дніпро → клієнт (next day). Concrete timestamps as proof.

### 🇷🇺 RU — Direct mood, **Cost-vs-Self-Storage Calculator hero** signature

- **Audience:** Russian-speaking Dnipro entrepreneurs (large bilingual base)
- **Buyer behaviour:** ROI-focused, "стоит ли переносить склад"
- **Hero:** Side-by-side comparison block "Свой склад в Днепре" vs "Наш склад в Киеве" with concrete numbers (зарплата складского работника, аренда, простои)
- **WOW-element:** **"Break-even Calculator Static Block"** — at what monthly volume does Kyiv-warehouse model becomes economical (200-300 orders/мес threshold)

### 🇬🇧 EN — Direct mood, **Industrial Region Map** signature

- **Audience:** International brands evaluating Eastern Ukraine market entry
- **Buyer behaviour:** wants regional context — Dnipropetrovsk = industrial center, B2B opportunity
- **Hero:** map with Kyiv warehouse + Dnipro region highlighted, with B2B distribution overlay
- **WOW-element:** **"Eastern Ukraine industrial profile"** — Dnipro region facts (population, e-com volume, key industries) + how Kyiv hub serves it

---

## Critical anti-cannibalization rules

**Title MUST contain "Дніпро/Днепр/Dnipro" within first 30 chars.**
**H1 MUST contain city name.**
**Lede MUST mention city in first 30 words.**
**NEVER use bare "фулфілмент" or "фулфілмент Київ" in title/H1/H2/schema.**

KEYWORD AUDIT will hard-fail if any of these violated.

---

## Schema requirements

- LocalBusiness `address` MUST be Kyiv warehouse (Shchaslyve + Bilohorodka), NOT pretend Dnipro address
- `areaServed` includes BOTH:
  - `{"@type":"Country","name":"UA"}`
  - `{"@type":"City","name":"Dnipro"}`
  - `{"@type":"AdministrativeArea","name":"Дніпропетровська область"}`
- Service.serviceType: "Fulfillment Ukraine — Dnipro region e-commerce delivery"
- Service.description: explicit geo-targeting

---

## Hub-and-spoke wiring (different from service pages)

**Hub:** `/ua/fulfilment-ukraina/` (country-wide page, not /poslugy/ services hub)

**Step 9 WIRE-UP changes:**
1. ❌ DO NOT add to `Header.astro` mega-menu
2. ❌ DO NOT add to `Footer.astro`
3. ✅ ADD to lang-switcher map in `Header.astro` (~line 310) — needed for UA↔RU↔EN nav on the page itself
4. ✅ ADD section "Регіональне покриття" to `/ua/fulfilment-ukraina/` linking to `/fulfilment-dnipro/` + future cities (Харків, Запоріжжя, Львів)
5. ✅ ADD subtle link in `/ua/fulfilment-kyiv/` "Інші регіони" → Dnipro page
6. ✅ Update `llms.txt` with 3 new URLs in regional/geo subsection
7. ✅ Update semantic core `MTP_SEMANTIC_CORE_FULL.md` adding row for /fulfilment-dnipro/
8. ❌ SKIP LinkedIn distribution — geo-pages too narrow for company-page broadcast

---

## Funnel CTAs (all 3 langs same structure)

Body MUST contain ≥6 internal links to converter pages:
1. Hero CTA → form submit
2. After WOW element → `/ua/calculator/` "розрахуйте вартість"
3. Mid-page → `/ua/tsiny/` "детальні тарифи"
4. After process section → `/komplektatsiya-zamovlen/` "комплектація 47 секунд"
5. After when-to-switch section → `/ua/fulfilment-dlya-internet-magazynu/`
6. SEO closing → `/poslugy/` "повний перелік послуг" + `/ua/fulfilment-ukraina/` "по всій Україні"
7. Final DarkCTA → standard `<CTA/>` form via Base.astro showCTA=true

---

## Validation test — "3 angles, not translations"

After WRITER step, verify:
- UA H1 vs RU H1 — different framing (UA: route-timing, RU: cost-vs-self-storage)
- Each language has 2 sections that DO NOT exist in others:
  - **UA:** "Як з Києва за 1-2 дні до дніпровського покупця" (route-process emphasis)
  - **RU:** "Когда выгодно закрывать склад в Днепре и переходить на Киев" (decision framework)
  - **EN:** "Eastern Ukraine industrial profile — why Dnipro region matters for B2B fulfillment"

---

## Word target detail

UA: 1800 / RU: 1800 / EN: 1500 — geo-pages don't need 2700-word depth like service pillars. Funnel architecture means content depth is less critical than CTAs.

---

## Next step

STITCH PREVIEW — generate base concept for each of 3 archetype variants. Save to `docs/design-system/stitch-exports/2026-05-05_fulfilment-dnipro/`. Show user. **HARD STOP** until "approved".
