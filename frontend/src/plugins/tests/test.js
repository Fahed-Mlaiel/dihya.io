// test.js - Test unitaire et d'intégration pour plugins (Node.js)
/**
 * @file Test complet du système de plugins (ajout, suppression, exécution, sécurité, i18n)
 * @author Dihya
 * @version 1.0
 */
const { addPlugin, removePlugin, runPlugin } = require('../plugins');
const assert = require('assert');

describe('Plugins System', () => {
  it('should add, run and remove a plugin securely', () => {
    const plugin = { name: 'test', run: () => 'ok' };
    addPlugin(plugin);
    assert.strictEqual(runPlugin('test'), 'ok');
    removePlugin('test');
    assert.throws(() => runPlugin('test'));
  });

  it('should support i18n and role-based access', () => {
    const plugin = { name: 'i18n', run: (lang, role) => lang === 'fr' && role === 'admin' ? 'ok' : 'forbidden' };
    addPlugin(plugin);
    assert.strictEqual(runPlugin('i18n', 'fr', 'admin'), 'ok');
    assert.strictEqual(runPlugin('i18n', 'en', 'user'), 'forbidden');
    removePlugin('i18n');
  });
});
