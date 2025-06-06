// views.js - Vues/metiers pour threed (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Threed</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Threed (3D)
   */
  renderThreedView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
