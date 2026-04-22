// Shared helpers for CF Pages Functions
// Replaces Vercel's req.body / res.status().json() / res.setHeader() patterns

export const ALLOWED_ORIGINS = [
  'https://www.fulfillmentmtp.com.ua',
  'https://fulfillmentmtp.com.ua',
  'https://fulfillmentmtp.pages.dev',
  'https://profm-site-astro.vercel.app',
];

export function corsHeaders(request, methods = 'GET, POST, OPTIONS', extra = {}) {
  const origin = request.headers.get('origin') || '';
  const allowed = ALLOWED_ORIGINS.includes(origin);
  return {
    'Access-Control-Allow-Origin': allowed ? origin : '',
    'Access-Control-Allow-Methods': methods,
    'Access-Control-Allow-Headers': 'Content-Type, X-Api-Key, Authorization',
    'Access-Control-Allow-Credentials': 'true',
    'Vary': 'Origin',
    ...extra,
  };
}

export function json(body, init = {}) {
  const headers = { 'Content-Type': 'application/json', ...(init.headers || {}) };
  return new Response(JSON.stringify(body), { status: init.status || 200, headers });
}

export function text(body, init = {}) {
  const headers = { 'Content-Type': 'text/plain; charset=utf-8', ...(init.headers || {}) };
  return new Response(body, { status: init.status || 200, headers });
}

export function redirect(url, status = 302) {
  return new Response(null, { status, headers: { Location: url } });
}

export async function readJson(request) {
  try {
    const ct = request.headers.get('content-type') || '';
    if (ct.includes('application/json')) return await request.json();
    if (ct.includes('application/x-www-form-urlencoded') || ct.includes('multipart/form-data')) {
      const fd = await request.formData();
      const obj = {};
      for (const [k, v] of fd.entries()) obj[k] = v;
      return obj;
    }
    return {};
  } catch {
    return {};
  }
}

export function getClientIp(request) {
  return (
    request.headers.get('cf-connecting-ip') ||
    request.headers.get('x-forwarded-for')?.split(',')[0]?.trim() ||
    request.headers.get('x-real-ip') ||
    'unknown'
  );
}

export function getRedisConfig(env) {
  return {
    url: env.storage_KV_REST_API_URL || env.STORAGE_URL || env.KV_REST_API_URL,
    token: env.storage_KV_REST_API_TOKEN || env.STORAGE_REST_API_TOKEN || env.KV_REST_API_TOKEN,
  };
}
