// Ultra advanced RBAC mock test (clé en main)
const mocks = require('./rbac_mocks');
describe('Ultra Advanced RBAC Mock', () => {
  it('should have a test_user with test permission', () => {
    expect(mocks.test_user.permissions).toContain('test');
  });
});
