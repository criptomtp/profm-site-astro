import { corsHeaders, json, readJson } from './_helpers.js';

export async function onRequestOptions({ request }) {
  return new Response(null, { status: 204, headers: corsHeaders(request, 'POST, OPTIONS') });
}

export async function onRequestPost({ request, env }) {
  const headers = corsHeaders(request, 'POST, OPTIONS');

  const { TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID } = env;
  if (!TELEGRAM_BOT_TOKEN || !TELEGRAM_CHAT_ID) {
    return json({ error: 'Bot not configured' }, { status: 500, headers });
  }

  const body = await readJson(request);
  if (!body.phone) return json({ error: 'phone required' }, { status: 400, headers });

  const phone = String(body.phone).slice(0, 20);
  const page = String(body.page || '/').slice(0, 100);
  const name = String(body.name || '').slice(0, 50);

  const lines = ['🆕 <b>Нова заявка з сайту!</b>', ''];
  if (name) lines.push(`👤 ${name}`);
  lines.push(`📱 ${phone}`);
  lines.push(`📋 ${page}`);
  lines.push(`🕐 ${new Date().toLocaleString('uk-UA', { timeZone: 'Europe/Kyiv' })}`);

  try {
    const tgRes = await fetch(
      `https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ chat_id: TELEGRAM_CHAT_ID, text: lines.join('\n'), parse_mode: 'HTML' }),
      }
    );
    const result = await tgRes.json();
    return json({ ok: !!result.ok }, { status: tgRes.ok ? 200 : 502, headers });
  } catch {
    return json({ error: 'Failed to send' }, { status: 500, headers });
  }
}

export async function onRequest({ request }) {
  return json({ error: 'Method not allowed' }, { status: 405, headers: corsHeaders(request, 'POST, OPTIONS') });
}
