// index.test.js – Test d'import du point d'entrée principal JS samples (fixtures/core/samples)
const samples = require('./index');
test('import samples index.js', () => {
  expect(samples).toBeDefined();
  expect(typeof samples).toBe('object');
});
