const plugins = require('./__init__');
test('import __init__.js plugins', () => {
  expect(plugins.AdvancedPlugin).toBeDefined();
});
