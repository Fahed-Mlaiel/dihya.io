// views_helper.js - Fonctions utilitaires avancées pour les vues A_I (JS)

function formatA_IDetails(details) {
  return `[a_i] ${details}`;
}

module.exports = {
  renderTitle: (title) => `<h1>${title}</h1>`,
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  renderError: (msg) => `<div class='error'>${msg}</div>`,
  formatA_IDetails
};
