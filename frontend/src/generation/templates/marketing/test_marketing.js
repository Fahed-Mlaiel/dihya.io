// Test marketing : couverture complète, sécurité, i18n, plugins
const { generateMarketingProject } = require('./template');

describe('Marketing Template', () => {
  it('génère un projet marketing complet', () => {
    const project = generateMarketingProject({
      locale: 'en',
      context: { description: 'Campagne digitale' },
      roles: ['admin', 'marketer', 'guest'],
      plugins: ['analytics', 'automation']
    });
    expect(project.titre).toBeDefined();
    expect(project.roles).toContain('marketer');
    expect(project.plugins).toContain('analytics');
    expect(project.security.jwt).toBe(true);
    expect(project.ia.fallback).toContain('LLaMA');
    expect(project.seo.robots).toBe(true);
    expect(project.multitenancy).toBe(true);
  });
});
