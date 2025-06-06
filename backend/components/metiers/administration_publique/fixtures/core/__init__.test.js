// Test d'import du module fixtures.core (JS)
const core = require('./');
describe('fixtures/core/__init__.js', () => {
  it('doit exposer les modèles, générateurs et samples principaux', () => {
    expect(core.sample3DModel).toBeDefined();
    expect(typeof core.generateModel).toBe('function');
    expect(typeof core.sampleModelsUltra).toBe('function');
    expect(typeof core.sampleUsersUltra).toBe('function');
  });
});
