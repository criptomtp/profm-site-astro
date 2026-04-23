// llms-full.txt integration.
//
// Concatenates a curated set of dist/**/index.md files (produced by the
// dual-md integration) into a single /llms-full.txt served at the site
// root. Companion to /llms.txt:
//   - /llms.txt        — short navigation index (human-curated, in public/)
//   - /llms-full.txt   — full text of priority pages (generated here)
//
// Consumers: retrieval-augmented agents (ChatGPT Deep Research, Perplexity
// AI, Claude, Cursor) that accept a single-URL content dump and prefer to
// "ingest everything at once" rather than crawl page-by-page.
//
// Must be registered AFTER dualMd() in astro.config.mjs so the .md files
// already exist when this runs.
//
// Precedent: docs.anthropic.com/llms-full.txt, vercel.com/llms-full.txt.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const SITE = 'https://www.fulfillmentmtp.com.ua';

// Curated list — each entry is a public URL path relative to SITE.
// The matching file lives at dist<path>index.md. Order = reading order
// for the agent (pillars first, then services, industries, geo, blog).
const PATHS = [
  // Pillars — "what is fulfillment"
  '/ua/shcho-take-fulfilment/',
  '/ru/chto-takoe-fulfilment/',
  '/en/what-is-fulfillment/',

  // About / trust
  '/ua/about/',
  '/ru/about/',
  '/en/about/',

  // Services hub
  '/ua/services/',
  '/ru/services/',
  '/en/services/',

  // Core services
  '/ua/3pl-logistyka/',
  '/ru/3pl-logistika/',
  '/en/3pl-logistics/',
  '/ua/skladski-poslugy/',
  '/ru/skladskie-uslugi/',
  '/en/warehouse-services/',
  '/ua/paletne-zberigannya/',
  '/ru/paletnoe-khranenie/',
  '/en/pallet-storage/',

  // Industry verticals (UA primary — RU/EN siblings follow naming)
  '/ua/fulfilment-dlya-internet-magazynu/',
  '/ru/fulfilment-dlya-internet-magazynu/',
  '/ua/fulfilment-dlya-marketpleysiv/',
  '/ru/fulfilment-dlya-marketpleysov/',
  '/ua/fulfilment-dlya-kosmetyky/',
  '/ru/fulfilment-dlya-kosmetiki/',
  '/ua/fulfilment-dlya-maloho-biznesu/',
  '/ru/fulfilment-dlya-malogo-biznesa/',
  '/ua/fulfilment-vazhkykh-tovariv/',
  '/ru/fulfilment-vazhkykh-tovariv/',
  '/en/heavy-goods/',

  // Geo landing
  '/ua/fulfilment-kyiv/',
  '/ru/fulfilment-kiev/',
  '/en/fulfillment-kyiv/',
  '/ua/fulfilment-ukraina/',
  '/ru/fulfilment-ukraina/',
  '/en/fulfillment-ukraine/',

  // Pricing & tools
  '/ua/tsiny/',
  '/ru/tsenu/',
  '/en/prices/',
  '/ua/calculator/',
  '/ru/calculator/',
  '/en/calculator/',
  '/ua/guide/',
  '/ru/guide/',
  '/en/guide/',
  '/ua/faq/',
  '/ru/faq/',
  '/en/faq/',
  '/glosariy/',
  '/ru/glossariy/',
  '/en/glossary/',

  // Top pillar-linked blog posts
  '/ua/blog/scho-take-fulfilment/',
  '/blog/chto-takoe-fulfilment/',
  '/en/blog/post/what-is-fulfillment-complete-guide/',
  '/ua/blog/top-fulfilment-operatoriv-2026/',
  '/blog/top-fulfilment-operatorov-2026/',
  '/en/blog/post/top-fulfillment-operators-ukraine-2026/',
  '/ua/blog/top-marketpleysiv-ukrayiny/',
  '/blog/top-marketplejsov-ukrainy/',
  '/en/blog/post/top-marketplaces-ukraine/',
];

function stripFrontmatter(md) {
  // Remove leading --- ... --- block if present.
  if (!md.startsWith('---')) return md;
  const end = md.indexOf('\n---', 3);
  if (end === -1) return md;
  return md.slice(end + 4).replace(/^\n+/, '');
}

function readMd(distDir, urlPath) {
  const clean = urlPath.endsWith('/') ? urlPath : urlPath + '/';
  const abs = path.join(distDir, clean, 'index.md');
  if (!fs.existsSync(abs)) return null;
  return fs.readFileSync(abs, 'utf8');
}

export default function llmsFull() {
  return {
    name: 'llms-full',
    hooks: {
      'astro:build:done': async ({ dir, logger }) => {
        const distDir = fileURLToPath(dir).replace(/[\\/]$/, '');
        const parts = [];
        const built = new Date().toISOString();

        parts.push('# MTP Group Fulfillment — Full Knowledge Base');
        parts.push('');
        parts.push(
          '> Full text of priority pages in Ukrainian, Russian, and English. ' +
          'Generated from the canonical HTML content on ' + built + '. ' +
          'For the short navigation index see ' + SITE + '/llms.txt. ' +
          'For individual pages, fetch <URL>.md (e.g. ' + SITE + '/ua/services/index.md).'
        );
        parts.push('');
        parts.push('## About');
        parts.push(
          '3PL fulfillment operator in Ukraine. 3,900 m² warehouse near Kyiv, ' +
          '150+ active e-commerce clients, 60,000+ shipments per month. ' +
          'Founded 2014 by Mykola Liashchuk. ' +
          'Contact: +38 (050) 144-46-45, mtpgrouppromo@gmail.com, https://t.me/nikolay_mtp.'
        );
        parts.push('');

        let written = 0;
        let missing = 0;
        const missingList = [];

        for (const p of PATHS) {
          const md = readMd(distDir, p);
          if (!md) {
            missing++;
            missingList.push(p);
            continue;
          }
          const body = stripFrontmatter(md).trim();
          if (!body) continue;
          parts.push('\n<!-- ============================================================ -->');
          parts.push(`<!-- SOURCE: ${SITE}${p} -->`);
          parts.push('<!-- ============================================================ -->\n');
          parts.push(body);
          parts.push('');
          written++;
        }

        const outPath = path.join(distDir, 'llms-full.txt');
        fs.writeFileSync(outPath, parts.join('\n'), 'utf8');

        // Append _headers entry for /llms-full.txt
        const headersPath = path.join(distDir, '_headers');
        const headersAppend = [
          '',
          '# --- llms-full.txt ---',
          '/llms-full.txt',
          '  Content-Type: text/plain; charset=utf-8',
          '  X-Robots-Tag: noindex, follow',
          '  Access-Control-Allow-Origin: *',
          '  Cache-Control: public, max-age=3600',
          '',
        ];
        const existing = fs.existsSync(headersPath) ? fs.readFileSync(headersPath, 'utf8') : '';
        fs.writeFileSync(headersPath, existing + headersAppend.join('\n'), 'utf8');

        const sizeKb = Math.round(fs.statSync(outPath).size / 1024);
        logger.info(`llms-full: ${written} pages concatenated, ${missing} missing, ${sizeKb} KB`);
        if (missing > 0) {
          logger.warn(`llms-full: missing md for: ${missingList.join(', ')}`);
        }
      },
    },
  };
}
