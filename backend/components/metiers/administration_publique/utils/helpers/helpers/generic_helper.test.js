// generic_helper.test.js
// Tests unitaires JS pour generic_helper
const { capitalizeFirst } = require('./generic_helper');

describe('capitalizeFirst', () => {
  it('capitalise la première lettre', () => {
    expect(capitalizeFirst('hello')).toBe('Hello');
  });
  it('gère le cas vide', () => {
    expect(capitalizeFirst('')).toBe('');
  });
});
