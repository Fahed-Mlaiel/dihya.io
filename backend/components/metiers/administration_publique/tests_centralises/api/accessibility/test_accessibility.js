const mockFunctions = require("../../../mocks/functions_mock");
// test_accessibility.js – Test ultra avancé d'accessibilité API administration_publique (centralisé)

const { checkAccessibility } = require('../../../api/accessibility/accessibility');

describe('Accessibilité API administration_publique', () => {
  it('doit valider l’accessibilité d’une ressource complète', () => {
    const data = { label: 'Ultra', lang: 'fr' };
    const result = checkAccessibility(data);
    expect(result).toBe(true);
  });

  it('doit détecter une ressource non accessible (label manquant)', () => {
    const data = { lang: 'fr' };
    const result = checkAccessibility(data);
    expect(result).toBe(false);
  });
});
