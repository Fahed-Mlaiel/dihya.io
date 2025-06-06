// Test d'import du point d'entrée samples logger (clé en main)
const samples = require('./__init__.js');
describe('Import samples logger (__init__.js)', () => {
  it('should import without error', () => {
    expect(samples).toBeDefined();
    expect(samples).toHaveProperty('sampleLoggerHelper');
  });
});
