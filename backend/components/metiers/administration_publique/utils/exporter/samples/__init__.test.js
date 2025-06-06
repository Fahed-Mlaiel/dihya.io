// Test d'import du point d'entrée samples exporter (JS)
const samples = require('./__init__.js');
describe('Import samples exporter (__init__.js)', () => {
  it('should import without error', () => {
    expect(samples).toBeDefined();
  });
});
