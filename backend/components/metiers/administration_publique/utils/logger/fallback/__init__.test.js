// Test d'import du point d'entrée fallback logger (JS)
const fallback = require('./__init__.js');
describe('Import fallback logger (__init__.js)', () => {
  it('should import without error', () => {
    expect(fallback).toBeDefined();
  });
});
