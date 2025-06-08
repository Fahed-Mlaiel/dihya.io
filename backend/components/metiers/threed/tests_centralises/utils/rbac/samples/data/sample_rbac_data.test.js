// Test ultra avancé pour les données RBAC
const data = require('./sample_rbac_data.json');
describe('RBAC Data Sample', () => {
  it('should contain admin role', () => {
    expect(data.roles).toContain('admin');
  });
});
