// __init__.test.js – Test d’import du point d’entrée JS samples legacy helpers
const samples = require('./__init__');
test('import samples legacy helpers (__init__.js)', () => {
  expect(samples.sampleHelperLegacy).toBeDefined();
});
