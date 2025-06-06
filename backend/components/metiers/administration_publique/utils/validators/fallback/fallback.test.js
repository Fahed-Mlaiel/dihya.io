// fallback.test.js
// Test unitaire avancé pour fallback validators (JS)
const fallback = require('./fallback');
describe('fallback validators JS', () => {
  it('doit fournir une solution de secours', () => {
    expect(typeof fallback.fallbackValidate).toBe('function');
  });
});
