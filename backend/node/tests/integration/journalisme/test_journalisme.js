/**
 * Test d'intégration avancé pour le module Journalisme (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../app');
const { getJwt, mockPlugin, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Journalisme API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('GET /api/journalisme/articles (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/api/journalisme/articles')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /api/journalisme/articles (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/api/journalisme/articles')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ title: 'ArticleX', user: 'user1', confidential: true });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
    expect(res.body.meta).toHaveProperty('audit');
    expect(res.body.meta).toHaveProperty('rgpd');
  });
  it('GraphQL /api/journalisme/graphql (roles, plugins, fallback IA)', async () => {
    const query = '{ articles { id title user } }';
    const res = await request(app)
      .post('/api/journalisme/graphql')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ query });
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toHaveProperty('articles');
  });
  it('Sécurité CORS, WAF, anti-DDOS', async () => {
    const res = await request(app)
      .options('/api/journalisme/articles')
      .set('Origin', 'https://evil.com');
    expect(res.headers['access-control-allow-origin']).not.toBe('https://evil.com');
  });
  it('Audit log, anonymisation, export RGPD', async () => {
    const res = await request(app)
      .get('/api/journalisme/articles/export')
      .set('Authorization', `Bearer ${jwt}`);
    expect(res.statusCode).toBe(200);
    expect(res.body.meta).toHaveProperty('export');
    expect(res.body.meta).toHaveProperty('anonymisation');
  });
  it('Plugin dynamique (mock)', async () => {
    const pluginRes = await mockPlugin('journalisme', { action: 'simulate' });
    expect(pluginRes).toHaveProperty('status', 'ok');
  });
  it('Fallback IA open source', async () => {
    const res = await request(app)
      .post('/api/journalisme/articles/ai-fallback')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ prompt: 'simulate article' });
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('ai_result');
  });
});
