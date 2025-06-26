// views.js - Vues/metiers pour tourisme (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Tourisme</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Tourisme (tourisme)
   */
  renderTourismeView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
