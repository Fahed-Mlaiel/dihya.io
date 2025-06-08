// __init__.js - Point d'entrée ultra avancé pour les tests de scripts d'automatisation

const audit = require('./audit');
const backup = require('./backup');
const compliance = require('./compliance');
const restore = require('./restore');

module.exports = {
  audit,
  backup,
  compliance,
  restore,
  description: 'Module centralisé pour les tests de scripts d’automatisation (audit, backup, compliance, restore).',
  meta: {
    domain: 'scripts',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
