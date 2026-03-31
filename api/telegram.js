export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
  const TELEGRAM_CHAT_ID = process.env.TELEGRAM_CHAT_ID || '234255114';

  if (!TELEGRAM_BOT_TOKEN) {
    return res.status(500).json({ error: 'Bot token not configured' });
  }

  try {
    const body = req.body || {};

    // Support both formats:
    // Format A (forwarded from inline JS): { chat_id, text, parse_mode }
    // Format B (simple): { phone, page }
    let chat_id = body.chat_id || TELEGRAM_CHAT_ID;
    let text = body.text;
    let parse_mode = body.parse_mode || 'HTML';

    if (!text && body.phone) {
      text = [
        '\uD83C\uDD95 <b>Нова заявка з сайту!</b>',
        '',
        `\uD83D\uDCF1 ${body.phone}`,
        `\uD83D\uDCCB ${body.page || '/'}`,
        `\uD83D\uDD50 ${new Date().toLocaleString('uk-UA', { timeZone: 'Europe/Kyiv' })}`,
      ].join('\n');
    }

    if (!text) {
      return res.status(400).json({ error: 'No message content' });
    }

    const tgRes = await fetch(
      `https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ chat_id, text, parse_mode }),
      }
    );

    const result = await tgRes.json();
    return res.status(tgRes.ok ? 200 : 502).json({ ok: result.ok });
  } catch (error) {
    return res.status(500).json({ error: 'Failed to send' });
  }
}
