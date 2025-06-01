/**
 * @file postcss.config.js
 * @description Configuration PostCSS finale pour Dihya Coding : design moderne, robustesse, conformité RGPD, auditabilité, extensibilité, sécurité, souveraineté et documentation claire.
 * Toutes les options sont commentées pour auditabilité, traçabilité et bonnes pratiques.
 */

module.exports = {
  plugins: {
    // Ajoute les préfixes pour compatibilité navigateurs (SEO/accessibilité)
    autoprefixer: {
      overrideBrowserslist: [
        '>0.2%',
        'not dead',
        'not op_mini all'
      ]
    },
    // Permet l’utilisation de variables CSS modernes, nesting, fallback
    'postcss-preset-env': {
      stage: 2,
      features: {
        'nesting-rules': true,
        'custom-properties': true
      },
      autoprefixer: { grid: true }
    },
    // Intègre Tailwind CSS pour UI/UX moderne, responsive, thèmes personnalisés
    tailwindcss: {},
    // Optimise la minification CSS pour la performance et le SEO
    cssnano: process.env.NODE_ENV === 'production' ? {
      preset: 'default'
    } : false
  }
};

/*
  Sécurité & RGPD : 
    - Aucun traitement de données personnelles dans le CSS.
    - Les logs et traces sont gérés côté JS, pas dans cette config.
  Auditabilité : 
    - Ce fichier est commenté pour la traçabilité et la conformité.
  Extensibilité : 
    - Ajoutez vos plugins PostCSS selon vos besoins métiers (ex: plugins métiers, dark mode, etc.).
  Robustesse : 
    - Compatible avec tous les navigateurs modernes.
  Documentation claire : 
    - Chaque option est expliquée pour faciliter la maintenance et la contribution.
  Souveraineté numérique : 
    - Utilisation exclusive de plugins open-source.
*/