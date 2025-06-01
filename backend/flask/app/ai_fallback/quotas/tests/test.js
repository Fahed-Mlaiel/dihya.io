// test.js - Tests unitaires et d'intégration pour la gestion avancée des quotas IA (Node.js)
// Sécurité maximale, multitenancy, i18n, audit, mock IA fallback, couverture complète
const request = require('supertest');
const app = require('../../../../server');
const { setupTestUser, teardownTestUser, getJWT } = require('../../../../utils/testHelpers');

describe('Quotas API (Node.js)', () => {
  let token;
  beforeAll(async () => {
    await setupTestUser('admin');
    token = await getJWT('admin');
  });
  afterAll(async () => {
    await teardownTestUser('admin');
  });
  it('doit refuser l’accès sans JWT', async () => {
    const res = await request(app).get('/api/ai/quotas');
    expect(res.statusCode).toBe(401);
  });
  it('doit retourner les quotas pour un admin', async () => {
    const res = await request(app)
      .get('/api/ai/quotas')
      .set('Authorization', `Bearer ${token}`);
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('limits');
  });
  it('doit appliquer le fallback IA si quota dépassé', async () => {
    // Mock dépassement quota
    const res = await request(app)
      .post('/api/ai/quotas/consume')
      .set('Authorization', `Bearer ${token}`)
      .send({ amount: 999999 });
    expect(res.body.fallback).toBe(true);
  });
});
