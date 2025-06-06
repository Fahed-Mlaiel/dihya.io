// index.test.js – Test d’import du point d’entrée JS views
const views = require('./index');
test('import index.js views', () => {
  expect(views).toBeDefined();
});
