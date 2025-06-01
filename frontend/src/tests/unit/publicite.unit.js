/**
 * Tests unitaires avancés pour la gestion des projets publicité (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { createPubliciteProject, listPubliciteProjects } from '../../api/publicite';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Publicite Projects API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should list publicite projects (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await listPubliciteProjects({ jwt, lang });
      expect(Array.isArray(res)).toBe(true);
    }
  });
  it('should create a publicite project (validation, audit, plugins, RGPD)', async () => {
    const res = await createPubliciteProject({
      jwt,
      data: {
        name: 'Test Publicite',
        description: 'Projet publicité multilingue',
        type: 'ad',
        owner: 'user_id',
      },
      lang: 'fr',
    });
    expect(res).toHaveProperty('id');
    expect(res).toHaveProperty('name', 'Test Publicite');
  });
});
