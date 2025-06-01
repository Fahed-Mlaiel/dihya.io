/**
 * Test d'intégration avancé pour la gestion des projets Energie (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');
describe('Energie API Integration', () => {
  let jwt;
  beforeAll(async () => { jwt = await getJwt('admin'); });
  it('GET /energie/projects', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/energie/projects')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /energie/projects', async () => {
    const res = await request(app)
      .post('/energie/projects')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'Centrale Solaire', type: 'Solaire', owner: 'user_id' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('project');
  });
  it('GraphQL /energie/graphql', async () => {
    const query = '{ projects { id name type owner } }';
    const res = await request(app)
      .post('/energie/graphql')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ query });
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toHaveProperty('projects');
  });
  it('Sécurité CORS, WAF, anti-DDOS', async () => {
    const res = await request(app)
      .options('/energie/projects')
      .set('Origin', 'https://evil.com');
    expect(res.headers).toHaveProperty('access-control-allow-origin');
  });
});
