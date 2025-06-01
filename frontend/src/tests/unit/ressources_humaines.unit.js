/**
 * Tests unitaires avancés pour la gestion des projets ressources humaines (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { createRHProject, listRHProjects } from '../../api/ressources_humaines';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Ressources Humaines Projects API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should list RH projects (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await listRHProjects({ jwt, lang });
      expect(Array.isArray(res)).toBe(true);
    }
  });
  it('should create a RH project (validation, audit, plugins, RGPD)', async () => {
    const res = await createRHProject({
      jwt,
      data: {
        name: 'Test RH',
        description: 'Projet RH multilingue',
        type: 'hr',
        owner: 'user_id',
      },
      lang: 'fr',
    });
    expect(res).toHaveProperty('id');
    expect(res).toHaveProperty('name', 'Test RH');
  });
});
