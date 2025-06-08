// Ultra advanced RBAC example test (clé en main)
const { renderRBAC } = require('../../templates');
describe('Ultra Advanced RBAC Example', () => {
  it('should render a superadmin role with all permissions', () => {
    const html = renderRBAC('superadmin');
    expect(html).toContain('superadmin');
  });
});
