// index.test.js - Test d'intégration pour index.js (services)
const services = require('./index');
describe('services/index.js', () => {
  it('doit exposer les services principaux', () => {
    expect(typeof services).toBe('object');
    expect(services).toHaveProperty('getEnvironnement'); // à adapter selon les exports réels
  });
});
