// __init__.test.js – Test d’import des points d’entrée helpers/validators JS
const helpers = require('./helpers');
const validators = require('./validators');
test('import helpers entrypoint', () => {
  expect(helpers).toBeDefined();
});
test('import validators entrypoint', () => {
  expect(validators).toBeDefined();
});
