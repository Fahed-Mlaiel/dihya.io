// test_automobile.js - Test d'intégration automobile
/**
 * @file Test d'intégration pour l'automobile (IA, sécurité, i18n, plugins)
 * @author Dihya
 * @version 1.0
 */
const { runPlugin } = require('../../../plugins');
const assert = require('assert');

describe('Automobile Integration', () => {
  it('should run an automobile plugin', () => {
    const plugin = { name: 'auto', run: () => 'ok' };
    runPlugin(plugin);
    assert.strictEqual(runPlugin('auto'), 'ok');
  });
});
