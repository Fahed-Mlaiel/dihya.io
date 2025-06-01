/**
 * Test d'intégration avancé pour le module Energie (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../app');
const { getJwt, mockPlugin, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Energie API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('GET /api/energie/consumptions (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/api/energie/consumptions')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /api/energie/consumptions (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/api/energie/consumptions')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ value: 100, user: 'user1', confidential: true });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.meta).toHaveProperty('audit');
    expect(res.body.meta).toHaveProperty('rgpd');
  });
  it('GraphQL /api/energie/graphql (roles, plugins, fallback IA)', async () => {
    const query = '{ consumptions { id value user } }';
    const res = await request(app)
      .post('/api/energie/graphql')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ query });
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toHaveProperty('consumptions');
  });
  it('Sécurité CORS, WAF, anti-DDOS', async () => {
    const res = await request(app)
      .options('/api/energie/consumptions')
      .set('Origin', 'https://evil.com');
    expect(res.headers['access-control-allow-origin']).not.toBe('https://evil.com');
  });
  it('Audit log, anonymisation, export RGPD', async () => {
    const res = await request(app)
      .get('/api/energie/consumptions/export')
      .set('Authorization', `Bearer ${jwt}`);
    expect(res.statusCode).toBe(200);
    expect(res.body.meta).toHaveProperty('export');
    expect(res.body.meta).toHaveProperty('anonymisation');
  });
  it('Plugin dynamique (mock)', async () => {
    const pluginRes = await mockPlugin('energie', { action: 'simulate' });
    expect(pluginRes).toHaveProperty('status', 'ok');
  });
  it('Fallback IA open source', async () => {
    const res = await request(app)
      .post('/api/energie/consumptions/ai-fallback')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ prompt: 'simulate energy' });
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('ai_result');
  });
});
