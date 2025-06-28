// test_helper_security.js – Tests helpers security (JS)
const { hashPassword } = require('../../../../fixtures/helpers/security/helper_security');
test('hashPassword', () => {
  expect(hashPassword('abc')).toBe(hashPassword('abc'));
});
