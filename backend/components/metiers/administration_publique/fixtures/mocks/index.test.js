// index.test.js - Test d'intégration pour index.js (mocks)
const mocks = require('./index');
describe('mocks/index.js', () => {
  it('doit exposer les mocks principaux', () => {
    expect(typeof mocks).toBe('object');
  });
  it('doit exposer la fixture sample', () => {
    expect(mocks).toHaveProperty('sample');
  });
});
