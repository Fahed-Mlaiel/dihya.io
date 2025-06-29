// views.js - Vues/metiers pour automobile (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Automobile</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Automobile (automobile)
   */
  renderAutomobileView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
