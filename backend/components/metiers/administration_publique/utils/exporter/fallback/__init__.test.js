// Test d'import du point d'entrée fallback exporter (JS)
const fallback = require('./__init__.js');
describe('Import fallback exporter (__init__.js)', () => {
  it('should import without error', () => {
    expect(fallback).toBeDefined();
  });
});
