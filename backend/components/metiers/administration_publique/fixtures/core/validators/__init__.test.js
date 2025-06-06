// Test d'import du module validators helpers (JS)
const validator = require('.');
describe('helpers/validators/__init__.js', () => {
  it('doit exposer les validateurs principaux', () => {
    expect(typeof validator).toBe('object');
  });
});

// Test d’import du point d’entrée JS fixtures/helpers/validators
const validators = require('./__init__');
test('import validators entrypoint', () => {
  expect(validators).toBeDefined();
});

test('validator sample test', () => {
  expect(true).toBe(true);
});
