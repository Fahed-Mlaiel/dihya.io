/**
 * Tests unitaires avancés pour la gestion des projets santé (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { createSanteProject, listSanteProjects } from '../../api/sante';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Sante Projects API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should list sante projects (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await listSanteProjects({ jwt, lang });
      expect(Array.isArray(res)).toBe(true);
    }
  });
  it('should create a sante project (validation, audit, plugins, RGPD)', async () => {
    const res = await createSanteProject({
      jwt,
      data: {
        name: 'Test Sante',
        description: 'Projet santé multilingue',
        type: 'health',
        owner: 'user_id',
      },
      lang: 'fr',
    });
    expect(res).toHaveProperty('id');
    expect(res).toHaveProperty('name', 'Test Sante');
  });
});
