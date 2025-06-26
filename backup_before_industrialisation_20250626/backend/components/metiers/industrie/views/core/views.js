// views.js - Vues/metiers pour industrie (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Industrie</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Industrie (industrie)
   */
  renderIndustrieView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
