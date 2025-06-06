// rbac.integration.test.js – Tests d'intégration RBAC (multi-rôles, conformité RGPD)
const { hasPermission } = require('./rbac');

describe('RBAC – Intégration et conformité', () => {
  it('un utilisateur multi-rôles hérite de toutes les permissions de ses rôles', () => {
    const user = { roles: ['editor', 'viewer'] };
    expect(hasPermission(user, 'read')).toBe(true);
    expect(hasPermission(user, 'write')).toBe(true);
    expect(hasPermission(user, 'delete')).toBe(false);
  });

  it('aucun accès sans rôle', () => {
    const user = { roles: [] };
    expect(hasPermission(user, 'read')).toBe(false);
  });

  it('retourne false si user est null ou mal formé', () => {
    expect(hasPermission(null, 'read')).toBe(false);
    expect(hasPermission({}, 'read')).toBe(false);
  });
});
