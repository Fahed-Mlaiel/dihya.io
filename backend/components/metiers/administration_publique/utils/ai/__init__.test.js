// __init__.test.js – Test d’import du point d’entrée JS global IA

test('import __init__.js IA global ne plante pas', () => {
  const entry = require('./__init__.js');
  expect(entry).toBeDefined();
  expect(entry).toHaveProperty('core');
  expect(entry).toHaveProperty('fallback');
  expect(entry).toHaveProperty('helpers');
  expect(entry).toHaveProperty('samples');
});
