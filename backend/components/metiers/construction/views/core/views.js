// views.js - Vues/metiers pour construction (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Construction</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Construction (construction)
   */
  renderConstructionView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
