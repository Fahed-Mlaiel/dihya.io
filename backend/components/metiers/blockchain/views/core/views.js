// views.js - Vues/metiers pour blockchain (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Blockchain</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Blockchain (blockchain)
   */
  renderBlockchainView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
