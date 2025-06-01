/**
 * Test d'intégration avancé pour les utilitaires (validation, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const { SUPPORTED_LANGUAGES } = require('./utils');
describe('Utils Integration', () => {
  it('SUPPORTED_LANGUAGES contient toutes les langues requises', () => {
    expect(SUPPORTED_LANGUAGES).toEqual(
      expect.arrayContaining(['fr', 'en', 'ar', 'ber', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es'])
    );
  });
});
