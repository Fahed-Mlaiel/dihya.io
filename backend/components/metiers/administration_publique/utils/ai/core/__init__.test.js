// __init__.test.js – Test d’import du point d’entrée JS utils/ai/core

test('import __init__.js utils/ai/core ne plante pas', () => {
  const entry = require('./__init__.js');
  expect(entry).toBeDefined();
});
