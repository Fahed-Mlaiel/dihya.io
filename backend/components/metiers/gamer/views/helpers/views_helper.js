// views_helper.js - Fonctions utilitaires avancées pour les vues Gamer (JS)

function formatGamerDetails(details) {
  return `[gamer] ${details}`;
}

module.exports = {
  renderTitle: (title) => `<h1>${title}</h1>`,
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  renderError: (msg) => `<div class='error'>${msg}</div>`,
  formatGamerDetails
};
