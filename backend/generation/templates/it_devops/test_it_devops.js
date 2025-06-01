/**
 * Tests unitaires et d’intégration pour le template IT/DevOps
 * @module it_devops/test_it_devops
 * @author Dihya Team
 */

const { generateProject } = require('./template');

describe('IT/DevOps Template', () => {
  it('génère un projet complet avec sécurité, i18n, SEO, plugins, RGPD', () => {
    const config = { lang: 'fr', tenant: 'opsTeam', role: 'admin' };
    const project = generateProject(config);
    expect(project.routes).toBeDefined();
    expect(project.i18n.fr).toBeDefined();
    expect(project.seo).toBeDefined();
    expect(project.plugins).toContain('it_devops');
    expect(project.rgpd).toBe(true);
  });

  it('refuse une config incomplète', () => {
    expect(() => generateProject({})).toThrow();
  });
});
