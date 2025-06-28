const modelTechniqueExemple = require('../../../../../../legacy/documentation/models/exemples/model_technique_exemple');

// Test ultra avancé pour model exemple JS
describe('Model Exemple', () => {
  it('doit valider le modèle exemple', () => {
    const logs = [];
    const spy = jest.spyOn(console, 'log').mockImplementation(msg => logs.push(msg));
    modelTechniqueExemple();
    expect(logs[0]).toMatch(/Modèle technique legacy Construction/);
    expect(logs.some(l => l.includes('Architecture'))).toBe(true);
    expect(logs.some(l => l.includes('API'))).toBe(true);
    expect(logs.some(l => l.includes('Sécurité'))).toBe(true);
    expect(logs.some(l => l.includes('Déploiement'))).toBe(true);
    spy.mockRestore();
  });
  it('doit gérer les cas limites (appel détourné)', () => {
    const logs = [];
    const spy = jest.spyOn(console, 'log').mockImplementation(msg => logs.push(msg));
    modelTechniqueExemple.call(null);
    expect(logs.length).toBeGreaterThan(0);
    spy.mockRestore();
  });
});
