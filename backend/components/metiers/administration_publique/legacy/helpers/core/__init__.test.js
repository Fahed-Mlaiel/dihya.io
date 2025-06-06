// Test d’import du point d’entrée JS legacy/helpers/core
const core = require('./__init__');
test('import core entrypoint', () => {
  expect(core).toBeDefined();
});
