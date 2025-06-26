// views.js - Vues/metiers pour sante (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Sante</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Sante (sante)
   */
  renderSanteView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
