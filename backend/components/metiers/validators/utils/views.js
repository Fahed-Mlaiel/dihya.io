// views.js – Fonctions de rendu pour Environnement (Node.js)
module.exports = function renderView(data) {
  return `Vue environnementale: ${JSON.stringify(data)}`;
};
