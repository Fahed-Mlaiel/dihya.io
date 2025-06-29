// views_helper.js - Fonctions utilitaires avancées pour les vues Medias (JS)

function formatMediasDetails(details) {
  return `[medias] ${details}`;
}

module.exports = {
  renderTitle: (title) => `<h1>${title}</h1>`,
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  renderError: (msg) => `<div class='error'>${msg}</div>`,
  formatMediasDetails
};
