---
page: /ru/services/
archetype: Industrial
mood: Tactical Monolith (Swiss Brutalism)
approval_date: pending
stitch_project_id: "16366500142707399412"
stitch_screen_id: "87e24dc794554c80a4132f1f8e3bbe28"
stitch_screen_title: "MTP Group — 3PL CIS Market Entry Landing Page"
dimensions: 2560x10566
palette:
  - "#e63329 (red accent)"
  - "#000 (primary)"
  - "#fff (surface)"
---

# Stitch Preview — /ru/services/ (Industrial, CIS-facing)

## Rationale

Google GSC flagged `/ru/services/` as Duplicate (chose different canonical) because it was a
word-for-word translation of `/ua/services/` — same H2s, same 6 service cards in identical order,
same stats, same FAQ. To deduplicate, this rewrite positions `/ru/services/` as a distinct CIS
market-entry product, not a translation.

- UA `/ua/services/` → local Ukrainian ecommerce (Nova Poshta, Rozetka, Prom, hryvnia)
- RU `/ru/services/` → **CIS B2B entering Ukraine** (Kazakhstan, Moldova, Georgia, Armenia,
  Uzbekistan sellers wanting access to Ukrainian market)
  - Customs / ВЭД onboarding
  - УкрСЕПРО certification path
  - UAH/EUR/USD settlement with home-country withholding docs
  - 21-day onboarding (vs 14-day UA) to account for cross-border docs
  - Rozetka + Prom + Kaspi cross-listing matrix

## WOW Element

**Market-entry timeline strip**: 21-day vertical timeline (day 0 → day 21) with 6 milestones —
customs doc set, УкрСЕПРО, Rozetka account verification, first pallet arrival, system integration,
first shipment. Each milestone shows minimum doc pack required and which side (seller vs MTP)
handles it.

## Archetype signals applied

- Split hero (left: headline + CIS target; right: timeline preview)
- Uppercase labels (`3PL · МЕЖДУНАРОДНЫЙ ВХОД · УКРАИНА`)
- StatsBar under hero (60k отправлений · 10+ лет · 99.7% точность · 21 день запуск)
- Zero border-radius, high-contrast black/white with red accent only
- Service grid reorganized around CIS pain points, not UA local ones

## Internal references

- Archetype spec: `docs/design-system/archetypes/industrial.md`
- Sibling language: `/ua/services/` remains unchanged (UA local angle)
- Prior CIS rewrites (confirmed live 2026-04-20):
  - `docs/design-system/pages/ru-about.md`
  - `docs/design-system/pages/ru-guide.md`
  - `docs/design-system/pages/ru-recalls.md`

## Stitch suggestions returned by model

1. Add a section for specific CIS country case studies (Kazakhstan, Moldova)
2. Show the mobile version of the timeline
3. Adjust the intensity of the red accents

## Status

**Awaiting user approval** of `screenshot.png` before proceeding to АГЕНТ 3 (Writer).
