// __init__.js - Point d'entrée ultra avancé pour les tests RGPD

const tests = require('./tests_rgpd.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests RGPD (anonymisation, conformité, audit, export).',
  meta: {
    domain: 'rgpd',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
