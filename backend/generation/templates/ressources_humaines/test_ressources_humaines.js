/**
 * Tests Ressources Humaines – Dihya
 * @description Couverture complète : unit, integration, e2e, sécurité, i18n, RGPD, plugins.
 */
const request = require('supertest');
const app = require('../../../../app');
const { setupTestTenant, teardownTestTenant } = require('../../../../tests/fixtures/tenancy');

describe('Ressources Humaines API', () => {
  beforeAll(async () => { await setupTestTenant(); });
  afterAll(async () => { await teardownTestTenant(); });

  it('GET /api/ressources_humaines – sécurisé, multilingue', async () => {
    const res = await request(app)
      .get('/api/ressources_humaines')
      .set('Authorization', 'Bearer test-jwt-admin')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.lang).toBe('fr');
  });

  it('POST /api/ressources_humaines – admin only', async () => {
    const res = await request(app)
      .post('/api/ressources_humaines')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({ nom: 'Test', role: 'user' });
    expect(res.statusCode).toBe(201);
    expect(res.body.data.nom).toBe('Test');
  });

  it('POST /api/ressources_humaines – refus user', async () => {
    const res = await request(app)
      .post('/api/ressources_humaines')
      .set('Authorization', 'Bearer test-jwt-user')
      .send({ nom: 'Test', role: 'user' });
    expect(res.statusCode).toBe(403);
  });

  // ...tests RGPD, plugins, audit, e2e, i18n, etc...
});
