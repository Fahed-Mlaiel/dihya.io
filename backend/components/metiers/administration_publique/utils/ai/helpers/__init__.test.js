// __init__.test.js – Test d’import du point d’entrée JS helpers IA

test('import __init__.js helpers IA ne plante pas', () => {
  const entry = require('./__init__.js');
  expect(entry).toBeDefined();
});
