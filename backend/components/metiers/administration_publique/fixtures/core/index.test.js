// index.test.js - Test d'intégration pour index.js (fixtures/core)
const core = require('./index');
describe('fixtures/core/index.js', () => {
  it('doit exposer les modèles, générateurs et samples principaux', () => {
    expect(core.sample3DModel).toBeDefined();
    expect(Array.isArray(core.assets)).toBe(true);
    expect(Array.isArray(core.users)).toBe(true);
    expect(typeof core.sampleModelsUltra).toBe('function');
    expect(typeof core.sampleUsersUltra).toBe('function');
  });
  it('doit exposer les générateurs principaux', () => {
    expect(typeof core.generateModel).toBe('function');
    expect(typeof core.generateUser).toBe('function');
  });
});
