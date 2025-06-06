// Test d'import du point d'entrée core i18n (JS)
const core = require('./__init__.js');
describe('Import core i18n (__init__.js)', () => {
  it('should import without error', () => {
    expect(core).toBeDefined();
  });
});
