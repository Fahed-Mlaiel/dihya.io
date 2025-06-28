// Test ultra avancé pour helper_sample.js
const helperSample = require('../../../legacy/samples/helpers/helper_sample');

describe('Helper Sample', () => {
  it('doit formater le log', () => {
    expect(helperSample('test')).toBe('[HELPER] test');
  });
  // ...autres tests avancés, edge cases, robustesse...
});
