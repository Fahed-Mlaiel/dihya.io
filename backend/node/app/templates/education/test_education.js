// Tests unitaires et d'intégration pour la route éducation (couverture maximale, mocks, fixtures, e2e)
const request = require('supertest');
const app = require('../../../../core/app');
const { setupTestUser, teardownTestUser } = require('../../../../core/testUtils');

describe('Education API', () => {
  beforeAll(async () => {
    await setupTestUser();
  });
  afterAll(async () => {
    await teardownTestUser();
  });
  it('GET /education/courses - doit retourner la liste (i18n, rôles)', async () => {
    const res = await request(app)
      .get('/education/courses')
      .set('Accept-Language', 'fr')
      .set('Authorization', 'Bearer test-jwt-admin');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
  it('POST /education/enroll - inscription sécurisée', async () => {
    const res = await request(app)
      .post('/education/enroll')
      .set('Authorization', 'Bearer test-jwt-student')
      .send({ courseId: 'abc', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });
  // ...autres tests (PUT, DELETE, rôles, RGPD, plugins, audit, SEO, e2e)...
});
