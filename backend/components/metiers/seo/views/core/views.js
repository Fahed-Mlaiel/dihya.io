// views.js - Vues/metiers pour seo (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Seo</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Seo (seo)
   */
  renderSeoView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
