// views.js - Vues/metiers pour arts (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Arts</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Arts (arts)
   */
  renderArtsView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
