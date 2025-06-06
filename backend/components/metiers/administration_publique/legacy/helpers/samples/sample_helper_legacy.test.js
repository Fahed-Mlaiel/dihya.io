// sample_helper_legacy.test.js – Test JS exemple helper legacy
const { sampleHelperLegacy } = require('./sample_helper_legacy');
test('sampleHelperLegacy fonctionne', () => {
  expect(sampleHelperLegacy({ a: 1 })).toEqual({ a: 1, helper: true });
  expect(sampleHelperLegacy()).toEqual({ helper: true, empty: true });
});
