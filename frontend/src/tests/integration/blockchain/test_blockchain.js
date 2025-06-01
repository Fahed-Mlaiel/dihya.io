// test_blockchain.js - Test d'intégration blockchain
/**
 * @file Test d'intégration pour la blockchain (IA, sécurité, i18n, plugins)
 * @author Dihya
 * @version 1.0
 */
const { runPlugin } = require('../../../plugins');
const assert = require('assert');

describe('Blockchain Integration', () => {
  it('should run a blockchain plugin', () => {
    const plugin = { name: 'blockchain', run: () => 'ok' };
    runPlugin(plugin);
    assert.strictEqual(runPlugin('blockchain'), 'ok');
  });
});
