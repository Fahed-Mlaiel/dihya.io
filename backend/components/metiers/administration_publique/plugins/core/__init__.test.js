// __init__.test.js – Test d’import du point d’entrée JS core/plugins
const core = require('./__init__');
test('import AdvancedPlugin depuis __init__.js', () => {
  expect(core.AdvancedPlugin).toBeDefined();
});
