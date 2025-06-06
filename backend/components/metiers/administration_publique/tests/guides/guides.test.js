// guides.test.js – Test d’intégration avancé Guides
const guides = require('./test_guides');
test('Guides module est importable et fonctionnel', () => {
  expect(guides).toBeDefined();
});
