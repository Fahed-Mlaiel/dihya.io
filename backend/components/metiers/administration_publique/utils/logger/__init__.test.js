// __init__.test.js – Test d'initialisation JS logger
const entry = require('./__init__');
describe('Initialisation JS logger utils threed', () => {
  it('doit charger l’index sans erreur', () => {
    expect(entry).toBeDefined();
  });
});
