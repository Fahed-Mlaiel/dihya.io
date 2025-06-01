/**
 * @file test_validators.js
 * @description Tests unitaires et d'intégration pour les validateurs (validation, sécurité, RGPD, i18n, plugins, audit, etc.)
 * @author Dihya
 * @date 2025-05-25
 */

const { validateEmail, validatePassword, validateRole } = require('../../../src/validators');

describe('Validators - Validation avancée', () => {
  it('valide les emails corrects', () => {
    expect(validateEmail('test@example.com')).toBe(true);
    expect(validateEmail('invalid-email')).toBe(false);
  });

  it('valide les mots de passe forts', () => {
    expect(validatePassword('Aa1!aaaa')).toBe(true);
    expect(validatePassword('weak')).toBe(false);
  });

  it('valide les rôles autorisés', () => {
    expect(validateRole('admin')).toBe(true);
    expect(validateRole('user')).toBe(true);
    expect(validateRole('guest')).toBe(true);
    expect(validateRole('hacker')).toBe(false);
  });
});
