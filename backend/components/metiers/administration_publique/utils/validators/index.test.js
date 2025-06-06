// index.test.js – Test d'intégration du point d'entrée validators JS (conformité, CI/CD)
const validators = require('./index');
describe('Entrée JS validators utils threed', () => {
  it('doit exposer validateEmail, validateRequired, helpers et fallback', () => {
    expect(validators).toHaveProperty('validateEmail');
    expect(validators).toHaveProperty('validateRequired');
    expect(validators).toHaveProperty('validatorsHelper');
    expect(validators).toHaveProperty('fallbackValidate');
  });
});
