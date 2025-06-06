// Test d’intégration du point d’entrée JS pour les helpers de vues Threed
const entry = require('./__init__.js');
describe('Entrée JS helpers vues Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
