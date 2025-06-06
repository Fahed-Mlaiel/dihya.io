// sample_fallback_case.test.js – Tests unitaires et edge cases JS
const { sampleFallbackCase } = require('./sample_fallback_case');

test('sampleFallbackCase structure', () => {
  expect(typeof sampleFallbackCase).toBe('object');
  expect(sampleFallbackCase).toHaveProperty('id');
  expect(sampleFallbackCase).toHaveProperty('description');
  expect(sampleFallbackCase).toHaveProperty('status');
});

test('sampleFallbackCase status', () => {
  expect(['compliant', 'partial', 'non-compliant']).toContain(sampleFallbackCase.status);
});
