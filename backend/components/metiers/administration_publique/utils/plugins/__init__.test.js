// __init__.test.js – Test d'initialisation JS plugins (conformité, CI/CD)
const entry = require('./__init__');
describe('Initialisation JS plugins utils threed', () => {
  it('doit charger l’index sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
