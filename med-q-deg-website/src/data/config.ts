/**
 * MedQ-Deg Website Configuration
 *
 * This file contains all configurable data for the website.
 * Modify these values to quickly update the content without changing
 * the component logic.
 */

export const SITE_CONFIG = {
  // Basic Info
  title: 'MedQ-Deg',
  subtitle: 'A Multi-Dimensional Benchmark for Medical Image Degradation Recognition',
  description:
    'First benchmark for open-set degradation recognition in medical imaging with 6 categories and 28 degradation types.',

  // Links
  links: {
    paper: '#',
    github: '#',
    dataset: '#',
    demo: '/examples',
  },

  // Social / Contact
  authors: ['Author 1', 'Author 2', 'Author 3'],
  affiliation: 'Your Institution',

  // Stats shown on homepage
  stats: {
    categories: 6,
    types: 28,
    datasets: 4,
    modalities: ['MRI', 'CT', 'X-Ray', 'Ultrasound'],
  },

  // Colors for categories
  categoryColors: {
    blur: '#6366f1',      // Indigo
    noise: '#8b5cf6',     // Violet
    artifact: '#ec4899',  // Pink
    contrast: '#f59e0b',  // Amber
    compression: '#10b981', // Emerald
    other: '#64748b',     // Slate
  },
} as const;

// Export type for type safety
export type SiteConfig = typeof SITE_CONFIG;

/**
 * Category Configuration
 * Modify these values to update degradation categories
 */
export const CATEGORIES = [
  {
    id: 'blur',
    name: 'Blur',
    nameZh: '模糊',
    color: '#6366f1',
    icon: 'blur_on',
    description: 'Motion blur, Gaussian blur, defocus artifacts',
  },
  {
    id: 'noise',
    name: 'Noise',
    nameZh: '噪声',
    color: '#8b5cf6',
    icon: 'grain',
    description: 'Gaussian noise, salt & pepper, speckle noise',
  },
  {
    id: 'artifact',
    name: 'Artifact',
    nameZh: '伪影',
    color: '#ec4899',
    icon: 'warning',
    description: 'Motion artifacts, ring artifacts, aliasing',
  },
  {
    id: 'contrast',
    name: 'Contrast',
    nameZh: '对比度',
    color: '#f59e0b',
    icon: 'brightness_6',
    description: 'Low contrast, overexposure, underexposure',
  },
  {
    id: 'compression',
    name: 'Compression',
    nameZh: '压缩',
    color: '#10b981',
    icon: 'compress',
    description: 'JPEG compression, block artifacts',
  },
  {
    id: 'other',
    name: 'Other',
    nameZh: '其他',
    color: '#64748b',
    icon: 'more_horiz',
    description: 'Other types of degradation',
  },
] as const;

/**
 * Degradation Types
 * Add or modify degradation types here
 */
export const DEGRADATION_TYPES = [
  // Blur types
  { id: 'gaussian_blur', name: 'Gaussian Blur', category: 'blur' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'motion_blur', name: 'Motion Blur', category: 'blur' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'defocus_blur', name: 'Defocus Blur', category: 'blur' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'box_blur', name: 'Box Blur', category: 'blur' as const, severity: ['mild', 'moderate', 'severe'] },

  // Noise types
  { id: 'gaussian_noise', name: 'Gaussian Noise', category: 'noise' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'salt_pepper', name: 'Salt & Pepper', category: 'noise' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'speckle_noise', name: 'Speckle Noise', category: 'noise' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'poisson_noise', name: 'Poisson Noise', category: 'noise' as const, severity: ['mild', 'moderate', 'severe'] },

  // Artifact types
  { id: 'motion_artifact', name: 'Motion Artifact', category: 'artifact' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'ring_artifact', name: 'Ring Artifact', category: 'artifact' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'aliasing', name: 'Aliasing', category: 'artifact' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'stripe_artifact', name: 'Stripe Artifact', category: 'artifact' as const, severity: ['mild', 'moderate', 'severe'] },

  // Contrast types
  { id: 'low_contrast', name: 'Low Contrast', category: 'contrast' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'high_contrast', name: 'High Contrast', category: 'contrast' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'overexposure', name: 'Overexposure', category: 'contrast' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'underexposure', name: 'Underexposure', category: 'contrast' as const, severity: ['mild', 'moderate', 'severe'] },

  // Compression types
  { id: 'jpeg_compression', name: 'JPEG Compression', category: 'compression' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'block_artifact', name: 'Block Artifact', category: 'compression' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'jpeg_2000', name: 'JPEG 2000', category: 'compression' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'webp_compression', name: 'WebP Compression', category: 'compression' as const, severity: ['mild', 'moderate', 'severe'] },

  // Other types (will add more)
  { id: 'haze', name: 'Haze', category: 'other' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'rain', name: 'Rain', category: 'other' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'frost', name: 'Frost', category: 'other' as const, severity: ['mild', 'moderate', 'severe'] },
  { id: 'snow', name: 'Snow', category: 'other' as const, severity: ['mild', 'moderate', 'severe'] },
] as const;

/**
 * Methods / Contributions
 * Modify to update the contributions section
 */
export const CONTRIBUTIONS = [
  {
    id: 'benchmark',
    title: 'MedQ-Deg Benchmark',
    description: 'First comprehensive benchmark for medical image degradation recognition with 28 degradation types across 6 categories',
    icon: 'assessment',
    link: '/benchmark',
  },
  {
    id: 'dpl',
    title: 'DPL Method',
    description: 'Degradation-aware Prompt Learning with learnable prompts and prototype-based unknown detector',
    icon: 'psychology',
    link: '/methods',
  },
  {
    id: 'dpt',
    title: 'DPT Framework',
    description: 'Degradation Prompt Transfer for downstream task adaptation with degradation-aware prompts',
    icon: 'sync_alt',
    link: '/methods#dpt',
  },
] as const;

/**
 * Page Layout Configuration
 * Modify these values to change page layouts
 */
export const PAGE_LAYOUTS = {
  home: {
    hero: 'centered', // 'centered' | 'split' | 'full'
    stats: 'cards',   // 'cards' | 'inline' | 'minimal'
    contributions: 'grid', // 'grid' | 'list' | 'carousel'
  },
  benchmark: {
    view: 'grid',     // 'grid' | 'list' | 'table'
    filter: 'sidebar', // 'sidebar' | 'top' | 'inline'
    cards: 'standard', // 'standard' | 'detailed' | 'minimal'
  },
  results: {
    charts: 'tabs',   // 'tabs' | 'stacked' | 'grid'
  },
} as const;

/**
 * Animation Configuration
 */
export const ANIMATION_CONFIG = {
  enabled: true,
  duration: 500,      // ms
  stagger: 100,       // ms
  easing: 'ease-out',
  scrollThreshold: 0.1,
} as const;

/**
 * Theme Configuration
 */
export const THEME_CONFIG = {
  defaultMode: 'dark', // 'light' | 'dark' | 'system'
  allowToggle: true,
  gradients: {
    primary: 'from-primary-600 to-accent-600',
    hero: 'from-surface-950 via-surface-900 to-surface-950',
  },
} as const;
