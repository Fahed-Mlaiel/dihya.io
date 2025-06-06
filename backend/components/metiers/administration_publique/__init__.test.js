// Test d’intégration du point d’entrée JS pour le module Threed
const entry = require('./__init__.js');

describe('Entrée JS du module Threed', () => {
  it('doit exposer les sous-modules principaux', () => {
    expect(entry).toHaveProperty('api');
    expect(entry).toHaveProperty('services');
    expect(entry).toHaveProperty('templates');
    expect(entry).toHaveProperty('views');
  });
});
