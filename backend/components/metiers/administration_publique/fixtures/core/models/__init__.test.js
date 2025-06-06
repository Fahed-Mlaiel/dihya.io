// Test d'import du module models (JS)
const models = require('./');

describe('models/__init__.js', () => {
  it('doit exposer les fixtures principales', () => {
    expect(models.sample3DModel).toBeDefined();
    expect(Array.isArray(models.assets)).toBe(true);
    expect(Array.isArray(models.users)).toBe(true);
    expect(models.sample).toBeDefined();
  });
});
