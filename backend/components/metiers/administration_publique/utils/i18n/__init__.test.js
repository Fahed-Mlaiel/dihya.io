// __init__.test.js – Test d'initialisation JS i18n
const entry = require('./__init__');
describe('Initialisation JS i18n utils threed', () => {
  it('doit charger tous les sous-modules sans erreur', () => {
    expect(entry).toHaveProperty('sampleI18n');
    expect(entry).toHaveProperty('i18n_helper');
    expect(entry).toHaveProperty('fallback');
    // Ajoutez d'autres propriétés selon les sous-modules exposés
  });
});
