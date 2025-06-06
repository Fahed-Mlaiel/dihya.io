// __init__.test.js – Test d'import du point d'entrée JS helpers (fixtures/helpers/helpers)
const helpers = require('./helpers');
test('import helpers entrypoint (__init__.js)', () => {
  expect(helpers).toBeDefined();
  expect(typeof helpers).toBe('object');
});
