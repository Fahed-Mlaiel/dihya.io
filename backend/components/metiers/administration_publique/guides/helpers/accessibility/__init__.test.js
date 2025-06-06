// __init__.test.js – Test d'import du point d'entrée JS accessibility (guides/helpers/accessibility)
const accessibility = require('./__init__');
test('import accessibility entrypoint (__init__.js)', () => {
  expect(accessibility.checkAccessibility).toBeDefined();
  expect(accessibility.auditAccessibility).toBeDefined();
});
