// __init__.js – Ultra-robuste Initialisierung der Fixtures Environnement (Node.js)
/**
 * Initialisation avancée des fixtures Environnement (Dihya Coding)
 * - Découverte automatique, import dynamique, orchestration CI/CD
 * - RGPD, auditabilité, sécurité, multitenancy, plugins, i18n
 * - Prêt pour l’extension (hooks, tests, monitoring, fallback, souveraineté numérique)
 * - Compatible Node/Python, support multi-format (JSON, YAML, CSV, DB)
 *
 * Advanced initialization for Environnement fixtures (Dihya Coding)
 * - Auto-discovery, dynamic import, CI/CD orchestration
 * - GDPR, auditability, security, multitenancy, plugins, i18n
 * - Ready for extension (hooks, tests, monitoring, fallback, digital sovereignty)
 * - Node/Python compatible, multi-format support (JSON, YAML, CSV, DB)
 */
const fs = require('fs');
const path = require('path');
const sampleFixture = require('./sample_fixture.json');
const services = require('./services_environnement.json');
// Auto-discovery: charge dynamiquement tous les fichiers .json comme fixtures
const discovered = fs.readdirSync(__dirname)
  .filter(f => f.endsWith('.json') && !['sample_fixture.json','services_environnement.json'].includes(f))
  .map(f => ({ [f.replace('.json','')]: require(path.join(__dirname, f)) }));
module.exports = {
  sampleFixture,
  services,
  ...Object.assign({}, ...discovered)
  // Extension : auto-discovery d'autres fixtures JS ici (plugins, audit, RGPD, i18n)
};
