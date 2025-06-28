// views_helper.js - Fonctions utilitaires avancées pour les vues Environnement (JS)

function formatEnvironnementDetails(details) {
  return `[environnement] ${details}`;
}

module.exports = {
  renderTitle: (title) => `<h1>${title}</h1>`,
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  renderError: (msg) => `<div class='error'>${msg}</div>`,
  formatEnvironnementDetails
};
