// __init__.test.js – Test d'initialisation JS views (conformité, CI/CD)
const entry = require('./__init__');
describe('Initialisation JS views utils threed', () => {
  it('doit charger l’index sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
