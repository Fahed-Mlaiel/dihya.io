// __init__.test.js – Test d'initialisation JS helpers
const entry = require('./__init__');
describe('Initialisation JS helpers utils threed', () => {
  it('doit charger tous les sous-modules sans erreur', () => {
    expect(entry).toHaveProperty('sampleHelper');
    expect(entry).toHaveProperty('utils_helper');
    expect(entry).toHaveProperty('fallback');
    // Ajoutez d'autres propriétés selon les sous-modules exposés
  });
});
