import { corsHeaders, json } from './_helpers.js';
import { makeRedis } from './_session.js';

const GSC_KEY = 'mtp:gsc:history';
const GSC_LATEST = 'mtp:gsc:latest';
const SITE_URL = 'https://fulfillmentmtp.com.ua/';

const TARGET_KEYWORDS = [
  'фулфілмент', 'фулфилмент', 'fulfillment',
  'фулфілмент київ', 'фулфилмент киев', 'fulfillment kyiv',
  'фулфілмент для маркетплейсів', 'фулфилмент для маркетплейсов',
  'фулфілмент україна', 'фулфилмент украина',
  'mtp group', 'фулфілмент для інтернет магазинів',
  'фулфілмент склад', 'склад фулфілмент київ',
];

const TARGET_PAGES = [
  '/', '/ru/', '/en/',
  '/ua/fulfilment-dlya-marketpleysiv/', '/fulfilment-dlya-marketpleysov/', '/en/fulfillment-for-marketplaces/',
  '/ua/fulfilment-kyiv/', '/fulfilment-kiev/', '/en/fulfillment-kyiv/',
  '/ua/services/', '/services/', '/en/services/',
  '/ua/tsiny/', '/tsenu/', '/en/prices/',
];

const METHODS = 'POST, OPTIONS';
const openCors = (request) => ({ ...corsHeaders(request, METHODS), 'Access-Control-Allow-Origin': '*' });

async function getAccessToken(env) {
  const resp = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      client_id: env.GSC_CLIENT_ID,
      client_secret: env.GSC_CLIENT_SECRET,
      refresh_token: env.GSC_REFRESH_TOKEN,
      grant_type: 'refresh_token',
    }),
  });
  const data = await resp.json();
  if (!data.access_token) throw new Error('Failed to get access token: ' + JSON.stringify(data));
  return data.access_token;
}

async function gscQuery(token, body) {
  const resp = await fetch(
    `https://www.googleapis.com/webmasters/v3/sites/${encodeURIComponent(SITE_URL)}/searchAnalytics/query`,
    {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    }
  );
  return resp.json();
}

export async function onRequestOptions({ request }) {
  return new Response(null, { status: 204, headers: openCors(request) });
}

export async function onRequestPost({ request, env }) {
  const headers = openCors(request);
  try {
    if (!env.GSC_CLIENT_ID || !env.GSC_REFRESH_TOKEN) {
      return json({ error: 'GSC credentials not configured' }, { status: 500, headers });
    }

    const redis = makeRedis(env);
    const token = await getAccessToken(env);

    const now = new Date();
    const end = now.toISOString().slice(0, 10);
    const start = new Date(now - 7 * 86400000).toISOString().slice(0, 10);

    const queryData = await gscQuery(token, { startDate: start, endDate: end, dimensions: ['query'], rowLimit: 50 });
    const queries = (queryData.rows || []).map(r => ({
      q: r.keys[0],
      clicks: r.clicks,
      impressions: r.impressions,
      ctr: Math.round(r.ctr * 1000) / 10,
      position: Math.round(r.position * 10) / 10,
    }));

    for (const kw of TARGET_KEYWORDS) {
      if (queries.some(q => q.q === kw)) continue;
      try {
        const kwData = await gscQuery(token, {
          startDate: start, endDate: end,
          dimensions: ['query'],
          dimensionFilterGroups: [{ filters: [{ dimension: 'query', operator: 'equals', expression: kw }] }],
          rowLimit: 1,
        });
        for (const r of kwData.rows || []) {
          queries.push({
            q: r.keys[0],
            clicks: r.clicks,
            impressions: r.impressions,
            ctr: Math.round(r.ctr * 1000) / 10,
            position: Math.round(r.position * 10) / 10,
            tracked: true,
          });
        }
      } catch {}
    }

    const pageData = await gscQuery(token, { startDate: start, endDate: end, dimensions: ['page'], rowLimit: 100 });
    const indexedUrls = new Set();
    const pages = (pageData.rows || []).map(r => {
      const url = r.keys[0].replace('https://fulfillmentmtp.com.ua', '').replace('https://www.fulfillmentmtp.com.ua', '');
      indexedUrls.add(url);
      return { url, clicks: r.clicks, impressions: r.impressions, position: Math.round(r.position * 10) / 10 };
    });

    for (const tp of TARGET_PAGES) {
      if (!indexedUrls.has(tp)) pages.push({ url: tp, clicks: 0, impressions: 0, position: 0, notIndexed: true });
    }

    const snapshot = { date: end, queries, pages, timestamp: Date.now() };
    await redis.set(GSC_LATEST, snapshot);

    let history = (await redis.get(GSC_KEY)) || [];
    history = history.filter(h => h.date !== end);
    history.push(snapshot);
    if (history.length > 90) history = history.slice(-90);
    await redis.set(GSC_KEY, history);

    return json({ ok: true, date: end, queries: queries.length, pages: pages.length, snapshots: history.length }, { status: 200, headers });
  } catch (e) {
    return json({ error: e.message }, { status: 500, headers });
  }
}

export async function onRequest({ request }) {
  return json({ error: 'POST only' }, { status: 405, headers: openCors(request) });
}
