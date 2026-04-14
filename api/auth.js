import { Redis } from '@upstash/redis';
import { scrypt, randomBytes, timingSafeEqual } from 'crypto';

const redis = new Redis({
  url: process.env.storage_KV_REST_API_URL || process.env.STORAGE_URL,
  token: process.env.storage_KV_REST_API_TOKEN || process.env.STORAGE_REST_API_TOKEN,
});

const USERS_KEY = 'mtp:users:v2';
const USERS_KEY_OLD = 'mtp:users';
const SESSIONS_KEY = 'mtp:sessions';
const RATE_LIMIT_PREFIX = 'mtp:ratelimit:login:';
const RATE_LIMIT_MAX = 5;
const RATE_LIMIT_WINDOW = 60;
const SESSION_TTL_HOURS = 24;

// --- Password hashing with scrypt ---

function hashPassword(password) {
  return new Promise((resolve, reject) => {
    const salt = randomBytes(16).toString('hex');
    scrypt(password, salt, 64, (err, derived) => {
      if (err) return reject(err);
      resolve(salt + ':' + derived.toString('hex'));
    });
  });
}

function verifyPassword(password, stored) {
  return new Promise((resolve, reject) => {
    const [salt, hash] = stored.split(':');
    if (!salt || !hash) return resolve(false);
    scrypt(password, salt, 64, (err, derived) => {
      if (err) return reject(err);
      const hashBuf = Buffer.from(hash, 'hex');
      resolve(timingSafeEqual(hashBuf, derived));
    });
  });
}

function isHashed(password) {
  return typeof password === 'string' && password.includes(':') && password.length > 80;
}

// --- Default users ---

async function getDefaultUsers() {
  const adminPassword = process.env.ADMIN_PASSWORD;
  if (!adminPassword) return null;
  const hashed = await hashPassword(adminPassword);
  return [
    {
      id: 'admin',
      username: 'mtp_admin',
      password: hashed,
      name: 'Admin',
      role: 'admin',
      permissions: ['crm', 'dashboard', 'seo', 'content', 'settings', 'users']
    }
  ];
}

// --- Users with auto-migration from v1 (plain-text) to v2 (hashed) ---

async function getUsers() {
  let users = await redis.get(USERS_KEY);
  if (users && Array.isArray(users) && users.length > 0) return users;

  // Try migrating from old key (v1 with plain-text passwords)
  const oldUsers = await redis.get(USERS_KEY_OLD);
  if (oldUsers && Array.isArray(oldUsers) && oldUsers.length > 0) {
    const migrated = [];
    for (const u of oldUsers) {
      const hashed = isHashed(u.password) ? u.password : await hashPassword(u.password);
      migrated.push({ ...u, password: hashed });
    }
    await redis.set(USERS_KEY, migrated);
    return migrated;
  }

  // No users — create defaults
  const defaults = await getDefaultUsers();
  if (!defaults) return null;
  await redis.set(USERS_KEY, defaults);
  return defaults;
}

// --- Session helpers ---

function generateSessionId() {
  return randomBytes(32).toString('hex');
}

function isSessionExpired(session) {
  if (!session.created) return true;
  const created = new Date(session.created).getTime();
  return Date.now() - created > SESSION_TTL_HOURS * 60 * 60 * 1000;
}

async function verifySession(req) {
  const token = req.headers.authorization?.replace('Bearer ', '') || req.query.session;
  if (!token) return null;
  const sessions = await redis.get(SESSIONS_KEY) || {};
  const s = sessions[token];
  if (!s || isSessionExpired(s)) return null;
  return s;
}

async function cleanExpiredSessions() {
  const sessions = await redis.get(SESSIONS_KEY) || {};
  let cleaned = false;
  for (const [key, s] of Object.entries(sessions)) {
    if (isSessionExpired(s)) {
      delete sessions[key];
      cleaned = true;
    }
  }
  if (cleaned) await redis.set(SESSIONS_KEY, sessions);
}

// --- CORS ---

function getClientIp(req) {
  return req.headers['x-forwarded-for']?.split(',')[0]?.trim()
    || req.headers['x-real-ip']
    || req.socket?.remoteAddress
    || 'unknown';
}

const ALLOWED_ORIGINS = [
  'https://www.fulfillmentmtp.com.ua',
  'https://fulfillmentmtp.com.ua',
  'https://profm-site-astro.vercel.app',
];

// --- Handler ---

export default async function handler(req, res) {
  const origin = req.headers.origin;
  if (ALLOWED_ORIGINS.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
  }
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Vary', 'Origin');

  if (req.method === 'OPTIONS') return res.status(200).end();

  const action = req.query.action || req.body?.action;

  try {
    // LOGIN
    if (req.method === 'POST' && action === 'login') {
      if (!process.env.ADMIN_PASSWORD) {
        return res.status(503).json({ error: 'Auth not configured' });
      }

      const clientIp = getClientIp(req);
      const rateLimitKey = RATE_LIMIT_PREFIX + clientIp;
      const failedAttempts = (await redis.get(rateLimitKey)) || 0;
      if (failedAttempts >= RATE_LIMIT_MAX) {
        return res.status(429).json({ error: 'Too many failed attempts. Try again later.' });
      }

      const { username, password } = req.body;
      if (!username || !password) {
        return res.status(400).json({ error: 'Username and password required' });
      }

      const users = await getUsers();
      if (!users) {
        return res.status(503).json({ error: 'Auth not configured' });
      }

      const user = users.find(u => u.username === username);
      if (!user) {
        await redis.set(rateLimitKey, failedAttempts + 1, { ex: RATE_LIMIT_WINDOW });
        return res.status(401).json({ error: 'Invalid credentials' });
      }

      // Handle migration: if password is still plain-text, hash it on successful match
      let passwordMatch = false;
      if (isHashed(user.password)) {
        passwordMatch = await verifyPassword(password, user.password);
      } else if (user.password === password) {
        // Plain-text match — migrate to hashed
        passwordMatch = true;
        user.password = await hashPassword(password);
        await redis.set(USERS_KEY, users);
      }

      if (!passwordMatch) {
        await redis.set(rateLimitKey, failedAttempts + 1, { ex: RATE_LIMIT_WINDOW });
        return res.status(401).json({ error: 'Invalid credentials' });
      }

      await redis.del(rateLimitKey);

      // Clean expired sessions periodically
      await cleanExpiredSessions();

      const sessionId = generateSessionId();
      const sessions = await redis.get(SESSIONS_KEY) || {};
      sessions[sessionId] = {
        userId: user.id,
        username: user.username,
        role: user.role,
        permissions: user.permissions,
        created: new Date().toISOString()
      };
      await redis.set(SESSIONS_KEY, sessions);

      return res.status(200).json({
        ok: true,
        session: sessionId,
        user: { id: user.id, name: user.name, role: user.role, permissions: user.permissions }
      });
    }

    // CHECK SESSION
    if (req.method === 'GET' && action === 'check') {
      const s = await verifySession(req);
      if (!s) return res.status(401).json({ error: 'Invalid or expired session' });
      return res.status(200).json({ ok: true, user: s });
    }

    // LOGOUT
    if (req.method === 'POST' && action === 'logout') {
      const token = req.headers.authorization?.replace('Bearer ', '');
      if (token) {
        const sessions = await redis.get(SESSIONS_KEY) || {};
        delete sessions[token];
        await redis.set(SESSIONS_KEY, sessions);
      }
      return res.status(200).json({ ok: true });
    }

    // --- Protected endpoints below: require valid session ---

    const currentUser = await verifySession(req);
    if (!currentUser) {
      return res.status(401).json({ error: 'Unauthorized — valid session required' });
    }

    // LIST USERS (admin only)
    if (req.method === 'GET' && action === 'users') {
      if (currentUser.role !== 'admin') {
        return res.status(403).json({ error: 'Admin access required' });
      }
      const users = await getUsers();
      if (!users) return res.status(200).json([]);
      return res.status(200).json(users.map(u => ({
        id: u.id, username: u.username, name: u.name, role: u.role, permissions: u.permissions
      })));
    }

    // CREATE USER (admin only)
    if (req.method === 'POST' && action === 'create_user') {
      if (currentUser.role !== 'admin') {
        return res.status(403).json({ error: 'Admin access required' });
      }

      const { username, password, name, role, permissions } = req.body;
      if (!username || !password) return res.status(400).json({ error: 'username and password required' });
      if (password.length < 8) return res.status(400).json({ error: 'Password must be at least 8 characters' });

      const users = await getUsers();
      if (users.find(u => u.username === username)) return res.status(400).json({ error: 'Username exists' });

      const hashedPwd = await hashPassword(password);
      const newUser = {
        id: Date.now().toString(),
        username,
        password: hashedPwd,
        name: name || username,
        role: role || 'manager',
        permissions: permissions || ['crm', 'dashboard']
      };
      users.push(newUser);
      await redis.set(USERS_KEY, users);
      return res.status(201).json({
        ok: true,
        user: { id: newUser.id, username: newUser.username, name: newUser.name, role: newUser.role, permissions: newUser.permissions }
      });
    }

    // UPDATE USER (admin only)
    if ((req.method === 'PUT' || req.method === 'POST') && action === 'update_user') {
      if (currentUser.role !== 'admin') {
        return res.status(403).json({ error: 'Admin access required' });
      }

      const { id, name, role, permissions, password } = req.body;
      const users = await getUsers();
      const idx = users.findIndex(u => u.id === id);
      if (idx === -1) return res.status(404).json({ error: 'User not found' });

      if (name) users[idx].name = name;
      if (role) users[idx].role = role;
      if (permissions) users[idx].permissions = permissions;
      if (password) {
        if (password.length < 8) return res.status(400).json({ error: 'Password must be at least 8 characters' });
        users[idx].password = await hashPassword(password);
      }
      await redis.set(USERS_KEY, users);
      return res.status(200).json({ ok: true });
    }

    // DELETE USER (admin only)
    if (req.method === 'DELETE' && action === 'delete_user') {
      if (currentUser.role !== 'admin') {
        return res.status(403).json({ error: 'Admin access required' });
      }

      const id = req.query.id;
      if (id === 'admin') return res.status(400).json({ error: 'Cannot delete admin' });

      let users = await getUsers();
      users = users.filter(u => u.id !== id);
      await redis.set(USERS_KEY, users);
      return res.status(200).json({ ok: true });
    }

    return res.status(400).json({ error: 'Unknown action' });
  } catch (error) {
    console.error('Auth API error:', error);
    return res.status(500).json({ error: 'Internal server error' });
  }
}
