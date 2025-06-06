// Test d'import du point d'entrée helpers/helpers (JS)
const helpers = require('./__init__.js');
describe('Import helpers/helpers (__init__.js)', () => {
  it('should import without error', () => {
    expect(helpers).toBeDefined();
  });
});
