// views.js - Vues/metiers pour medias (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Medias</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Medias (medias)
   */
  renderMediasView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
