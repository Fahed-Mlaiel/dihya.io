// __init__.js - Point d'entrée ultra avancé pour les tests helpers logger

const tests = require('./tests_logger.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests helpers logger (journalisation, audit, conformité).',
  meta: {
    domain: 'helpers',
    subdomain: 'logger',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
