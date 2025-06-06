// index.test.js – Test d'import du point d'entrée principal JS guides/helpers
const helpers = require('./index');
test('import helpers index.js', () => {
  expect(helpers).toBeDefined();
  expect(typeof helpers).toBe('object');
  expect(helpers.accessibility || helpers.checkAccessibility).toBeDefined();
  expect(helpers.plugins || helpers.checkPlugin).toBeDefined();
  expect(helpers.services || helpers.checkService).toBeDefined();
});
