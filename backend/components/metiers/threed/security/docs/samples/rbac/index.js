// index.js
// Point d’entrée principal pour le module RBAC (clé en main)

const helpers = require('./helpers');
const samples = require('./samples');

module.exports = {
  ...helpers,
  ...samples
};

// Utilisation :
// const rbac = require('./index');
// rbac.<fonction_helper_ou_sample>()
// Voir samples pour des scénarios concrets.
