// Initialisation des blueprints Plugins (Node.js)
const audit = require('./audit');
const generators = require('./generators');

module.exports = {
  audit,
  generators
};

// Documentation intégrée
/**
 * Utilisation :
 * const { audit, generators } = require('./plugins');
 * audit.runAudit(...);
 */
