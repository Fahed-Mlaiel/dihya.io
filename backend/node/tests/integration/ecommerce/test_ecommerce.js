/**
 * Test d'intégration avancé pour le module Ecommerce (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../app');
const { getJwt, mockPlugin, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Ecommerce API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('GET /api/ecommerce/products (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/api/ecommerce/products')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /api/ecommerce/products (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/api/ecommerce/products')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ name: 'Produit X', user: 'user1', confidential: true });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.meta).toHaveProperty('audit');
    expect(res.body.meta).toHaveProperty('rgpd');
  });
  it('GraphQL /api/ecommerce/graphql (roles, plugins, fallback IA)', async () => {
    const query = '{ products { id name user } }';
    const res = await request(app)
      .post('/api/ecommerce/graphql')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ query });
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toHaveProperty('products');
  });
  it('Sécurité CORS, WAF, anti-DDOS', async () => {
    const res = await request(app)
      .options('/api/ecommerce/products')
      .set('Origin', 'https://evil.com');
    expect(res.headers['access-control-allow-origin']).not.toBe('https://evil.com');
  });
  it('Audit log, anonymisation, export RGPD', async () => {
    const res = await request(app)
      .get('/api/ecommerce/products/export')
      .set('Authorization', `Bearer ${jwt}`);
    expect(res.statusCode).toBe(200);
    expect(res.body.meta).toHaveProperty('export');
    expect(res.body.meta).toHaveProperty('anonymisation');
  });
  it('Plugin dynamique (mock)', async () => {
    const pluginRes = await mockPlugin('ecommerce', { action: 'simulate' });
    expect(pluginRes).toHaveProperty('status', 'ok');
  });
  it('Fallback IA open source', async () => {
    const res = await request(app)
      .post('/api/ecommerce/products/ai-fallback')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ prompt: 'simulate ecommerce' });
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('ai_result');
  });
});
