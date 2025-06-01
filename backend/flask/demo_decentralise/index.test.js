// tests/index.test.js — Tests automatisés pour la logique métier de la démo décentralisée
const { startDemo } = require('./index');

describe('Demo Decentralisée', () => {
  it('startDemo renvoie le message attendu', () => {
    expect(startDemo()).toMatch(/démarrée/i);
  });
});
