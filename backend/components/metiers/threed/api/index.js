// Point d'entrée global du module API Threed (JS)
/**
 * API Threed – Entrée principale JS
 * Synchronisation JS/Python, conformité RGPD, accessibilité, audit, CI/CD, edge cases.
 * Voir README.md pour la structure et les bonnes pratiques.
 */
const core = require('./core/__init__.js');
module.exports = {
  ApiService: core.ApiService,
  ...core
};
