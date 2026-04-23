// Dual-file Markdown integration for Astro.
// For every built HTML page, extracts <main data-md-root> content and writes
// a clean Markdown twin next to index.html (e.g. /ua/foo/index.md).
//
// SEO protection (decided in the 2026-04-22 council):
//   1. X-Robots-Tag: noindex, follow — set globally on *.md (emitted to dist/_headers)
//   2. Link: <HTML-URL>; rel="canonical" — per-page header injected into dist/_headers
//   3. NOT added to sitemap-index.xml — md files are alternate format, canonical HTML indexes
//   4. robots.txt does NOT block *.md — Googlebot needs to read to respect noindex
//
// Consumers:
//   - Humans copy-pasting URLs into ChatGPT / Claude UI
//   - Coding agents (Cursor, Claude Code) when user references a page
//   - LLM training/search bots that prefer Accept: text/markdown alternates
//
// Precedent: docs.anthropic.com, vercel.com/docs, stripe.com/docs, all Mintlify sites.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseHTML } from 'linkedom';
import TurndownService from 'turndown';
import * as turndownPluginGfm from 'turndown-plugin-gfm';

const SKIP_ROUTES = [
  '/admin/', '/thanks/', '/api/', '/files/', '/schedule/', '/new/',
  '/ua/thanks/', '/ru/thanks/', '/en/thanks/',
  '/404.html',
];

function shouldSkip(route) {
  return SKIP_ROUTES.some(p => route.includes(p));
}

function walkHtml(dir, baseDir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name.startsWith('_') || entry.name === 'css' || entry.name === 'js' ||
          entry.name === 'images' || entry.name === 'fonts' || entry.name === 'admin') continue;
      walkHtml(full, baseDir, out);
    } else if (entry.name === 'index.html') {
      out.push(full);
    }
  }
  return out;
}

function routeFromHtmlPath(htmlPath, distDir) {
  const rel = htmlPath.slice(distDir.length).replace(/\\/g, '/'); // windows-safe
  const dir = rel.replace(/\/index\.html$/, '/');
  return dir || '/';
}

function buildTurndown() {
  const td = new TurndownService({
    headingStyle: 'atx',
    bulletListMarker: '-',
    codeBlockStyle: 'fenced',
    emDelimiter: '_',
    strongDelimiter: '**',
    linkStyle: 'inlined',
    hr: '---',
  });
  td.use(turndownPluginGfm.gfm);

  // Custom rule: <details><summary> → ### {summary}\n{body}
  td.addRule('detailsSummary', {
    filter: 'details',
    replacement: (content, node) => {
      const summary = node.querySelector('summary');
      const heading = summary ? summary.textContent.trim() : 'Details';
      if (summary) summary.remove();
      const body = node.textContent.trim();
      return `\n\n### ${heading}\n\n${body}\n\n`;
    },
  });

  td.remove(['script', 'style', 'noscript', 'iframe', 'svg']);

  return td;
}

function extractMain(document) {
  const main = document.querySelector('[data-md-root]');
  if (!main) return null;

  const title = main.getAttribute('data-md-title') || '';
  const description = main.getAttribute('data-md-description') || '';
  const lang = main.getAttribute('data-md-lang') || 'uk';
  const canonical = main.getAttribute('data-md-canonical') || '';

  main.querySelectorAll('[data-md-skip]').forEach(n => n.remove());
  main.querySelectorAll('form').forEach(n => n.remove());
  main.querySelectorAll('[id*="Popup"],[id*="Modal"]').forEach(n => n.remove());
  main.querySelectorAll('.sticky-cta, .hero-tg, .hero-guar, .hero-form, .final-form, .final-cta').forEach(n => n.remove());
  main.querySelectorAll('svg').forEach(n => n.remove());

  return { main, title, description, lang, canonical };
}

function buildFrontmatter({ title, description, lang, canonical }) {
  const lines = ['---'];
  if (title) lines.push(`title: ${JSON.stringify(title)}`);
  if (description) lines.push(`description: ${JSON.stringify(description)}`);
  if (lang) lines.push(`lang: ${lang}`);
  if (canonical) lines.push(`canonical: ${canonical}`);
  lines.push(`generated: ${new Date().toISOString()}`);
  lines.push('---', '');
  return lines.join('\n');
}

function cleanMarkdown(md) {
  md = md.replace(/\n{3,}/g, '\n\n');
  md = md.trim();
  return md + '\n';
}

function countWords(text) {
  return (text.match(/\S+/g) || []).length;
}

export default function dualMd() {
  return {
    name: 'dual-md',
    hooks: {
      'astro:build:done': async ({ dir, logger }) => {
        const distDir = fileURLToPath(dir).replace(/[\\/]$/, '');
        const td = buildTurndown();

        const htmlFiles = walkHtml(distDir, distDir);

        let written = 0;
        let skipped = 0;
        let errors = 0;
        let thin = 0;
        const canonicalHeaders = [];

        for (const htmlPath of htmlFiles) {
          const route = routeFromHtmlPath(htmlPath, distDir);
          if (shouldSkip(route)) { skipped++; continue; }

          try {
            const html = fs.readFileSync(htmlPath, 'utf8');
            const { document } = parseHTML(html);
            const extracted = extractMain(document);
            if (!extracted) { skipped++; continue; }

            const { main, title, description, lang, canonical } = extracted;
            const body = td.turndown(main.innerHTML);
            const words = countWords(body);
            if (words < 100) {
              logger.warn(`dual-md: thin page (${words} words) at ${route}`);
              thin++;
            }

            const frontmatter = buildFrontmatter({ title, description, lang, canonical });
            const out = frontmatter + cleanMarkdown(body);

            const mdPath = path.join(path.dirname(htmlPath), 'index.md');
            fs.writeFileSync(mdPath, out, 'utf8');
            written++;

            if (canonical) {
              const mdRoute = route.endsWith('/') ? route + 'index.md' : route + '/index.md';
              canonicalHeaders.push({ mdRoute, canonical });
            }
          } catch (err) {
            errors++;
            logger.warn(`dual-md: failed to process ${route}: ${err.message}`);
          }
        }

        // Append noindex + canonical Link headers to dist/_headers.
        // If _headers missing (shouldn't happen — public/_headers is authoritative),
        // create a minimal one so the MD files still get noindex protection.
        const headersPath = path.join(distDir, '_headers');
        const append = [];
        append.push('');
        append.push('# --- dual-md: generated by integrations/dual-md.mjs ---');
        append.push('# Global noindex for all .md twins (Googlebot must be able to read to respect).');
        append.push('/*.md');
        append.push('  X-Robots-Tag: noindex, follow');
        append.push('  Content-Type: text/markdown; charset=utf-8');
        append.push('  Access-Control-Allow-Origin: *');
        append.push('  Cache-Control: public, max-age=3600');
        append.push('');
        append.push('# Per-page canonical pointers (HTML version is authoritative).');
        for (const { mdRoute, canonical } of canonicalHeaders) {
          append.push(mdRoute);
          append.push(`  Link: <${canonical}>; rel="canonical"`);
          append.push('');
        }

        const existing = fs.existsSync(headersPath) ? fs.readFileSync(headersPath, 'utf8') : '';
        fs.writeFileSync(headersPath, existing + append.join('\n'), 'utf8');

        logger.info(`dual-md: ${written} written, ${skipped} skipped, ${errors} errors, ${thin} thin (<100 words), ${canonicalHeaders.length} canonical headers queued`);
      },
    },
  };
}
