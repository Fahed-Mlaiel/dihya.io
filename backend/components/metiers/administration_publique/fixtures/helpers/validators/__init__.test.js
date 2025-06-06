// __init__.test.js – Test d'import du point d'entrée JS validators (fixtures/helpers/validators)
const validators = require('./validators');
test('import validators entrypoint (__init__.js)', () => {
  expect(validators).toBeDefined();
  expect(typeof validators).toBe('object');
});
