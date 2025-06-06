// __init__.js – Point d'entrée global du module API Threed (JS)
// Synchronisation JS/Python, conformité RGPD, accessibilité, audit, CI/CD, edge cases.
const core = require('./core');
const routes = require('./routes');
const tests = require('./tests');

module.exports = {
  ...core,
  ...routes,
  ...tests,
  api: require('./index.js'),
  ThreedController: core.controllers ? core.controllers.ThreedController : undefined
};
