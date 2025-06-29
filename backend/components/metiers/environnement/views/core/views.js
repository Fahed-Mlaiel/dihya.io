// views.js - Vues/metiers pour environnement (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Environnement</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Environnement (environnement)
   */
  renderEnvironnementView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
