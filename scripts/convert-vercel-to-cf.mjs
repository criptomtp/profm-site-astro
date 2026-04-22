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
  // In CF Pages _redirects source:
  //   Named params: /:name (one segment)
  //   Wildcard: /* (captured as :splat in destination)
  // Vercel :name* (catch-all) → CF * in source
  return src.replace(/:[a-zA-Z_]+\*/g, '*');
}

function convertDestPath(dst) {
  // Destination: keep :name named params, convert :name* to :splat
  return dst.replace(/:[a-zA-Z_]+\*/g, ':splat');
}

function expandRegexAlternatives(rule) {
  // Handle Vercel's `/:s(xxx|yyy|zzz)/` regex alternatives by expanding to multiple rules.
  // Match pattern like `/prefix/:s(a|b|c)/suffix` -> emit one rule per alternative.
  const match = rule.source.match(/^(.*?):s\(([^)]+)\)(.*)$/);
  if (!match) return [rule];
  const [, prefix, alternatives, suffix] = match;
  return alternatives.split('|').map(alt => ({
    ...rule,
    source: `${prefix}${alt}${suffix}`,
  }));
}

const redirects = [];
for (const r of (vercel.redirects || [])) {
  // Host-based rule: non-www → www
  if (r.has && r.has.some(h => h.type === 'host' && h.value === 'fulfillmentmtp.com.ua')) {
    // CF Pages external redirect: source = https://host/*  destination uses :splat
    const src = convertSourcePath(r.source).replace(/^\/$/, '/*');
    const dst = convertDestPath(r.destination || '');
    redirects.push(`https://fulfillmentmtp.com.ua${src} ${dst} ${r.statusCode || 308}`);
    continue;
  }

  for (const expanded of expandRegexAlternatives(r)) {
    const src = convertSourcePath(expanded.source);
    const dst = convertDestPath(expanded.destination);
    redirects.push(`${src} ${dst} ${expanded.statusCode || 308}`);
  }
}

lines.push(...redirects);
fs.writeFileSync(path.join(ROOT, 'public/_redirects'), lines.join('\n') + '\n', 'utf8');
console.log(`✓ public/_redirects written (${redirects.length} rules)`);

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
