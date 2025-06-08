// index.js
// Point d’entrée principal pour le monitoring (clé en main)

const helpers = require('./helpers');
const samples = require('./samples');

module.exports = {
  ...helpers,
  ...samples
};

// Utilisation :
// const monitoring = require('./index');
// monitoring.collectMetrics(...)
// Voir samples pour des scénarios complets.
