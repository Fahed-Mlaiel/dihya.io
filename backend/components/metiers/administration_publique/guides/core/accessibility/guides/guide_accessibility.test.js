// guide_accessibility.test.js - Tests ultra avancés pour guide_accessibility.js (guides/core/accessibility/guides)
const { getAccessibilityGuide } = require('./guide_accessibility');
describe('guide_accessibility.js', () => {
  it('doit retourner un guide d’accessibilité complet', () => {
    const guide = getAccessibilityGuide();
    expect(guide.title).toBe('Guide Accessibilité 3D');
    expect(Array.isArray(guide.bestPractices)).toBe(true);
    expect(guide.bestPractices).toContain('Respecter les standards WCAG 2.1');
    expect(Array.isArray(guide.integrationSteps)).toBe(true);
    expect(guide.integrationSteps).toContain('Analyser les besoins utilisateurs');
  });
});
