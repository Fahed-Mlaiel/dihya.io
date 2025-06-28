// test_helper_audit.js – Tests helpers audit (JS)
const { logAuditEvent } = require('../../../../fixtures/helpers/audit/helper_audit');
test('logAuditEvent', () => {
  console.log = jest.fn();
  logAuditEvent('event');
  expect(console.log).toHaveBeenCalledWith('AUDIT: event');
});
