// Test d’intégration du point d’entrée JS pour les tests RGPD Threed
const entry = require('./__init__.js');
describe('Entrée JS tests RGPD Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
