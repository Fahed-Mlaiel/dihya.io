// views.js - Vues/metiers pour vr_ar (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur vr_ar</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour vr_ar (vr_ar)
   */
  rendervr_arView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
