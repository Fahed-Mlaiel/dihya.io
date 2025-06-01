// test_beaute.js - Test d'intégration beauté
/**
 * @file Test d'intégration pour la beauté (IA, sécurité, i18n, plugins)
 * @author Dihya
 * @version 1.0
 */
const { runPlugin } = require('../../../plugins');
const assert = require('assert');

describe('Beauté Integration', () => {
  it('should run a beauté plugin', () => {
    const plugin = { name: 'beaute', run: () => 'ok' };
    runPlugin(plugin);
    assert.strictEqual(runPlugin('beaute'), 'ok');
  });
});
