// views.js - Vues/metiers pour health (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Health</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Health (health)
   */
  renderHealthView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
