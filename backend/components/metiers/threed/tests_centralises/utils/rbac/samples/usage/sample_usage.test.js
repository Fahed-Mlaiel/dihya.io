const { renderRBAC } = require('../templates/rbac_templates');
describe('Usage Example', () => {
  it('should print user role', () => {
    expect(renderRBAC('user')).toContain('user');
  });
});
