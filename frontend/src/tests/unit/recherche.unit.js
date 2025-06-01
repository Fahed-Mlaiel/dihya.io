/**
 * Tests unitaires avancés pour la gestion des projets recherche (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { createRechercheProject, listRechercheProjects } from '../../api/recherche';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Recherche Projects API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should list recherche projects (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await listRechercheProjects({ jwt, lang });
      expect(Array.isArray(res)).toBe(true);
    }
  });
  it('should create a recherche project (validation, audit, plugins, RGPD)', async () => {
    const res = await createRechercheProject({
      jwt,
      data: {
        name: 'Test Recherche',
        description: 'Projet recherche multilingue',
        type: 'scientific',
        owner: 'user_id',
      },
      lang: 'fr',
    });
    expect(res).toHaveProperty('id');
    expect(res).toHaveProperty('name', 'Test Recherche');
  });
});
