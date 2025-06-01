/**
 * Dihya Frontend Scripts Index
 * Exporte scripts d'automatisation, génération, tests, i18n, accessibilité, multilingue, souverain, documenté.
 */

const generateI18n = require('./generateI18n');
const runAccessibilityAudit = require('./runAccessibilityAudit');
const runE2ETests = require('./runE2ETests');
const buildFrontend = require('./buildFrontend');

module.exports = {
  generateI18n,
  runAccessibilityAudit,
  runE2ETests,
  buildFrontend,
};
