// __init__.js - Point d'entrée ultra avancé pour les tests d'audit et traçabilité

const tests = require('./tests_audit.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests d’audit et de traçabilité (logs, conformité, reporting).',
  meta: {
    domain: 'audit',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
