// Test d’intégration du point d’entrée JS pour les tests utils Threed
const entry = require('./__init__.js');
describe('Entrée JS tests utils Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
