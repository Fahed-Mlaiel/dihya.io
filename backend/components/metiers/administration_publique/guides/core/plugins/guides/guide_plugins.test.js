// guide_plugins.test.js – Tests unitaires JS pour guide_plugins.js
const { getPluginsGuide } = require('./guide_plugins');
describe('guide_plugins.js', () => {
  it('doit retourner un guide plugins complet', () => {
    const guide = getPluginsGuide();
    expect(guide.title).toBe('Guide Plugins 3D');
    expect(Array.isArray(guide.bestPractices)).toBe(true);
    expect(guide.bestPractices).toContain('Utiliser des plugins typés et documentés');
    expect(Array.isArray(guide.integrationSteps)).toBe(true);
    expect(guide.integrationSteps).toContain('Importer les plugins via le point d’entrée');
  });
});
