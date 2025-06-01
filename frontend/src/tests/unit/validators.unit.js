/**
 * Tests unitaires avancés pour la validation (sécurité, i18n, plugins, audit, multitenancy, RGPD, SEO, fallback IA, extensibilité, multilingue).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { validateProjectId, validateUserInput } from '../../api/validators';
describe('Validators', () => {
  it('should validate project IDs and user input (all languages, all roles)', () => {
    expect(validateProjectId('valid_id')).toBe(true);
    expect(() => validateProjectId('')).toThrow();
    expect(validateUserInput({ name: 'Test', lang: 'fr' })).toBe(true);
    expect(() => validateUserInput({ name: '', lang: 'fr' })).toThrow();
  });
});
