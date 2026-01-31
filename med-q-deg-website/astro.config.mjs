import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: 'https://your-username.github.io',
  base: '/',
  integrations: [
    react(),
    tailwind({
      applyBaseStyles: false,
    }),
  ],
  build: {
    format: 'file',
    assets: 'assets',
  },
  prefetch: {
    defaultStrategy: 'viewport',
    prefetchAll: true,
  },
  compressHTML: true,
});
