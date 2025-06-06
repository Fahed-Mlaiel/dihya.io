// helpers_plugins.test.js – Tests unitaires et edge cases JS
const { checkPlugin, auditPlugin } = require('./helpers_plugins');

test('checkPlugin returns true for enabled', () => {
  expect(checkPlugin({ enabled: true, version: '1.0.0' })).toBe(true);
  expect(checkPlugin({ enabled: false, version: null })).toBe(false);
});

test('auditPlugin returns audit object', () => {
  const result = auditPlugin({ enabled: true, version: '1.0.0' });
  expect(typeof result).toBe('object');
  expect(result).toHaveProperty('score');
  expect(result).toHaveProperty('compliant');
});
