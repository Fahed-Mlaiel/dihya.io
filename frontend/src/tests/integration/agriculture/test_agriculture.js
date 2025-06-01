// test_agriculture.js - Test d'intégration agriculture
/**
 * @file Test d'intégration pour l'agriculture (IA, sécurité, i18n, plugins)
 * @author Dihya
 * @version 1.0
 */
const { runPlugin } = require('../../../plugins');
const assert = require('assert');

describe('Agriculture Integration', () => {
  it('should run an agriculture plugin', () => {
    const plugin = { name: 'agri', run: () => 'ok' };
    runPlugin(plugin);
    assert.strictEqual(runPlugin('agri'), 'ok');
  });
});
