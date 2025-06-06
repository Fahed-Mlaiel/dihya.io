// rbac_helper.test.js
// Tests unitaires helpers RBAC JS
const { validateRole } = require('./rbac_helper');
describe('helpers RBAC JS', () => {
  it('valide un rôle', () => {
    expect(validateRole('admin')).toBe(true);
    expect(validateRole('')).toBe(false);
  });
});
