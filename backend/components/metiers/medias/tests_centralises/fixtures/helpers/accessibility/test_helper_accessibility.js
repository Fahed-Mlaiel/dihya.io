// test_helper_accessibility.js – Tests helpers accessibility (JS)
const { isAccessible } = require('../../../../fixtures/helpers/accessibility/helper_accessibility');
test('isAccessible', () => {
  expect(isAccessible({ ariaLabel: 'label' })).toBe(true);
  expect(isAccessible({})).toBe(false);
});
