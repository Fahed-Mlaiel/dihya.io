// index.js – Point d'entrée principal du module compliance samples (RGPD, sécurité 3D)
// Permet l'import modulaire de tous les exemples avancés (policies, checklists)

const policies = require('./policies');
const checklists = require('./checklists');

module.exports = {
  policies,
  checklists
};
