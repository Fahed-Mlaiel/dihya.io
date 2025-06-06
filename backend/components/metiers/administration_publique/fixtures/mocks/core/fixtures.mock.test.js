// fixtures.mock.test.js - Tests unitaires pour fixtures.mock.js (mocks/core)
const mock = require('./fixtures.mock');
describe('mocks/core/fixtures.mock.js', () => {
  it('doit exposer les mocks principaux', () => {
    expect(typeof mock).toBe('object');
  });
});
