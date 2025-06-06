// index.test.js – Test d'intégration du point d'entrée helpers JS
const helpers = require('./index');
describe('Entrée JS helpers utils threed', () => {
  it('doit exposer formatDate, isObject, deepClone', () => {
    expect(helpers).toHaveProperty('formatDate');
    expect(helpers).toHaveProperty('isObject');
    expect(helpers).toHaveProperty('deepClone');
  });
});
