// index.js
// Point d’entrée principal pour le module RGPD (clé en main)

const helpers = require('./helpers');
const samples = require('./samples');

module.exports = {
  ...helpers,
  ...samples
};

// Utilisation :
// const rgpd = require('./index');
// rgpd.<fonction_helper_ou_sample>()
// Voir samples pour des scénarios concrets.
