// views.js - Vues/metiers pour securite (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Securite</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Securite (securite)
   */
  renderSecuriteView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
