// views_helper.js - Fonctions utilitaires avancées pour les vues Ressources_humaines (JS)

function formatRessources_humainesDetails(details) {
  return `[ressources_humaines] ${details}`;
}

module.exports = {
  renderTitle: (title) => `<h1>${title}</h1>`,
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  renderError: (msg) => `<div class='error'>${msg}</div>`,
  formatRessources_humainesDetails
};
