// Test d'import du point d'entrée core audit (JS)
const core = require('./__init__.js');
describe('Import core audit (__init__.js)', () => {
  it('should import without error', () => {
    expect(core).toBeDefined();
  });
});
