// rbac_utils.test.js – Tests unitaires ultra avancés pour rbac_utils.js
const rbac = require('./rbac_utils');

describe('rbac_utils – Permissions', () => {
  it('admin a toutes les permissions', () => {
    const user = { roles: ['admin'] };
    rbac.PERMISSIONS.admin.forEach(p => {
      expect(rbac.hasPermission(user, p)).toBe(true);
    });
  });
  it('auditor peut lire et auditer, mais pas écrire', () => {
    const user = { roles: ['auditor'] };
    expect(rbac.hasPermission(user, 'read')).toBe(true);
    expect(rbac.hasPermission(user, 'audit')).toBe(true);
    expect(rbac.hasPermission(user, 'write')).toBe(false);
  });
  it('multi-rôles hérite de toutes les permissions', () => {
    const user = { roles: ['editor', 'auditor'] };
    expect(rbac.hasPermission(user, 'write')).toBe(true);
    expect(rbac.hasPermission(user, 'audit')).toBe(true);
  });
  it('getUserPermissions retourne toutes les permissions uniques', () => {
    const user = { roles: ['editor', 'auditor'] };
    const perms = rbac.getUserPermissions(user);
    expect(perms).toContain('write');
    expect(perms).toContain('audit');
    expect(perms).toContain('read');
  });
});
