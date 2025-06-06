// __init__.test.js – Test d'initialisation JS exporter
const entry = require('./__init__');
describe('Initialisation JS exporter utils threed', () => {
  it('doit charger tous les sous-modules sans erreur', () => {
    expect(entry).toHaveProperty('sampleExport');
    expect(entry).toHaveProperty('exporter_helper');
    expect(entry).toHaveProperty('fallback');
    // Ajoutez d'autres propriétés selon les sous-modules exposés
  });
});
