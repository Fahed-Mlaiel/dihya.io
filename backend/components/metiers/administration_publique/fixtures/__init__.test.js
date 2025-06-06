// Test d’import du point d’entrée JS fixtures/helpers
const helpers = require('./__init__');
test('import helpers entrypoint', () => {
  expect(helpers).toBeDefined();
});
