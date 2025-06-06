// plugin_manager.test.js – Tests unitaires avancés pour PluginManager (JS)
class DummyPlugin {
  run(x) { return x * 2; }
}

const PluginManager = require('./plugin_manager');

describe('PluginManager', () => {
  it('enregistre et récupère un plugin', () => {
    const pm = new PluginManager();
    const plugin = new DummyPlugin();
    pm.register('dummy', plugin);
    expect(pm.get('dummy')).toBe(plugin);
  });

  it('liste les plugins', () => {
    const pm = new PluginManager();
    pm.register('a', new DummyPlugin());
    pm.register('b', new DummyPlugin());
    expect(pm.listPlugins().sort()).toEqual(['a', 'b']);
  });

  it('exécute un plugin', () => {
    const pm = new PluginManager();
    const plugin = new DummyPlugin();
    pm.register('dummy', plugin);
    expect(pm.execute('dummy', 3)).toBe(6);
  });

  it('désenregistre un plugin', () => {
    const pm = new PluginManager();
    const plugin = new DummyPlugin();
    pm.register('dummy', plugin);
    pm.unregister('dummy');
    expect(pm.get('dummy')).toBeUndefined();
  });

  it('lance une erreur si plugin non trouvé', () => {
    const pm = new PluginManager();
    expect(() => pm.execute('notfound', 1)).toThrow();
  });
});
