// __init__.js - Point d'entrée ultra avancé pour les tests d'accessibilité et contrôle d'accès

const tests = require('./tests_access.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests d’accessibilité et de contrôle d’accès (RBAC, permissions, audit).',
  meta: {
    domain: 'access',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
