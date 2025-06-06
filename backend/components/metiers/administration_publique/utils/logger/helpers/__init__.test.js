// Test d'import du point d'entrée helpers logger (JS)
const helpers = require('./__init__.js');
describe('Import helpers logger (__init__.js)', () => {
  it('should import without error', () => {
    expect(helpers).toBeDefined();
  });
});
