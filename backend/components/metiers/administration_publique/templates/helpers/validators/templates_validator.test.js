// templates_validator.test.js – Tests unitaires JS pour validateurs templates Threed
const validator = require('./templates_validator');
describe('Validator templates Threed (JS)', () => {
  test('isValidTemplateFile fonctionne', () => {
    expect(typeof validator.isValidTemplateFile).toBe('function');
  });
  test('validateTemplateContent fonctionne', () => {
    expect(typeof validator.validateTemplateContent).toBe('function');
  });
});
