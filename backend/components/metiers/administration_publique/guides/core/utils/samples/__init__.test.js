// Test d’import du point d’entrée JS utils/samples
const samples = require('./__init__');
test('import samples entrypoint', () => {
  expect(samples).toBeDefined();
});
