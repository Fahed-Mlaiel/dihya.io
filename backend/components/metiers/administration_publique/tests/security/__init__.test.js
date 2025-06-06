// Test d’intégration du point d’entrée JS pour les tests sécurité Threed
const entry = require('./__init__.js');
describe('Entrée JS tests sécurité Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
