// Test d'import du point d'entrée core JS (clé en main)
const core = require('./__init__.js');
describe('Import core JS (__init__.js)', () => {
  it('should import without error', () => {
    expect(core).toBeDefined();
    expect(core).toHaveProperty('isPlainObject');
  });
});
