// Test d'import du point d'entrée samples i18n (JS)
const samples = require('./__init__.js');
describe('Import samples i18n (__init__.js)', () => {
  it('should import without error', () => {
    expect(samples).toBeDefined();
  });
});
