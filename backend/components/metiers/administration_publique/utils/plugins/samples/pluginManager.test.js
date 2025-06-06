// pluginManager.test.js
// Test unitaire avancé pour pluginManager (JS)
const pluginManager = require('../core/pluginManager');

describe('pluginManager JS', () => {
  it('enregistre et exécute un plugin', () => {
    pluginManager.register('test', () => 'ok');
    expect(pluginManager.run('test')).toBe('ok');
  });
});
