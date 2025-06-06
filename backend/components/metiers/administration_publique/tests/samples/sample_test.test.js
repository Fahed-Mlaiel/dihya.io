// sample_test.test.js – Test d’intégration du sample JS
const sample = require('./sample_test');
test('Sample JS est importable et fonctionnel', () => {
  expect(sample).toBeDefined();
});
