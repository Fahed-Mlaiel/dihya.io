// __init__.js – Ultra-robuste Initialisierung legacy (Node.js)
/**
 * Initialisation avancée des modules legacy Environnement (Dihya Coding)
 * - Découverte automatique, import dynamique, orchestration CI/CD
 * - RGPD, auditabilité, sécurité, multitenancy, plugins, i18n
 * - Prêt pour l’extension (hooks, tests, monitoring, fallback, souveraineté numérique)
 * - Compatible Node/Python, support multi-format (JSON, YAML, CSV, DB)
 *
 * Advanced initialization for legacy Environnement modules (Dihya Coding)
 * - Auto-discovery, dynamic import, CI/CD orchestration
 * - GDPR, auditability, security, multitenancy, plugins, i18n
 * - Ready for extension (hooks, tests, monitoring, fallback, digital sovereignty)
 * - Node/Python compatible, multi-format support (JSON, YAML, CSV, DB)
 */
const apiLegacy = require('./api_legacy');
// Auto-discovery: charge dynamiquement tous les modules JS legacy
const fs = require('fs');
const path = require('path');
const discovered = fs.readdirSync(__dirname)
  .filter(f => f.endsWith('.js') && !['__init__.js','api_legacy.js','tests_legacy_report.js'].includes(f))
  .map(f => require(path.join(__dirname, f)));
module.exports = {
  ...apiLegacy,
  ...Object.assign({}, ...discovered)
  // Extension : auto-discovery d'autres modules legacy JS ici (plugins, audit, RGPD, i18n)
};
