---
slug: glossary
created: 2026-04-23
archetype: editorial
status: approved-retroactive
---

# Glossary Hub — Concept

## Archetype: Editorial

Retroactive documentation — page was built during SEO audit item #12 execution in
autonomous mode; Stitch Preview (АГЕНТ 2.5) was skipped in error. Concept captured
post-implementation to maintain the Stitch-exports audit trail.

## Mood & Rationale

**Why Editorial**: glossary is a long-form reference/knowledge hub, analogous to
FAQ and the blog category index — big typography, TOC chips for term navigation,
no hero image, clear category feel. Matches `docs/design-system/archetypes/editorial.md`.

## Palette (locked)

- `#e63329` — red accent (hero label chip, section top borders, term lede borders)
- `#000` — primary text
- `#fff` — background

No other colors. Token source: `src/styles/stitch-tokens.css`.

## Layout Signals

1. Hero: small red label chip ("ГЛОСАРІЙ / ГЛОССАРИЙ / GLOSSARY") + oversized H1 + 1-sentence lede + breadcrumb trail.
2. TOC chips bar: horizontal pill-nav anchoring each defined term; sticky offset via `scroll-margin-top`.
3. Term sections: `<section>` per term, `.glos-term__lede` with 4px red left-border + `<dl>` for FBA/FBO/FBS fanout.
4. Related-links footer: dark (`#111`) band linking pillar / service hub / pricing / calculator / FAQ.

## WOW Element (single, per rule)

Schema.org `DefinedTermSet` + `DefinedTerm` embedded in page JSON-LD — canonical
AI-Overviews pattern for term dictionaries. Each term has its own `@id` anchor so
Google can deep-link to individual definitions in SERP rich results.

## Shared Components Used

- `src/layouts/Base.astro` — canonical, hreflang, schema props
- `src/components/Header.astro` — lang switcher (keys added: `glosariy` / `glossariy` / `glossary`)
- `src/components/Footer.astro` — Knowledge column, added glossary link 2026-04-23

## Stitch Preview

None captured (process violation). If regenerated later, drop `screenshot.png`
and `export.html` alongside this file.

## Approval

- **Approval path**: built during SEO audit autonomous run, user verified post-hoc on 2026-04-23.
- **Follow-up**: ADR at `docs/design-system/pages/glossary.md`.
