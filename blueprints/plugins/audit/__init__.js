// Initialisation avancée du plugin audit (Node.js)
// Export harmonisé du plugin d’audit

const { auditPlugin } = require('./audit_plugin');

/**
 * Exporte le plugin d’audit métier
 * @module plugins/audit
 */
module.exports = {
  auditPlugin
};

/**
 * Exemple d'utilisation :
 * const { auditPlugin } = require('./audit_plugin');
 * const log = auditPlugin({ enabled: true });
 * log('Action d’audit');
 */
