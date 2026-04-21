#!/usr/bin/env python3
"""
GBP audit — scrapes both MTP Group branches using saved session.

Branch URLs discovered from landing HTML:
- MTPFUL1 (Щасливе):    .../n/15823209279675093443/profile?fid=6178464177003970104
- MTPFUL2 (Білогородка): .../n/5471124292630647748/profile?fid=8491720345306679116

Outputs: docs/gbp/audit.json, audit.md, screenshots/*.png, _raw_*.html
"""
import json
import re
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SESSION_FILE = ROOT / 'scripts' / 'gbp-session' / 'state.json'
OUT_DIR = ROOT / 'docs' / 'gbp'
SCREEN_DIR = OUT_DIR / 'screenshots'
OUT_DIR.mkdir(parents=True, exist_ok=True)
SCREEN_DIR.mkdir(parents=True, exist_ok=True)

BRANCHES = [
    {
        'code': 'MTPFUL1',
        'label': 'Щасливе',
        'url': 'https://business.google.com/n/15823209279675093443/profile?fid=6178464177003970104',
    },
    {
        'code': 'MTPFUL2',
        'label': 'Білогородка',
        'url': 'https://business.google.com/n/5471124292630647748/profile?fid=8491720345306679116',
    },
]


def scrape_branch(page, branch):
    page.goto(branch['url'], wait_until='networkidle', timeout=60000)
    page.wait_for_timeout(3000)

    data = {
        'code': branch['code'],
        'label': branch['label'],
        'url': branch['url'],
        'final_url': page.url,
        'title': page.title(),
    }

    tag_prefix = branch['code']

    # Full-page screenshot + HTML dump
    try:
        page.screenshot(path=str(SCREEN_DIR / f'{tag_prefix}_profile.png'), full_page=True)
    except Exception as e:
        data['screenshot_error'] = str(e)
    try:
        (OUT_DIR / f'_raw_{tag_prefix}_profile.html').write_text(page.content(), encoding='utf-8')
    except Exception as e:
        data['html_dump_error'] = str(e)

    # All visible text
    try:
        data['body_text'] = page.locator('body').inner_text(timeout=5000)
    except Exception as e:
        data['body_text_error'] = str(e)

    # Try structured scrape: every editable card usually has an aria-label
    try:
        aria_labels = page.evaluate(
            """() => Array.from(document.querySelectorAll('[aria-label]'))
                .map(el => el.getAttribute('aria-label'))
                .filter(Boolean)
                .filter((v, i, arr) => arr.indexOf(v) === i)"""
        )
        data['aria_labels'] = aria_labels
    except Exception as e:
        data['aria_error'] = str(e)

    # Try to read H1/H2/H3 hierarchy
    try:
        headings = page.evaluate(
            """() => Array.from(document.querySelectorAll('h1,h2,h3,h4'))
                .map(el => ({level: el.tagName, text: (el.innerText||'').trim()}))
                .filter(h => h.text)"""
        )
        data['headings'] = headings
    except Exception as e:
        data['headings_error'] = str(e)

    return data


def main():
    if not SESSION_FILE.exists():
        print(f'ERROR: {SESSION_FILE} missing. Run scripts/gbp-auth.py first.')
        sys.exit(1)

    result = {
        'run_at': time.strftime('%Y-%m-%d %H:%M:%S'),
        'branches': [],
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            storage_state=str(SESSION_FILE),
            locale='uk-UA',
            viewport={'width': 1400, 'height': 900},
        )
        page = context.new_page()

        for b in BRANCHES:
            print(f'Scraping {b["code"]} ({b["label"]})...')
            try:
                data = scrape_branch(page, b)
                result['branches'].append(data)
            except Exception as e:
                result['branches'].append({'code': b['code'], 'error': str(e)})

        browser.close()

    (OUT_DIR / 'audit.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8'
    )

    # Markdown
    md = ['# GBP Branches Audit (Raw Capture)', f'_Run at: {result["run_at"]}_', '']
    for b in result['branches']:
        md.append(f'## {b.get("code")} — {b.get("label", "")}')
        md.append(f'**URL**: {b.get("url")}')
        md.append(f'**Final URL**: {b.get("final_url")}')
        md.append(f'**Title**: {b.get("title")}')
        md.append('')
        if b.get('error'):
            md.append(f'**ERROR**: {b["error"]}')
            continue
        md.append('### Body text')
        md.append('```')
        md.append((b.get('body_text') or '')[:6000])
        md.append('```')
        md.append('')
        md.append('### Headings')
        for h in (b.get('headings') or []):
            md.append(f'- {h["level"]}: {h["text"]}')
        md.append('')
        md.append('### Aria-labels (first 80)')
        for a in (b.get('aria_labels') or [])[:80]:
            md.append(f'- {a}')
        md.append('')
    (OUT_DIR / 'audit.md').write_text('\n'.join(md), encoding='utf-8')

    print(f'OK: {OUT_DIR / "audit.json"}')
    print(f'Branches scraped: {len(result["branches"])}')


if __name__ == '__main__':
    main()
