// Test industrie : couverture complète, sécurité, i18n, plugins
const { generateIndustrieProject } = require('./template');

describe('Industrie Template', () => {
  it('génère un projet industrie complet', () => {
    const project = generateIndustrieProject({
      locale: 'de',
      context: { description: 'Fabrik 4.0' },
      roles: ['admin', 'user', 'guest'],
      plugins: ['monitoring']
    });
    expect(project.titre).toBeDefined();
    expect(project.roles).toContain('admin');
    expect(project.plugins).toContain('monitoring');
    expect(project.security.jwt).toBe(true);
    expect(project.ia.fallback).toContain('LLaMA');
    expect(project.seo.robots).toBe(true);
    expect(project.multitenancy).toBe(true);
  });
});
