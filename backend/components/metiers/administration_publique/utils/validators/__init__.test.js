// __init__.test.js – Test d'initialisation JS validators (conformité, CI/CD)
const entry = require('./__init__');
describe('Initialisation JS validators utils threed', () => {
  it('doit charger l’index sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
