// index.test.js – Test d'import du point d'entrée principal JS samples (guides/core/samples)
const samples = require('./index');
test('import samples index.js', () => {
  expect(samples.sampleGuideDoc).toBeDefined();
});
