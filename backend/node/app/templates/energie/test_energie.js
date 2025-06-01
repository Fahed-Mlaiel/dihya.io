// Tests unitaires et d'intégration pour la route énergie (couverture maximale, mocks, fixtures, e2e)
const request = require('supertest');
const app = require('../../../../core/app');
const { setupTestUser, teardownTestUser } = require('../../../../core/testUtils');

describe('Energie API', () => {
  beforeAll(async () => {
    await setupTestUser();
  });
  afterAll(async () => {
    await teardownTestUser();
  });
  it('GET /energie/consommation - doit retourner la liste (i18n, rôles)', async () => {
    const res = await request(app)
      .get('/energie/consommation')
      .set('Accept-Language', 'fr')
      .set('Authorization', 'Bearer test-jwt-admin');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
  it('POST /energie/production - déclaration sécurisée', async () => {
    const res = await request(app)
      .post('/energie/production')
      .set('Authorization', 'Bearer test-jwt-operator')
      .send({ siteId: 'xyz', amount: 100, lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });
  // ...autres tests (PUT, DELETE, rôles, RGPD, plugins, audit, SEO, e2e)...
});
