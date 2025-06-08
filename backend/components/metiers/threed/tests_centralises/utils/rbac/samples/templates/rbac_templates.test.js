const { renderRBAC } = require('./rbac_templates');
describe('RBAC Templates', () => {
  it('should render role', () => {
    expect(renderRBAC('admin')).toContain('admin');
  });
});
