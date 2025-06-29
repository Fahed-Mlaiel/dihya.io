// views.js - Vues/metiers pour beaute (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Beaute</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Beaute (beaute)
   */
  renderBeauteView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
