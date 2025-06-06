// test_utils.js - Tests unitaires JS pour les utilitaires Threed
const audit = require('../utils/audit');
const i18n = require('../utils/i18n');

describe('Audit Threed', () => {
  it('doit retourner un score correct', () => {
    const result = audit.auditThreed({ status: 'active' });
    expect(result.score).toBe(97.0);
  });
});

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
