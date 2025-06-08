const fixtures = require('./rbac_fixtures');
describe('RBAC Fixtures', () => {
  it('should have admin with delete permission', () => {
    expect(fixtures.admin.permissions).toContain('delete');
  });
});
