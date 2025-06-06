// __init__.test.js – Test d'initialisation JS
const entry = require('./__init__');
describe('Initialisation JS utils threed', () => {
  it('doit charger l’index sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
