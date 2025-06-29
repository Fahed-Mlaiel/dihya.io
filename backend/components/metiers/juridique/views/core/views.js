// views.js - Vues/metiers pour juridique (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Juridique</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Juridique (juridique)
   */
  renderJuridiqueView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
