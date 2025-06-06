// __init__.test.js – Test d’intégration du point d’entrée JS core services
const entry = require('./__init__');
describe('Entrée JS core services', () => {
  it('doit exposer les modules principaux', () => {
    expect(entry).toHaveProperty('serviceThreed');
    expect(entry).toHaveProperty('servicesController');
    expect(entry).toHaveProperty('servicesThreed');
    expect(entry).toHaveProperty('api');
  });
});
