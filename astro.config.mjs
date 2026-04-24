import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import dualMd from './integrations/dual-md.mjs';
import llmsFull from './integrations/llms-full.mjs';
import imageSitemap from './integrations/image-sitemap.mjs';
import { buildLastmodMap } from './integrations/lastmod-map.mjs';

const lastmodMap = buildLastmodMap();
const buildDate = new Date();

export default defineConfig({
  site: 'https://www.fulfillmentmtp.com.ua',
  trailingSlash: 'always',
  build: { format: 'directory' },
  integrations: [
    dualMd(),
    llmsFull(),
    sitemap({
      filter: (page) =>
        !page.includes('/admin/') &&
        !page.includes('/thanks/') &&
        !page.includes('/schedule/') &&
        !page.includes('/new/') &&
        !page.includes('/files/'),
      serialize(item) {
        const iso = lastmodMap.get(item.url);
        item.lastmod = iso || buildDate.toISOString();

        const url = item.url;
        if (/^https:\/\/www\.fulfillmentmtp\.com\.ua\/(ru\/|en\/)?$/.test(url)) {
          item.changefreq = 'daily';
          item.priority = 1.0;
        } else if (/\/shcho-take-fulfilment\/|\/chto-takoe-fulfilment\/|\/what-is-fulfillment\/$/.test(url)) {
          item.changefreq = 'weekly';
          item.priority = 0.9;
        } else if (/\/(tsiny|tsenu|prices|calculator)\/$/.test(url)) {
          item.changefreq = 'weekly';
          item.priority = 0.9;
        } else if (/\/(3pl-logistyka|skladski-poslugy|services|paletne-zberigannya|fulfilment-|pallet-storage|warehouse-services|heavy-goods)/.test(url)) {
          item.changefreq = 'monthly';
          item.priority = 0.8;
        } else if (/\/blog\/$/.test(url)) {
          item.changefreq = 'weekly';
          item.priority = 0.7;
        } else if (/\/blog\//.test(url)) {
          item.changefreq = 'monthly';
          item.priority = 0.6;
        } else if (/\/(faq|guide|glosariy|glossariy|glossary|about|recalls)\/$/.test(url)) {
          item.changefreq = 'monthly';
          item.priority = 0.7;
        } else if (/\/(privacy|terms)\/$/.test(url)) {
          item.changefreq = 'yearly';
          item.priority = 0.3;
        } else {
          item.changefreq = 'monthly';
          item.priority = 0.5;
        }
        return item;
      },
    }),
    imageSitemap(),
  ],
  vite: {
    build: {
      rollupOptions: {
        output: {
          assetFileNames: (assetInfo) => {
            const name = assetInfo.names?.[0] || assetInfo.name || '';
            if (name.endsWith('.css')) {
              const src = typeof assetInfo.source === 'string'
                ? assetInfo.source
                : assetInfo.source instanceof Uint8Array
                  ? Buffer.from(assetInfo.source).toString('utf8')
                  : '';
              if (src.includes('.hdr-logo-mtp') || src.includes('.hdr-spacer')) {
                return '_astro/header.[hash][extname]';
              }
              if (src.includes('.footer-grid') || src.includes('.footer-bottom')) {
                return '_astro/footer.[hash][extname]';
              }
            }
            return '_astro/[name].[hash][extname]';
          },
        },
      },
    },
  },
});
