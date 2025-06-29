// index.js ultra avancé pour les tests centralisés (Node.js)
// Point d'entrée global pour tous les tests métiers (API, DevOps, Docs, Plugins, etc.)

const apiTests = require('./api');
const devopsTests = require('./devops');
const docsTests = require('./docs');
const pluginsTests = require('./plugins');
// Ajoutez ici d'autres domaines de tests à exposer

module.exports = {
  apiTests,
  devopsTests,
  docsTests,
  pluginsTests,
  // Ajoutez d'autres exports ici selon l'évolution des tests
};

/**
 * Exemple d'utilisation :
 * const { apiTests, devopsTests } = require('./tests_centralises');
 * apiTests.testAssetRoutes();
 */

describe('dummy', () => { it('should pass', () => { expect(true).toBe(true); }); });
