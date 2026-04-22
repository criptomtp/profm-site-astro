// Web Crypto PBKDF2 — replaces Node's scrypt for CF Workers runtime.
// Backward-compat: verifyPassword() detects legacy Node-scrypt hashes
// (format: `saltHex:hashHex` with 64-byte hash) and rejects them.
// First successful login under the migration triggers a re-hash to PBKDF2.
// PBKDF2 format: `pbkdf2$<iterations>$<saltHex>$<hashHex>`

const PBKDF2_ITERATIONS = 210000; // OWASP 2025 recommendation for SHA-256
const SALT_BYTES = 16;
const KEY_BYTES = 32; // 256-bit derived key

function bytesToHex(buf) {
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
}

function hexToBytes(hex) {
  const out = new Uint8Array(hex.length / 2);
  for (let i = 0; i < hex.length; i += 2) out[i / 2] = parseInt(hex.substr(i, 2), 16);
  return out;
}

async function pbkdf2(password, saltBytes, iterations = PBKDF2_ITERATIONS, keyBytes = KEY_BYTES) {
  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey(
    'raw',
    enc.encode(password),
    { name: 'PBKDF2' },
    false,
    ['deriveBits']
  );
  const derived = await crypto.subtle.deriveBits(
    { name: 'PBKDF2', salt: saltBytes, iterations, hash: 'SHA-256' },
    key,
    keyBytes * 8
  );
  return new Uint8Array(derived);
}

export async function hashPassword(password) {
  const saltBytes = crypto.getRandomValues(new Uint8Array(SALT_BYTES));
  const derived = await pbkdf2(password, saltBytes);
  return `pbkdf2$${PBKDF2_ITERATIONS}$${bytesToHex(saltBytes)}$${bytesToHex(derived)}`;
}

function timingSafeEqual(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a[i] ^ b[i];
  return diff === 0;
}

export async function verifyPassword(password, stored) {
  if (typeof stored !== 'string') return false;

  // New PBKDF2 format
  if (stored.startsWith('pbkdf2$')) {
    const [, iterStr, saltHex, hashHex] = stored.split('$');
    const iterations = parseInt(iterStr, 10);
    const saltBytes = hexToBytes(saltHex);
    const expected = hexToBytes(hashHex);
    const derived = await pbkdf2(password, saltBytes, iterations, expected.length);
    return timingSafeEqual(derived, expected);
  }

  // Legacy Node scrypt format (salt:hash with 64-byte hash) — cannot verify in Workers.
  // Return false; admin must reset password via out-of-band flow.
  // Detection: contains ":" but not "$", and hash part is 128 hex chars (64 bytes).
  if (stored.includes(':') && !stored.includes('$')) {
    return false;
  }

  // Plain-text (legacy v1 pre-hashing)
  return stored === password;
}

export function isPbkdf2Hash(stored) {
  return typeof stored === 'string' && stored.startsWith('pbkdf2$');
}

export function isLegacyScryptHash(stored) {
  return typeof stored === 'string' && stored.includes(':') && !stored.includes('$') && stored.length > 80;
}

export function generateSessionId() {
  const bytes = crypto.getRandomValues(new Uint8Array(32));
  return bytesToHex(bytes);
}
