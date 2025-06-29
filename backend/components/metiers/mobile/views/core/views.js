// views.js - Vues/metiers pour mobile (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Mobile</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Mobile (mobile)
   */
  renderMobileView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
