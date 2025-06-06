// index.test.js – Test d’import du point d’entrée JS services
const services = require('./index');
test('import index.js services', () => {
  expect(services).toBeDefined();
});
