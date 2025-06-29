// views_helper.js - Fonctions utilitaires avancées pour les vues Banque_Finance (JS)

function formatBanque_FinanceDetails(details) {
  return `[banque_finance] ${details}`;
}

module.exports = {
  renderTitle: (title) => `<h1>${title}</h1>`,
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  renderError: (msg) => `<div class='error'>${msg}</div>`,
  formatBanque_FinanceDetails
};
