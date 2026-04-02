import { Redis } from '@upstash/redis';

const redis = new Redis({
  url: process.env.storage_KV_REST_API_URL || process.env.STORAGE_URL || process.env.KV_REST_API_URL,
  token: process.env.storage_KV_REST_API_TOKEN || process.env.STORAGE_REST_API_TOKEN || process.env.KV_REST_API_TOKEN,
});

const GSC_KEY = 'mtp:gsc:history';
const GSC_LATEST = 'mtp:gsc:latest';

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();

  // GET — read GSC data for dashboard
  if (req.method === 'GET') {
    try {
      const latest = await redis.get(GSC_LATEST);
      const history = await redis.get(GSC_KEY);
      return res.status(200).json({
        latest: latest || null,
        history: history || [],
      });
    } catch (e) {
      return res.status(500).json({ error: e.message });
    }
  }

  // POST — save new GSC snapshot (called by gsc-sync.py)
  if (req.method === 'POST') {
    try {
      const { date, queries, pages } = req.body;
      if (!date || !queries) {
        return res.status(400).json({ error: 'Missing date or queries' });
      }

      const snapshot = { date, queries, pages: pages || [], timestamp: Date.now() };

      // Save as latest
      await redis.set(GSC_LATEST, snapshot);

      // Append to history (keep last 90 days)
      let history = await redis.get(GSC_KEY) || [];
      history.push(snapshot);
      if (history.length > 90) history = history.slice(-90);
      await redis.set(GSC_KEY, history);

      return res.status(200).json({ ok: true, snapshots: history.length });
    } catch (e) {
      return res.status(500).json({ error: e.message });
    }
  }

  return res.status(405).json({ error: 'Method not allowed' });
}
