// views.js - Vues/metiers pour crypto (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Crypto</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Crypto (crypto)
   */
  renderCryptoView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
