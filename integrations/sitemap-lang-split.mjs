// sitemap-lang-split integration (L3)
//
// Splits @astrojs/sitemap's single dist/sitemap-0.xml into per-language files:
//   sitemap-uk.xml — UA root pages + legacy /ua/* pages
//   sitemap-ru.xml — /ru/* pages
//   sitemap-en.xml — /en/* pages
//
// Why: GSC Coverage report aggregates per submitted sitemap. Splitting by
// language lets us see UA vs RU vs EN indexability independently and submit
// one sitemap per "International Targeting" language slot.
//
// Pipeline order: must run AFTER @astrojs/sitemap (which produces sitemap-0)
// and BEFORE image-sitemap (which rebuilds sitemap-index.xml with lastmod —
// it will pick up the 3 new lang sitemaps automatically).

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const SITE = 'https://www.fulfillmentmtp.com.ua';

function escapeXml(s) {
  return String(s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&apos;');
}

function pickLang(absUrl) {
  const rel = absUrl.replace(SITE, '').replace(/^\//, '');
  if (rel.startsWith('ru/') || rel === 'ru/') return 'ru';
  if (rel.startsWith('en/') || rel === 'en/') return 'en';
  // Everything else (root /, /ua/* legacy, /blog/*, /api-docs/*) → uk
  return 'uk';
}

export default function sitemapLangSplit() {
  return {
    name: 'sitemap-lang-split',
    hooks: {
      'astro:build:done': async ({ dir, logger }) => {
        const distDir = fileURLToPath(dir).replace(/[\\/]$/, '');
        const sourcePath = path.join(distDir, 'sitemap-0.xml');
        if (!fs.existsSync(sourcePath)) {
          logger.warn('sitemap-lang-split: sitemap-0.xml not found, skipping');
          return;
        }
        const xml = fs.readFileSync(sourcePath, 'utf8');

        // Preserve original urlset opening tag (with all namespace attrs from
        // @astrojs/sitemap — image, video, news, xhtml — so consumers stay happy).
        const urlsetOpenMatch = xml.match(/<urlset[^>]*>/);
        if (!urlsetOpenMatch) {
          logger.warn('sitemap-lang-split: malformed sitemap-0.xml, skipping');
          return;
        }
        const urlsetOpen = urlsetOpenMatch[0];

        // Each <url>...</url> block stays intact (preserves <lastmod>, <changefreq>,
        // <priority>, <xhtml:link> hreflang siblings — all of which we don't want
        // to lose during the split).
        const blocks = xml.match(/<url>[\s\S]*?<\/url>/g) || [];
        const buckets = { uk: [], ru: [], en: [] };
        for (const blk of blocks) {
          const locM = blk.match(/<loc>([^<]+)<\/loc>/);
          if (!locM) continue;
          buckets[pickLang(locM[1].trim())].push(blk);
        }

        const outNames = { uk: 'sitemap-uk.xml', ru: 'sitemap-ru.xml', en: 'sitemap-en.xml' };
        const counts = { uk: 0, ru: 0, en: 0 };
        for (const [lang, name] of Object.entries(outNames)) {
          const out = `<?xml version="1.0" encoding="UTF-8"?>\n${urlsetOpen}\n${buckets[lang].join('\n')}\n</urlset>\n`;
          fs.writeFileSync(path.join(distDir, name), out, 'utf8');
          counts[lang] = buckets[lang].length;
        }

        // Drop the now-redundant aggregate
        fs.unlinkSync(sourcePath);

        // Rewrite sitemap-index.xml: drop sitemap-0 entry, insert 3 new ones.
        // image-sitemap (next in pipeline) will rebuild this again with proper
        // <lastmod> values — we just need the <loc>s present so it picks them up.
        const indexPath = path.join(distDir, 'sitemap-index.xml');
        if (fs.existsSync(indexPath)) {
          const indexXml = fs.readFileSync(indexPath, 'utf8');
          const childLocs = [...indexXml.matchAll(/<sitemap[^>]*>\s*<loc>([^<]+)<\/loc>/g)]
            .map(m => m[1].trim())
            .filter(loc => !loc.endsWith('/sitemap-0.xml'));
          for (const name of Object.values(outNames)) {
            const u = `${SITE}/${name}`;
            if (!childLocs.includes(u)) childLocs.push(u);
          }
          const entries = childLocs.map(loc =>
            `  <sitemap>\n    <loc>${escapeXml(loc)}</loc>\n  </sitemap>`
          );
          const newIdx = `<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${entries.join('\n')}\n</sitemapindex>\n`;
          fs.writeFileSync(indexPath, newIdx, 'utf8');
        }

        logger.info(`sitemap-lang-split: ${counts.uk} uk · ${counts.ru} ru · ${counts.en} en (sitemap-0.xml removed)`);
      },
    },
  };
}
