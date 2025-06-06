// Test d'import du module services/core (JS)
const services = require('./');
describe('services/core/__init__.js', () => {
  it('doit exposer les services principaux', () => {
    expect(typeof services).toBe('object');
  });
});
