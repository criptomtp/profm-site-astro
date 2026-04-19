# Archetype: Direct

Warm, local, immediate. Conversion-first. Reference target: future `src/pages/index.astro` redesign.

## When to use

- UA home
- RU home
- Calculator pages (UA / RU / EN)
- Contact pages
- CRO-focused landing pages where the user already has intent

## Visual signals

- **Hero**: full-width background image with warm overlay (dark-to-transparent gradient from left). Text block centered or left-aligned within the overlay.
- **Badge**: small red pill with uppercase Ukrainian / Russian text — "ФУЛФІЛМЕНТ В УКРАЇНІ" style. Narrower letter-spacing than Industrial labels.
- **Hero form**: visible above the fold. Single phone input + single red CTA button. Never behind a scroll.
- **Hero stats**: 3–4 inline stats under the form, compact, not a full-width bar.
- **Typography**: H1 in Unbounded 700–800, clamp 28px–56px, line-height 1.1–1.2. Warmer than Industrial (shorter line breaks).
- **Sections**: predominantly white with single dark CTA zone before footer.
- **Color accents**: red CTA button dominates. Red accent under numbers in stats.

## Do

- Put one form in the hero, one dark CTA zone before the footer.
- Keep copy conversational — "Ти займаєшся продажами — ми логістикою".
- Use warm images (warehouse interior, team, partners) with human presence when possible.
- Include trust signals (partner logos marquee) within 1 viewport of hero.

## Don't

- No uppercase stats bar like Industrial — too cold for this mood.
- No split-hero 2-column grid (that's Industrial's signature).
- No long-form essay blocks — Direct is about moving the visitor toward the form.
- No more than 2 forms per page.

## Shared components to use

- `LabelChip.astro` (variant `red`, smaller sizing)
- `SplitHero.astro` — use the "full-bleed" slot variant, not the 2-col variant
- `DarkCTA.astro`

## Example pages

- `src/pages/index.astro` (current — pre-redesign baseline)
- To become the canonical reference after the Tier 1 redesign.
