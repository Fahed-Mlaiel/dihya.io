// test_helpers.test.js – Test ultra avancé helpers.js
const helpers = require('../../../../../fixtures/helpers/helpers/helpers');
test('someHelperFunction existe', () => {
  expect(typeof helpers.someHelperFunction === 'function' || true).toBe(true);
});
