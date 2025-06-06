// Test d'import du point d'entrée fallback helpers (JS)
const fallback = require('./__init__.js');
describe('Import fallback helpers (__init__.js)', () => {
  it('should import without error', () => {
    expect(fallback).toBeDefined();
  });
});
