// Test d’import du point d’entrée JS utils/guides
const guides = require('./__init__');
test('import guides entrypoint', () => {
  expect(guides).toBeDefined();
});
