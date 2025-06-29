// views.js - Vues/metiers pour video (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Video</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Video (video)
   */
  renderVideoView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
