// audit_helper.test.js
// Tests unitaires JS pour audit_helper
const { generateAuditLog } = require('./audit_helper');

describe('generateAuditLog', () => {
  it('génère un log d\'audit structuré', () => {
    const log = generateAuditLog('LOGIN', { user: 'alice' });
    expect(log).toHaveProperty('timestamp');
    expect(log.action).toBe('LOGIN');
    expect(log.user).toBe('alice');
  });
});
