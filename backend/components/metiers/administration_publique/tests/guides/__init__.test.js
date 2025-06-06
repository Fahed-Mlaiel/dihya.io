// Test d’intégration du point d’entrée JS pour les tests guides Threed
const entry = require('./__init__.js');
describe('Entrée JS tests guides Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
