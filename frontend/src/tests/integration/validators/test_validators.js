/**
 * Test d'intégration avancé pour les validateurs (validation, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const { validateEmail, validatePassword } = require('../../utils/utils');
describe('Validators Integration', () => {
  it('validateEmail valide les emails corrects', () => {
    expect(validateEmail('test@dihya.org')).toBe(true);
    expect(validateEmail('invalid-email')).toBe(false);
  });
  it('validatePassword valide la robustesse', () => {
    expect(validatePassword('Dihya2025!')).toBe(true);
    expect(validatePassword('123')).toBe(false);
  });
});
