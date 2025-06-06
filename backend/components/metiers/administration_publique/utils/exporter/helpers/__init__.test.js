// Test d'import du point d'entrée helpers exporter (JS)
const helpers = require('./__init__.js');
describe('Import helpers exporter (__init__.js)', () => {
  it('should import without error', () => {
    expect(helpers).toBeDefined();
  });
});
