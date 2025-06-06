// rbac.test.js – Tests unitaires du module RBAC (logique métier, conformité)
const { ROLES, PERMISSIONS, hasPermission } = require('./rbac');

describe('RBAC – Logique métier', () => {
  it('admin a toutes les permissions', () => {
    const user = { roles: ['admin'] };
    expect(hasPermission(user, 'read')).toBe(true);
    expect(hasPermission(user, 'write')).toBe(true);
    expect(hasPermission(user, 'delete')).toBe(true);
    expect(hasPermission(user, 'manage_users')).toBe(true);
  });

  it('editor ne peut pas supprimer ni gérer les utilisateurs', () => {
    const user = { roles: ['editor'] };
    expect(hasPermission(user, 'read')).toBe(true);
    expect(hasPermission(user, 'write')).toBe(true);
    expect(hasPermission(user, 'delete')).toBe(false);
    expect(hasPermission(user, 'manage_users')).toBe(false);
  });

  it('viewer ne peut que lire', () => {
    const user = { roles: ['viewer'] };
    expect(hasPermission(user, 'read')).toBe(true);
    expect(hasPermission(user, 'write')).toBe(false);
  });
});
