// test_helper_validators.js – Tests helpers validators (JS)
const { isValidEmail } = require('../../../../fixtures/helpers/validators/helper_validators');
test('isValidEmail', () => {
  expect(isValidEmail('test@example.com')).toBe(true);
  expect(isValidEmail('invalid-email')).toBe(false);
});
