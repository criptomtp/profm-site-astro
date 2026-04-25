// image-sitemap integration
//
// Builds /sitemap-images.xml from dist/**/*.html using Google's image-sitemap
// namespace (https://www.google.com/schemas/sitemap-image/1.1). Helps Google
// Images discover warehouse photos / hero assets faster.
//
// Also appends the image sitemap reference to /sitemap-index.xml so crawlers
// discover it via the sitemap index.
//
// Must run AFTER @astrojs/sitemap — we amend the sitemap-index.xml it already
// produced.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const SITE = 'https://www.fulfillmentmtp.com.ua';

const SKIP_DIRS = [
  '/admin/', '/thanks/', '/schedule/', '/new/', '/files/', '/api/',
  '/ua/thanks/', '/en/thanks/',
];

function escapeXml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

function walkHtml(dir, out) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const abs = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walkHtml(abs, out);
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      out.push(abs);
    }
  }
}

function urlFromHtmlPath(distDir, htmlPath) {
  let rel = htmlPath.slice(distDir.length).replace(/\\/g, '/');
  if (rel.endsWith('/index.html')) rel = rel.slice(0, -'index.html'.length);
  else if (rel.endsWith('.html')) rel = rel.slice(0, -'.html'.length) + '/';
  if (!rel.startsWith('/')) rel = '/' + rel;
  return SITE + rel;
}

// Extract <img src="...">. Supports double or single quotes. Ignores data-URI
// and external (non-site) images. Rewrites relative /images/foo.jpg into
// absolute URLs. Also skips images inside <picture> <source> for now — the
// <img> fallback is enough for Google Images.
function extractImages(html) {
  const imgs = new Set();
  const imgRe = /<img\b[^>]*?\bsrc\s*=\s*(?:"([^"]+)"|'([^']+)')[^>]*>/gi;
  let m;
  while ((m = imgRe.exec(html))) {
    const src = (m[1] || m[2] || '').trim();
    if (!src) continue;
    if (src.startsWith('data:')) continue;
    if (src.startsWith('//')) continue;
    let abs;
    if (src.startsWith('http://') || src.startsWith('https://')) {
      if (!src.startsWith(SITE)) continue;
      abs = src;
    } else if (src.startsWith('/')) {
      abs = SITE + src;
    } else {
      continue;
    }
    imgs.add(abs);
  }
  return [...imgs];
}

function shouldSkip(htmlPath, distDir) {
  const rel = htmlPath.slice(distDir.length).replace(/\\/g, '/');
  return SKIP_DIRS.some(d => rel.startsWith(d));
}

export default function imageSitemap() {
  return {
    name: 'image-sitemap',
    hooks: {
      'astro:build:done': async ({ dir, logger }) => {
        const distDir = fileURLToPath(dir).replace(/[\\/]$/, '');
        const htmlFiles = [];
        walkHtml(distDir, htmlFiles);

        const urlEntries = [];
        let totalImages = 0;

        for (const htmlPath of htmlFiles) {
          if (shouldSkip(htmlPath, distDir)) continue;
          const pageUrl = urlFromHtmlPath(distDir, htmlPath);
          const html = fs.readFileSync(htmlPath, 'utf8');
          const images = extractImages(html);
          if (images.length === 0) continue;
          totalImages += images.length;
          const imageTags = images.map(u =>
            `    <image:image><image:loc>${escapeXml(u)}</image:loc></image:image>`
          ).join('\n');
          urlEntries.push(
            `  <url>\n    <loc>${escapeXml(pageUrl)}</loc>\n${imageTags}\n  </url>`
          );
        }

        const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
${urlEntries.join('\n')}
</urlset>
`;

        const outPath = path.join(distDir, 'sitemap-images.xml');
        fs.writeFileSync(outPath, xml, 'utf8');

        // Rebuild sitemap-index.xml with our image sitemap appended AND a
        // <lastmod> for every child sitemap entry. The original astrojs/sitemap
        // output omits <lastmod>, which means Google can't tell which child
        // sitemap actually changed between crawls. We use each child file's
        // mtime as the authoritative lastmod (sitemaps.org spec: "Date the file
        // at <loc> changed").
        const indexPath = path.join(distDir, 'sitemap-index.xml');
        if (fs.existsSync(indexPath)) {
          const indexXml = fs.readFileSync(indexPath, 'utf8');
          // Extract every existing <loc> inside <sitemap>...</sitemap>
          const locRe = /<sitemap[^>]*>\s*<loc>([^<]+)<\/loc>/g;
          const childLocs = [];
          let lm;
          while ((lm = locRe.exec(indexXml)) !== null) childLocs.push(lm[1].trim());

          const imageSitemapUrl = `${SITE}/sitemap-images.xml`;
          if (!childLocs.includes(imageSitemapUrl)) childLocs.push(imageSitemapUrl);

          const entries = childLocs.map(loc => {
            let lastmod = new Date().toISOString();
            if (loc.startsWith(SITE + '/')) {
              const rel = loc.slice(SITE.length + 1);
              const filePath = path.join(distDir, rel);
              if (fs.existsSync(filePath)) {
                lastmod = new Date(fs.statSync(filePath).mtime).toISOString();
              }
            }
            return `  <sitemap>\n    <loc>${escapeXml(loc)}</loc>\n    <lastmod>${lastmod}</lastmod>\n  </sitemap>`;
          });

          const newIndexXml = `<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${entries.join('\n')}\n</sitemapindex>\n`;
          fs.writeFileSync(indexPath, newIndexXml, 'utf8');
        }

        const headersPath = path.join(distDir, '_headers');
        const headersAppend = [
          '',
          '# --- sitemap-images.xml ---',
          '/sitemap-images.xml',
          '  Content-Type: application/xml; charset=utf-8',
          '  Cache-Control: public, max-age=3600',
          '',
        ];
        const existing = fs.existsSync(headersPath) ? fs.readFileSync(headersPath, 'utf8') : '';
        fs.writeFileSync(headersPath, existing + headersAppend.join('\n'), 'utf8');

        logger.info(`image-sitemap: ${urlEntries.length} pages, ${totalImages} images indexed`);
      },
    },
  };
}
