// views.js - Vues/metiers pour immobilier (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Immobilier</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Immobilier (immobilier)
   */
  renderImmobilierView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
