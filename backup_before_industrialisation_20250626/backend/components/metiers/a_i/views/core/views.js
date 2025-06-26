// views.js - Vues/metiers pour a_i (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur A_I</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour A_I (a_i)
   */
  renderA_IView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
