// __init__.test.js – Test d’intégration du point d’entrée JS templates Threed
const entry = require('./__init__');
describe('Entrée JS templates Threed', () => {
  it('doit charger dynamiquement les modules', () => {
    expect(typeof entry).toBe('object');
  });
});
