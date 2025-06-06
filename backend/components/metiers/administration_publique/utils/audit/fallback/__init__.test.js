// Test d'import du point d'entrée fallback audit (JS)
const fallback = require('./__init__.js');
describe('Import fallback audit (__init__.js)', () => {
  it('should import without error', () => {
    expect(fallback).toBeDefined();
  });
});
