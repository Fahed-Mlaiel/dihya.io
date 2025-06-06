// i18n.test.js – Tests unitaires JS pour i18n Threed
const i18n = require('./i18n');
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
