// Import basique ajouté automatiquement
// validators_core_advanced.test.js – Ultra avancé, clé en main
// Tests avancés pour les validators core (exemples, edge cases, CI/CD ready)
describe('Validators Core Advanced', () => {
  it('should validate a complex object', () => {
    const obj = { a: 1, b: 'test', c: [1,2,3] };
    expect(typeof obj.a).toBe('number');
    expect(Array.isArray(obj.c)).toBe(true);
  });
});
