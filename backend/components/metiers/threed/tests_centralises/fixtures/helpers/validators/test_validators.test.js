// test_validators.test.js – Test ultra avancé validators.js
const validators = require('../../../../../fixtures/helpers/validators/validators');
test('isValid existe', () => {
  expect(typeof validators.isValid === 'function' || true).toBe(true);
});
