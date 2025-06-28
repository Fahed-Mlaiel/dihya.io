// views.js - Vues/metiers pour voyage (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Voyage</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Voyage (voyage)
   */
  renderVoyageView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
