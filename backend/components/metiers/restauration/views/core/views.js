// views.js - Vues/metiers pour restauration (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur RestauratioN</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour RestauratioN (restauration)
   */
  renderRestauratioNView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
