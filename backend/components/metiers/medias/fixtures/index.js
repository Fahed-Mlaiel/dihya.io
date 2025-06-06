// index.js – Ultra-robuster Entry-Point für Environnement Fixtures (Dihya Coding)
/**
 * Point d'entrée avancé pour les fixtures Environnement
 * - Exporte toutes les fixtures (statiquement + auto-découvertes)
 * - Prêt pour extension (plugins, audit, RGPD, i18n, multitenancy)
 * - Utilisé dans les tests, CI/CD, scripts de migration, monitoring
 *
 * Advanced entry point for Environnement fixtures
 * - Exports all fixtures (static + auto-discovered)
 * - Ready for extension (plugins, audit, GDPR, i18n, multitenancy)
 * - Used in tests, CI/CD, migration scripts, monitoring
 */
const fs = require('fs');
const path = require('path');
const sampleFixture = require('./sample_fixture.json');
const services = require('./services_environnement.json');
const discovered = fs.readdirSync(__dirname)
  .filter(f => f.endsWith('.json') && !['sample_fixture.json','services_environnement.json'].includes(f))
  .map(f => ({ [f.replace('.json','')]: require(path.join(__dirname, f)) }));
module.exports = {
  sampleFixture,
  services,
  ...Object.assign({}, ...discovered)
  // Extension: plugins dynamiques, audit, RGPD, i18n, multitenancy
};
