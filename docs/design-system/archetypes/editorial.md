# Archetype: Editorial

Readability-first, quiet, confident. Reference: `src/pages/en/faq.astro`.

## When to use

- FAQ pages
- Blog posts (index + articles)
- About / team pages
- Legal / privacy
- Long-form content where reading is the primary job

## Visual signals

- **Hero**: no image. Centered or left-aligned big H1 with short descriptive subtitle. Generous whitespace above and below.
- **Label chip**: muted gray or black (not red) — "Frequently Asked Questions" style. Smaller and more subtle than Industrial.
- **Typography**: H1 in Unbounded 700–900, clamp 40px–72px, explicit `<br>` line breaks for poetic rhythm. Body in DM Sans 16–18px with generous line-height (1.6–1.7).
- **Category nav**: horizontal pill nav with active-state, anchored to sections. Sticky on scroll on desktop.
- **Sections**: mostly white. One muted section (`#f7f7f7`) for contrast. Accordions for dense Q&A content.
- **Color accents**: red reserved for category-active state, H2 underlines, primary CTA at end. Almost no red in body.

## Do

- Lead with typography, not imagery.
- Use StatsBar once, near top, to anchor credibility before long reading.
- Use AccordionGroup for Q&A — not `<details>` native (no control).
- Keep a single CTA at the end of the page — "Calculate cost" or "Get a quote".

## Don't

- No hero background image.
- No aggressive red backgrounds or labels.
- No split 2-col layouts (too busy for reading).
- No forms above the fold — this mood is about trust-building, not immediate conversion.

## Shared components to use

- `LabelChip.astro` (variant `muted`)
- `StatsBar.astro` (once)
- `AccordionGroup.astro`
- `DarkCTA.astro` (only at page end)

## Example pages

- `src/pages/en/faq.astro` (canonical reference)
