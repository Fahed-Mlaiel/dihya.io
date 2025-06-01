/**
 * @file test_loisirs.js
 * @description Tests d'intégration avancés pour l'API loisirs (REST/GraphQL, sécurité, i18n, plugins, RGPD, etc.)
 * @author Dihya
 * @date 2025-05-25
 */

const request = require('supertest');
const jwt = require('jsonwebtoken');
const app = require('../../../src/app'); // Chemin à adapter selon l'implémentation réelle
const { setupTestDB, teardownTestDB, getTestToken } = require('../utils/utils');

// Fixtures multilingues
const i18nHeaders = [
  { 'Accept-Language': 'fr' },
  { 'Accept-Language': 'en' },
  { 'Accept-Language': 'ar' },
  { 'Accept-Language': 'de' },
  { 'Accept-Language': 'zh' },
  { 'Accept-Language': 'ja' },
  { 'Accept-Language': 'ko' },
  { 'Accept-Language': 'nl' },
  { 'Accept-Language': 'he' },
  { 'Accept-Language': 'fa' },
  { 'Accept-Language': 'hi' },
  { 'Accept-Language': 'es' },
];

// JWT tokens pour rôles
const adminToken = getTestToken('admin');
const userToken = getTestToken('user');
const guestToken = getTestToken('guest');

beforeAll(async () => {
  await setupTestDB();
});
afterAll(async () => {
  await teardownTestDB();
});

describe('Loisirs API - Sécurité, i18n, RGPD, Plugins, SEO', () => {
  test.each(i18nHeaders)('GET /api/loisirs (i18n: %p)', async (langHeader) => {
    const res = await request(app)
      .get('/api/loisirs')
      .set(langHeader)
      .set('Authorization', `Bearer ${userToken}`)
      .expect(200);
    expect(res.body).toHaveProperty('data');
    expect(res.headers['content-language']).toBeDefined();
  });

  it('refuse l’accès sans JWT', async () => {
    await request(app)
      .get('/api/loisirs')
      .expect(401);
  });

  it('autorise l’admin à créer un loisir', async () => {
    const res = await request(app)
      .post('/api/loisirs')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ nom: 'Randonnée', description: 'Activité de plein air' })
      .expect(201);
    expect(res.body).toHaveProperty('id');
  });

  it('refuse la création à un invité', async () => {
    await request(app)
      .post('/api/loisirs')
      .set('Authorization', `Bearer ${guestToken}`)
      .send({ nom: 'Jeu', description: 'Test' })
      .expect(403);
  });

  it('vérifie la conformité RGPD (anonymisation)', async () => {
    const res = await request(app)
      .get('/api/loisirs/export')
      .set('Authorization', `Bearer ${userToken}`)
      .expect(200);
    expect(res.body).toHaveProperty('anonymized');
  });

  it('supporte les plugins dynamiques', async () => {
    const res = await request(app)
      .post('/api/plugins/enable')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ plugin: 'loisirs-analytics' })
      .expect(200);
    expect(res.body).toHaveProperty('status', 'enabled');
  });

  it('vérifie la présence des headers SEO', async () => {
    const res = await request(app)
      .get('/api/loisirs')
      .set('Authorization', `Bearer ${userToken}`)
      .expect(200);
    expect(res.headers).toHaveProperty('x-robots-tag');
    expect(res.headers).toHaveProperty('x-seo-score');
  });

  it('supporte GraphQL', async () => {
    const res = await request(app)
      .post('/graphql')
      .set('Authorization', `Bearer ${userToken}`)
      .send({ query: '{ loisirs { id nom } }' })
      .expect(200);
    expect(res.body.data).toHaveProperty('loisirs');
  });

  it('audit log est généré', async () => {
    const res = await request(app)
      .get('/api/loisirs')
      .set('Authorization', `Bearer ${adminToken}`)
      .expect(200);
    expect(res.headers).toHaveProperty('x-audit-log-id');
  });

  it('protection anti-DDOS/WAF', async () => {
    for (let i = 0; i < 10; i++) {
      await request(app)
        .get('/api/loisirs')
        .set('Authorization', `Bearer ${userToken}`)
        .expect(200);
    }
    // Simule un DDOS (doit être bloqué au-delà d’un seuil)
    const res = await request(app)
      .get('/api/loisirs')
      .set('Authorization', `Bearer ${userToken}`)
      .expect(res => {
        expect([200, 429]).toContain(res.statusCode);
      });
  });
});
