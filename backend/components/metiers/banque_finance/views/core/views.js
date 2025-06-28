// views.js - Vues/metiers pour banque_finance (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Banque_Finance</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Banque_Finance (banque_finance)
   */
  renderBanque_FinanceView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
