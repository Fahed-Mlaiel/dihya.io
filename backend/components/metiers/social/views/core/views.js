// views.js - Vues/metiers pour social (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Social</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Social (social)
   */
  renderSocialView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
