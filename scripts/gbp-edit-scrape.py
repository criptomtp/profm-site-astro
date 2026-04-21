#!/usr/bin/env python3
"""
GBP detailed scraper — clicks "Редагувати профіль" in the admin overlay
for each branch and captures the edit panel state (all field values).

Also captures: Фотографії, Публікації, Ефективність tabs.

Outputs:
- docs/gbp/audit-detailed.json
- docs/gbp/audit-detailed.md
- docs/gbp/screenshots/{CODE}_{section}.png
- docs/gbp/_raw_{CODE}_{section}.html
"""
import json
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout

ROOT = Path(__file__).resolve().parent.parent
SESSION_FILE = ROOT / 'scripts' / 'gbp-session' / 'state.json'
OUT_DIR = ROOT / 'docs' / 'gbp'
SCREEN_DIR = OUT_DIR / 'screenshots'

BRANCHES = [
    {'code': 'MTPFUL1', 'label': 'Щасливе',
     'url': 'https://business.google.com/n/15823209279675093443/profile?fid=6178464177003970104'},
    {'code': 'MTPFUL2', 'label': 'Білогородка',
     'url': 'https://business.google.com/n/5471124292630647748/profile?fid=8491720345306679116'},
]

SECTION_LABELS = [
    ('edit', 'Редагувати профіль'),
    ('photos', 'Фотографії'),
    ('posts', 'Публікації'),
    ('performance', 'Ефективність'),
    ('reviews', 'Читати відгуки'),
    ('services', 'Редагування послуг'),
    ('products', 'Змінити товари'),
]


def snap(page, code, section):
    try:
        page.screenshot(path=str(SCREEN_DIR / f'{code}_{section}.png'), full_page=True)
    except Exception:
        pass
    try:
        (OUT_DIR / f'_raw_{code}_{section}.html').write_text(page.content(), encoding='utf-8')
    except Exception:
        pass


def extract_body(page):
    try:
        return page.locator('body').inner_text(timeout=5000)
    except Exception:
        return ''


def extract_dialog_text(page):
    """If an overlay/modal is open, grab its text."""
    for sel in ['[role="dialog"]', '[aria-modal="true"]', '.modal', 'div[data-modal]']:
        try:
            el = page.locator(sel).first
            if el.count():
                return el.inner_text(timeout=3000)
        except Exception:
            continue
    return ''


def scrape_section(page, code, section_key, section_label):
    """Click a button with matching aria-label or text, capture result."""
    result = {'section': section_key, 'label': section_label, 'ok': False}
    # Close any open overlay first
    try:
        page.keyboard.press('Escape')
        page.wait_for_timeout(500)
    except Exception:
        pass

    selectors = [
        f'button[aria-label="{section_label}"]',
        f'div[aria-label="{section_label}"]',
        f'[role="button"][aria-label="{section_label}"]',
        f'button:has-text("{section_label}")',
        f'div[role="button"]:has-text("{section_label}")',
        f'a:has-text("{section_label}")',
    ]
    clicked = False
    for sel in selectors:
        try:
            el = page.locator(sel).first
            if el.count():
                el.scroll_into_view_if_needed(timeout=3000)
                el.click(timeout=5000)
                clicked = True
                result['clicked_selector'] = sel
                break
        except Exception:
            continue
    result['clicked'] = clicked
    if not clicked:
        result['error'] = 'button not found'
        return result

    page.wait_for_timeout(3500)
    snap(page, code, section_key)
    result['body_text'] = extract_body(page)[:8000]
    result['dialog_text'] = extract_dialog_text(page)[:8000]
    # Collect aria-labels inside any dialog
    try:
        result['dialog_aria_labels'] = page.evaluate(
            """() => {
                const d = document.querySelector('[role="dialog"], [aria-modal="true"]');
                if (!d) return [];
                return Array.from(d.querySelectorAll('[aria-label]'))
                  .map(e => e.getAttribute('aria-label'))
                  .filter(Boolean);
            }"""
        )
    except Exception:
        result['dialog_aria_labels'] = []
    try:
        result['inputs'] = page.evaluate(
            """() => Array.from(document.querySelectorAll('[role="dialog"] input, [role="dialog"] textarea'))
                .map(e => ({
                    type: e.type || e.tagName.toLowerCase(),
                    name: e.name || '',
                    aria: e.getAttribute('aria-label') || '',
                    placeholder: e.placeholder || '',
                    value: (e.value || '').slice(0, 300),
                }))"""
        )
    except Exception:
        result['inputs'] = []
    result['ok'] = True

    # Close
    try:
        page.keyboard.press('Escape')
        page.wait_for_timeout(400)
    except Exception:
        pass
    return result


def scrape_branch(page, branch):
    data = {'code': branch['code'], 'label': branch['label'], 'url': branch['url'], 'sections': []}
    page.goto(branch['url'], wait_until='networkidle', timeout=60000)
    page.wait_for_timeout(4000)
    snap(page, branch['code'], 'landing')
    data['final_url'] = page.url
    data['body_text'] = extract_body(page)[:6000]

    for key, label in SECTION_LABELS:
        print(f'  [{branch["code"]}] -> {label}')
        data['sections'].append(scrape_section(page, branch['code'], key, label))
    return data


def main():
    if not SESSION_FILE.exists():
        print('Session missing — run scripts/gbp-auth.py')
        sys.exit(1)

    out = {'run_at': time.strftime('%Y-%m-%d %H:%M:%S'), 'branches': []}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            storage_state=str(SESSION_FILE),
            locale='uk-UA',
            viewport={'width': 1400, 'height': 900},
        )
        page = context.new_page()
        for b in BRANCHES:
            print(f'Branch {b["code"]} ({b["label"]})')
            try:
                out['branches'].append(scrape_branch(page, b))
            except Exception as e:
                out['branches'].append({'code': b['code'], 'error': str(e)})
        browser.close()

    (OUT_DIR / 'audit-detailed.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8'
    )

    md = ['# GBP Edit-panel Audit', f'_Run at: {out["run_at"]}_', '']
    for b in out['branches']:
        md.append(f'## {b.get("code")} — {b.get("label", "")}')
        md.append(f'URL: {b.get("url")}  Final: {b.get("final_url")}')
        md.append('')
        for s in b.get('sections', []):
            md.append(f'### {s["section"]} — {s["label"]} ({"OK" if s.get("ok") else "FAIL"})')
            if s.get('clicked_selector'):
                md.append(f'- clicked via: `{s["clicked_selector"]}`')
            if s.get('error'):
                md.append(f'- ERROR: {s["error"]}')
            if s.get('inputs'):
                md.append(f'- Inputs in dialog: {len(s["inputs"])}')
                for i in s['inputs'][:30]:
                    md.append(f'  - [{i["type"]}] aria="{i["aria"]}" name="{i["name"]}" value="{i["value"]}"')
            if s.get('dialog_aria_labels'):
                md.append(f'- Dialog aria-labels (first 40):')
                for a in s['dialog_aria_labels'][:40]:
                    md.append(f'  - {a}')
            if s.get('dialog_text'):
                md.append('```')
                md.append(s['dialog_text'][:3500])
                md.append('```')
            md.append('')
    (OUT_DIR / 'audit-detailed.md').write_text('\n'.join(md), encoding='utf-8')
    print(f'OK: {OUT_DIR}/audit-detailed.json')


if __name__ == '__main__':
    main()
