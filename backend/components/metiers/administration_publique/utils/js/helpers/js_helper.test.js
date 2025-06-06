// js_helper.test.js
// Tests unitaires JS pour js_helper
const { capitalizeFirst } = require('./js_helper');

describe('capitalizeFirst', () => {
  it('capitalise la première lettre', () => {
    expect(capitalizeFirst('hello')).toBe('Hello');
  });
  it('gère le cas vide', () => {
    expect(capitalizeFirst('')).toBe('');
  });
});
