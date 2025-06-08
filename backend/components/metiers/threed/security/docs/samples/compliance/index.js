// index.js
// Point d’entrée principal pour la conformité (clé en main)

const helpers = require('./helpers');
const samples = require('./samples');

module.exports = {
  ...helpers,
  ...samples
};

// Utilisation :
// const compliance = require('./index');
// compliance.checkRgpdCompliance(...)
// Voir samples pour des scénarios complets.
