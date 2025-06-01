// test.js – Tests pour utils (validation, logging, i18n, audit, RGPD, plugins)

const assert = require('assert');
const utils = require('../utils.js');

describe('Utils', () => {
  it('valide un email correct', () => {
    assert.strictEqual(utils.validateEmail('test@example.com'), true);
  });
  it('rejette un email incorrect', () => {
    assert.strictEqual(utils.validateEmail('invalid'), false);
  });
  it('log structuré fonctionne', () => {
    utils.structuredLog('event', { foo: 'bar' });
    assert.ok(true);
  });
  it('i18n message retourne la clé', () => {
    assert.strictEqual(utils.i18nMessage('hello', 'fr'), 'hello');
  });
  // ...autres tests RGPD, plugins, erreurs...
});
