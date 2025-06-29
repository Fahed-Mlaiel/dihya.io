// Test ultra avancé pour validator_sample.js
const validatorSample = require('../../../legacy/samples/validators/validator_sample');

describe('Validator Sample', () => {
  it('valide une chaîne correcte', () => {
    expect(validatorSample('abcd')).toBe(true);
  });
  it('refuse une chaîne trop courte', () => {
    expect(validatorSample('ab')).toBe(false);
  });
  // ...autres tests avancés, edge cases, robustesse...
});
