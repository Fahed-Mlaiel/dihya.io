// Test d'import du point d'entrée core helpers (JS)
const core = require('./__init__.js');
describe('Import core helpers (__init__.js)', () => {
  it('should import without error', () => {
    expect(core).toBeDefined();
  });
});
