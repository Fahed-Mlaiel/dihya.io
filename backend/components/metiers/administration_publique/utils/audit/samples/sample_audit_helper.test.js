// Test du helper d’audit d’exemple (JS)
const { sampleAuditLog } = require('./sample_audit_helper');
describe('sampleAuditLog', () => {
  it('should log and return true', () => {
    expect(sampleAuditLog('user123', 'LOGIN')).toBe(true);
  });
});
