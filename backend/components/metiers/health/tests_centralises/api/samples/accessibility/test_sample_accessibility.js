// test_sample_accessibility.js – Test ultra avancé des samples accessibilité API Health (centralisé)

const { sampleAccessibilityCheck } = require('../../../api/samples/accessibility');

describe('Samples Accessibilité API Health', () => {
  it('doit valider l’accessibilité d’une ressource complète', () => {
    const data = { label: 'Ultra', lang: 'fr' };
    const result = sampleAccessibilityCheck(data);
    expect(result.accessible).toBe(true);
    expect(result.lang).toBe('fr');
  });

  it('doit détecter une ressource non accessible (label manquant)', () => {
    const data = { lang: 'fr' };
    const result = sampleAccessibilityCheck(data);
    expect(result.accessible).toBe(false);
    expect(result.reason).toBe('missing_label');
  });
});
