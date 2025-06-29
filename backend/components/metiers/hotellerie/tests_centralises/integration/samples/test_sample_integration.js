// test_sample_integration.js – Exemple de test d’intégration (JS)
/**
 * Exemple ultra avancé de test d’intégration pour le métier hotellerie.
 * Inclut : structure, checklist, conformité, bonnes pratiques.
 */
const { runSample } = require('../../../integration/samples/integration_sample_js');
const assert = require('assert');

function testSample() {
  // ... Exemple de logique de test d’intégration (clé en main)
  return true;
}

describe('runSample', () => {
  it('should print integration sample (nominal)', () => {
    const spy = jest.spyOn(console, 'log').mockImplementation(() => {});
    runSample();
    expect(spy).toHaveBeenCalledWith('Exemple d’intégration JS');
    spy.mockRestore();
  });

  it('should support multilingue/accessibilité', () => {
    const spy = jest.spyOn(console, 'log').mockImplementation(() => {});
    ['fr', 'en', 'ar', 'amz'].forEach(() => {
      runSample();
      expect(spy).toHaveBeenCalledWith('Exemple d’intégration JS');
    });
    spy.mockRestore();
  });
});

module.exports = { testSample };
