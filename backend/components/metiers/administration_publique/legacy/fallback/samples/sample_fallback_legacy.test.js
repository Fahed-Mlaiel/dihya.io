// sample_fallback_legacy.test.js – Test JS exemple fallback legacy
const { sampleFallbackLegacy } = require('./sample_fallback_legacy');
test('sampleFallbackLegacy fonctionne', () => {
  expect(sampleFallbackLegacy({ a: 1 })).toEqual({ a: 1, fallback: true });
  expect(sampleFallbackLegacy()).toEqual({ fallback: true, empty: true });
});
