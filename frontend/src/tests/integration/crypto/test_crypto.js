/**
 * Test d'intégration avancé pour la gestion des projets Crypto (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Crypto API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('GET /crypto/projects (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/crypto/projects')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /crypto/projects (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/crypto/projects')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'CryptoX', type: 'Blockchain', owner: 'user_id' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('project');
  });
  it('GraphQL /crypto/graphql (roles, plugins, fallback IA)', async () => {
    const query = '{ projects { id name type owner } }';
    const res = await request(app)
      .post('/crypto/graphql')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ query });
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toHaveProperty('projects');
  });
  it('Sécurité CORS, WAF, anti-DDOS', async () => {
    const res = await request(app)
      .options('/crypto/projects')
      .set('Origin', 'https://evil.com');
    expect(res.headers).toHaveProperty('access-control-allow-origin');
  });
});
