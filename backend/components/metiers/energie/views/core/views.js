// views.js - Vues/metiers pour energie (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Energie</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Energie (energie)
   */
  renderEnergieView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
