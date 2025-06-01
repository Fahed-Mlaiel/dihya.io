// test_arts.js - Test d'intégration arts
/**
 * @file Test d'intégration pour les arts (IA, sécurité, i18n, plugins)
 * @author Dihya
 * @version 1.0
 */
const { runPlugin } = require('../../../plugins');
const assert = require('assert');

describe('Arts Integration', () => {
  it('should run an arts plugin', () => {
    const plugin = { name: 'arts', run: () => 'ok' };
    runPlugin(plugin);
    assert.strictEqual(runPlugin('arts'), 'ok');
  });
});
