// Test d’intégration du point d’entrée JS pour les tests plugins Threed
const entry = require('./__init__.js');
describe('Entrée JS tests plugins Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
