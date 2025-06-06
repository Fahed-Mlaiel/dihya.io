// sample_usage.test.js
// Tests unitaires avancés pour les exemples RBAC JS
const rbac = require('../core/rbac_core');
const data = require('./sample_rbac_data.json');

describe('Sample usage RBAC JS', () => {
  it('vérifie la permission read', () => {
    expect(rbac.checkPermission(data.user, 'read')).toBe(true);
  });
  it('vérifie la permission inconnue', () => {
    expect(rbac.checkPermission(data.user, 'unknown')).toBe(false);
  });
  it('récupère les rôles', () => {
    expect(rbac.getUserRoles(data.user)).toContain('admin');
  });
});
