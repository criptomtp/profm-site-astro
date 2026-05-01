# ADR: /fulfilment-dlya-odyahu/ (UA + RU + EN)

**Date:** 2026-05-01
**Archetype:** Direct (CTA-driven, conversion-focused)
**Stitch concept:** V1 (default) — see `docs/design-system/stitch-exports/2026-04-30_fulfilment-dlya-odyahu/`
**Approval:** "approved V1" — 2026-05-01

---

## URLs

| Language | URL | File path |
|---|---|---|
| UA | `/fulfilment-dlya-odyahu/` | `src/pages/fulfilment-dlya-odyahu.astro` |
| RU | `/ru/fulfilment-dlya-odezhdy/` | `src/pages/ru/fulfilment-dlya-odezhdy.astro` |
| EN | `/en/fulfilment-for-clothing/` | `src/pages/en/fulfilment-for-clothing.astro` |

UA on root (no `/ua/` prefix) per URL Policy 2026-04-22.

---

## Content angles (different per language, NOT translations)

- **UA — Operational angle:** SKU-облік за моделлю + кольором + розміром, обробка повернень з фото-перевіркою, сезонні піки маркетплейсів, FBS-інтеграції з Rozetka/Prom/Kasta. Аудиторія: українські fashion-бренди + селлери маркетплейсів.
- **RU — Cost-economy angle:** Економіка входу для брендів з СНД (KZ/MD/GE/AM), 21-денний onboarding, біллінг USD/EUR, ×2 економія vs власний склад. Аудиторія: бренди з СНД + русскомовні UA-селлери.
- **EN — Cross-border angle:** Ship from Ukraine to EU in 3-5 days via Polish consolidation, war-resilient ops (0 days downtime since 2022), GDPR-compliant, EUR billing, native Shopify/Etsy/Amazon EU. Аудиторія: international DTC fashion brands.

---

## Design decisions

- **Hero:** Direct mood — full-width dark hero (`#000`) with `linear-gradient` overlay over `/images/odyahu-hero.jpg`. Left-side H1 + subheading + red 3px vertical rule. Right-side white form-card with `<HeroCTA>` component (canonical, light theme, lang-specific copy).
- **Stats strip:** 4 numbers under hero — different per language (UA = ops metrics, RU = economy metrics, EN = international metrics).
- **Hero form:** `<HeroCTA>` component (NOT custom `id="heroForm"`). Verified Telegram delivery via `window.mtpSubmitLead`. Source tags: `hero /fulfilment-dlya-odyahu/`, `hero /ru/fulfilment-dlya-odezhdy/`, `hero /en/fulfilment-for-clothing/`.
- **6 problem cards** in 3-col grid on white. Each card has red number badge + h3 + p (max 14px).
- **4-step "How it works"** with red circles + dotted line. Pricing per step.
- **Pricing comparison table** (own warehouse vs MTP) — language-specific currency (UAH for UA, USD-equivalent for RU, EUR for EN).
- **Tariffs table** — full transparent pricing (10-11 rows). Volume tiers (0-49 / 50-99 / 100-199 / 200+).
- **Integrations strip** — 6 logos (Rozetka, Prom, Kasta, KeyCRM, SalesDrive, Nova Poshta).
- **Deep dive section** — dark `#0a0a0a` background, 4 long-form blocks (h3 + 3 paragraphs each). Different topics per language.
- **3 audience cards** — defines target personas.
- **FAQ** — 6-7 questions with proper FAQPage schema.
- **SEO article** — 600-800 words long-form content for E-E-A-T and AI citation readiness.

---

## Schema.org markup

- `Service` with `provider`, `areaServed`, `serviceType`, `audience`, `offers`
- `FAQPage` with 6-7 Q/A pairs (different per language)
- `BreadcrumbList` 3-level
- (UA only) plus `LocalBusiness` placeholder for future addition

---

## Hreflang

All 3 pages cross-link via:
```html
<link rel="alternate" hreflang="uk" href=".../fulfilment-dlya-odyahu/">
<link rel="alternate" hreflang="ru" href=".../ru/fulfilment-dlya-odezhdy/">
<link rel="alternate" hreflang="en" href=".../en/fulfilment-for-clothing/">
<link rel="alternate" hreflang="x-default" href=".../fulfilment-dlya-odyahu/">
```

---

## Integration touchpoints

- ✅ `src/components/Header.astro` mega-menu (3 cols updated): UA col1, RU col1, EN col1 — added with `NEW` badge
- ✅ `src/components/Header.astro` switcherMap: 3 entries (`fulfilment-dlya-odyahu`, `fulfilment-dlya-odezhdy`, `fulfilment-for-clothing`)
- ✅ `public/llms.txt`: 3 entries added in Services section after cosmetics block
- ✅ Hero images: `/public/images/odyahu-hero.jpg`, `/public/images/odyahu-rails.jpg`, `/public/images/odyahu-packing.jpg` (Pollinations.ai)
- ✅ `docs/MTP_SEMANTIC_CORE_FULL.md` row 2 marked `🚧 In Progress` 2026-04-30 → ready to flip to ✅ Done after deploy verification

---

## Build verification (2026-05-01)

```
[dual-md] 198 written, 3 skipped, 0 errors, 0 thin
```

| Page | HTML | .md twin | Words |
|---|---|---|---|
| UA | 118 KB | 33 KB | 2,731 |
| RU | 113 KB | 29 KB | 2,429 |
| EN | 102 KB | 21 KB | 3,067 |

All exceed the 1,200-word minimum from the project checklist.

---

## Rollback trigger

If CR drops &gt;15% **AND** organic positions drop &gt;20% within 7 days of deploy → `git revert` and post-mortem.

---

## Future iterations

- **VA (Trust & Scale)** — when we collect 8+ logos of fashion clients with NDA permission
- **VB (Live Ops)** — likely never (mismatch with audience)
- **Add real client cases** in deep-dive sections (currently industry-typical numbers, no NDA cases)
- **Add `/blog/case-fashion-bestsellers/`** as supporting content magnet (Tier 2 backlog)
