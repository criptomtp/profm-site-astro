# Archetype: Industrial

Data-driven, international, B2B confidence. Reference: `src/pages/en/index.astro`.

## When to use

- EN home
- Service hub pages for enterprise / international clients
- Anything pitched to decision-makers who want numbers, scale, operational proof

## Visual signals

- **Hero**: split 2-column grid. Left = text block, right = warehouse image. Full-width red `en-hero__bg` image above the grid with low-opacity overlay.
- **Label chip**: red `#e63329` background, white text, uppercase, letter-spacing 0.12em — "INDUSTRIAL LOGISTICS SOLUTIONS" style.
- **Stats bar**: 4-column grid, huge numbers in black/red, uppercase labels underneath in muted gray.
- **Typography**: H1 in Unbounded 900 weight, clamp 36px–72px, line-height 1.0–1.1.
- **Sections**: alternating white / dark `#0a0a0a` / light `#f3f3f3` backgrounds to break rhythm.
- **Color accents**: red used for labels, underlines, number highlights, single primary CTA button. Never for large section backgrounds.

## Do

- Uppercase short labels above every H2.
- Use the StatsBar component at least twice per page (hero area + mid-page).
- Stack dark sections (`#0a0a0a` background) for contrast moments.
- Keep copy tight and operational — "60,000 shipments / month", "30 sec order assembly".

## Don't

- No hero overlay text on image without grid structure.
- No warm gradients or soft shadows.
- No decorative icons — only utilitarian (arrow, check, number).

## Shared components to use

- `LabelChip.astro` (variant `red`)
- `StatsBar.astro`
- `DarkCTA.astro`

## Example pages

- `src/pages/en/index.astro` (canonical reference)
