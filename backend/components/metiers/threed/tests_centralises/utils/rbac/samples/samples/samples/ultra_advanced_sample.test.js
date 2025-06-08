// Ultra advanced RBAC sample test (clé en main)
const sample = require('./sample_advanced');
describe('Ultra Advanced RBAC Sample', () => {
  it('should have a backup_admin role', () => {
    expect(sample.role).toBe('backup_admin');
  });
});
