// __init__.test.js – Test d’import du point d’entrée JS samples IA

test('import __init__.js samples IA ne plante pas', () => {
  const entry = require('./__init__.js');
  expect(entry).toBeDefined();
});
