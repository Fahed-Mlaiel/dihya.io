// test_sample_input.js
// Tests avancés pour sample_input.js (validation d'input)
const validateInput = require('../../../../samples/validators/input/sample_input');

describe('validateInput', () => {
  it('valide une chaîne non vide', () => {
    expect(validateInput('valide')).toBe(true);
  });
  it('rejette une chaîne vide', () => {
    expect(validateInput('')).toBe(false);
  });
  it('rejette un type non string', () => {
    expect(validateInput(123)).toBe(false);
  });
});
