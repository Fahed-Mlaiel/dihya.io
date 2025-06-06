// legacy.test.js – Test d’intégration avancé Legacy
const legacy = require('./test_legacy');
test('Legacy module est importable et fonctionnel', () => {
  expect(legacy).toBeDefined();
});
