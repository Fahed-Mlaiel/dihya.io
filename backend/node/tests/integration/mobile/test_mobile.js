/**
 * @file test_mobile.js
 * @description Tests d'intégration avancés pour l'API mobile (REST/GraphQL, sécurité, i18n, plugins, RGPD, etc.)
 * @author Dihya
 * @date 2025-05-25
 */

const request = require('supertest');
const app = require('../../../src/app');
const { setupTestDB, teardownTestDB, getTestToken } = require('../utils/utils');

const adminToken = getTestToken('admin');
const userToken = getTestToken('user');

beforeAll(async () => { await setupTestDB(); });
afterAll(async () => { await teardownTestDB(); });

describe('Mobile API - Sécurité, i18n, RGPD, Plugins, SEO', () => {
  it('GET /api/mobile retourne la liste (auth, i18n)', async () => {
    const res = await request(app)
      .get('/api/mobile')
      .set('Authorization', `Bearer ${userToken}`)
      .set('Accept-Language', 'fr')
      .expect(200);
    expect(res.body).toHaveProperty('data');
  });

  it('POST /api/mobile (admin)', async () => {
    const res = await request(app)
      .post('/api/mobile')
      .set('Authorization', `Bearer ${adminToken}`)
      .send({ nom: 'App IA', description: 'Application mobile IA' })
      .expect(201);
    expect(res.body).toHaveProperty('id');
  });

  it('refuse la création à un user', async () => {
    await request(app)
      .post('/api/mobile')
      .set('Authorization', `Bearer ${userToken}`)
      .send({ nom: 'Test', description: 'Test' })
      .expect(403);
  });

  it('supporte GraphQL', async () => {
    const res = await request(app)
      .post('/graphql')
      .set('Authorization', `Bearer ${userToken}`)
      .send({ query: '{ mobile { id nom } }' })
      .expect(200);
    expect(res.body.data).toHaveProperty('mobile');
  });

  it('audit log est généré', async () => {
    const res = await request(app)
      .get('/api/mobile')
      .set('Authorization', `Bearer ${adminToken}`)
      .expect(200);
    expect(res.headers).toHaveProperty('x-audit-log-id');
  });
});
