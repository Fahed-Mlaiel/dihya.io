// index.js
// Point d’entrée principal pour la gestion des accès (clé en main)

const helpers = require('./helpers');
const samples = require('./samples');

module.exports = {
  ...helpers,
  ...samples
};

// Utilisation :
// const access = require('./index');
// const token = access.generateMfaToken('user1');
// const sso = access.initiateSsoLogin('google', 'https://app.dihya.io/callback');
// Voir samples pour des scénarios complets.
