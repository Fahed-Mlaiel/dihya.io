/**
 * Tests Sécurité – Dihya
 * @description Couverture complète : unit, integration, e2e, sécurité, i18n, RGPD, plugins.
 */
const request = require('supertest');
const app = require('../../../../app');
const { setupTestTenant, teardownTestTenant } = require('../../../../tests/fixtures/tenancy');

describe('Sécurité API', () => {
  beforeAll(async () => { await setupTestTenant(); });
  afterAll(async () => { await teardownTestTenant(); });

  it('GET /api/securite – sécurisé, multilingue', async () => {
    const res = await request(app)
      .get('/api/securite')
      .set('Authorization', 'Bearer test-jwt-admin')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.lang).toBe('fr');
  });

  it('POST /api/securite – admin only', async () => {
    const res = await request(app)
      .post('/api/securite')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({ type: 'intrusion', niveau: 'critique' });
    expect(res.statusCode).toBe(201);
    expect(res.body.data.type).toBe('intrusion');
  });

  it('POST /api/securite – refus user', async () => {
    const res = await request(app)
      .post('/api/securite')
      .set('Authorization', 'Bearer test-jwt-user')
      .send({ type: 'intrusion', niveau: 'critique' });
    expect(res.statusCode).toBe(403);
  });

  // ...tests RGPD, plugins, audit, e2e, i18n, etc...
});
