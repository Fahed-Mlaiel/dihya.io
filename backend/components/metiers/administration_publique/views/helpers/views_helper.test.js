// Test unitaire pour views_helper.js
const helpers = require('./views_helper.js');
describe('Helpers de vues Threed (JS)', () => {
  it('doit exposer une fonction principale', () => {
    expect(typeof helpers.renderHelperView).toBe('function');
  });
  // Ajouter d'autres tests unitaires selon les helpers disponibles
});
