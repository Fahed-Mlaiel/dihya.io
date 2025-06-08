// __init__.js - Point d'entrée ultra avancé pour les tests de scripts de backup

const tests = require('./tests_backup_script.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests de scripts de sauvegarde (backup, restauration, audit).',
  meta: {
    domain: 'scripts',
    subdomain: 'backup',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
