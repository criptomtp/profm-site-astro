export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const body = req.body || {};
    const { Name, Phone, Email, tildaspec } = body;

    // Parse tildaspec for form metadata
    let formName = 'Заявка з сайту';
    if (tildaspec) {
      try {
        const spec = JSON.parse(tildaspec);
        formName = spec.formname || spec.descr || formName;
      } catch {}
    }

    // Option 1: Send to Telegram bot (recommended - free, instant)
    const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
    const TELEGRAM_CHAT_ID = process.env.TELEGRAM_CHAT_ID;

    if (TELEGRAM_BOT_TOKEN && TELEGRAM_CHAT_ID) {
      const message = [
        `📩 ${formName}`,
        `👤 Ім'я: ${Name || '—'}`,
        `📱 Телефон: ${Phone || '—'}`,
        `📧 Email: ${Email || '—'}`,
        `🕐 ${new Date().toLocaleString('uk-UA', { timeZone: 'Europe/Kyiv' })}`,
      ].join('\n');

      await fetch(
        `https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            chat_id: TELEGRAM_CHAT_ID,
            text: message,
            parse_mode: 'HTML',
          }),
        }
      );
    }

    // Option 2: Forward to email via Web3Forms (set WEB3FORMS_KEY env var)
    const WEB3FORMS_KEY = process.env.WEB3FORMS_KEY;
    if (WEB3FORMS_KEY) {
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
    }

    // Redirect to thank-you page
    const thankYou = req.headers.referer?.includes('/ua/') ? '/ua/thanks' : '/thanks';
    res.redirect(302, thankYou);
  } catch (error) {
    console.error('Form error:', error);
    res.redirect(302, '/thanks');
  }
}
