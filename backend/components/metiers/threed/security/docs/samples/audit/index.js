// index.js
// Point d’entrée principal pour l’audit (clé en main)

const helpers = require('./helpers');
const samples = require('./samples');

module.exports = {
  ...helpers,
  ...samples
};

// Utilisation :
// const audit = require('./index');
// audit.logAuditEvent(...)
// Voir samples pour des scénarios complets.
