const mocks = require('./rbac_mocks');
describe('RBAC Mocks', () => {
  it('should have guest with no permissions', () => {
    expect(mocks.guest.permissions).toHaveLength(0);
  });
});
