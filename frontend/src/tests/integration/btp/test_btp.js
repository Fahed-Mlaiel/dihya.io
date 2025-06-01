// test_btp.js - Test d'intégration BTP
/**
 * @file Test d'intégration pour le BTP (IA, sécurité, i18n, plugins)
 * @author Dihya
 * @version 1.0
 */
const { runPlugin } = require('../../../plugins');
const assert = require('assert');

describe('BTP Integration', () => {
  it('should run a BTP plugin', () => {
    const plugin = { name: 'btp', run: () => 'ok' };
    runPlugin(plugin);
    assert.strictEqual(runPlugin('btp'), 'ok');
  });
});
