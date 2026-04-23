#!/usr/bin/env python3
"""Identify /ua/* URLs from GSC data and bucket them by migration risk.

Risk buckets (90d GSC window):
  BATCH 0 - zero-risk   : 0 impressions (not indexed or dead)
  BATCH 1 - low-risk    : 1-10 impressions
  BATCH 2 - medium-risk : 11-100 impressions
  BATCH 3 - high-risk   : 101-1000 impressions
  BATCH 4 - flagship    : 1000+ impressions (migrate LAST, monitor closely)

Reads: docs/gsc/full-pages.json (90d data already pulled)
Writes: docs/url-migration/batch-candidates.md
"""
import json, os, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GSC_FILE = os.path.join(ROOT, 'docs', 'gsc', 'full-pages.json')
OUT_DIR = os.path.join(ROOT, 'docs', 'url-migration')
OUT_FILE = os.path.join(OUT_DIR, 'batch-candidates.md')

BASE = 'https://www.fulfillmentmtp.com.ua'

def bucket(impr):
    if impr == 0: return 0
    if impr <= 10: return 1
    if impr <= 100: return 2
    if impr <= 1000: return 3
    return 4

def bucket_name(b):
    return ['BATCH 0 — zero-risk (0 impressions)',
            'BATCH 1 — low-risk (1-10 impressions)',
            'BATCH 2 — medium-risk (11-100 impressions)',
            'BATCH 3 — high-risk (101-1000 impressions)',
            'BATCH 4 — flagship (1000+ impressions)'][b]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(GSC_FILE) as f:
        data = json.load(f)

    # Filter /ua/* URLs only
    ua_pages = [p for p in data['pages']
                if p['url'].startswith(f'{BASE}/ua/')
                and p['url'] != f'{BASE}/ua/']

    # Also find /ua/* URLs that may not be in GSC (never indexed)
    # We'll surface these separately by cross-checking src/pages/ua/
    ua_files = set()
    pages_dir = os.path.join(ROOT, 'src', 'pages', 'ua')
    for root, _, files in os.walk(pages_dir):
        for f in files:
            if f.endswith('.astro'):
                rel = os.path.relpath(os.path.join(root, f), pages_dir)
                slug = rel.replace('.astro', '').replace(os.sep, '/')
                if slug == 'index':
                    continue
                if slug.endswith('/index'):
                    slug = slug[:-6]
                ua_files.add(f'/ua/{slug}/')

    gsc_paths = {p['url'].replace(BASE, '') for p in ua_pages}
    missing_from_gsc = ua_files - gsc_paths

    # Bucket GSC pages
    buckets = defaultdict(list)
    for p in ua_pages:
        b = bucket(p['impressions_90d'])
        buckets[b].append(p)

    # Write report
    lines = []
    lines.append('# UA URL Migration — Batch Candidates')
    lines.append('')
    lines.append(f'**Generated:** from GSC 90d window ({data["generated_at"][:10]})')
    lines.append(f'**Source:** `docs/gsc/full-pages.json`')
    lines.append(f'**Rule:** `/ua/slug/` → `/slug/` with 301 redirect, keep content unchanged')
    lines.append('')
    lines.append(f'## Summary')
    lines.append(f'- Total `/ua/*` URLs in GSC: **{len(ua_pages)}**')
    lines.append(f'- Total `/ua/*.astro` files in codebase: **{len(ua_files)}**')
    lines.append(f'- Files NOT in GSC data (never indexed or new): **{len(missing_from_gsc)}**')
    lines.append('')

    # Count per bucket
    lines.append('## Bucket distribution')
    lines.append('')
    lines.append('| Bucket | Count | Combined impressions | Combined clicks |')
    lines.append('|---|---|---|---|')
    for b in sorted(buckets.keys()):
        total_impr = sum(p['impressions_90d'] for p in buckets[b])
        total_clk = sum(p['clicks_90d'] for p in buckets[b])
        lines.append(f'| {bucket_name(b)} | {len(buckets[b])} | {total_impr:,} | {total_clk:,} |')
    lines.append(f'| Files never indexed | {len(missing_from_gsc)} | 0 | 0 |')
    lines.append('')

    # Detail per bucket
    for b in sorted(buckets.keys()):
        rows = sorted(buckets[b], key=lambda x: x['impressions_90d'])
        lines.append(f'## {bucket_name(b)}')
        lines.append('')
        if not rows:
            lines.append('_none_')
            lines.append('')
            continue
        lines.append('| URL | Impressions 90d | Clicks 90d | Avg position |')
        lines.append('|---|---:|---:|---:|')
        for p in rows:
            short = p['url'].replace(BASE, '')
            lines.append(f'| `{short}` | {p["impressions_90d"]:,} | {p["clicks_90d"]:,} | {p["avg_position"]} |')
        lines.append('')

    if missing_from_gsc:
        lines.append('## Files never indexed (0 GSC data)')
        lines.append('')
        lines.append('_These files exist in `src/pages/ua/` but have no GSC impressions in the 90d window — safe to migrate first._')
        lines.append('')
        for path in sorted(missing_from_gsc):
            lines.append(f'- `{path}`')
        lines.append('')

    lines.append('## Recommended migration order')
    lines.append('')
    lines.append('1. **Start here →** Files never indexed + BATCH 0 (zero SEO risk)')
    lines.append('2. **Next batch →** BATCH 1 (low-traffic, minimal risk)')
    lines.append('3. **After 7d of clean metrics →** BATCH 2')
    lines.append('4. **After 14d of clean metrics →** BATCH 3')
    lines.append('5. **Last, only after pattern validated →** BATCH 4 (flagship pages)')
    lines.append('')
    lines.append('For each migration:')
    lines.append('- Move `src/pages/ua/SLUG.astro` → `src/pages/SLUG.astro`')
    lines.append('- Update canonical in the file: `/ua/SLUG/` → `/SLUG/`')
    lines.append('- Update hreflang `uk` across UA/RU/EN triplet: remove `/ua/` from UA href')
    lines.append('- Add to `public/_redirects`: `/ua/SLUG/  /SLUG/  301!`')
    lines.append('- Grep and replace internal links `/ua/SLUG/` → `/SLUG/` across `src/`')
    lines.append('- Update `Header.astro` language-switcher map if listed there')
    lines.append('- Update `public/llms.txt` if listed there')
    lines.append('- `npm run build` and verify no errors')
    lines.append('- Deploy, then GSC Request Indexing for new URL')
    lines.append('')

    with open(OUT_FILE, 'w') as f:
        f.write('\n'.join(lines))
    print(f'Wrote {OUT_FILE}')
    print(f'  {len(ua_pages)} /ua/* URLs from GSC')
    print(f'  {len(ua_files)} /ua/*.astro files')
    print(f'  {len(missing_from_gsc)} files never indexed')

if __name__ == '__main__':
    main()
