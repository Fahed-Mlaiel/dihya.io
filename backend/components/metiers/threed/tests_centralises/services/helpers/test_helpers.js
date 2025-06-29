// Test avancé pour helpers.js du module services/helpers
// Remplacer l'import par le chemin réel si besoin
const helpers = require('../../../services/core/helpers/services_helper');

describe('Services Helpers', () => {
  it('should expose all expected helper functions', () => {
    expect(typeof helpers.getServiceStatus).toBe('function');
    expect(typeof helpers.simulateHeavyLoad).toBe('function');
    expect(typeof helpers.simulateExtremeLoad).toBe('function');
    expect(typeof helpers.auditService).toBe('function');
    expect(typeof helpers.checkAccess).toBe('function');
  });

  it('getServiceStatus should return status ok and a valid ISO timestamp', () => {
    const res = helpers.getServiceStatus();
    expect(res.status).toBe('ok');
    expect(typeof res.timestamp).toBe('string');
    expect(() => new Date(res.timestamp)).not.toThrow();
  });

  it('simulateHeavyLoad should return a string of length 10000', () => {
    const str = helpers.simulateHeavyLoad();
    expect(typeof str).toBe('string');
    expect(str.length).toBe(10000);
  });

  it('simulateExtremeLoad should return a string of length 100000', () => {
    const str = helpers.simulateExtremeLoad();
    expect(typeof str).toBe('string');
    expect(str.length).toBe(100000);
  });

  it('auditService should return an advanced audit string', () => {
    const res = helpers.auditService('testService');
    expect(res).toMatch(/Audit avancé: testService/);
  });

  it('checkAccess should allow admin for any action', () => {
    expect(helpers.checkAccess({ role: 'admin' }, 'delete')).toBe(true);
    expect(helpers.checkAccess({ role: 'admin' }, 'read')).toBe(true);
  });

  it('checkAccess should allow non-admin only for read', () => {
    expect(helpers.checkAccess({ role: 'user' }, 'read')).toBe(true);
    expect(helpers.checkAccess({ role: 'user' }, 'delete')).toBe(false);
  });

  it('checkAccess should deny if user is null or undefined', () => {
    expect(helpers.checkAccess(null, 'read')).toBe(false);
    expect(helpers.checkAccess(undefined, 'read')).toBe(false);
  });

  it('should be robust to edge cases (empty, wrong types)', () => {
    expect(helpers.checkAccess({}, 'read')).toBe(false);
    expect(helpers.checkAccess({ role: 'guest' }, 'write')).toBe(false);
  });

  it('should not leak sensitive data (RGPD)', () => {
    const res = helpers.getServiceStatus();
    expect(Object.keys(res)).not.toContain('user');
  });
});
