// fallback_services.test.js – Tests unitaires et edge cases JS
const { fallbackServices } = require('./fallback_services');

test('fallbackServices structure', () => {
  expect(typeof fallbackServices).toBe('object');
  expect(fallbackServices).toHaveProperty('id');
  expect(fallbackServices).toHaveProperty('description');
});
