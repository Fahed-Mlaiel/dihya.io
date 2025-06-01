// index.js – Dihya Frontend Assets

// Point d’entrée pour l’import/export des assets frontend
// Exemples d’utilisation, conventions, scripts d’automatisation

/**
 * Dihya Frontend Assets Index
 * Exporte images, icônes, polices, templates, helpers d'accessibilité, multilingue, souverain, documenté.
 */

const images = {
  logo: '/assets/images/dihya.svg',
  favicon: '/assets/images/favicon.ico',
  // ...autres images...
};

const icons = {
  home: '/assets/icons/home.svg',
  user: '/assets/icons/user.svg',
  // ...autres icônes...
};

const fonts = {
  montserrat: '/assets/fonts/Montserrat.woff2',
  inter: '/assets/fonts/Inter.woff2',
  roboto: '/assets/fonts/Roboto.woff2',
  // ...autres polices...
};

const templates = {
  dashboard: '/assets/templates/dashboard.html',
  // ...autres templates...
};

function getImage(name = 'logo') {
  return images[name] || images.logo;
}

function getIcon(name = 'home') {
  return icons[name] || icons.home;
}

function getFont(name = 'montserrat') {
  return fonts[name] || fonts.montserrat;
}

function getTemplate(name = 'dashboard') {
  return templates[name] || templates.dashboard;
}

module.exports = {
  images,
  icons,
  fonts,
  templates,
  getImage,
  getIcon,
  getFont,
  getTemplate,
};
