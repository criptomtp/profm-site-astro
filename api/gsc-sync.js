import { Redis } from '@upstash/redis';

const redis = new Redis({
  url: process.env.storage_KV_REST_API_URL || process.env.STORAGE_URL || process.env.KV_REST_API_URL,
  token: process.env.storage_KV_REST_API_TOKEN || process.env.STORAGE_REST_API_TOKEN || process.env.KV_REST_API_TOKEN,
});

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

async function getAccessToken() {
  const resp = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      client_id: process.env.GSC_CLIENT_ID,
      client_secret: process.env.GSC_CLIENT_SECRET,
      refresh_token: process.env.GSC_REFRESH_TOKEN,
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

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'POST only' });

  try {
    // Check credentials
    if (!process.env.GSC_CLIENT_ID || !process.env.GSC_REFRESH_TOKEN) {
      return res.status(500).json({ error: 'GSC credentials not configured' });
    }

    const token = await getAccessToken();

    const now = new Date();
    const end = now.toISOString().slice(0, 10);
    const start = new Date(now - 7 * 86400000).toISOString().slice(0, 10);

    // 1. Top queries
    const queryData = await gscQuery(token, {
      startDate: start, endDate: end,
      dimensions: ['query'],
      rowLimit: 50,
    });

    const queries = (queryData.rows || []).map(r => ({
      q: r.keys[0],
      clicks: r.clicks,
      impressions: r.impressions,
      ctr: Math.round(r.ctr * 1000) / 10,
      position: Math.round(r.position * 10) / 10,
    }));

    // 2. Target keywords not in top queries
    for (const kw of TARGET_KEYWORDS) {
      if (queries.some(q => q.q === kw)) continue;
      try {
        const kwData = await gscQuery(token, {
          startDate: start, endDate: end,
          dimensions: ['query'],
          dimensionFilterGroups: [{ filters: [{ dimension: 'query', operator: 'equals', expression: kw }] }],
          rowLimit: 1,
        });
        for (const r of (kwData.rows || [])) {
          queries.push({
            q: r.keys[0],
            clicks: r.clicks,
            impressions: r.impressions,
            ctr: Math.round(r.ctr * 1000) / 10,
            position: Math.round(r.position * 10) / 10,
            tracked: true,
          });
        }
      } catch (e) { /* skip */ }
    }

    // 3. Pages
    const pageData = await gscQuery(token, {
      startDate: start, endDate: end,
      dimensions: ['page'],
      rowLimit: 100,
    });

    const indexedUrls = new Set();
    const pages = (pageData.rows || []).map(r => {
      const url = r.keys[0].replace('https://fulfillmentmtp.com.ua', '').replace('https://www.fulfillmentmtp.com.ua', '');
      indexedUrls.add(url);
      return {
        url,
        clicks: r.clicks,
        impressions: r.impressions,
        position: Math.round(r.position * 10) / 10,
      };
    });

    // Mark not-indexed target pages
    for (const tp of TARGET_PAGES) {
      if (!indexedUrls.has(tp)) {
        pages.push({ url: tp, clicks: 0, impressions: 0, position: 0, notIndexed: true });
      }
    }

    // 4. Save to Redis
    const snapshot = { date: end, queries, pages, timestamp: Date.now() };
    await redis.set(GSC_LATEST, snapshot);

    let history = await redis.get(GSC_KEY) || [];
    // Don't duplicate same date
    history = history.filter(h => h.date !== end);
    history.push(snapshot);
    if (history.length > 90) history = history.slice(-90);
    await redis.set(GSC_KEY, history);

    return res.status(200).json({
      ok: true,
      date: end,
      queries: queries.length,
      pages: pages.length,
      snapshots: history.length,
    });
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
}
