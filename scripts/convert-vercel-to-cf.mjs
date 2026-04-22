#!/usr/bin/env node
// Converts vercel.json redirects + headers to CF Pages _redirects + _headers format.
// Writes to public/_redirects and public/_headers — they get copied to dist/ during Astro build.
// Re-run any time vercel.json changes: `node scripts/convert-vercel-to-cf.mjs`

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const vercel = JSON.parse(fs.readFileSync(path.join(ROOT, 'vercel.json'), 'utf8'));

// ---------- _redirects ----------
const lines = [];
lines.push('# Generated from vercel.json by scripts/convert-vercel-to-cf.mjs');
lines.push('# DO NOT EDIT MANUALLY — edit vercel.json and re-run the script.');
lines.push('');

function convertSourcePath(src) {
  // CF Pages _redirects source syntax:
  //   Named params: /:name (matches one segment)
  //   Wildcard: /* (captured as :splat in destination)
  //   NO regex support — [^/]+ and similar must be rewritten to *
  let s = src.replace(/:[a-zA-Z_]+\*/g, '*');
  // Strip Vercel regex char classes — replace `[^/]+` with `*` (prefix match)
  s = s.replace(/\[\^\/\]\+/g, '*');
  return s;
}

function convertDestPath(dst) {
  // Destination: keep :name named params, convert :name* to :splat
  return dst.replace(/:[a-zA-Z_]+\*/g, ':splat');
}

function expandRegexAlternatives(rule) {
  // Handle Vercel's `/:s(xxx|yyy|zzz)/` regex alternatives by expanding to multiple rules.
  const match = rule.source.match(/^(.*?):s\(([^)]+)\)(.*)$/);
  if (!match) return [rule];
  const [, prefix, alternatives, suffix] = match;
  return alternatives.split('|').map(alt => ({
    ...rule,
    source: `${prefix}${alt}${suffix}`,
  }));
}

function isDynamic(src) {
  // A rule is "dynamic" in CF terms if source contains * or :name params.
  return /\*|:[a-zA-Z]/.test(src);
}

const staticRules = [];
const dynamicRules = [];
const skippedHostRules = [];

for (const r of (vercel.redirects || [])) {
  // Host-based apex→www: CF Pages _redirects does NOT support absolute URLs.
  // Handle at the zone level via Cloudflare Bulk Redirects / Page Rules after DNS cutover.
  if (r.has && r.has.some(h => h.type === 'host' && h.value === 'fulfillmentmtp.com.ua')) {
    skippedHostRules.push(`${r.source} → ${r.destination}`);
    continue;
  }

  for (const expanded of expandRegexAlternatives(r)) {
    const src = convertSourcePath(expanded.source);
    const dst = convertDestPath(expanded.destination);
    const rule = `${src} ${dst} ${expanded.statusCode || 308}`;
    if (isDynamic(src)) dynamicRules.push(rule);
    else staticRules.push(rule);
  }
}

// Order: static rules first (no CF limit, matched faster), then dynamic rules (CF limit: 100).
lines.push('# --- static rules (exact path match) ---');
lines.push(...staticRules);
lines.push('');
lines.push('# --- dynamic rules (wildcards / named params, max 100) ---');
lines.push(...dynamicRules);

// CF Pages specific rules — appended AFTER all vercel.json rules.
// Must stay at the bottom: CF matches first-match-wins, and the catch-all
// below is the last-resort soft-404 killer.
lines.push('');
lines.push('# --- CF Pages specific (bottom of file — last match wins) ---');
// /sitemap.xml was returning HTML (hit the catch-all). Canonical sitemap is sitemap-index.xml.
lines.push('/sitemap.xml  /sitemap-index.xml  301');
// Real 404 for anything not matched above. Serves /404.html with status 404.
// Without this, unknown URLs fall through to SPA-style serving and get 200 + homepage HTML.
// Astro builds `dist/404.html` (flat file), so we reference it explicitly.
lines.push('/*  /404.html  404');

fs.writeFileSync(path.join(ROOT, 'public/_redirects'), lines.join('\n') + '\n', 'utf8');
console.log(`✓ public/_redirects written: ${staticRules.length} static + ${dynamicRules.length} dynamic`);
if (skippedHostRules.length) {
  console.log(`  ⚠ Skipped ${skippedHostRules.length} apex-host rule(s) — add them via CF Dashboard Bulk Redirects:`);
  skippedHostRules.forEach(r => console.log(`    ${r}`));
}
if (dynamicRules.length > 100) {
  console.log(`  ⚠ Dynamic rules (${dynamicRules.length}) exceed CF Pages limit of 100. Move oldest to CF Bulk Redirects.`);
}

// ---------- _headers ----------
const hlines = [];
hlines.push('# Generated from vercel.json by scripts/convert-vercel-to-cf.mjs');
hlines.push('# DO NOT EDIT MANUALLY — edit vercel.json and re-run the script.');
hlines.push('');

function convertHeaderPath(src) {
  // Vercel /(.*)  → CF Pages /*
  // Vercel /images/(.*) → /images/*
  return src.replace(/\/\(\.\*\)$/, '/*').replace(/\(\.\*\)/, '*');
}

for (const block of (vercel.headers || [])) {
  hlines.push(convertHeaderPath(block.source));
  for (const h of block.headers) {
    hlines.push(`  ${h.key}: ${h.value}`);
  }
  hlines.push('');
}

fs.writeFileSync(path.join(ROOT, 'public/_headers'), hlines.join('\n'), 'utf8');
console.log(`✓ public/_headers written (${(vercel.headers || []).length} blocks)`);
