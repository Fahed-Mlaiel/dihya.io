// __init__.test.js – Test d'import du point d'entrée JS samples (guides/fallback/samples)
const samples = require('./__init__');
test('import samples entrypoint (__init__.js)', () => {
  expect(samples.sampleFallbackCase).toBeDefined();
});
