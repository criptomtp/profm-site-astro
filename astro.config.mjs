import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://fulfillmentmtp.com.ua',
  trailingSlash: 'always',
  build: { format: 'directory' },
});
