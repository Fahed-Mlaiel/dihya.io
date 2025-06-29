// views.js - Vues/metiers pour voice (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur voice</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour voice (voice)
   */
  rendervoiceView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
