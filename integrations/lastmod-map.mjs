// Build a Map<url, ISO-date> of per-page lastmod using git log.
// Used by @astrojs/sitemap `serialize` to emit accurate lastmod values
// instead of a single build-time timestamp for every URL.
//
// Fallback: if git isn't available (shallow clone, new file, CF Pages
// environment quirk), we fall back to the build date so lastmod is
// never missing.

import { execSync } from 'node:child_process';
import { readdirSync, statSync } from 'node:fs';
import { join, relative, sep } from 'node:path';

const PAGES_DIR = 'src/pages';
const SITE = 'https://www.fulfillmentmtp.com.ua';

function walk(dir) {
  const out = [];
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    const st = statSync(full);
    if (st.isDirectory()) out.push(...walk(full));
    else out.push(full);
  }
  return out;
}

function fileToUrl(absFile) {
  let rel = relative(PAGES_DIR, absFile).split(sep).join('/');
  if (!/\.(astro|md|mdx|html)$/i.test(rel)) return null;
  rel = rel.replace(/\.(astro|md|mdx|html)$/i, '');
  if (rel === 'index') return `${SITE}/`;
  if (rel.endsWith('/index')) rel = rel.slice(0, -'/index'.length);
  return `${SITE}/${rel}/`;
}

function gitIso(file) {
  try {
    const out = execSync(`git log -1 --format=%cI -- "${file}"`, {
      stdio: ['ignore', 'pipe', 'ignore'],
    })
      .toString()
      .trim();
    return out || null;
  } catch {
    return null;
  }
}

let cached = null;

export function buildLastmodMap() {
  if (cached) return cached;
  const map = new Map();
  const buildDate = new Date().toISOString();
  try {
    const files = walk(PAGES_DIR);
    for (const f of files) {
      const url = fileToUrl(f);
      if (!url) continue;
      const iso = gitIso(f) || buildDate;
      // If multiple files map to same URL (shouldn't, but safety),
      // keep the newest.
      const prev = map.get(url);
      if (!prev || new Date(iso) > new Date(prev)) map.set(url, iso);
    }
  } catch (e) {
    console.warn('[lastmod-map] failed to scan pages:', e.message);
  }
  cached = map;
  console.log(`[lastmod-map] built ${map.size} entries`);
  return cached;
}
