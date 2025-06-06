// Test d’intégration du point d’entrée JS pour les vues core Threed
const entry = require('./__init__.js');
describe('Entrée JS vues core Threed', () => {
  it('peut être importée sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
