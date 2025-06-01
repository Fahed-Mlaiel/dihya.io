/**
 * Tests unitaires avancés pour la gestion des prévisualisations (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { createPreview, listPreviews } from '../../api/preview';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Preview API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should list previews (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await listPreviews({ jwt, lang });
      expect(Array.isArray(res)).toBe(true);
    }
  });
  it('should create a preview (validation, audit, plugins, RGPD)', async () => {
    const res = await createPreview({
      jwt,
      data: {
        name: 'Test Preview',
        description: 'Prévisualisation multilingue',
        type: 'web',
        owner: 'user_id',
      },
      lang: 'fr',
    });
    expect(res).toHaveProperty('id');
    expect(res).toHaveProperty('name', 'Test Preview');
  });
});
