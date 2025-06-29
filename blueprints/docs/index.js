// index.js ultra avancé pour le domaine Documentation (Node.js)
// Point d'entrée centralisé pour la documentation API, guides d'intégration, etc.

const apiReference = require('./api_reference/api_reference');
const integrationGuide = require('./integration_guide/integration_guide');
// Ajoutez ici d'autres modules de documentation à exposer

module.exports = {
  apiReference,
  integrationGuide,
  // Ajoutez d'autres exports ici selon l'évolution du socle
};

/**
 * Exemple d'utilisation :
 * const { apiReference, integrationGuide } = require('./docs');
 * apiReference.generate();
 * integrationGuide.guide();
 */
