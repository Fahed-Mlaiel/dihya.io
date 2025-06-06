// __init__.test.js – Test d'initialisation JS metrics (conformité, CI/CD)
const entry = require('./__init__');
describe('Initialisation JS metrics utils threed', () => {
  it('doit charger l’index sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
