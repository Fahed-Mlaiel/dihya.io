// __init__.test.js – Test d'import du point d'entrée JS services (guides/fallback/services)
const services = require('./__init__');
test('import services entrypoint (__init__.js)', () => {
  expect(services).toBeDefined();
});
