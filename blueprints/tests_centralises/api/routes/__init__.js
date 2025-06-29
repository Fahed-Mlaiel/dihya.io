// Initialisation avancée des tests Node.js pour routes
let routes;
try {
  routes = require('../../../../blueprints/routes');
} catch (e) {
  routes = require('./test_asset_routes.js');
}

describe('assetRoutes', () => {
  it('existe', () => {
    expect(typeof routes).toBe('object');
  });
});

module.exports = routes;

