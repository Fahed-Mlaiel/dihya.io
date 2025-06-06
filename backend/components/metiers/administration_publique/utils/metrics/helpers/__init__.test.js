// Test d'import du point d'entrée helpers metrics (JS)
const helpers = require('./__init__.js');
describe('Import helpers metrics (__init__.js)', () => {
  it('should import without error', () => {
    expect(helpers).toBeDefined();
  });
});
