// Test d’intégration du point d’entrée JS pour les tests templates Threed
const entry = require('./__init__.js');
describe('Entrée JS tests templates Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
