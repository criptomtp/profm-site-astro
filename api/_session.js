import { Redis } from '@upstash/redis';

const redis = new Redis({
  url: process.env.storage_KV_REST_API_URL || process.env.STORAGE_URL || process.env.KV_REST_API_URL,
  token: process.env.storage_KV_REST_API_TOKEN || process.env.STORAGE_REST_API_TOKEN || process.env.KV_REST_API_TOKEN,
});

const SESSIONS_KEY = 'mtp:sessions';
const SESSION_TTL_HOURS = 24;

function isSessionExpired(session) {
  if (!session.created) return true;
  const created = new Date(session.created).getTime();
  return Date.now() - created > SESSION_TTL_HOURS * 60 * 60 * 1000;
}

export async function verifySession(req) {
  const token = req.headers.authorization?.replace('Bearer ', '') || req.query.session;
  if (!token) return null;
  const sessions = await redis.get(SESSIONS_KEY) || {};
  const s = sessions[token];
  if (!s || isSessionExpired(s)) return null;
  return s;
}
