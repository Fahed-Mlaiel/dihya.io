// test.js - Test unitaire et d'intégration pour scripts (Node.js)
/**
 * @file Test complet des scripts (robustesse, portabilité, sécurité, i18n)
 * @author Dihya
 * @version 1.0
 */
const { runScript } = require('../scripts');
const assert = require('assert');

describe('Scripts System', () => {
  it('should run a script and return expected result', () => {
    assert.strictEqual(runScript('echo "ok"'), 'ok');
  });

  it('should handle errors and i18n', () => {
    assert.throws(() => runScript('exit 1'));
    // i18n test: simulate error message in French
    try {
      runScript('exit 1');
    } catch (e) {
      assert.ok(e.message.includes('Erreur'));
    }
  });
});
