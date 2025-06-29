// views.js - Vues/metiers pour mode (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Mode</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Mode (mode)
   */
  renderModeView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
