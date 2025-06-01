/**
 * Tests unitaires et d’intégration pour le template intelligence artificielle
 * @module intelligence_artificielle/test_intelligence_artificielle
 * @author Dihya Team
 */

const { generateProject } = require('./template');

describe('Intelligence Artificielle Template', () => {
  it('génère un projet complet avec sécurité, i18n, SEO, plugins, RGPD, fallback IA', () => {
    const config = { lang: 'fr', tenant: 'labIA', role: 'admin' };
    const project = generateProject(config);
    expect(project.routes).toBeDefined();
    expect(project.i18n.fr).toBeDefined();
    expect(project.seo).toBeDefined();
    expect(project.plugins).toContain('intelligence_artificielle');
    expect(project.iaFallback).toBeDefined();
    expect(project.rgpd).toBe(true);
  });

  it('refuse une config incomplète', () => {
    expect(() => generateProject({})).toThrow();
  });
});
