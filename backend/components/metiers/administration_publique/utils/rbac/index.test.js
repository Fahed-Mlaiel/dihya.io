// index.test.js
// Test d'intégration du point d'entrée RBAC JS
const rbac = require('./index');
describe('Entrée JS RBAC', () => {
  it('doit exposer les fonctions core, helpers et fallback', () => {
    expect(rbac).toHaveProperty('checkPermission');
    expect(rbac).toHaveProperty('getUserRoles');
    expect(rbac).toHaveProperty('validateRole');
    expect(rbac).toHaveProperty('fallbackPolicy');
  });
});
