// __init__.test.js – Test d’import du point d’entrée JS core fallback IA

test('import __init__.js core fallback IA ne plante pas', () => {
  const entry = require('./__init__.js');
  expect(entry).toBeDefined();
});
