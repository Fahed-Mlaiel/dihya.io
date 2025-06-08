// __init__.js - Point d'entrée ultra avancé pour les tests de conformité réglementaire

const tests = require('./tests_compliance.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests de conformité réglementaire (processus, audit, reporting).',
  meta: {
    domain: 'compliance',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
