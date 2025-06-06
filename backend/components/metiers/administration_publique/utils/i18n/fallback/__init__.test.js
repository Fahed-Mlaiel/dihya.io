// Test d'import du point d'entrée fallback i18n (JS)
const fallback = require('./__init__.js');
describe('Import fallback i18n (__init__.js)', () => {
  it('should import without error', () => {
    expect(fallback).toBeDefined();
  });
});
