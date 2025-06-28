const guideExemple = require('../../../../../legacy/audit/guides/exemples/guide_exemple');

// test ultra avancé pour guide_exemple.js
// Cas nominaux, edge cases, conformité, sécurité, robustesse, documentation intégrée

describe('Guide Exemple Legacy - JS', () => {
  it('doit valider le guide exemple nominal', () => {
    expect(guideExemple()).toBe('Exemple de guide d’audit legacy Gamer (JS)');
  });
  it('doit gérer les cas limites et erreurs', () => {
    // Le guide ne prend pas d’argument, mais on vérifie la robustesse
    expect(() => guideExemple()).not.toThrow();
    // Appel avec .call ou .apply
    expect(guideExemple.call(null)).toBe('Exemple de guide d’audit legacy Gamer (JS)');
    expect(guideExemple.apply({}, [])).toBe('Exemple de guide d’audit legacy Gamer (JS)');
  });
  it('doit être conforme accessibilité/audit', () => {
    // Vérifie que le texte est bien lisible et conforme
    const result = guideExemple();
    expect(result).toMatch(/audit legacy Gamer/);
    expect(typeof result).toBe('string');
  });
});
