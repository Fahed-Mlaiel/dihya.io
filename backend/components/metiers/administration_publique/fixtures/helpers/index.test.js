// index.test.js – Test d'import du point d'entrée principal JS helpers (fixtures/helpers)
const helpers = require('./index');
test('import helpers index.js', () => {
  expect(helpers).toBeDefined();
  expect(typeof helpers).toBe('object');
});
