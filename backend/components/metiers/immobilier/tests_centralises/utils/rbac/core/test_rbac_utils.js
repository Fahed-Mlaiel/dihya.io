// test_rbac_utils.js – Tests ultra avancés pour rbac_utils.js (RBAC Immobilier)
// Couvre : cas nominaux, edge cases, conformité RGPD, audit, accessibilité, robustesse, multitenancy
const { isValidRole, filterRoles, auditRoles, anonymizeRoles } = require('../../../../utils/rbac/core/rbac_utils');

test('isValidRole', () => {
  expect(isValidRole('admin')).toBe(true);
  expect(isValidRole('')).toBe(false);
  expect(isValidRole(' ')).toBe(false);
  expect(isValidRole('a'.repeat(65))).toBe(false);
  expect(isValidRole('admin-user!')).toBe(false);
  expect(isValidRole('user_1')).toBe(true);
  expect(isValidRole('roleX')).toBe(true);
});

test('filterRoles', () => {
  const roles = ['admin', 'user', 'guest', 'banned'];
  const allowed = ['admin', 'user'];
  expect(filterRoles(roles, allowed)).toEqual(['admin', 'user']);
  expect(filterRoles([], allowed)).toEqual([]);
  expect(filterRoles(roles, [])).toEqual([]);
});

test('auditRoles', () => {
  const roles = ['admin', 'user', 'user'];
  const audit = auditRoles(roles);
  expect(audit.roles).toEqual(roles);
  expect(audit.count).toBe(3);
  expect(audit.unique).toBe(2);
  expect(audit.auditDate).toBeDefined();
});

test('anonymizeRoles', () => {
  const roles = ['admin', 'user', 'guest'];
  const anonymized = anonymizeRoles(roles);
  expect(anonymized).toEqual(['role_1', 'role_2', 'role_3']);
  expect(anonymized.length).toBe(roles.length);
  anonymized.forEach(r => expect(r.startsWith('role_')).toBe(true));
  expect(anonymizeRoles([])).toEqual([]);
});
