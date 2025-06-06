// i18n_utils.test.js – Tests unitaires ultra avancés pour i18n_utils.js
const i18n = require('./i18n_utils');

describe('i18n_utils – Traduction', () => {
  it('traduit dans toutes les langues supportées', () => {
    i18n.SUPPORTED_LANGS.forEach(lang => {
      expect(i18n.translate('Test', lang)).toMatch(new RegExp(`\[${lang.toUpperCase()}\]`));
    });
  });
  it('retourne le message brut si langue non supportée', () => {
    expect(i18n.translate('Test', 'xx')).toBe('Test');
  });
});

describe('i18n_utils – Langues supportées', () => {
  it('reconnaît les langues supportées', () => {
    expect(i18n.isSupportedLang('fr')).toBe(true);
    expect(i18n.isSupportedLang('en')).toBe(true);
    expect(i18n.isSupportedLang('xx')).toBe(false);
  });
});
