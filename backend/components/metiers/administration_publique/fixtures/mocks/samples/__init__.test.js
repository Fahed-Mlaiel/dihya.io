// Test d'import du module mocks/samples (JS)
const sample = require('./');
describe('mocks/samples/__init__.js', () => {
  it('doit exposer la fixture sample', () => {
    expect(typeof sample).toBe('object');
  });
});
