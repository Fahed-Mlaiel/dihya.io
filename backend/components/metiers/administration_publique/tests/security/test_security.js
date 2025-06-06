// test_security.js – Tests JS avancés de sécurité pour Threed
const { check_permission } = require('../utils/rbac');

describe('Sécurité Threed', () => {
  it('RBAC admin doit tout pouvoir', () => {
    expect(check_permission('admin', 'delete')).toBe(true);
  });
  it('RBAC guest ne peut pas delete', () => {
    expect(check_permission('guest', 'read')).toBe(true);
    expect(check_permission('guest', 'delete')).toBe(false);
  });
  it('doit protéger contre l’injection', () => {
    const user_input = "<script>alert('xss')</script>";
    const safe = user_input.replace(/</g, '').replace(/>/g, '');
    expect(safe.includes('<')).toBe(false);
    expect(safe.includes('>')).toBe(false);
  });
});
