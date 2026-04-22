import { corsHeaders, json, readJson } from './_helpers.js';
import { makeRedis } from './_session.js';

const GSC_KEY = 'mtp:gsc:history';
const GSC_LATEST = 'mtp:gsc:latest';

const METHODS = 'GET, POST, OPTIONS';
const openCors = (request) => ({ ...corsHeaders(request, METHODS), 'Access-Control-Allow-Origin': '*' });

export async function onRequestOptions({ request }) {
  return new Response(null, { status: 204, headers: openCors(request) });
}

export async function onRequestGet({ request, env }) {
  const headers = openCors(request);
  try {
    const redis = makeRedis(env);
    const latest = await redis.get(GSC_LATEST);
    const history = await redis.get(GSC_KEY);
    return json({ latest: latest || null, history: history || [] }, { status: 200, headers });
  } catch (e) {
    return json({ error: e.message }, { status: 500, headers });
  }
}

export async function onRequestPost({ request, env }) {
  const headers = openCors(request);
  try {
    const redis = makeRedis(env);
    const { date, queries, pages } = await readJson(request);
    if (!date || !queries) return json({ error: 'Missing date or queries' }, { status: 400, headers });

    const snapshot = { date, queries, pages: pages || [], timestamp: Date.now() };
    await redis.set(GSC_LATEST, snapshot);

    let history = (await redis.get(GSC_KEY)) || [];
    history.push(snapshot);
    if (history.length > 90) history = history.slice(-90);
    await redis.set(GSC_KEY, history);

    return json({ ok: true, snapshots: history.length }, { status: 200, headers });
  } catch (e) {
    return json({ error: e.message }, { status: 500, headers });
  }
}

export async function onRequest({ request }) {
  return json({ error: 'Method not allowed' }, { status: 405, headers: openCors(request) });
}
