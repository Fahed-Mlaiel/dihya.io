// Test ultra avancé pour rbac_sample.js
const rbacSample = require('../../../legacy/samples/rbac/rbac_sample');

describe('RBAC Sample', () => {
  it('doit donner tous les droits à admin', () => {
    expect(rbacSample('alice', 'admin')).toMatch('tous les droits');
  });
  it('doit restreindre un user non admin', () => {
    expect(rbacSample('bob', 'user')).toMatch('accès restreint');
  });
  it('doit gérer un user vide', () => {
    expect(rbacSample('', 'admin')).toMatch('tous les droits');
    expect(rbacSample('', 'user')).toMatch('accès restreint');
  });
  it('doit gérer un user null', () => {
    expect(rbacSample(null, 'admin')).toMatch('tous les droits');
    expect(rbacSample(null, 'user')).toMatch('accès restreint');
  });
  it('doit gérer un rôle inconnu', () => {
    expect(rbacSample('eve', 'guest')).toMatch('accès restreint');
  });
  // ...autres tests avancés, edge cases, sécurité...
});
