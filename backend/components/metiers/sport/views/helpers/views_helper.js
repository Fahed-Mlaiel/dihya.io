// views_helper.js - Fonctions utilitaires avancées pour les vues Sport (JS)

function formatSportDetails(details) {
  return `[sport] ${details}`;
}

module.exports = {
  renderTitle: (title) => `<h1>${title}</h1>`,
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  renderError: (msg) => `<div class='error'>${msg}</div>`,
  formatSportDetails
};
