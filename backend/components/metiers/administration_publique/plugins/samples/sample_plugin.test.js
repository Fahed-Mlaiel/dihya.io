// sample_plugin.test.js
// Tests unitaires pour SamplePlugin (clé en main, CI/CD ready)

const SamplePlugin = require('./sample_plugin');

describe('SamplePlugin', () => {
  it('doit s\'initialiser correctement', () => {
    const plugin = new SamplePlugin({ mode: 'test' });
    expect(plugin.options).toEqual({ mode: 'test' });
  });

  it('doit initialiser la config', () => {
    const plugin = new SamplePlugin();
    expect(plugin.init({ level: 1 })).toBe(true);
    expect(plugin.config).toEqual({ level: 1 });
  });

  it('doit exécuter le run sample', () => {
    const plugin = new SamplePlugin();
    plugin.init({ level: 2 });
    const result = plugin.run('DATA');
    expect(result).toEqual({ processed: true, data: 'DATA', config: { level: 2 } });
  });
});
