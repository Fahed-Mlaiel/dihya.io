// Test d'import du point d'entrée samples helpers (JS)
const samples = require('./__init__.js');
describe('Import samples helpers (__init__.js)', () => {
  it('should import without error', () => {
    expect(samples).toBeDefined();
  });
});
