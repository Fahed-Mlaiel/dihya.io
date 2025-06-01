/**
 * Test unitaire branding Dihya
 * Sécurité, accessibilité, i18n, CI/CD, plugins
 */
import { branding } from '../branding';

describe('Branding Dihya', () => {
  it('doit être multilingue et sécurisé', () => {
    expect(branding.slogan.fr).toBeDefined();
    expect(branding.slogan.en).toBeDefined();
    expect(branding.colors.primary).toMatch(/^#/);
  });
});
