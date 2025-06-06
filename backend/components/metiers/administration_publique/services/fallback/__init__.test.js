// __init__.test.js – Test d’intégration du point d’entrée JS fallback services
const entry = require('./__init__');
describe('Entrée JS fallback services', () => {
  it('doit exposer servicesTest', () => {
    expect(entry).toHaveProperty('servicesTest');
  });
});
