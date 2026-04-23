import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import dualMd from './integrations/dual-md.mjs';
import llmsFull from './integrations/llms-full.mjs';
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
        return item;
      },
    }),
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
