// Test juridique : couverture complète, sécurité, i18n, plugins
const { generateJuridiqueProject } = require('./template');

describe('Juridique Template', () => {
  it('génère un projet juridique complet', () => {
    const project = generateJuridiqueProject({
      locale: 'fr',
      context: { description: 'Gestion contrats' },
      roles: ['admin', 'juriste', 'guest'],
      plugins: ['audit', 'signature']
    });
    expect(project.titre).toBeDefined();
    expect(project.roles).toContain('juriste');
    expect(project.plugins).toContain('signature');
    expect(project.security.jwt).toBe(true);
    expect(project.ia.fallback).toContain('LLaMA');
    expect(project.seo.robots).toBe(true);
    expect(project.multitenancy).toBe(true);
  });
});
