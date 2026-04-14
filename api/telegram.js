const ALLOWED_ORIGINS = [
  'https://www.fulfillmentmtp.com.ua',
  'https://fulfillmentmtp.com.ua',
  'https://profm-site-astro.vercel.app',
];

function getCorsOrigin(req) {
  const origin = req.headers.origin || req.headers.referer?.replace(/\/[^/]*$/, '') || '';
  return ALLOWED_ORIGINS.includes(origin) ? origin : '';
}

export default async function handler(req, res) {
  const corsOrigin = getCorsOrigin(req);
  if (corsOrigin) {
    res.setHeader('Access-Control-Allow-Origin', corsOrigin);
    res.setHeader('Vary', 'Origin');
  }
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
  const TELEGRAM_CHAT_ID = process.env.TELEGRAM_CHAT_ID;

  if (!TELEGRAM_BOT_TOKEN || !TELEGRAM_CHAT_ID) {
    return res.status(500).json({ error: 'Bot not configured' });
  }

  try {
    const body = req.body || {};

    if (!body.phone) {
      return res.status(400).json({ error: 'phone required' });
    }

    const phone = String(body.phone).slice(0, 20);
    const page = String(body.page || '/').slice(0, 100);

    const text = [
      '🆕 <b>Нова заявка з сайту!</b>',
      '',
      `📱 ${phone}`,
      `📋 ${page}`,
      `🕐 ${new Date().toLocaleString('uk-UA', { timeZone: 'Europe/Kyiv' })}`,
    ].join('\n');

    const tgRes = await fetch(
      `https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ chat_id: TELEGRAM_CHAT_ID, text, parse_mode: 'HTML' }),
      }
    );

    const result = await tgRes.json();
    return res.status(tgRes.ok ? 200 : 502).json({ ok: result.ok });
  } catch (error) {
    return res.status(500).json({ error: 'Failed to send' });
  }
}
