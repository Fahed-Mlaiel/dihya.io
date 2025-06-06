// index.test.js – Test d’import du point d’entrée global helpers templates

test('import index.js helpers ne plante pas', () => {
  const entry = require('./index.js');
  expect(entry).toBeDefined();
  expect(entry).toHaveProperty('templates_helper');
  expect(entry).toHaveProperty('templates_mock');
  expect(entry).toHaveProperty('templates_validator');
});
