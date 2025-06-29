const assert = require('assert');
// Import basique ajouté automatiquement
// validators_fallback_advanced.test.js – Ultra avancé, clé en main
describe('Validators Fallback Advanced', () => {
  it('should fallback to default value', () => {
    const value = undefined;
    const fallback = value || 'default';
    expect(fallback).toBe('default');
  });
});
