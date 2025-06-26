// Initialisation des blueprints Docs (Node.js)
const apiReference = require('./api_reference');
const integrationGuide = require('./integration_guide');

module.exports = {
  apiReference,
  integrationGuide
};

// Documentation intégrée
/**
 * Utilisation :
 * const { apiReference, integrationGuide } = require('./docs');
 * apiReference.generate();
 */
