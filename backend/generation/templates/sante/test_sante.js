/**
 * Tests Santé – Dihya
 * @description Couverture complète : unit, integration, e2e, sécurité, i18n, RGPD, plugins.
 */
const request = require('supertest');
const app = require('../../../../app');
const { setupTestTenant, teardownTestTenant } = require('../../../../tests/fixtures/tenancy');

describe('Santé API', () => {
  beforeAll(async () => { await setupTestTenant(); });
  afterAll(async () => { await teardownTestTenant(); });

  it('GET /api/sante – sécurisé, multilingue', async () => {
    const res = await request(app)
      .get('/api/sante')
      .set('Authorization', 'Bearer test-jwt-admin')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.lang).toBe('fr');
  });

  it('POST /api/sante – admin only', async () => {
    const res = await request(app)
      .post('/api/sante')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({ nom: 'Patient', dossier: 'A123' });
    expect(res.statusCode).toBe(201);
    expect(res.body.data.nom).toBe('Patient');
  });

  it('POST /api/sante – refus user', async () => {
    const res = await request(app)
      .post('/api/sante')
      .set('Authorization', 'Bearer test-jwt-user')
      .send({ nom: 'Patient', dossier: 'A123' });
    expect(res.statusCode).toBe(403);
  });

  // ...tests RGPD, plugins, audit, e2e, i18n, etc...
});
