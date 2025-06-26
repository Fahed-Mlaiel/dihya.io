// test_helper_core.js – Tests helpers core (JS)
const { coreBusinessLogic } = require('../../../../fixtures/helpers/core/helper_core');
test('coreBusinessLogic addition', () => {
  expect(coreBusinessLogic(2, 3)).toBe(5);
});
