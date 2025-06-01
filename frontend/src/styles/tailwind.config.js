/**
 * @file tailwind.config.js
 * @description Configuration Tailwind CSS pour Dihya Coding : design moderne, accessibilité, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Respecte les bonnes pratiques CSS, responsive, dark/light, contrastes, focus, animations accessibles, branding amazigh-tech.
 * Conforme au cahier des charges Dihya Coding.
 */

module.exports = {
  content: [
    '../../**/*.html',
    '../../**/*.js',
    '../../**/*.jsx',
    '../../**/*.ts',
    '../../**/*.tsx',
    '../../**/*.md',
    '../../**/*.svelte',
    '../../**/*.vue'
  ],
  darkMode: 'media', // ou 'class' pour gestion manuelle
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#2563eb',
          dark: '#1e40af',
          light: '#60a5fa'
        },
        secondary: {
          DEFAULT: '#facc15',
          dark: '#b45309',
          light: '#fde68a'
        },
        accent: {
          DEFAULT: '#f59e42',
          dark: '#b45309',
          light: '#fef9c3'
        },
        background: {
          light: '#f9fafb',
          dark: '#181a1b'
        },
        surface: {
          light: '#fff',
          dark: '#23272f'
        },
        amazigh: {
          blue: '#2563eb',
          yellow: '#facc15',
          orange: '#f59e42',
          red: '#e11d48'
        },
        success: '#22c55e',
        error: '#ef4444',
        info: '#2563eb',
        warning: '#f59e42'
      },
      fontFamily: {
        sans: ['Inter', 'Segoe UI', 'Arial', 'sans-serif'],
        amazigh: ['"Tifinagh", "Inter", "Segoe UI", Arial, sans-serif']
      },
      borderRadius: {
        DEFAULT: '0.375em',
        xl: '1em',
        full: '9999px'
      },
      boxShadow: {
        amazigh: '0 2px 16px 0 rgba(250,204,21,0.10)'
      },
      transitionProperty: {
        width: 'width',
        spacing: 'margin, padding'
      },
      backgroundImage: {
        'amazigh-motif': 'repeating-linear-gradient(135deg, #facc15, #facc15 2px, transparent 2px, transparent 8px)'
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/line-clamp')
  ],
  safelist: [
    'sr-only', 'focus-visible', 'hidden', 'badge', 'alert', 'alert-success', 'alert-error', 'amazigh-motif'
  ],
  // RGPD & sécurité : pas de classes dynamiques générées à partir de données utilisateur
  // Auditabilité : documentez toute extension ou modification dans ce fichier
};