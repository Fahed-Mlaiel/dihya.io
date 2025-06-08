// __init__.js - Point d'entrée ultra avancé pour les tests de scripts de conformité

const tests = require('./tests_compliance_script.js');

module.exports = {
  ...tests,
  description: 'Module centralisé pour les tests de scripts de conformité (vérification, audit, reporting).',
  meta: {
    domain: 'scripts',
    subdomain: 'compliance',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
