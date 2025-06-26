// index.js ultra avancé pour les tests centralisés API (Node.js)
// Point d'entrée pour tous les tests de routes, générateurs, etc.

const testAssetRoutes = require('./routes/test_asset_routes');
const testBackendApi = require('./generators/test_backendApi');
// Ajoutez ici d'autres tests API à exposer

module.exports = {
  testAssetRoutes,
  testBackendApi,
  // Ajoutez d'autres exports ici selon l'évolution des tests
};

/**
 * Exemple d'utilisation :
 * const { testAssetRoutes } = require('./api');
 * testAssetRoutes();
 */

describe('dummy', () => { it('should pass', () => { expect(true).toBe(true); }); });
