// views.js - Vues/metiers pour ressources_humaines (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Ressources_humaines</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Ressources_humaines (ressources_humaines)
   */
  renderRessources_humainesView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
