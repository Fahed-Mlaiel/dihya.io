// test_helper_transformers.js – Tests helpers transformers (JS)
const { toUppercase } = require('../../../../fixtures/helpers/transformers/helper_transformers');
test('toUppercase', () => {
  expect(toUppercase('abc')).toBe('ABC');
});
