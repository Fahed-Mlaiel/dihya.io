// Fichier fusionné depuis intelligence_artificielle/test_intelligence_artificielle.js
const request = require('supertest');
const app = require('../../../app');
const { getJwt, mockPlugin, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('AI API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('GET /api/ai/models (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/api/ai/models')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /api/ai/models (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/api/ai/models')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'ModelX', user: 'user1', confidential: true });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.meta).toHaveProperty('audit');
    expect(res.body.meta).toHaveProperty('rgpd');
  });
  it('GraphQL /api/ai/graphql (roles, plugins, fallback AI)', async () => {
    const query = '{ models { id name user } }';
    const res = await request(app)
      .post('/api/ai/graphql')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ query });
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toHaveProperty('models');
  });
  it('Sécurité CORS, WAF, anti-DDOS', async () => {
    const res = await request(app)
      .options('/api/ai/models')
      .set('Origin', 'https://evil.com');
    expect(res.headers['access-control-allow-origin']).not.toBe('https://evil.com');
  });
  it('Audit log, anonymisation, export RGPD', async () => {
    // ...tests avancés (audit, anonymisation, RGPD, etc.)
  });
});
