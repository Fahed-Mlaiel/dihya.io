// __init__.js - Point d'entrée ultra avancé pour les tests du moteur RBAC

const tests = require('./tests_engine.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests du moteur RBAC (règles, logique d’accès, audit).',
  meta: {
    domain: 'rbac',
    subdomain: 'engine',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
