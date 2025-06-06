// Tests unitaires pour guide_views.js (JS)
const views = require('./guide_views');
test('doc existe', () => {
  expect(views.doc).toBeDefined();
});
