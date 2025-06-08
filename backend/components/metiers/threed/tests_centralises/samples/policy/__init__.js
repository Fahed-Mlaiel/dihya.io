// __init__.js - Point d'entrée ultra avancé pour les tests de politiques de sécurité et de gestion

const tests = require('./tests_policy.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests de politiques de sécurité et de gestion (application, vérification, audit).',
  meta: {
    domain: 'policy',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
