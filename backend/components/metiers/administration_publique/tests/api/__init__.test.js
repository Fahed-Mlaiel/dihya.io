// Test d’intégration du point d’entrée JS pour les tests API Threed
const entry = require('./__init__.js');
describe('Entrée JS tests API Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
