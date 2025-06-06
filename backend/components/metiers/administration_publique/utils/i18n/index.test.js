// index.test.js – Test d'intégration du point d'entrée i18n JS
const i18n = require('./index');
describe('Entrée JS i18n utils threed', () => {
  it('doit exposer i18n', () => {
    expect(i18n).toHaveProperty('i18n');
  });
});
