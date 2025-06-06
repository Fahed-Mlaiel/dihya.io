// __init__.test.js – Test d'import global du module rbac (JS)
const rbac = require('./__init__');

describe('__init__ (rbac)', () => {
  it('importe tous les utilitaires RBAC', () => {
    expect(rbac.hasPermission).toBeDefined();
    expect(rbac.getUserPermissions).toBeDefined();
    expect(Array.isArray(rbac.ROLES)).toBe(true);
    expect(typeof rbac.PERMISSIONS).toBe('object');
  });
});
