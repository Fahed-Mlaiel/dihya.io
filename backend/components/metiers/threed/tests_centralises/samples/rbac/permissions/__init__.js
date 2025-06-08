// __init__.js - Point d'entrée ultra avancé pour les tests de permissions RBAC

const tests = require('./tests_permissions.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests de permissions RBAC (gestion, vérification, audit).',
  meta: {
    domain: 'rbac',
    subdomain: 'permissions',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
