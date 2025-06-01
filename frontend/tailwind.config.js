/**
 * @file tailwind.config.js
 * @description Configuration Tailwind CSS finale pour Dihya Coding : design moderne, accessibilité, robustesse, conformité RGPD, auditabilité, extensibilité, sécurité, souveraineté et documentation claire.
 * Toutes les options sont commentées pour auditabilité, traçabilité et bonnes pratiques.
 */

module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {
      colors: {
        // Palette Dihya Coding (accessibilité, branding amazigh, design moderne)
        primary: "#2B4C7E",        // Bleu amazigh
        secondary: "#F5A623",      // Or/jaune
        accent: "#E94F37",         // Rouge vif
        neutral: "#F4F4F4",        // Gris clair
        info: "#3ABFF8",
        success: "#36D399",
        warning: "#FBBD23",
        error: "#F87272",
        // Couleurs métiers (exemple pour extensibilité)
        health: "#4CAF50",
        legal: "#7B1FA2",
        finance: "#1976D2",
        energy: "#FF9800"
      },
      fontFamily: {
        // Typographie moderne, accessible, multilingue
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        mono: ['Fira Mono', 'ui-monospace', 'SFMono-Regular', 'monospace'],
        amazigh: ['"Noto Sans Tifinagh"', 'Inter', 'sans-serif']
      },
      borderRadius: {
        xl: '1.25rem',
        '2xl': '2rem'
      },
      boxShadow: {
        'card': '0 2px 16px 0 rgba(43,76,126,0.08)'
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),        // Accessibilité et design des formulaires
    require('@tailwindcss/typography'),   // SEO et lisibilité
    require('@tailwindcss/aspect-ratio'), // Responsive images/videos
    require('@tailwindcss/line-clamp')    // Gestion du contenu long
  ],
  safelist: [
    // Pour auditabilité et robustesse, garantir certains styles critiques
    'bg-primary', 'text-primary', 'bg-secondary', 'text-secondary',
    'bg-accent', 'text-accent', 'bg-neutral', 'text-neutral'
  ],
  darkMode: 'media', // Accessibilité : support du mode sombre selon les préférences utilisateur
};

/*
  Sécurité & RGPD : 
    - Aucun traitement de données personnelles dans le CSS généré.
    - Les logs et traces sont gérés côté JS, pas dans cette config.
  Auditabilité : 
    - Ce fichier est commenté pour la traçabilité et la conformité.
  Extensibilité : 
    - Ajoutez vos plugins Tailwind selon vos besoins métiers (ex: dark mode, métiers, branding).
  Robustesse : 
    - Compatible avec tous les navigateurs modernes.
  Documentation claire : 
    - Chaque option est expliquée pour faciliter la maintenance et la contribution.
  Souveraineté numérique : 
    - Utilisation exclusive de plugins open-source.
  Branding : 
    - Palette et typographie inspirées de la culture amazigh, personnalisables.
*/