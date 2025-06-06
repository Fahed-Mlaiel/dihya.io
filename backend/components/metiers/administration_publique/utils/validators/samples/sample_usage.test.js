// sample_usage.test.js
// Tests unitaires avancés pour les exemples validators JS
const validators = require('../core/validators');
const data = require('./sample_validators_data.json');

describe('Sample usage validators JS', () => {
  it('valide un email', () => {
    expect(validators.validateEmail(data.email)).toBe(true);
  });
  it('valide un champ obligatoire', () => {
    expect(validators.validateRequired(data.requiredField)).toBe(true);
  });
  it('échoue sur un champ vide', () => {
    expect(validators.validateRequired('')).toBe(false);
  });
});
