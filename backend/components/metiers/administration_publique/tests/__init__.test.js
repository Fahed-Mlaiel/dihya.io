// __init__.test.js – Test d’import du point d’entrée JS racine tests Threed

test('import __init__.js racine tests ne plante pas', () => {
  const entry = require('./__init__.js');
  expect(entry).toBeDefined();
});
