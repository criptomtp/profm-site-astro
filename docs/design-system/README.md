# MTP Design System

Source of truth for the Stitch-driven visual language on fulfillmentmtp.com.ua.

## Structure

```
docs/design-system/
  README.md              — this file
  archetypes/            — three fixed moods (Industrial / Direct / Editorial)
    industrial.md
    direct.md
    editorial.md
  stitch-exports/        — raw Stitch artifacts per approved concept
    YYYY-MM-DD_[slug]/
      concept.md
      screenshot.png
      export.html        (optional)
  pages/                 — per-page ADR + baseline + validation
    [slug].md            — archetype, mood deviation, Stitch link, approval date
    [slug]-baseline.md   — GSC + GA4 + PageSpeed before redesign
    [slug]-rollback.md   — only if rollback triggered
```

## Rules

1. **Three moods only**: Industrial / Direct / Editorial. A fourth mood requires architect approval and a new file under `archetypes/`.
2. **Tokens are fixed**: #e63329 / #000 / #fff. Typography: Unbounded for display, DM Sans for body/UI.
3. **Shared atoms live in code**: `src/components/stitch/` + `src/styles/stitch-tokens.css`. Do not duplicate.
4. **Stitch output is never production code**: HTML/CSS from Stitch = visual reference only. Astro code is written manually.
5. **Every Stitch concept is committed**: no Stitch project IDs in code — artifacts in `stitch-exports/`.
6. **Per-page ADR is mandatory** before deploy: which archetype, which mood deviation, Stitch export link.
7. **Redesign rollback triggers**: CR -15% OR positions -20% within 7 days → revert.

## Archetype → page-type mapping

| Archetype | Page types |
|---|---|
| Industrial | EN home, service-hub pages, international landing |
| Direct | UA home, calculator, contact, CRO landing |
| Editorial | FAQ, blog posts, about, legal |

## Priority queue (redesign)

Tier NOW:
1. `/ua/` home — Direct mood
2. `/ru/` home — Direct mood (different accent from UA)
3. `/en/calculator/`, `/ua/calculator/`, `/ru/calculator/` — Direct mood

Tier NEXT:
- Service hub pages
- Blog posts (explore Stitch proposals first before deciding scope)

Do not redesign: pages with active Google Ads driving stable CR, pages with stable organic CTR.
