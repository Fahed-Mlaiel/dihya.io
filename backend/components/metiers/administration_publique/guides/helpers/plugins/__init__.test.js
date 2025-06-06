// __init__.test.js – Test d'import du point d'entrée JS plugins (guides/helpers/plugins)
const plugins = require('./__init__');
test('import plugins entrypoint (__init__.js)', () => {
  expect(plugins.checkPlugin).toBeDefined();
  expect(plugins.auditPlugin).toBeDefined();
});
