// views.js - Vues/metiers pour recherche (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Recherche</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Recherche (recherche)
   */
  renderRechercheView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
