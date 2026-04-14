import { Redis } from '@upstash/redis';

const redis = new Redis({
  url: process.env.storage_KV_REST_API_URL || process.env.STORAGE_URL || process.env.KV_REST_API_URL,
  token: process.env.storage_KV_REST_API_TOKEN || process.env.STORAGE_REST_API_TOKEN || process.env.KV_REST_API_TOKEN,
});

const LEADS_KEY = 'mtp:leads';
const RATE_LIMIT_PREFIX = 'rl:leads:';
const RATE_LIMIT_MAX = 30;
const RATE_LIMIT_WINDOW = 60;

const ALLOWED_ORIGINS = [
  'https://www.fulfillmentmtp.com.ua',
  'https://fulfillmentmtp.com.ua',
  'https://profm-site-astro.vercel.app',
];

function getCorsOrigin(req) {
  const origin = req.headers.origin || req.headers.referer?.replace(/\/[^/]*$/, '') || '';
  return ALLOWED_ORIGINS.includes(origin) ? origin : '';
}

function checkApiKey(req) {
  const key = req.headers['x-api-key'];
  const expected = process.env.LEADS_API_KEY;
  return expected && key === expected;
}

async function checkRateLimit(ip) {
  const key = RATE_LIMIT_PREFIX + ip;
  const count = await redis.incr(key);
  if (count === 1) await redis.expire(key, RATE_LIMIT_WINDOW);
  return count <= RATE_LIMIT_MAX;
}

export default async function handler(req, res) {
  const corsOrigin = getCorsOrigin(req);
  if (corsOrigin) {
    res.setHeader('Access-Control-Allow-Origin', corsOrigin);
    res.setHeader('Vary', 'Origin');
  }
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Api-Key');

  if (req.method === 'OPTIONS') return res.status(200).end();

  // Rate limiting
  const ip = req.headers['x-forwarded-for']?.split(',')[0]?.trim() || req.socket?.remoteAddress || 'unknown';
  const allowed = await checkRateLimit(ip).catch(() => true);
  if (!allowed) return res.status(429).json({ error: 'Too many requests' });

  try {
    // POST — add new lead (public, from site forms)
    if (req.method === 'POST') {
      const body = req.body;
      if (!body || !body.phone) return res.status(400).json({ error: 'phone required' });

      const leads = await redis.get(LEADS_KEY) || [];

      const newLead = {
        id: Date.now().toString(),
        company: body.company || '',
        contact: body.contact || '',
        phone: String(body.phone).slice(0, 20),
        email: String(body.email || '').slice(0, 100),
        shipments: Number(body.shipments) || 0,
        type: body.type || 'other',
        source: body.source || 'site',
        status: 'new',
        date: new Date().toISOString().slice(0, 10),
        nextContact: body.nextContact || '',
        comments: Array.isArray(body.comments) ? body.comments.slice(0, 5) : [],
        onboarding: [false, false, false, false, false, false, false],
        timeline: [],
      };

      leads.push(newLead);
      await redis.set(LEADS_KEY, leads);

      // Notify Telegram
      const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
      const TELEGRAM_CHAT_ID = process.env.TELEGRAM_CHAT_ID;
      if (TELEGRAM_BOT_TOKEN && TELEGRAM_CHAT_ID) {
        const text = `🆕 Нова заявка!\n📱 ${newLead.phone}\n📋 ${String(body.page || '/').slice(0, 100)}`;
        await fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ chat_id: TELEGRAM_CHAT_ID, text, parse_mode: 'HTML' }),
        }).catch(() => {});
      }

      return res.status(201).json({ id: newLead.id, ok: true });
    }

    // GET/PUT/DELETE — protected by API key (CRM only)
    if (!checkApiKey(req)) {
      return res.status(401).json({ error: 'Unauthorized' });
    }

    // GET — all leads
    if (req.method === 'GET') {
      const leads = await redis.get(LEADS_KEY) || [];
      return res.status(200).json(leads);
    }

    // PUT — update lead
    if (req.method === 'PUT') {
      const body = req.body;
      if (!body.id) return res.status(400).json({ error: 'id required' });

      const leads = await redis.get(LEADS_KEY) || [];
      const idx = leads.findIndex(l => String(l.id) === String(body.id));
      if (idx === -1) return res.status(404).json({ error: 'lead not found' });

      leads[idx] = { ...leads[idx], ...body };
      await redis.set(LEADS_KEY, leads);
      return res.status(200).json(leads[idx]);
    }

    // DELETE — remove lead
    if (req.method === 'DELETE') {
      const id = req.query.id || req.body?.id;
      if (!id) return res.status(400).json({ error: 'id required' });

      let leads = await redis.get(LEADS_KEY) || [];
      leads = leads.filter(l => String(l.id) !== String(id));
      await redis.set(LEADS_KEY, leads);
      return res.status(200).json({ ok: true });
    }

    return res.status(405).json({ error: 'Method not allowed' });
  } catch (error) {
    console.error('Leads API error:', error);
    return res.status(500).json({ error: 'Internal server error' });
  }
}
