// Test d'import du point d'entrée helpers audit (JS)
const helpers = require('./__init__.js');
describe('Import helpers audit (__init__.js)', () => {
  it('should import without error', () => {
    expect(helpers).toBeDefined();
  });
});
