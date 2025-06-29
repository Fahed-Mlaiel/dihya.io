// views.js - Vues/metiers pour agriculture (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Agriculture</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Agriculture (agriculture)
   */
  renderAgricultureView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
