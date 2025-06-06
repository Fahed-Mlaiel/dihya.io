// Test d'import du point d'entrée core exporter (JS)
const core = require('./__init__.js');
describe('Import core exporter (__init__.js)', () => {
  it('should import without error', () => {
    expect(core).toBeDefined();
  });
});
