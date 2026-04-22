import { corsHeaders, readJson, redirect, json } from './_helpers.js';

export async function onRequestPost({ request, env }) {
  const body = await readJson(request);
  const { Name, Phone, Email, tildaspec } = body;

  let formName = 'Заявка з сайту';
  if (tildaspec) {
    try {
      const spec = JSON.parse(tildaspec);
      formName = spec.formname || spec.descr || formName;
    } catch {}
  }

  const { TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, WEB3FORMS_KEY } = env;

  if (TELEGRAM_BOT_TOKEN && TELEGRAM_CHAT_ID) {
    const message = [
      `📩 ${formName}`,
      `👤 Ім'я: ${Name || '—'}`,
      `📱 Телефон: ${Phone || '—'}`,
      `📧 Email: ${Email || '—'}`,
      `🕐 ${new Date().toLocaleString('uk-UA', { timeZone: 'Europe/Kyiv' })}`,
    ].join('\n');

    try {
      await fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ chat_id: TELEGRAM_CHAT_ID, text: message, parse_mode: 'HTML' }),
      });
    } catch {}
  }

  if (WEB3FORMS_KEY) {
    try {
      await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          access_key: WEB3FORMS_KEY,
          subject: formName,
          name: Name || '',
          phone: Phone || '',
          email: Email || '',
        }),
      });
    } catch {}
  }

  const referer = request.headers.get('referer') || '';
  const thankYou = referer.includes('/ua/') ? '/ua/thanks/' : '/thanks/';
  return redirect(thankYou, 302);
}

export async function onRequest({ request }) {
  return json({ error: 'Method not allowed' }, { status: 405, headers: corsHeaders(request, 'POST') });
}
