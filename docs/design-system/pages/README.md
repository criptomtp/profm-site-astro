# Per-page ADR

Every new page OR redesigned page gets a short record here.

## File naming

- `[slug].md` — main ADR
- `[slug]-baseline.md` — only for redesigns, pre-redesign metrics
- `[slug]-rollback.md` — only if rollback triggered

## ADR template (`[slug].md`)

```
# Page: /ua/calculator/

- **Archetype**: Direct
- **Mood deviation**: none (or describe what differs from archetype doc)
- **Stitch export**: docs/design-system/stitch-exports/2026-04-20_ua-calculator/
- **Approved by user**: 2026-04-20
- **Deployed**: 2026-04-21
- **Validated** (28 days clean): 2026-05-19

## Why this mood
[1–2 sentences]

## Unique decisions
[anything off-archetype worth flagging for future maintainers]
```

## Baseline template (`[slug]-baseline.md`)

```
# Baseline: /ua/calculator/ (captured 2026-04-20)

## GSC (28 days)
- Top queries: [query] — pos X.X, CTR X%, impressions N, clicks N
- (list top 10)

## GA4 (28 days)
- Organic sessions: N
- Form CR: X%
- Bounce rate: X%
- Scroll 75%: X%
- Avg engagement time: Xs

## PageSpeed
- Mobile: LCP Xs / CLS X / INP Xms / Perf X
- Desktop: LCP Xs / CLS X / INP Xms / Perf X

## SERP screenshot
[link or embed]
```
