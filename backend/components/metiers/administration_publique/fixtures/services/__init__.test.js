// Test d'import du module services (JS)
const services = require('./');
describe('services/__init__.js', () => {
  it('doit exposer les services principaux', () => {
    expect(typeof services).toBe('object');
  });
});
