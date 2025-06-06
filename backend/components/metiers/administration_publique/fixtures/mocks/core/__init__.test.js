// Test d'import du module mocks/core (JS)
const mock = require('./');
describe('mocks/core/__init__.js', () => {
  it('doit exposer les mocks principaux', () => {
    expect(typeof mock).toBe('object');
  });
});
