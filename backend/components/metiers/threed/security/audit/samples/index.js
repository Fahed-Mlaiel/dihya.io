// index.js - Point d'entrée des samples d'audit
// Permet l'import modulaire de tous les exemples avancés (logs, reports)

const logs = require('./logs');
const reports = require('./reports');

module.exports = {
  logs,
  reports
};
