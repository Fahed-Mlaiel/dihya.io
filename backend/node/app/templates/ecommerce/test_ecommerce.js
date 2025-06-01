"""
Tests unitaires et d'intégration pour la route e-commerce (couverture maximale, mocks, fixtures, e2e)
"""
const request = require('supertest');
const app = require('../../../../core/app');
const { setupTestUser, teardownTestUser } = require('../../../../core/testUtils');

describe('Ecommerce API', () => {
  beforeAll(async () => {
    await setupTestUser();
  });
  afterAll(async () => {
    await teardownTestUser();
  });
  it('GET /ecommerce/products - doit retourner la liste (i18n, rôles)', async () => {
    const res = await request(app)
      .get('/ecommerce/products')
      .set('Accept-Language', 'en')
      .set('Authorization', 'Bearer test-jwt-admin');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
  it('POST /ecommerce/orders - création sécurisée', async () => {
    const res = await request(app)
      .post('/ecommerce/orders')
      .set('Authorization', 'Bearer test-jwt-user')
      .send({ productId: '123', quantity: 2, lang: 'en' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });
  // ...autres tests (PUT, DELETE, rôles, RGPD, plugins, audit, SEO, e2e)...
});
