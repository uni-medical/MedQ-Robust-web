# MedQ-Deg Website

A modern, interactive website showcasing the MedQ-Deg benchmark for medical image degradation recognition.

## 🚀 Features

- **Interactive Benchmark Explorer**: Browse all 28 degradation types across 6 categories
- **Visual Examples Gallery**: View real-world examples with image viewer
- **Performance Visualizations**: D3.js-powered charts showing benchmark results
- **Responsive Design**: Optimized for all screen sizes
- **Dark Theme**: Professional glassmorphism design
- **Fast Performance**: Built with Astro for optimal loading speeds

## 📦 Tech Stack

- **Framework**: [Astro](https://astro.build/) - Static site generation
- **UI Library**: [React](https://react.dev/) - Interactive components
- **Styling**: [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS
- **Animations**: [Framer Motion](https://www.framer.com/motion/) - Smooth transitions
- **Data Viz**: [D3.js](https://d3js.org/) - Charts and visualizations
- **Deployment**: GitHub Pages

## 🛠️ Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📁 Project Structure

```
src/
├── components/
│   ├── common/           # Header, Footer, SEO
│   └── visualization/    # Charts, Gallery, Interactive components
├── data/
│   └── config.ts         # Site configuration and data
├── layouts/
│   └── Layout.astro      # Main layout template
├── pages/
│   ├── index.astro       # Homepage
│   ├── benchmark.astro   # Degradation types catalog
│   ├── examples.astro    # Visual examples gallery
│   └── results.astro     # Performance visualizations
└── styles/
    └── global.css        # Global styles and utilities
```

## 🎨 Customization

### Update Site Content

All configurable content is centralized in `src/data/config.ts`:

```typescript
export const SITE_CONFIG = {
  title: 'MedQ-Deg',
  subtitle: '...',
  links: {
    paper: '#',     // Update with your paper URL
    github: '#',    // Update with your GitHub repo
    dataset: '#',   // Update with your dataset URL
  },
  // ...
};
```

### Replace Placeholder Images

Images are located in:
- `public/images/` - General images, logos, OG images
- `public/data/` - Example degradation images

To replace placeholders:
1. Add your images to the appropriate directory
2. Update image paths in the page components
3. Update the `ImageGallery` component to load your images

### Update Performance Data

Replace sample data in visualization components:
- `src/components/visualization/PerformanceChart.tsx` - Bar chart data
- `src/components/visualization/ConfusionMatrix.tsx` - Confusion matrix values
- `src/components/visualization/TSNEVisualization.tsx` - t-SNE coordinates

## 🚀 Deployment

### GitHub Pages

1. **Configure Repository**:
   - Go to Settings → Pages
   - Source: GitHub Actions

2. **Update Site URL**:
   Edit `astro.config.mjs`:
   ```javascript
   export default defineConfig({
     site: 'https://your-username.github.io',
     base: '/your-repo-name/',
   });
   ```

3. **Deploy**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

The GitHub Action will automatically build and deploy your site.

### Custom Domain (Optional)

1. Add a `CNAME` file to `public/`:
   ```
   your-domain.com
   ```

2. Configure DNS with your domain provider:
   - A record: `185.199.108.153`
   - A record: `185.199.109.153`
   - A record: `185.199.110.153`
   - A record: `185.199.111.153`

3. Update `astro.config.mjs`:
   ```javascript
   site: 'https://your-domain.com',
   base: '/',
   ```

## 📊 Data Integration

### Loading External Data

Create a data loader in `src/utils/dataLoader.ts`:

```typescript
export async function loadDegradationExamples() {
  // Fetch from API or load from JSON
  const response = await fetch('/data/examples.json');
  return response.json();
}
```

Use in pages:
```astro
---
import { loadDegradationExamples } from '@utils/dataLoader';
const examples = await loadDegradationExamples();
---
```

## 🎯 Quick Data Replacement Guide

### 1. Update Links
`src/data/config.ts` → Update `SITE_CONFIG.links`

### 2. Add Images
Place images in `public/images/degradations/`

### 3. Update Charts
Replace sample data in `src/components/visualization/*.tsx`

### 4. Deploy
```bash
git add .
git commit -m "Update content"
git push
```

## 🐛 Troubleshooting

**Build fails with TypeScript errors:**
```bash
npm run build -- --no-check
```

**Images not loading:**
- Check image paths start with `/` (e.g., `/images/logo.png`)
- Verify images are in the `public/` directory

**GitHub Pages shows 404:**
- Ensure `base` in `astro.config.mjs` matches your repo name
- Check GitHub Actions logs for build errors

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

Built with modern web technologies for optimal performance and user experience.

---

**需要帮助？** 查看 [Astro 文档](https://docs.astro.build) 或 [提交 Issue](https://github.com/your-username/your-repo/issues)
