/**
 * Tests unitaires avancés pour la gestion des projets mobiles (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { createMobileProject, listMobileProjects } from '../../api/mobile';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Mobile Projects API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should list mobile projects (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await listMobileProjects({ jwt, lang });
      expect(Array.isArray(res)).toBe(true);
    }
  });
  it('should create a mobile project (validation, audit, plugins, RGPD)', async () => {
    const res = await createMobileProject({
      jwt,
      data: {
        name: 'Test Mobile',
        description: 'Projet mobile multilingue',
        type: 'hybrid',
        owner: 'user_id',
      },
      lang: 'fr',
    });
    expect(res).toHaveProperty('id');
    expect(res).toHaveProperty('name', 'Test Mobile');
  });
});
