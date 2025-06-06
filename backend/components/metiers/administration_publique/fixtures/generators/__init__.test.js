// Test d'import du module generators (JS)
const generator = require('.');

describe('generators/__init__.js', () => {
  it('doit exposer les fonctions principales', () => {
    expect(typeof generator.generateModel).toBe('function');
    expect(typeof generator.generateUser).toBe('function');
  });
});
