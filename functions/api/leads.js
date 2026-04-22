import { corsHeaders, json, readJson, getClientIp } from './_helpers.js';
import { makeRedis, verifySession } from './_session.js';

const LEADS_KEY = 'mtp:leads';
const RATE_LIMIT_PREFIX = 'rl:leads:';
const RATE_LIMIT_MAX = 30;
const RATE_LIMIT_WINDOW = 60;

function checkApiKey(request, env) {
  const key = request.headers.get('x-api-key');
  const expected = env.LEADS_API_KEY;
  return !!expected && key === expected;
}

async function checkAuth(request, env) {
  if (checkApiKey(request, env)) return true;
  const session = await verifySession(request, env);
  return !!session;
}

async function checkRateLimit(redis, ip) {
  const key = RATE_LIMIT_PREFIX + ip;
  const count = await redis.incr(key);
  if (count === 1) await redis.expire(key, RATE_LIMIT_WINDOW);
  return count <= RATE_LIMIT_MAX;
}

const METHODS = 'GET, POST, PUT, DELETE, OPTIONS';

export async function onRequestOptions({ request }) {
  return new Response(null, { status: 204, headers: corsHeaders(request, METHODS) });
}

export async function onRequest({ request, env }) {
  const headers = corsHeaders(request, METHODS);
  const redis = makeRedis(env);
  const method = request.method;
  const ip = getClientIp(request);

  const allowed = await checkRateLimit(redis, ip).catch(() => true);
  if (!allowed) return json({ error: 'Too many requests' }, { status: 429, headers });

  try {
    if (method === 'POST') {
      const body = await readJson(request);
      if (!body || !body.phone) return json({ error: 'phone required' }, { status: 400, headers });

      const leads = (await redis.get(LEADS_KEY)) || [];

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

      const { TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID } = env;
      if (TELEGRAM_BOT_TOKEN && TELEGRAM_CHAT_ID) {
        const text = `🆕 Нова заявка!\n📱 ${newLead.phone}\n📋 ${String(body.page || '/').slice(0, 100)}`;
        fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ chat_id: TELEGRAM_CHAT_ID, text, parse_mode: 'HTML' }),
        }).catch(() => {});
      }

      return json({ id: newLead.id, ok: true }, { status: 201, headers });
    }

    const authorized = await checkAuth(request, env);
    if (!authorized) return json({ error: 'Unauthorized' }, { status: 401, headers });

    if (method === 'GET') {
      const leads = (await redis.get(LEADS_KEY)) || [];
      return json(leads, { status: 200, headers });
    }

    if (method === 'PUT') {
      const body = await readJson(request);
      if (!body.id) return json({ error: 'id required' }, { status: 400, headers });
      const leads = (await redis.get(LEADS_KEY)) || [];
      const idx = leads.findIndex(l => String(l.id) === String(body.id));
      if (idx === -1) return json({ error: 'lead not found' }, { status: 404, headers });
      leads[idx] = { ...leads[idx], ...body };
      await redis.set(LEADS_KEY, leads);
      return json(leads[idx], { status: 200, headers });
    }

    if (method === 'DELETE') {
      const url = new URL(request.url);
      const body = await readJson(request).catch(() => ({}));
      const id = url.searchParams.get('id') || body.id;
      if (!id) return json({ error: 'id required' }, { status: 400, headers });
      let leads = (await redis.get(LEADS_KEY)) || [];
      leads = leads.filter(l => String(l.id) !== String(id));
      await redis.set(LEADS_KEY, leads);
      return json({ ok: true }, { status: 200, headers });
    }

    return json({ error: 'Method not allowed' }, { status: 405, headers });
  } catch (e) {
    return json({ error: 'Internal server error', detail: String(e?.message || e) }, { status: 500, headers });
  }
}
