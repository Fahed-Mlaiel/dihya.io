// rbac_core.test.js
// Tests unitaires core RBAC JS
const { checkPermission, getUserRoles } = require('./rbac_core');
describe('core RBAC JS', () => {
  it('vérifie la permission', () => {
    expect(checkPermission({permissions:['read']}, 'read')).toBe(true);
    expect(checkPermission({permissions:['read']}, 'write')).toBe(false);
  });
  it('récupère les rôles', () => {
    expect(getUserRoles({roles:['admin']})).toContain('admin');
  });
});
