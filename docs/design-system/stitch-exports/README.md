# Stitch Exports

Every approved Stitch concept is committed here before any Astro code is written.

## Folder naming

`YYYY-MM-DD_[slug]/` — example: `2026-04-19_en-home/`, `2026-04-20_ua-calculator/`

## Required files

- `concept.md` — mood choice (Industrial / Direct / Editorial), rationale, WOW element, Stitch prompt used
- `screenshot.png` — full-page PNG from Stitch (visual source of truth for regression)

## Optional files

- `export.html` — raw Stitch HTML (reference only, never copied into `.astro`)
- `export.css` — raw Stitch CSS (reference only)
- `variants/` — folder with 2–3 alternative screens if `generate_variants` was used

## Why this folder exists

Vendor-lock protection. Stitch is SaaS — may change pricing, lose projects, or shut down. The git artifacts here are the project's source of truth. Never reference a Stitch project ID in runtime code.
