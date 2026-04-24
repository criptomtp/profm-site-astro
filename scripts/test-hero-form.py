#!/usr/bin/env python3
"""
End-to-end test of hero form on prod.
Submits clearly-marked test number, captures network for /g/collect, /api/telegram, /api/leads.
Wraps gtag + dataLayer.push to see what app code calls (vs what gtag flushes).
"""
import asyncio
import sys
from urllib.parse import parse_qs, urlparse

URL = 'https://www.fulfillmentmtp.com.ua/'
TEST_PHONE = '+380 99 999 99 99'

WRAP_GTAG = """
window.__gtagCalls = [];
window.__dlCalls = [];
(function(){
  var origGtag = window.gtag;
  window.gtag = function(){
    try { window.__gtagCalls.push(Array.from(arguments)); } catch(e){}
    if (origGtag) return origGtag.apply(window, arguments);
  };
  var origPush = window.dataLayer && window.dataLayer.push;
  if (origPush){
    window.dataLayer.push = function(){
      try { window.__dlCalls.push(Array.from(arguments)); } catch(e){}
      return origPush.apply(window.dataLayer, arguments);
    };
  }
})();
"""

async def main():
    from playwright.async_api import async_playwright

    captured = {'collect': [], 'telegram': None, 'leads': None, 'console': []}

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        ctx = await browser.new_context(user_agent='Mozilla/5.0 PLAYWRIGHT-TEST-DO-NOT-CALL')
        page = await ctx.new_page()
        await page.add_init_script(WRAP_GTAG)

        page.on('console', lambda m: captured['console'].append(f'[{m.type}] {m.text[:200]}'))

        async def on_request(req):
            url = req.url
            if '/g/collect' in url or '/collect?' in url:
                p = parse_qs(urlparse(url).query)
                en = p.get('en', [None])[0]
                body = req.post_data or ''
                body_events = []
                if body:
                    for line in body.split('\n'):
                        bp = parse_qs(line)
                        if 'en' in bp:
                            body_events.append(bp['en'][0])
                captured['collect'].append({
                    'en': en or ('+'.join(body_events) if body_events else '?'),
                    'tid': p.get('tid', ['?'])[0],
                })

        async def on_response(resp):
            u = resp.url
            if '/api/telegram' in u: captured['telegram'] = {'status': resp.status}
            elif '/api/leads' in u: captured['leads'] = {'status': resp.status}

        page.on('request', on_request)
        page.on('response', on_response)

        print(f'→ open {URL}')
        await page.goto(URL, wait_until='domcontentloaded')
        await page.wait_for_timeout(2000)

        print(f'→ fill + submit hero form ({TEST_PHONE})')
        await page.fill('#heroForm input[name="phone"]', TEST_PHONE)

        # capture gtag/dl calls BEFORE navigation
        await page.evaluate('document.getElementById("heroForm").querySelector("button").click()')
        # wait for mtpSubmitLead body to run BUT before navigation kicks in
        await page.wait_for_timeout(500)

        gtag_calls = await page.evaluate('window.__gtagCalls || []')
        dl_calls = await page.evaluate('window.__dlCalls || []')

        print(f'\n========= gtag() CALLS during submit (before navigation) =========')
        for i, c in enumerate(gtag_calls):
            print(f'  [{i}] {c}')

        print(f'\n========= dataLayer.push() CALLS during submit =========')
        for i, c in enumerate(dl_calls):
            print(f'  [{i}] {c}')

        # Now wait for any async flushes + navigation
        await page.wait_for_timeout(5000)

        await browser.close()

    print(f'\n========= /g/collect captured ({len(captured["collect"])}) =========')
    for c in captured['collect']:
        print(f'  • en={c["en"]:30s}  tid={c["tid"]}')

    print(f'\n/api/telegram: {captured["telegram"]}')
    print(f'/api/leads:    {captured["leads"]}')

    if captured['console']:
        print('\nconsole (last 5):')
        for line in captured['console'][-5:]:
            print(f'  {line[:140]}')

    print('\n========= VERDICT =========')
    fs_called = any(len(c) >= 2 and c[1] == 'form_submit' for c in gtag_calls)
    gl_called = any(len(c) >= 2 and c[1] == 'generate_lead' for c in gtag_calls)
    fs_sent = any('form_submit' in c['en'] for c in captured['collect'])
    gl_sent = any('generate_lead' in c['en'] for c in captured['collect'])
    tg_ok = captured['telegram'] and captured['telegram']['status'] in (200, 201, 204)
    leads_ok = captured['leads'] and captured['leads']['status'] in (200, 201, 204)

    print(f'  gtag("event","form_submit",...)  CALLED by app:   {"✅" if fs_called else "❌"}')
    print(f'  gtag("event","generate_lead",...) CALLED by app:  {"✅" if gl_called else "❌"}')
    print(f'  /g/collect en=form_submit         SENT to GA4:    {"✅" if fs_sent else "❌"}')
    print(f'  /g/collect en=generate_lead       SENT to GA4:    {"✅" if gl_sent else "❌"}')
    print(f'  /api/telegram                     STATUS:         {"✅" if tg_ok else "❌"} {captured["telegram"]}')
    print(f'  /api/leads                        STATUS:         {"✅" if leads_ok else "❌"} {captured["leads"]}')

if __name__ == '__main__':
    sys.exit(asyncio.run(main()))
