// __init__.js - Point d'entrée ultra avancé pour les tests de scripts de restauration

const tests = require('./tests_restore_script.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests de scripts de restauration (recovery, rollback, audit).',
  meta: {
    domain: 'scripts',
    subdomain: 'restore',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
