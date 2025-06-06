// helpers_services.test.js – Tests unitaires et edge cases JS
const { checkService, auditService } = require('./helpers_services');

test('checkService returns true for ok', () => {
  expect(checkService({ status: 'ok', uptime: 99 })).toBe(true);
  expect(checkService({ status: 'fail', uptime: 10 })).toBe(false);
});

test('auditService returns audit object', () => {
  const result = auditService({ status: 'ok', uptime: 99 });
  expect(typeof result).toBe('object');
  expect(result).toHaveProperty('score');
  expect(result).toHaveProperty('compliant');
});
