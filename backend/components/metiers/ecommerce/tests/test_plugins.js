// test_plugins.js – Test des plugins Environnement (Node.js/Jest)
const pluginManager = require('../utils/pluginManager');
const samplePlugin = require('../utils/sample_plugin');

describe('PluginManager Environnement', () => {
  beforeAll(() => {
    pluginManager.register(samplePlugin);
  });
  it('doit exécuter tous les plugins', () => {
    const result = pluginManager.runAll('test');
    expect(result.length).toBeGreaterThan(0);
    expect(result[0]).toMatch(/Traitement environnemental/);
  });
});
