// views_helper.js - Fonctions utilitaires avancées pour les vues administration_publique (JS)

function formatadministration_publiqueDetails(details) {
  return `[administration_publique] ${details}`;
}

module.exports = {
  renderTitle: (title) => `<h1>${title}</h1>`,
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  renderError: (msg) => `<div class='error'>${msg}</div>`,
  formatadministration_publiqueDetails
};
