// views.js - Vues/metiers pour assurance (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Assurance</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Assurance (assurance)
   */
  renderAssuranceView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
