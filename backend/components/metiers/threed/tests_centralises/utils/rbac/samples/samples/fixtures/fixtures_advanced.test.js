const fixtures = require('./fixtures_advanced');
describe('Fixtures Advanced', () => {
  it('should have superadmin with all permissions', () => {
    expect(fixtures.superadmin.permissions).toContain('*');
  });
});
