/**
 * Tests unitaires et d’intégration pour le template immobilier
 * @module immobilier/test_immobilier
 * @author Dihya Team
 */

const { generateProject } = require('./template');

describe('Immobilier Template', () => {
  it('génère un projet complet avec sécurité, i18n, SEO, plugins, RGPD', () => {
    const config = { lang: 'fr', tenant: 'agenceY', role: 'admin' };
    const project = generateProject(config);
    expect(project.routes).toBeDefined();
    expect(project.i18n.fr).toBeDefined();
    expect(project.seo).toBeDefined();
    expect(project.plugins).toContain('immobilier');
    expect(project.rgpd).toBe(true);
  });

  it('refuse une config incomplète', () => {
    expect(() => generateProject({})).toThrow();
  });
});
