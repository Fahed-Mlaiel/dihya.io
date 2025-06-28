// views.js - Vues/metiers pour services_personne (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur ServicesPersonne</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour ServicesPersonne (services_personne)
   */
  renderServicesPersonneView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
