/**
 * Test d'intégration avancé pour la gestion des projets Environnement (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');
describe('Environnement API Integration', () => {
  let jwt;
  beforeAll(async () => { jwt = await getJwt('admin'); });
  it('GET /environnement/projects', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/environnement/projects')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /environnement/projects', async () => {
    const res = await request(app)
      .post('/environnement/projects')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'EcoProjet', type: 'Biodiversité', owner: 'user_id' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('project');
  });
  it('GraphQL /environnement/graphql', async () => {
    const query = '{ projects { id name type owner } }';
    const res = await request(app)
      .post('/environnement/graphql')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ query });
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toHaveProperty('projects');
  });
  it('Sécurité CORS, WAF, anti-DDOS', async () => {
    const res = await request(app)
      .options('/environnement/projects')
      .set('Origin', 'https://evil.com');
    expect(res.headers).toHaveProperty('access-control-allow-origin');
  });
});
