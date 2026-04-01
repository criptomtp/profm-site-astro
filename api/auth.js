import { Redis } from '@upstash/redis';

const redis = new Redis({
  url: process.env.storage_KV_REST_API_URL || process.env.STORAGE_URL,
  token: process.env.storage_KV_REST_API_TOKEN || process.env.STORAGE_REST_API_TOKEN,
});

const USERS_KEY = 'mtp:users';
const SESSIONS_KEY = 'mtp:sessions';

// Default admin user
const DEFAULT_USERS = [
  {
    id: 'admin',
    username: 'mtp_admin',
    password: 'MTP2026secure!',
    name: 'Адмін',
    role: 'admin',
    permissions: ['crm', 'dashboard', 'seo', 'content', 'settings', 'users']
  }
];

async function getUsers() {
  const users = await redis.get(USERS_KEY);
  if (!users || !Array.isArray(users) || users.length === 0) {
    await redis.set(USERS_KEY, DEFAULT_USERS);
    return DEFAULT_USERS;
  }
  return users;
}

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  if (req.method === 'OPTIONS') return res.status(200).end();

  const action = req.query.action || req.body?.action;

  try {
    // LOGIN
    if (req.method === 'POST' && action === 'login') {
      const { username, password } = req.body;
      const users = await getUsers();
      const user = users.find(u => u.username === username && u.password === password);
      if (!user) return res.status(401).json({ error: 'Невірний логін або пароль' });

      const sessionId = Date.now().toString(36) + Math.random().toString(36).slice(2);
      const sessions = await redis.get(SESSIONS_KEY) || {};
      sessions[sessionId] = { userId: user.id, username: user.username, role: user.role, permissions: user.permissions, created: new Date().toISOString() };
      await redis.set(SESSIONS_KEY, sessions);

      return res.status(200).json({ ok: true, session: sessionId, user: { id: user.id, name: user.name, role: user.role, permissions: user.permissions } });
    }

    // CHECK SESSION
    if (req.method === 'GET' && action === 'check') {
      const session = req.query.session || req.headers.authorization?.replace('Bearer ', '');
      if (!session) return res.status(401).json({ error: 'No session' });

      const sessions = await redis.get(SESSIONS_KEY) || {};
      const s = sessions[session];
      if (!s) return res.status(401).json({ error: 'Invalid session' });

      return res.status(200).json({ ok: true, user: s });
    }

    // LIST USERS (admin only)
    if (req.method === 'GET' && action === 'users') {
      const users = await getUsers();
      return res.status(200).json(users.map(u => ({ id: u.id, username: u.username, name: u.name, role: u.role, permissions: u.permissions })));
    }

    // CREATE USER (admin only)
    if (req.method === 'POST' && action === 'create_user') {
      const { username, password, name, role, permissions } = req.body;
      if (!username || !password) return res.status(400).json({ error: 'username and password required' });

      const users = await getUsers();
      if (users.find(u => u.username === username)) return res.status(400).json({ error: 'Username exists' });

      const newUser = {
        id: Date.now().toString(),
        username, password, name: name || username,
        role: role || 'manager',
        permissions: permissions || ['crm', 'dashboard']
      };
      users.push(newUser);
      await redis.set(USERS_KEY, users);
      return res.status(201).json({ ok: true, user: { id: newUser.id, username: newUser.username, name: newUser.name, role: newUser.role, permissions: newUser.permissions } });
    }

    // UPDATE USER (POST or PUT)
    if ((req.method === 'PUT' || req.method === 'POST') && action === 'update_user') {
      const { id, name, role, permissions, password } = req.body;
      const users = await getUsers();
      const idx = users.findIndex(u => u.id === id);
      if (idx === -1) return res.status(404).json({ error: 'User not found' });

      if (name) users[idx].name = name;
      if (role) users[idx].role = role;
      if (permissions) users[idx].permissions = permissions;
      if (password) users[idx].password = password;
      await redis.set(USERS_KEY, users);
      return res.status(200).json({ ok: true });
    }

    // DELETE USER
    if (req.method === 'DELETE' && action === 'delete_user') {
      const id = req.query.id;
      if (id === 'admin') return res.status(400).json({ error: 'Cannot delete admin' });

      let users = await getUsers();
      users = users.filter(u => u.id !== id);
      await redis.set(USERS_KEY, users);
      return res.status(200).json({ ok: true });
    }

    return res.status(400).json({ error: 'Unknown action' });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
}
