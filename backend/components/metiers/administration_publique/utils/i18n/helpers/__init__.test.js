// Test d'import du point d'entrée helpers i18n (JS)
const helpers = require('./__init__.js');
describe('Import helpers i18n (__init__.js)', () => {
  it('should import without error', () => {
    expect(helpers).toBeDefined();
  });
});
