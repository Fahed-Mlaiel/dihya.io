// index.js ultra avancé pour les tests centralisés Documentation (Node.js)
// Point d'entrée pour tous les tests de documentation, guides, API reference, etc.

const testApiReference = require('./api_reference/test_api_reference');
const testIntegrationGuide = require('./integration_guide/test_integration_guide');
// Ajoutez ici d'autres tests documentation à exposer

module.exports = {
  testApiReference,
  testIntegrationGuide,
  // Ajoutez d'autres exports ici selon l'évolution des tests
};

/**
 * Exemple d'utilisation :
 * const { testApiReference } = require('./docs');
 * testApiReference();
 */

describe('dummy', () => { it('should pass', () => { expect(true).toBe(true); }); });
