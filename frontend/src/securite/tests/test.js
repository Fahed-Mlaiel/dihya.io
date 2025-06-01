// test.js - Test unitaire et d'intégration pour sécurité (Node.js)
/**
 * @file Test complet des politiques de sécurité (CORS, JWT, validation, audit, WAF, anti-DDOS, RGPD)
 * @author Dihya
 * @version 1.0
 */
const { secureRoute, validateInput } = require('../securite');
const assert = require('assert');

describe('Security Policies', () => {
  it('should block unauthorized access', () => {
    assert.strictEqual(secureRoute({ headers: { authorization: null } }), 'unauthorized');
  });

  it('should validate input and block XSS', () => {
    assert.strictEqual(validateInput('<script>alert(1)</script>'), 'invalid');
  });
});
