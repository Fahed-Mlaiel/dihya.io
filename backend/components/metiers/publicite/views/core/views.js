// views.js - Vues/metiers pour publicite (exemple)

module.exports = {
  renderHome: () => '<h1>Bienvenue sur Publicite</h1>',
  renderModel: (model) => `<div>Modèle: ${model.name}</div>`,
  /**
   * Vue avancée pour Publicite (publicite)
   */
  renderPubliciteView: (data) => {
    return {
      name: data.name,
      status: data.status,
      details: data.details || '',
    };
  }
};
