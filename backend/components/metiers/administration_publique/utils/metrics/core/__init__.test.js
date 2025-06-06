// Test d'import du point d'entrée core metrics (JS)
const core = require('./__init__.js');
describe('Import core metrics (__init__.js)', () => {
  it('should import without error', () => {
    expect(core).toBeDefined();
  });
});
