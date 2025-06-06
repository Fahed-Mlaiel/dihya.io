// Test d'import du point d'entrée JS du sous-module views
const views = require('./__init__');
test('import views entrypoint', () => {
  expect(views).toBeDefined();
});
