// views.js - Vues/metiers pour gamer (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Gamer</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Gamer (gamer)
   */
  renderGamerView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
