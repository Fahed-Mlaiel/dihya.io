// Test d’import du point d’entrée JS legacy/fallback/migrations
const migrations = require('./__init__');
test('import migrations entrypoint', () => {
  expect(migrations).toBeDefined();
});
