// views.js - Vues/metiers pour ecommerce (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Ecommerce</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Ecommerce (ecommerce)
   */
  renderEcommerceView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
