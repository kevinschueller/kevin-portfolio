// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.kevinschueller.com',
  integrations: [sitemap()],
  build: {
    format: 'directory',
  },
});
