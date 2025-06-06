// Test d'import du point d'entrée core logger (JS)
const core = require('./__init__.js');
describe('Import core logger (__init__.js)', () => {
  it('should import without error', () => {
    expect(core).toBeDefined();
  });
});
