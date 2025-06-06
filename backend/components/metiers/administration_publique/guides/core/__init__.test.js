// __init__.test.js – Test d’import du point d’entrée JS
// Test d’import du point d’entrée JS du module guides/core
const core = require('./__init__');
test('import core entrypoint', () => {
  expect(core).toBeDefined();
  // Vérifie l’accès à un sous-module (exemple)
  expect(core.utils || core.fixtures).toBeDefined();
});
