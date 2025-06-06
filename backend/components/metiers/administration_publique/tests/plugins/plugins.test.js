// plugins.test.js – Test d’intégration avancé Plugins (fusionné, import direct PluginManager)
const { PluginManager } = require('./__init__');

describe('Plugins Threed – Intégration', () => {
  it('peut enregistrer, exécuter et désenregistrer un plugin', () => {
    class DummyPlugin { run(x) { return x + 1; } }
    const pm = new PluginManager();
    pm.register('dummy', new DummyPlugin());
    expect(pm.get('dummy')).toBeDefined();
    expect(pm.execute('dummy', 2)).toBe(3);
    pm.unregister('dummy');
    expect(pm.get('dummy')).toBeUndefined();
  });
});
