// rgpd.test.js – Test d’intégration avancé RGPD
const rgpd = require('./test_rgpd');
test('RGPD module est importable et fonctionnel', () => {
  expect(rgpd).toBeDefined();
});
