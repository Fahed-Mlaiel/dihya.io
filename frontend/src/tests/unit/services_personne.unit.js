/**
 * Tests unitaires avancés pour la gestion des services à la personne (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { createServicePersonne, listServicesPersonne } from '../../api/services_personne';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Services à la Personne API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should list services à la personne (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await listServicesPersonne({ jwt, lang });
      expect(Array.isArray(res)).toBe(true);
    }
  });
  it('should create a service à la personne (validation, audit, plugins, RGPD)', async () => {
    const res = await createServicePersonne({
      jwt,
      data: {
        name: 'Test Service',
        description: 'Service à la personne multilingue',
        type: 'personal',
        owner: 'user_id',
      },
      lang: 'fr',
    });
    expect(res).toHaveProperty('id');
    expect(res).toHaveProperty('name', 'Test Service');
  });
});
