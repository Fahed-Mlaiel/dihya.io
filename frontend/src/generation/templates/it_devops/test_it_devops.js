// Test IT/DevOps : couverture complète, sécurité, i18n, plugins
const { generateITDevOpsProject } = require('./template');

describe('IT/DevOps Template', () => {
  it('génère un projet IT/DevOps complet', () => {
    const project = generateITDevOpsProject({
      locale: 'en',
      context: { description: 'CI/CD Pipeline' },
      roles: ['admin', 'devops', 'guest'],
      plugins: ['monitoring', 'alerting']
    });
    expect(project.titre).toBeDefined();
    expect(project.roles).toContain('devops');
    expect(project.plugins).toContain('alerting');
    expect(project.security.jwt).toBe(true);
    expect(project.ia.fallback).toContain('LLaMA');
    expect(project.seo.robots).toBe(true);
    expect(project.multitenancy).toBe(true);
  });
});
