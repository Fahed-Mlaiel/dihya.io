// Ultra advanced RBAC template test (clé en main)
const { renderRBAC } = require('./rbac_templates');
describe('Ultra Advanced RBAC Template', () => {
  it('should render a compliance role', () => {
    expect(renderRBAC('compliance')).toContain('compliance');
  });
});
