#!/usr/bin/env python3
"""
Debug: open Company Page admin view, dump every clickable element
that looks like a post composer trigger, plus full page screenshot
and HTML. No posting — just diagnostics.
"""
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / 'scripts' / 'linkedin-session' / 'state.json'
OUT = ROOT / 'scripts' / 'linkedin-session'

PAGE_ID = '112973784'
URLS = [
    f'https://www.linkedin.com/company/{PAGE_ID}/admin/dashboard/',
    f'https://www.linkedin.com/company/{PAGE_ID}/admin/page-posts/published/',
    f'https://www.linkedin.com/company/{PAGE_ID}/admin/feed/posts/',
]


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,
            args=['--disable-blink-features=AutomationControlled'])
        ctx = browser.new_context(storage_state=str(STATE),
            locale='uk-UA', viewport={'width':1400,'height':900},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
        page = ctx.new_page()
        for i, url in enumerate(URLS, 1):
            print(f'\n--- {i}. {url}')
            page.goto(url, wait_until='domcontentloaded')
            page.wait_for_timeout(4000)
            print(f'    landed: {page.url}')

            # try scrolling
            page.mouse.wheel(0, 300)
            page.wait_for_timeout(1000)

            shot = OUT / f'debug-{i}.png'
            html = OUT / f'debug-{i}.html'
            page.screenshot(path=str(shot), full_page=True)
            html.write_text(page.content(), encoding='utf-8')
            print(f'    saved: {shot.name} + {html.name}')

            # enumerate candidates
            candidates = page.evaluate('''() => {
                const out = [];
                const pats = /post|публік|допис|створ|start a|share|write|напиш|што|что|новин|нового|share.?box|commentary/i;
                document.querySelectorAll('button, div[role="button"], a[role="button"], [data-test-id], [data-control-name*="share" i], textarea, input[type="text"]').forEach(el => {
                    const text = (el.innerText || el.value || '').trim().slice(0, 100);
                    const aria = el.getAttribute('aria-label') || '';
                    const placeholder = el.getAttribute('placeholder') || '';
                    const testid = el.getAttribute('data-test-id') || '';
                    const ctrl = el.getAttribute('data-control-name') || '';
                    const cls = (el.className || '').toString().slice(0, 120);
                    const combined = `${text} ${aria} ${placeholder} ${testid} ${ctrl}`;
                    if (pats.test(combined)) {
                        out.push({ tag: el.tagName.toLowerCase(), text, aria, placeholder, testid, ctrl, cls });
                    }
                });
                return out.slice(0, 40);
            }''')
            print(f'    candidates ({len(candidates)}):')
            for c in candidates:
                print(f'      <{c["tag"]}> text={c["text"]!r} aria={c["aria"]!r} placeholder={c.get("placeholder","")!r} testid={c["testid"]!r} ctrl={c.get("ctrl","")!r}')

        print('\nWindow stays open 15s — look manually.')
        page.wait_for_timeout(15000)
        browser.close()


if __name__ == '__main__':
    main()
