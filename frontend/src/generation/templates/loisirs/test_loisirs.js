// Test loisirs : couverture complète, sécurité, i18n, plugins
const { generateLoisirsProject } = require('./template');

describe('Loisirs Template', () => {
  it('génère un projet loisirs complet', () => {
    const project = generateLoisirsProject({
      locale: 'es',
      context: { description: 'Gestion des loisirs' },
      roles: ['admin', 'user', 'guest'],
      plugins: ['booking', 'events']
    });
    expect(project.titre).toBeDefined();
    expect(project.roles).toContain('user');
    expect(project.plugins).toContain('booking');
    expect(project.security.jwt).toBe(true);
    expect(project.ia.fallback).toContain('LLaMA');
    expect(project.seo.robots).toBe(true);
    expect(project.multitenancy).toBe(true);
  });
});
