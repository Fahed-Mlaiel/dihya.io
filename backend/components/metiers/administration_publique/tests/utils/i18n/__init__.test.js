// __init__.test.js – Test d'import global du module i18n (JS)
const i18n = require('./__init__');

describe('__init__ (i18n)', () => {
  it('importe tous les utilitaires i18n', () => {
    expect(i18n.translate).toBeDefined();
    expect(i18n.isSupportedLang).toBeDefined();
    expect(Array.isArray(i18n.SUPPORTED_LANGS)).toBe(true);
  });
});
