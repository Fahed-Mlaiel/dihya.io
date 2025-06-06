// index.test.js – Test d'intégration du point d'entrée plugins JS (conformité, CI/CD)
const plugins = require('./index');
describe('Entrée JS plugins utils threed', () => {
  it('doit exposer pluginManager, SamplePlugin, helpers et fallback', () => {
    expect(plugins).toHaveProperty('pluginManager');
    expect(plugins).toHaveProperty('run');
    expect(plugins).toHaveProperty('pluginsHelper');
    expect(plugins).toHaveProperty('fallbackPlugin');
  });
});
