// Test unitaire pour sample_plugin.js
const plugin = require('./sample_plugin');
test('plugin fonctionne', () => {
  expect(plugin.run()).toBe('Plugin exécuté!');
});
