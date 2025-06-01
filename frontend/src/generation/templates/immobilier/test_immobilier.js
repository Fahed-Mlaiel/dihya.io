// Test de génération immobilier (exemple complet, sécurité, i18n, audit)
const { generateI18n } = require('../i18n/template');

describe('Immobilier Template', () => {
  it('génère les traductions pour chaque langue', () => {
    const context = { description: 'Gestion immobilière avancée' };
    const locales = ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es', 'amazigh'];
    locales.forEach(locale => {
      const i18n = generateI18n(locale, context);
      expect(i18n.titre).toBeDefined();
      expect(i18n.bienvenue).toBeDefined();
      expect(i18n.description).toBe('Gestion immobilière avancée');
    });
  });
});
