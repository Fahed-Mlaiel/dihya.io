// Test d'intégration du point d'entrée __init__.js (JS)
const entry = require('./__init__.js');

describe('__init__.js API Threed', () => {
  it('doit exporter api et ThreedController', () => {
    expect(entry).toHaveProperty('api');
    expect(entry).toHaveProperty('ThreedController');
  });
  it('doit être un objet métier conforme', () => {
    expect(typeof entry).toBe('object');
  });
});
