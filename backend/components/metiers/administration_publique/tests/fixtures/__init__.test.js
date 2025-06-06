// Test d’intégration du point d’entrée JS pour les tests fixtures Threed
const entry = require('./__init__.js');
describe('Entrée JS tests fixtures Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
