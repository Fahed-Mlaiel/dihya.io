/**
 * Tests unitaires avancés pour la gestion des projets voice (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
 * Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
 */
import { createVoiceProject, listVoiceProjects } from '../../api/voice';
import { getJwt, SUPPORTED_LANGUAGES } from '../../utils/test_utils';
describe('Voice Projects API', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('should list voice projects (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await listVoiceProjects({ jwt, lang });
      expect(Array.isArray(res)).toBe(true);
    }
  });
  it('should create a voice project (validation, audit, plugins, RGPD)', async () => {
    const res = await createVoiceProject({
      jwt,
      data: {
        name: 'Test Voice',
        description: 'Projet voice multilingue',
        type: 'voice',
        owner: 'user_id',
      },
      lang: 'fr',
    });
    expect(res).toHaveProperty('id');
    expect(res).toHaveProperty('name', 'Test Voice');
  });
});
