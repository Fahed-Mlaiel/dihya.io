// Test d’import du point d’entrée JS legacy/helpers/core/impl
const impl = require('./__init__');
test('import impl entrypoint', () => {
  expect(impl).toBeDefined();
});
