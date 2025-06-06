// Test d'import du point d'entrée fallback JS (clé en main)
const fallback = require('./__init__.js');
describe('Import fallback JS (__init__.js)', () => {
  it('should import without error', () => {
    expect(fallback).toBeDefined();
    expect(fallback).toHaveProperty('fallbackValue');
  });
});
