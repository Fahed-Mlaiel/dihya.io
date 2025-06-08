// __init__.js - Point d'entrée ultra avancé pour les tests de scripts d'audit

const tests = require('./tests_audit_script.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests de scripts d’audit (vérification, conformité, reporting).',
  meta: {
    domain: 'scripts',
    subdomain: 'audit',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
