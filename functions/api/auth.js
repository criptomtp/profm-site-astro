import { corsHeaders, json, readJson, getClientIp } from './_helpers.js';
import { makeRedis, SESSIONS_KEY, verifySession, isSessionExpired } from './_session.js';
import { hashPassword, verifyPassword, isPbkdf2Hash, isLegacyScryptHash, generateSessionId } from './_crypto.js';

const USERS_KEY = 'mtp:users:v2';
const USERS_KEY_OLD = 'mtp:users';
const RATE_LIMIT_PREFIX = 'mtp:ratelimit:login:';
const RATE_LIMIT_MAX = 5;
const RATE_LIMIT_WINDOW = 60;

const METHODS = 'GET, POST, PUT, DELETE, OPTIONS';

async function getDefaultUsers(env) {
  const adminPassword = env.ADMIN_PASSWORD;
  if (!adminPassword) return null;
  const hashed = await hashPassword(adminPassword);
  return [{
    id: 'admin',
    username: 'mtp_admin',
    password: hashed,
    name: 'Admin',
    role: 'admin',
    permissions: ['crm', 'dashboard', 'seo', 'content', 'settings', 'users'],
  }];
}

async function getUsers(redis, env) {
  let users = await redis.get(USERS_KEY);
  if (users && Array.isArray(users) && users.length > 0) return users;

  const oldUsers = await redis.get(USERS_KEY_OLD);
  if (oldUsers && Array.isArray(oldUsers) && oldUsers.length > 0) {
    const migrated = [];
    for (const u of oldUsers) {
      // If old entry has plain-text, hash it now. Legacy scrypt hashes cannot be verified in Workers,
      // so we re-hash plain passwords only; scrypt hashes are kept as-is and will force reset on login.
      const needsHash = !isPbkdf2Hash(u.password) && !isLegacyScryptHash(u.password);
      const hashed = needsHash ? await hashPassword(u.password) : u.password;
      migrated.push({ ...u, password: hashed });
    }
    await redis.set(USERS_KEY, migrated);
    return migrated;
  }

  const defaults = await getDefaultUsers(env);
  if (!defaults) return null;
  await redis.set(USERS_KEY, defaults);
  return defaults;
}

async function cleanExpiredSessions(redis) {
  const sessions = (await redis.get(SESSIONS_KEY)) || {};
  let cleaned = false;
  for (const [key, s] of Object.entries(sessions)) {
    if (isSessionExpired(s)) { delete sessions[key]; cleaned = true; }
  }
  if (cleaned) await redis.set(SESSIONS_KEY, sessions);
}

export async function onRequestOptions({ request }) {
  return new Response(null, { status: 204, headers: corsHeaders(request, METHODS) });
}

export async function onRequest({ request, env }) {
  const headers = corsHeaders(request, METHODS);
  const method = request.method;
  const url = new URL(request.url);
  const body = ['POST', 'PUT'].includes(method) ? await readJson(request) : {};
  const action = url.searchParams.get('action') || body.action;

  const redis = makeRedis(env);

  try {
    // LOGIN
    if (method === 'POST' && action === 'login') {
      if (!env.ADMIN_PASSWORD) return json({ error: 'Auth not configured' }, { status: 503, headers });

      const clientIp = getClientIp(request);
      const rateLimitKey = RATE_LIMIT_PREFIX + clientIp;
      const failedAttempts = (await redis.get(rateLimitKey)) || 0;
      if (failedAttempts >= RATE_LIMIT_MAX) return json({ error: 'Too many failed attempts. Try again later.' }, { status: 429, headers });

      const { username, password } = body;
      if (!username || !password) return json({ error: 'Username and password required' }, { status: 400, headers });

      const users = await getUsers(redis, env);
      if (!users) return json({ error: 'Auth not configured' }, { status: 503, headers });

      const user = users.find(u => u.username === username);
      if (!user) {
        await redis.set(rateLimitKey, failedAttempts + 1, { ex: RATE_LIMIT_WINDOW });
        return json({ error: 'Invalid credentials' }, { status: 401, headers });
      }

      let passwordMatch = false;

      // Admin scrypt migration: if this is admin AND entered password matches env ADMIN_PASSWORD,
      // accept login and re-hash to PBKDF2 regardless of what's stored (scrypt/plain/anything).
      // Check this FIRST so scrypt-stored admin can still log in via env password.
      if (user.id === 'admin' && env.ADMIN_PASSWORD && password === env.ADMIN_PASSWORD) {
        passwordMatch = true;
        user.password = await hashPassword(password);
        await redis.set(USERS_KEY, users);
      } else if (isPbkdf2Hash(user.password)) {
        passwordMatch = await verifyPassword(password, user.password);
      } else if (isLegacyScryptHash(user.password)) {
        // Non-admin scrypt user — cannot verify in Workers runtime. Admin must reset.
        return json({
          error: 'Password migration required. Admin must reset this user via users panel.',
        }, { status: 403, headers });
      } else if (user.password === password) {
        // Plain-text legacy match — migrate to PBKDF2
        passwordMatch = true;
        user.password = await hashPassword(password);
        await redis.set(USERS_KEY, users);
      }

      if (!passwordMatch) {
        await redis.set(rateLimitKey, failedAttempts + 1, { ex: RATE_LIMIT_WINDOW });
        return json({ error: 'Invalid credentials' }, { status: 401, headers });
      }

      await redis.del(rateLimitKey);
      await cleanExpiredSessions(redis);

      const sessionId = generateSessionId();
      const sessions = (await redis.get(SESSIONS_KEY)) || {};
      sessions[sessionId] = {
        userId: user.id,
        username: user.username,
        role: user.role,
        permissions: user.permissions,
        created: new Date().toISOString(),
      };
      await redis.set(SESSIONS_KEY, sessions);

      return json({
        ok: true,
        session: sessionId,
        user: { id: user.id, name: user.name, role: user.role, permissions: user.permissions },
      }, { status: 200, headers });
    }

    // CHECK SESSION
    if (method === 'GET' && action === 'check') {
      const s = await verifySession(request, env);
      if (!s) return json({ error: 'Invalid or expired session' }, { status: 401, headers });
      return json({ ok: true, user: s }, { status: 200, headers });
    }

    // LOGOUT
    if (method === 'POST' && action === 'logout') {
      const token = (request.headers.get('authorization') || '').replace('Bearer ', '');
      if (token) {
        const sessions = (await redis.get(SESSIONS_KEY)) || {};
        delete sessions[token];
        await redis.set(SESSIONS_KEY, sessions);
      }
      return json({ ok: true }, { status: 200, headers });
    }

    // Protected endpoints
    const currentUser = await verifySession(request, env);
    if (!currentUser) return json({ error: 'Unauthorized — valid session required' }, { status: 401, headers });

    // LIST USERS (admin only)
    if (method === 'GET' && action === 'users') {
      if (currentUser.role !== 'admin') return json({ error: 'Admin access required' }, { status: 403, headers });
      const users = await getUsers(redis, env);
      if (!users) return json([], { status: 200, headers });
      return json(users.map(u => ({ id: u.id, username: u.username, name: u.name, role: u.role, permissions: u.permissions })), { status: 200, headers });
    }

    // CREATE USER (admin only)
    if (method === 'POST' && action === 'create_user') {
      if (currentUser.role !== 'admin') return json({ error: 'Admin access required' }, { status: 403, headers });
      const { username, password, name, role, permissions } = body;
      if (!username || !password) return json({ error: 'username and password required' }, { status: 400, headers });
      if (password.length < 8) return json({ error: 'Password must be at least 8 characters' }, { status: 400, headers });

      const users = await getUsers(redis, env);
      if (users.find(u => u.username === username)) return json({ error: 'Username exists' }, { status: 400, headers });

      const newUser = {
        id: Date.now().toString(),
        username,
        password: await hashPassword(password),
        name: name || username,
        role: role || 'manager',
        permissions: permissions || ['crm', 'dashboard'],
      };
      users.push(newUser);
      await redis.set(USERS_KEY, users);
      return json({ ok: true, user: { id: newUser.id, username: newUser.username, name: newUser.name, role: newUser.role, permissions: newUser.permissions } }, { status: 201, headers });
    }

    // UPDATE USER (admin only)
    if ((method === 'PUT' || method === 'POST') && action === 'update_user') {
      if (currentUser.role !== 'admin') return json({ error: 'Admin access required' }, { status: 403, headers });
      const { id, name, role, permissions, password } = body;
      const users = await getUsers(redis, env);
      const idx = users.findIndex(u => u.id === id);
      if (idx === -1) return json({ error: 'User not found' }, { status: 404, headers });

      if (name) users[idx].name = name;
      if (role) users[idx].role = role;
      if (permissions) users[idx].permissions = permissions;
      if (password) {
        if (password.length < 8) return json({ error: 'Password must be at least 8 characters' }, { status: 400, headers });
        users[idx].password = await hashPassword(password);
      }
      await redis.set(USERS_KEY, users);
      return json({ ok: true }, { status: 200, headers });
    }

    // DELETE USER (admin only)
    if (method === 'DELETE' && action === 'delete_user') {
      if (currentUser.role !== 'admin') return json({ error: 'Admin access required' }, { status: 403, headers });
      const id = url.searchParams.get('id');
      if (id === 'admin') return json({ error: 'Cannot delete admin' }, { status: 400, headers });

      let users = await getUsers(redis, env);
      users = users.filter(u => u.id !== id);
      await redis.set(USERS_KEY, users);
      return json({ ok: true }, { status: 200, headers });
    }

    return json({ error: 'Unknown action' }, { status: 400, headers });
  } catch (error) {
    return json({ error: 'Internal server error', detail: String(error?.message || error) }, { status: 500, headers });
  }
}
