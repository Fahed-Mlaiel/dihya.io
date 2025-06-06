// Test d’import du point d’entrée JS views/samples
const samples = require('./__init__');
test('import samples entrypoint', () => {
  expect(samples).toBeDefined();
});
