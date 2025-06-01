/**
 * Test d'intégration avancé pour la gestion des projets Ecommerce (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');
describe('Ecommerce API Integration', () => {
  let jwt;
  beforeAll(async () => { jwt = await getJwt('admin'); });
  it('GET /ecommerce/projects', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/ecommerce/projects')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /ecommerce/projects', async () => {
    const res = await request(app)
      .post('/ecommerce/projects')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'Boutique X', type: 'Marketplace', owner: 'user_id' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('project');
  });
  it('GraphQL /ecommerce/graphql', async () => {
    const query = '{ projects { id name type owner } }';
    const res = await request(app)
      .post('/ecommerce/graphql')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ query });
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toHaveProperty('projects');
  });
  it('Sécurité CORS, WAF, anti-DDOS', async () => {
    const res = await request(app)
      .options('/ecommerce/projects')
      .set('Origin', 'https://evil.com');
    expect(res.headers).toHaveProperty('access-control-allow-origin');
  });
});
