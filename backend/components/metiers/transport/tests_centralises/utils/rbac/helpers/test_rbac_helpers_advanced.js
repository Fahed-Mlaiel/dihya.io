const { validateRole } = require('../../../../utils/rbac/helpers/rbac_helper');

describe('RBAC Helpers JS – Ultra Advanced', () => {
  it('valide un rôle non vide', () => {
    expect(validateRole('admin')).toBe(true);
    expect(validateRole('user')).toBe(true);
  });

  it('rejette un rôle vide ou non string', () => {
    expect(validateRole('')).toBe(false);
    expect(validateRole(null)).toBe(false);
    expect(validateRole(undefined)).toBe(false);
    expect(validateRole(123)).toBe(false);
    expect(validateRole({})).toBe(false);
  });

  it('gère les caractères spéciaux et accessibilité', () => {
    expect(validateRole('Éditeur')).toBe(true);
  });

  it('auditabilité: la sortie est toujours booléenne', () => {
    expect(typeof validateRole('admin')).toBe('boolean');
  });
});
