// __init__.test.js – Test d'import du point d'entrée JS services (guides/helpers/services)
const services = require('./__init__');
test('import services entrypoint (__init__.js)', () => {
  expect(services.checkService).toBeDefined();
  expect(services.auditService).toBeDefined();
});
