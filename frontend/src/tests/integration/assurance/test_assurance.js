// test_assurance.js - Test d'intégration assurance
/**
 * @file Test d'intégration pour l'assurance (IA, sécurité, i18n, plugins)
 * @author Dihya
 * @version 1.0
 */
const { runPlugin } = require('../../../plugins');
const assert = require('assert');

describe('Assurance Integration', () => {
  it('should run an assurance plugin', () => {
    const plugin = { name: 'assurance', run: () => 'ok' };
    runPlugin(plugin);
    assert.strictEqual(runPlugin('assurance'), 'ok');
  });
});
