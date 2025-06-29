// views.js - Vues/metiers pour transport (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Transport</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Transport (transport)
   */
  renderTransportView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
