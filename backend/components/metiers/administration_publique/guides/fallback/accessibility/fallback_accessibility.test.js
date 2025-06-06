// fallback_accessibility.test.js – Tests unitaires et edge cases JS
const { fallbackAccessibility } = require('./fallback_accessibility');

test('fallbackAccessibility structure', () => {
  expect(typeof fallbackAccessibility).toBe('object');
  expect(fallbackAccessibility).toHaveProperty('id');
  expect(fallbackAccessibility).toHaveProperty('description');
});

test('fallbackAccessibility status', () => {
  expect(['compliant', 'partial', 'non-compliant']).toContain(fallbackAccessibility.status);
});
