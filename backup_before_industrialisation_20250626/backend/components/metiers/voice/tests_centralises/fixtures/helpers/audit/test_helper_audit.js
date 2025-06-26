/* global console, jest */
// test_helper_audit.js – Tests helpers audit (JS)
const { logAuditEvent } = require('../../../../fixtures/helpers/audit/helper_audit');
test('logAuditEvent', () => {
  const spy = jest.spyOn(console, 'log').mockImplementation(() => {});
  logAuditEvent('event');
  expect(spy).toHaveBeenCalledWith('AUDIT: event');
  spy.mockRestore();
});
