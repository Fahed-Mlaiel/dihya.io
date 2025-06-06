// Test d'import du point d'entrée samples audit (JS)
const samples = require('./__init__.js');
describe('Import samples audit (__init__.js)', () => {
  it('should import without error', () => {
    expect(samples).toBeDefined();
  });
});
