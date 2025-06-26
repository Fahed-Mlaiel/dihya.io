// views.js - Vues/metiers pour administration_publique (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur administration_publique</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour administration_publique (administration_publique)
   */
  renderadministration_publiqueView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
