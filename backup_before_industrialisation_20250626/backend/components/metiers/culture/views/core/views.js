// views.js - Vues/metiers pour culture (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Culture</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Culture (culture)
   */
  renderCultureView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
