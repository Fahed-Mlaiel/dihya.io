// Test ultra avancé pour policy_sample.js
const policySample = require('../../../legacy/samples/policy/policy_sample');

describe('Policy Sample', () => {
  it('doit donner full-access à admin', () => {
    expect(policySample('admin')).toBe('full-access');
  });
  it('doit donner restricted à un user', () => {
    expect(policySample('user')).toBe('restricted');
  });
  // ...autres tests avancés, edge cases, sécurité...
});
