// fallback_plugins.test.js – Tests unitaires et edge cases JS
const { fallbackPlugins } = require('./fallback_plugins');

test('fallbackPlugins structure', () => {
  expect(typeof fallbackPlugins).toBe('object');
  expect(fallbackPlugins).toHaveProperty('id');
  expect(fallbackPlugins).toHaveProperty('description');
});
