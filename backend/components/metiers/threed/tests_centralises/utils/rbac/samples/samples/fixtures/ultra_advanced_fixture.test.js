// Ultra advanced RBAC fixture test (clé en main)
const fixtures = require('./rbac_fixtures');
describe('Ultra Advanced RBAC Fixture', () => {
  it('should have a compliance officer with audit permission', () => {
    expect(fixtures.compliance_officer.permissions).toContain('audit');
  });
});
