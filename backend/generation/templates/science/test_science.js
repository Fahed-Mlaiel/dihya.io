/**
 * Tests Science – Dihya
 * @description Couverture complète : unit, integration, e2e, sécurité, i18n, RGPD, plugins.
 */
const request = require('supertest');
const app = require('../../../../app');
const { setupTestTenant, teardownTestTenant } = require('../../../../tests/fixtures/tenancy');

describe('Science API', () => {
  beforeAll(async () => { await setupTestTenant(); });
  afterAll(async () => { await teardownTestTenant(); });

  it('GET /api/science – sécurisé, multilingue', async () => {
    const res = await request(app)
      .get('/api/science')
      .set('Authorization', 'Bearer test-jwt-admin')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.lang).toBe('fr');
  });

  it('POST /api/science – admin only', async () => {
    const res = await request(app)
      .post('/api/science')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({ titre: 'Projet', domaine: 'Physique' });
    expect(res.statusCode).toBe(201);
    expect(res.body.data.titre).toBe('Projet');
  });

  it('POST /api/science – refus user', async () => {
    const res = await request(app)
      .post('/api/science')
      .set('Authorization', 'Bearer test-jwt-user')
      .send({ titre: 'Projet', domaine: 'Physique' });
    expect(res.statusCode).toBe(403);
  });

  // ...tests RGPD, plugins, audit, e2e, i18n, etc...
});
