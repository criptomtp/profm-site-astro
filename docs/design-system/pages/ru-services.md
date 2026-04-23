---
page: /ru/services/
archetype: Industrial
mood: Tactical Monolith (Swiss Brutalism)
approval_date: 2026-04-23
stitch_project_id: "16366500142707399412"
stitch_screen_id: "87e24dc794554c80a4132f1f8e3bbe28"
stitch_export: docs/design-system/stitch-exports/2026-04-23_ru-services/
status: live
---

# ADR — /ru/services/ CIS-entry rewrite (dedup from /ua/services/)

## Problem

GSC Coverage Drilldown 2026-04-23 flagged `/ru/services/` as *"Копія. Google вибрав іншу канонічну сторінку ніж користувач"*. Root cause: `/ru/services/` was a word-for-word translation of `/ua/services/` — identical H2s, same 8 service cards in identical order, same stats, same FAQ. Google correctly collapsed the two.

## Solution

Full rewrite of `/ru/services/` with a **distinct positioning**: Ukrainian fulfillment as a market-entry product for CIS brands (Kazakhstan, Moldova, Georgia, Armenia, Uzbekistan, Azerbaijan), not a generic 3PL service. This reframes the page so it competes in a different intent cluster from `/ua/services/`.

## Positioning differences from /ua/services/

| Dimension | `/ua/services/` (unchanged) | `/ru/services/` (this rewrite) |
|---|---|---|
| Audience | Ukrainian SMB ecommerce | CIS brands entering Ukraine |
| Key pain points | UA local logistics cost | Customs, УкрСЕПРО, UAH settlement |
| Timeline | 1–3 day start | 21-day cross-border onboarding |
| Marketplaces | Rozetka, Prom — UA seller flow | Rozetka, Prom via agent-account |
| Pricing | UAH-facing | UAH + USD + EUR with SWIFT/SEPA |
| FAQ topics | SLA, billing, confidentiality | Customs, juridical model, acquiring, return consolidation |

## Archetype — Industrial

Split hero (text + country list card), uppercase section labels, StatsBar, zero border-radius,
monochrome grid of pain-point cards and service cards, dark timeline section as WOW centrepiece.
Palette fixed: #e63329 / #000 / #fff only.

## WOW element — 21-day timeline

6 phases (days 1–3 legal, 4–7 audit, 8–11 crossborder, 12–14 acceptance, 15–18 marketplaces,
19–21 launch) rendered as a dark 2-column grid. Each cell is a self-contained step with a red
day-label, bold phase heading, and operational description. Mobile collapses to single column.

## Internal linking

- Breadcrumb: Главная → Услуги для брендов из СНГ
- Hreflang: uk `/ua/services/`, ru `/ru/services/`, en `/en/services/`, x-default `/ua/services/`
- Mega-menu: already present (existing RU services entry)
- Footer: no change (existing link covers this URL)

## SEO

- Title: "Украинский фулфилмент для брендов из СНГ — MTP Group" (55 chars)
- Description: "3PL-вход на рынок Украины для продавцов из Казахстана, Молдовы, Грузии, Армении. Таможня, УкрСЕПРО, Rozetka, Prom, расчёт в USD. Запуск за 21 день." (156 chars)
- H1: exactly one (`Украинский фулфилмент для брендов из СНГ`)
- Schema.org: Service (6 areasServed countries + UA) + BreadcrumbList + FAQPage (11 Q&A)
- Content length: ~3 700 слов (vs ~1 500 слов в старой версии → +145%, значительно выше +20% правила)

## Content policy

- 6 pain-point cards (Industrial monolith grid, red top-border)
- 21-day timeline (dark 2-col grid, red day labels)
- 8 service cards (zero-gap grid, red numbering)
- Integration matrix table (platform × onboarding scheme × time × revenue share)
- 3 case snapshots (KZ/MD/GE hypothetical scenarios — no fabricated client names)
- 11-item FAQ (all CIS-specific: customs, juridical, currency, UкрSEPRO, consolidation)
- Long-form SEO article 9 H3 sections (~1500 words) explaining macro context, juridical model, customs strategy, certification reality, currency math, operational resilience, what MTP does NOT do, first step

## Language audit

- No Ukrainianisms (grep ran 2026-04-23 on the final file: zero hits)
- Terminology consistent with existing live CIS-facing pages: `/ru/about/`, `/ru/guide/`, `/ru/recalls/` (all rewritten 2026-04-20)

## Hero CTA compliance

Uses `<HeroCTA lang="ru" theme="dark" sourceTag="hero /ru/services/ CIS" />` — verified Telegram delivery path per CLAUDE.md hero form rule.

## CSS isolation

All styles prefixed `ru-srv-*` (BEM). Tokens scoped under `:root --ru-srv-*`. No class collisions with other pages.

## Verification

- Build to be verified (next step)
- Word count target met: content ≈ 3700 words vs thin CIS competitor avg ~1500–2000 → +85–145%
- Stitch approval: 2026-04-23 (user: "Нормально мені подобається")

## Rollback trigger

If within 7 days: conversion rate on /ru/services/ drops >15% OR organic position drops >20%, revert to prior version via `git revert`. Baseline CTR to be captured from GA4 + GSC before deploy.
