// Test d'import du point d'entrée helpers JS (clé en main)
const helpers = require('./__init__.js');
describe('Import helpers JS (__init__.js)', () => {
  it('should import without error', () => {
    expect(helpers).toBeDefined();
    expect(helpers).toHaveProperty('toCamelCase');
  });
});
