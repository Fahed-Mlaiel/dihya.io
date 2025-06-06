// __init__.test.js – Test d'import du point d'entrée JS guides/helpers
const helpers = require('./__init__');
test('import helpers entrypoint (__init__.js)', () => {
  expect(helpers).toBeDefined();
  expect(typeof helpers).toBe('object');
});
