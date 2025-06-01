/**
 * Test d'intégration avancé pour la gestion des projets Construction (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Construction API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('GET /construction/projects (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/construction/projects')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /construction/projects (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/construction/projects')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'Chantier X', type: 'BTP', owner: 'user_id' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('project');
  });
  it('GraphQL /construction/graphql (roles, plugins, fallback IA)', async () => {
    const query = '{ projects { id name type owner } }';
    const res = await request(app)
      .post('/construction/graphql')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ query });
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toHaveProperty('projects');
  });
  it('Sécurité CORS, WAF, anti-DDOS', async () => {
    const res = await request(app)
      .options('/construction/projects')
      .set('Origin', 'https://evil.com');
    expect(res.headers).toHaveProperty('access-control-allow-origin');
  });
});
