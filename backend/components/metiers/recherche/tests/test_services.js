// test_services.js – Test avancé des services Environnement (Node.js/Jest)
const services = require('../fixtures/services_environnement');

describe('Services Environnement', () => {
  it('doit contenir au moins un service', () => {
    expect(Array.isArray(services)).toBe(true);
    expect(services.length).toBeGreaterThan(0);
    expect(services[0]).toHaveProperty('service');
  });
});
