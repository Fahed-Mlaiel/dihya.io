// __init__.js - Point d'entrée ultra avancé pour les tests helpers utils

const tests = require('./tests_utils.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests helpers utils (fonctions utilitaires, audit, conformité).',
  meta: {
    domain: 'helpers',
    subdomain: 'utils',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
