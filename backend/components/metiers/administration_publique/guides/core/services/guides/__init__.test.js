// Test d’import du point d’entrée JS services/guides
const guides = require('./__init__');
test('import guides entrypoint', () => {
  expect(guides).toBeDefined();
});
