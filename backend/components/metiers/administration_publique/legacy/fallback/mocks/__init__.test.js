// Test d’import du point d’entrée JS legacy/fallback/mocks
const mocks = require('./__init__');
test('import mocks entrypoint', () => {
  expect(mocks).toBeDefined();
});
