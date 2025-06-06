// __init__.test.js – Test d’import du point d’entrée JS
test('import __init__.js ne plante pas', () => {
  const entry = require('./__init__.js');
  expect(entry.sample).toBeDefined();
});
