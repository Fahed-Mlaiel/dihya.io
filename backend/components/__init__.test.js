// __init__.test.js – Test d'import JS du dossier components

test('Import global components', () => {
  const components = require('./index');
  expect(components).toBeDefined();
});
