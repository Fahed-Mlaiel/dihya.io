// i18n_helper.test.js
// Tests unitaires JS pour i18n_helper
const { humanizeKey } = require('./i18n_helper');

describe('humanizeKey', () => {
  it('transforme une clé i18n en format lisible', () => {
    expect(humanizeKey('HELLO_WORLD')).toBe('Hello world');
  });
  it('gère le cas vide', () => {
    expect(humanizeKey('')).toBe('');
  });
});
