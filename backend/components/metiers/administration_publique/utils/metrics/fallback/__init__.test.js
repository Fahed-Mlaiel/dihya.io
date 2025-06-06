// Test d'import du point d'entrée fallback metrics (JS)
const fallback = require('./__init__.js');
describe('Import fallback metrics (__init__.js)', () => {
  it('should import without error', () => {
    expect(fallback).toBeDefined();
  });
});
