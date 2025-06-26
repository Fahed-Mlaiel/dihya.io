// views.js - Vues/metiers pour science (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Science</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Science (science)
   */
  renderScienceView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
