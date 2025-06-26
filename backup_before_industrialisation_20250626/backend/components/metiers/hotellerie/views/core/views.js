// views.js - Vues/metiers pour hotellerie (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Hotellerie</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Hotellerie (hotellerie)
   */
  renderHotellerieView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
