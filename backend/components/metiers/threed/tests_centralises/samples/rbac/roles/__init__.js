// __init__.js - Point d'entrée ultra avancé pour les tests de rôles RBAC

const tests = require('./tests_roles.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests de rôles RBAC (attribution, vérification, audit).',
  meta: {
    domain: 'rbac',
    subdomain: 'roles',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
