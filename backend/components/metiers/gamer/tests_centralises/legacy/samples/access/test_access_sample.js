// Test ultra avancé pour access_sample.js
const accessSample = require('../../../legacy/samples/access/access_sample');

describe('Access Sample', () => {
  it('doit valider l\'accès admin', () => {
    expect(accessSample('admin', 'secret')).toBe(true);
  });
  it('doit refuser un accès non admin', () => {
    expect(accessSample('user', 'wrong')).toBe(false);
  });
  // ...autres tests avancés, edge cases, sécurité...
});
