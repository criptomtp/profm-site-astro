import { Redis } from '@upstash/redis/cloudflare';
import { getRedisConfig } from './_helpers.js';

const SESSIONS_KEY = 'mtp:sessions';
const SESSION_TTL_HOURS = 24;

export function makeRedis(env) {
  return new Redis(getRedisConfig(env));
}

function isSessionExpired(session) {
  if (!session.created) return true;
  const created = new Date(session.created).getTime();
  return Date.now() - created > SESSION_TTL_HOURS * 60 * 60 * 1000;
}

export async function verifySession(request, env) {
  const auth = request.headers.get('authorization') || '';
  const url = new URL(request.url);
  const token = auth.replace('Bearer ', '') || url.searchParams.get('session');
  if (!token) return null;
  const redis = makeRedis(env);
  const sessions = (await redis.get(SESSIONS_KEY)) || {};
  const s = sessions[token];
  if (!s || isSessionExpired(s)) return null;
  return s;
}

export { SESSIONS_KEY, SESSION_TTL_HOURS, isSessionExpired };
