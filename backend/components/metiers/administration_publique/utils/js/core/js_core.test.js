// js_core.test.js
// Tests unitaires JS pour js_core
const { isPlainObject } = require('./js_core');

describe('isPlainObject', () => {
  it('retourne true pour un objet pur', () => {
    expect(isPlainObject({ a: 1 })).toBe(true);
  });
  it('retourne false pour un tableau', () => {
    expect(isPlainObject([1,2,3])).toBe(false);
  });
  it('retourne false pour null', () => {
    expect(isPlainObject(null)).toBe(false);
  });
});
