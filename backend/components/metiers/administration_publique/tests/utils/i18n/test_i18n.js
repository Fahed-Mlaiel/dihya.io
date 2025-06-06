// test_i18n.js – Tests JS avancés d'internationalisation pour Threed
const i18n = require('../utils/i18n');

describe('i18n Threed', () => {
  it('doit traduire en français', () => {
    expect(i18n.i18n('Test', 'fr')).toMatch('[FR]');
  });
  it('doit traduire en anglais', () => {
    expect(i18n.i18n('Test', 'en')).toMatch('[EN]');
  });
  it('doit fallback sur la valeur brute', () => {
    expect(i18n.i18n('Test', 'es')).toBe('Test');
  });
});
