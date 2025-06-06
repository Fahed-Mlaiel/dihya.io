// __init__.test.js – Test d'import du point d'entrée JS samples avancés (guides/core/samples/samples)
const samples = require('./__init__');
test('import samples entrypoint (__init__.js)', () => {
  expect(samples.sampleAccessibilityCase).toBeDefined();
  expect(samples.sampleAuditCase).toBeDefined();
});
