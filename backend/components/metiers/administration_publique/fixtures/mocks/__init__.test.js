// Test d'import du module mocks (JS)
const mocks = require('./');
describe('mocks/__init__.js', () => {
  it('doit exposer les mocks et samples principaux', () => {
    expect(typeof mocks).toBe('object');
    expect(mocks).toHaveProperty('sample');
  });
});
