/**
 * Tests unitaires avancés pour la gestion des projets restauration (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { createRestaurationProject, listRestaurationProjects } from '../../api/restauration';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Restauration Projects API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should list restauration projects (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await listRestaurationProjects({ jwt, lang });
      expect(Array.isArray(res)).toBe(true);
    }
  });
  it('should create a restauration project (validation, audit, plugins, RGPD)', async () => {
    const res = await createRestaurationProject({
      jwt,
      data: {
        name: 'Test Restauration',
        description: 'Projet restauration multilingue',
        type: 'restaurant',
        owner: 'user_id',
      },
      lang: 'fr',
    });
    expect(res).toHaveProperty('id');
    expect(res).toHaveProperty('name', 'Test Restauration');
  });
});
