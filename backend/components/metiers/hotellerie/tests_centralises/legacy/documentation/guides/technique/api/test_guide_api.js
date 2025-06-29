const guideApiExemple = require('../../../../../../legacy/documentation/guides/technique/api/guide_api_exemple');

// Test ultra avancé pour guide API JS
describe('Guide API', () => {
  it('doit valider le guide API', () => {
    const logs = [];
    const spy = jest.spyOn(console, 'log').mockImplementation(msg => logs.push(msg));
    guideApiExemple();
    expect(logs[0]).toMatch(/Guide API legacy Hotellerie/);
    expect(logs.some(l => l.includes('OpenAPI'))).toBe(true);
    expect(logs.some(l => l.includes('Authentification'))).toBe(true);
    expect(logs.some(l => l.includes('Sécurité'))).toBe(true);
    expect(logs.some(l => l.includes('Bonnes pratiques'))).toBe(true);
    spy.mockRestore();
  });
  it('doit gérer les cas limites (appel détourné)', () => {
    const logs = [];
    const spy = jest.spyOn(console, 'log').mockImplementation(msg => logs.push(msg));
    guideApiExemple.call(null);
    expect(logs.length).toBeGreaterThan(0);
    spy.mockRestore();
  });
});
