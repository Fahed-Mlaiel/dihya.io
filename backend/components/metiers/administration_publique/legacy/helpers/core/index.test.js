// index.test.js – Test d’import du point d’entrée JS legacy/helpers/core
const core = require('./index');
test('import index.js legacy/helpers/core', () => {
  expect(core).toBeDefined();
});
