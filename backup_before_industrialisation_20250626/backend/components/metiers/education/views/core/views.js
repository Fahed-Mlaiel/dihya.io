// views.js - Vues/metiers pour education (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Education</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Education (education)
   */
  renderEducationView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
