// __init__.test.js – Test d’import du point d’entrée JS static templates
const staticFiles = require('./__init__');
test('import __init__.js static templates', () => {
  expect(staticFiles).toBeDefined();
});
