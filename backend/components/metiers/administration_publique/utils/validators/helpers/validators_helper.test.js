// validators_helper.test.js
// Tests unitaires JS pour validators_helper
const { isValidEmail } = require('./validators_helper');

describe('isValidEmail', () => {
  it('valide un email correct', () => {
    expect(isValidEmail('test@example.com')).toBe(true);
  });
  it('rejette un email incorrect', () => {
    expect(isValidEmail('test@.com')).toBe(false);
    expect(isValidEmail('test.com')).toBe(false);
  });
});
