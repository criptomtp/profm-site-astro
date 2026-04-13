import { Redis } from '@upstash/redis';

const redis = new Redis({
  url: process.env.storage_KV_REST_API_URL || process.env.STORAGE_URL || process.env.KV_REST_API_URL,
  token: process.env.storage_KV_REST_API_TOKEN || process.env.STORAGE_REST_API_TOKEN || process.env.KV_REST_API_TOKEN,
});

const LEADS_KEY = 'mtp:leads';

const ALLOWED_ORIGINS = [
  'https://www.fulfillmentmtp.com.ua',
  'https://fulfillmentmtp.com.ua',
  'https://profm-site-astro.vercel.app',
];

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();

  // API key auth disabled — CRM dashboard doesn't support custom headers yet
  // TODO: add x-api-key to CRM JS when ready to enable auth

  try {
    // GET — all leads
    if (req.method === 'GET') {
      const leads = await redis.get(LEADS_KEY) || [];
      return res.status(200).json(leads);
    }

    // POST — add new lead
    if (req.method === 'POST') {
      const body = req.body;
      const leads = await redis.get(LEADS_KEY) || [];

      const newLead = {
        id: Date.now().toString(),
        company: body.company || '',
        contact: body.contact || '',
        phone: body.phone || '',
        email: body.email || '',
        shipments: body.shipments || 0,
        type: body.type || 'other',
        source: body.source || 'site',
        status: body.status || 'new',
        date: body.date || new Date().toISOString().slice(0, 10),
        nextContact: body.nextContact || '',
        comments: body.comments || [],
        onboarding: body.onboarding || [false, false, false, false, false, false, false],
        timeline: body.timeline || [],
      };

      leads.push(newLead);
      await redis.set(LEADS_KEY, leads);

      // Notify Telegram
      if (body.phone) {
        const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
        const TELEGRAM_CHAT_ID = process.env.TELEGRAM_CHAT_ID || '234255114';
        if (TELEGRAM_BOT_TOKEN) {
          const text = `🆕 Нова заявка!\n📱 ${body.phone}\n📋 ${body.page || '/'}`;
          await fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ chat_id: TELEGRAM_CHAT_ID, text, parse_mode: 'HTML' }),
          }).catch(() => {});
        }
      }

      return res.status(201).json(newLead);
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
    return res.status(500).json({ error: error.message });
  }
}
