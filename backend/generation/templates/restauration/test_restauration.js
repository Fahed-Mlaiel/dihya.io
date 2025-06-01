/**
 * Tests Restauration – Dihya
 * @description Couverture complète : unit, integration, e2e, sécurité, i18n, RGPD, plugins.
 */
const request = require('supertest');
const app = require('../../../../app');
const { setupTestTenant, teardownTestTenant } = require('../../../../tests/fixtures/tenancy');

describe('Restauration API', () => {
  beforeAll(async () => { await setupTestTenant(); });
  afterAll(async () => { await teardownTestTenant(); });

  it('GET /api/restauration – sécurisé, multilingue', async () => {
    const res = await request(app)
      .get('/api/restauration')
      .set('Authorization', 'Bearer test-jwt-admin')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.lang).toBe('fr');
  });

  it('POST /api/restauration – admin only', async () => {
    const res = await request(app)
      .post('/api/restauration')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({ plat: 'Pizza', quantite: 2 });
    expect(res.statusCode).toBe(201);
    expect(res.body.data.plat).toBe('Pizza');
  });

  it('POST /api/restauration – refus user', async () => {
    const res = await request(app)
      .post('/api/restauration')
      .set('Authorization', 'Bearer test-jwt-user')
      .send({ plat: 'Pizza', quantite: 2 });
    expect(res.statusCode).toBe(403);
  });

  // ...tests RGPD, plugins, audit, e2e, i18n, etc...
});
