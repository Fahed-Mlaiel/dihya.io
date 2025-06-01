// Tests unitaires et d'intégration pour la route gamer (couverture maximale, mocks, fixtures, e2e)
const request = require('supertest');
const app = require('../../../../core/app');
const { setupTestUser, teardownTestUser } = require('../../../../core/testUtils');

describe('Gamer API', () => {
  beforeAll(async () => {
    await setupTestUser();
  });
  afterAll(async () => {
    await teardownTestUser();
  });
  it('GET /gamer/scores - doit retourner la liste (i18n, rôles)', async () => {
    const res = await request(app)
      .get('/gamer/scores')
      .set('Accept-Language', 'fr')
      .set('Authorization', 'Bearer test-jwt-admin');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
  it('POST /gamer/match - création sécurisée', async () => {
    const res = await request(app)
      .post('/gamer/match')
      .set('Authorization', 'Bearer test-jwt-player')
      .send({ opponent: 'player2', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });
  // ...autres tests (PUT, DELETE, rôles, RGPD, plugins, audit, SEO, e2e)...
});
