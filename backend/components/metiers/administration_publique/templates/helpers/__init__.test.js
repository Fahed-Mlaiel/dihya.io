// __init__.test.js – Test d’import du point d’entrée JS helpers

test('import __init__.js helpers ne plante pas', () => {
  const entry = require('./__init__.js');
  expect(entry).toBeDefined();
});
