// index.js – Point d'entrée principal du module compliance (RGPD, sécurité 3D)
// Permet l'import modulaire de tous les sous-modules (anonymisation, purge, checklists, policies, samples)

const anonymisation = require('./anonymisation');
const purge = require('./purge');
const checklists = require('./checklists');
const policies = require('./policies');
const samples = require('./samples');

module.exports = {
  anonymisation,
  purge,
  checklists,
  policies,
  samples,
};
