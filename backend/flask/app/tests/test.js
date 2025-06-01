// test.js – Tests globaux API (sécurité, RGPD, audit, multi-langues, plugins, mocks)

const assert = require('assert');
const fetch = require('node-fetch');
const fixtures = require('./integration/fixtures/index.js');

describe('API Global Tests', () => {
  it('doit retourner les oeuvres arts (auth)', async () => {
    const res = await fetch('http://localhost:5000/api/arts/oeuvres', {
      headers: { 'Authorization': `Bearer ${fixtures.user.token}` }
    });
    const data = await res.json();
    assert.strictEqual(res.status, 200);
    assert.ok(Array.isArray(data.data));
  });
  // ...autres tests globaux : sécurité, RGPD, audit, multi-langues, plugins, mocks...
});
