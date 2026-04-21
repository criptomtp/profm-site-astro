import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.fulfillmentmtp.com.ua',
  trailingSlash: 'always',
  build: { format: 'directory' },
  integrations: [
    sitemap({
      filter: (page) =>
        !page.includes('/admin/') &&
        !page.includes('/thanks/') &&
        !page.includes('/schedule/') &&
        !page.includes('/new/') &&
        !page.includes('/files/') &&
        !page.includes('/blog/tpost/') &&
        !page.includes('/ua/blog/tpost/') &&
        !page.includes('/ru/blog/tpost/') &&
        !page.includes('/en/blog/tpost/'),
      lastmod: new Date(),
    }),
  ],
});
