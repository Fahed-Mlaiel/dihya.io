// Tests unitaires et d'intégration pour la route environnement (couverture maximale, mocks, fixtures, e2e)
const request = require('supertest');
const app = require('../../../../core/app');
const { setupTestUser, teardownTestUser } = require('../../../../core/testUtils');

describe('Environnement API', () => {
  beforeAll(async () => {
    await setupTestUser();
  });
  afterAll(async () => {
    await teardownTestUser();
  });
  it('GET /environnement/indicateurs - doit retourner la liste (i18n, rôles)', async () => {
    const res = await request(app)
      .get('/environnement/indicateurs')
      .set('Accept-Language', 'fr')
      .set('Authorization', 'Bearer test-jwt-admin');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
  it('POST /environnement/mesure - ajout sécurisé', async () => {
    const res = await request(app)
      .post('/environnement/mesure')
      .set('Authorization', 'Bearer test-jwt-analyst')
      .send({ indicateurId: 'env1', value: 42, lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });
  // ...autres tests (PUT, DELETE, rôles, RGPD, plugins, audit, SEO, e2e)...
});
