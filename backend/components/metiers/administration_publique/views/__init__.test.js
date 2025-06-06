// Test d’intégration du point d’entrée JS global des vues Threed
const entry = require('./__init__.js');
describe('Entrée JS globale vues Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
