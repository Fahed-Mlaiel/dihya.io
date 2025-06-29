// views.js - Vues/metiers pour sport (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Sport</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Sport (sport)
   */
  renderSportView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
