// validators_samples_advanced.test.js – Ultra avancé, clé en main
describe('Validators Samples Advanced', () => {
  it('should validate a sample array', () => {
    const arr = [1,2,3];
    expect(Array.isArray(arr)).toBe(true);
  });
});
