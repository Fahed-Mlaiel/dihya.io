// test_validators.js – Tests unitaires et edge cases validators JS
const validators = require('./validators');

test('isValid3DModel returns true for valid model', () => {
  expect(validators.isValid3DModel({ id: 'x', vertices: [] })).toBe(true);
  expect(validators.isValid3DModel({ id: 1, vertices: null })).toBe(false);
});

test('isValidUser returns true for valid user', () => {
  expect(validators.isValidUser({ id: 'u', role: 'admin' })).toBe(true);
  expect(validators.isValidUser({ id: 1, role: null })).toBe(false);
});

test('isFixtureAccessible returns true for accessible fixture', () => {
  expect(validators.isFixtureAccessible({ description: 'ok' })).toBe(true);
  expect(validators.isFixtureAccessible({ description: 123 })).toBe(false);
});
