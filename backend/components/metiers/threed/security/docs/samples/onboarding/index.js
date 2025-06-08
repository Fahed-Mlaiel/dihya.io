// index.js
// Point d’entrée principal pour l’onboarding (clé en main)

const helpers = require('./helpers');
const samples = require('./samples');

module.exports = {
  ...helpers,
  ...samples
};

// Utilisation :
// const onboarding = require('./index');
// onboarding.<fonction_helper_ou_sample>()
// Voir samples pour des scénarios concrets.
