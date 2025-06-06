// __init__.test.js – Test d’import du point d’entrée JS samples helpers templates
const samples = require('./__init__');
test('import samples helpers templates (__init__.js)', () => {
  expect(samples.sampleHelperTemplate).toBeDefined();
});
