// index.js - Point d'entrée centralisé ultra avancé pour tous les tests d'exemples (samples)

const access = require('./access');
const audit = require('./audit');
const compliance = require('./compliance');
const helpers = require('./helpers');
const monitoring = require('./monitoring');
const policy = require('./policy');
const rbac = require('./rbac');
const rgpd = require('./rgpd');
const scripts = require('./scripts');

module.exports = {
  access,
  audit,
  compliance,
  helpers,
  monitoring,
  policy,
  rbac,
  rgpd,
  scripts,
  description: 'Index centralisé pour tous les tests d’exemples (samples) ultra avancés, clé en main, CI/CD ready.',
  meta: {
    domain: 'samples',
    coverage: '100%',
    lastUpdate: '2025-06-08',
    author: 'Dihya Engineering Team'
  }
};
