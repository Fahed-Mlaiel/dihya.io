// Test d’import du point d’entrée JS legacy/helpers/validators
const validators = require('./__init__');
test('import validators entrypoint', () => {
  expect(validators).toBeDefined();
});
