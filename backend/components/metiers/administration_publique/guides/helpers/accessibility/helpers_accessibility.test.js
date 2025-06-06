// helpers_accessibility.test.js – Tests unitaires et edge cases JS
const { checkAccessibility, auditAccessibility } = require('./helpers_accessibility');

test('checkAccessibility returns true for compliant', () => {
  expect(checkAccessibility({ contrast: 8, keyboard: true })).toBe(true);
  expect(checkAccessibility({ contrast: 2, keyboard: false })).toBe(false);
});

test('auditAccessibility returns audit object', () => {
  const result = auditAccessibility({ contrast: 8, keyboard: true });
  expect(typeof result).toBe('object');
  expect(result).toHaveProperty('score');
  expect(result).toHaveProperty('compliant');
});
