// Fichier déplacé dans samples/pluginManager.test.js
// pluginManager.test.js – Tests unitaires JS pour pluginManager Threed
const { pluginManager } = require('./pluginManager');
describe('pluginManager Threed', () => {
  it('doit exécuter tous les plugins', () => {
    const result = pluginManager.runAll({ input: 'test' });
    expect(result.length).toBeGreaterThan(0);
  });
});
