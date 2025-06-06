// index.test.js – Test d’import du point d’entrée JS fixtures/helpers
const helpers = require('./index');
test('import index.js helpers', () => {
  expect(helpers).toBeDefined();
});
test('import index.js helpers (structure)', () => {
  expect(typeof helpers).toBe('object');
  expect(Object.keys(helpers).length).toBeGreaterThan(0);
});
