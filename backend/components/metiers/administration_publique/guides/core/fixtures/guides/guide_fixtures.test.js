// guide_fixtures.test.js – Tests unitaires JS pour guide_fixtures.js
const { getFixturesGuide } = require('./guide_fixtures');
describe('guide_fixtures.js', () => {
  it('doit retourner un guide de fixtures complet', () => {
    const guide = getFixturesGuide();
    expect(guide.title).toBe('Guide Fixtures 3D');
    expect(Array.isArray(guide.bestPractices)).toBe(true);
    expect(guide.bestPractices).toContain('Utiliser des fixtures typées et documentées');
    expect(Array.isArray(guide.integrationSteps)).toBe(true);
    expect(guide.integrationSteps).toContain('Importer les fixtures via le point d’entrée');
  });
});
