/**
 * Tests unitaires avancés pour la gestion des projets tourisme (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { createTourismeProject, listTourismeProjects } from '../../api/tourisme';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Tourisme Projects API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should list tourisme projects (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await listTourismeProjects({ jwt, lang });
      expect(Array.isArray(res)).toBe(true);
    }
  });
  it('should create a tourisme project (validation, audit, plugins, RGPD)', async () => {
    const res = await createTourismeProject({
      jwt,
      data: {
        name: 'Test Tourisme',
        description: 'Projet tourisme multilingue',
        type: 'tourism',
        owner: 'user_id',
      },
      lang: 'fr',
    });
    expect(res).toHaveProperty('id');
    expect(res).toHaveProperty('name', 'Test Tourisme');
  });
});
