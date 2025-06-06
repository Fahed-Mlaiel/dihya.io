// Test d’intégration du point d’entrée JS pour les tests d’intégration Threed
const entry = require('./__init__.js');
describe('Entrée JS tests intégration Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
