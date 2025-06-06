// __init__.test.js – Test d’intégration du point d’entrée JS helpers services
const entry = require('./__init__');
describe('Entrée JS helpers services', () => {
  it('doit exposer servicesHelper', () => {
    expect(entry).toHaveProperty('servicesHelper');
  });
});
