// __init__.test.js – Test d’import du point d’entrée JS samples legacy fallback
const samples = require('./__init__');
test('import samples legacy fallback (__init__.js)', () => {
  expect(samples.sampleFallbackLegacy).toBeDefined();
});
