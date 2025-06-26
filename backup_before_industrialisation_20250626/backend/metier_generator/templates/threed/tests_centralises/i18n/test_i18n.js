// Tests avancés pour l’i18n threed
const { translate, getAvailableLanguages } = require('../../api/i18n');
describe('i18n threed', () => {
  it('doit traduire une clé existante', () => {
    expect(translate('welcome', 'fr')).toBe('Bienvenue');
  });
  it('doit retourner la liste des langues disponibles', () => {
    const langs = getAvailableLanguages();
    expect(langs).toContain('fr');
    expect(langs).toContain('en');
  });
  it('doit retourner la clé si la traduction n’existe pas', () => {
    expect(translate('not_found', 'zz')).toBe('not_found');
  });
});
