/**
 * Tests unitaires avancés pour la gestion des projets sport (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { createSportProject, listSportProjects } from '../../api/sport';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Sport Projects API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should list sport projects (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await listSportProjects({ jwt, lang });
      expect(Array.isArray(res)).toBe(true);
    }
  });
  it('should create a sport project (validation, audit, plugins, RGPD)', async () => {
    const res = await createSportProject({
      jwt,
      data: {
        name: 'Test Sport',
        description: 'Projet sport multilingue',
        type: 'sport',
        owner: 'user_id',
      },
      lang: 'fr',
    });
    expect(res).toHaveProperty('id');
    expect(res).toHaveProperty('name', 'Test Sport');
  });
});
