// views_helper.js - Fonctions utilitaires avancées pour les vues Seo (JS)

function formatSeoDetails(details) {
  return `[seo] ${details}`;
}

module.exports = {
  renderTitle: (title) => `<h1>${title}</h1>`,
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  renderError: (msg) => `<div class='error'>${msg}</div>`,
  formatSeoDetails
};
