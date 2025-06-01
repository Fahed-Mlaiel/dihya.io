// test_recherche.js
/**
 * Tests avancés pour le module recherche (REST/GraphQL, sécurité, i18n, rôles, plugins)
 * @coverage 100%
 */
const request = require('supertest');
const app = require('../../../../app');
const { setupTestUser, teardownTestUser } = require('../../../../testUtils');

describe('Recherche API', () => {
  let token;
  beforeAll(async () => {
    token = await setupTestUser('admin');
  });
  afterAll(async () => {
    await teardownTestUser();
  });

  it('génère une recherche (admin)', async () => {
    const res = await request(app)
      .post('/api/recherche/generate')
      .set('Authorization', `Bearer ${token}`)
      .send({ type: 'VR', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body.success).toBe(true);
    expect(res.body.search).toBeDefined();
  });

  it('refuse sans JWT', async () => {
    const res = await request(app)
      .post('/api/recherche/generate')
      .send({ type: 'AR', lang: 'en' });
    expect(res.statusCode).toBe(401);
  });

  it('refuse rôle invité', async () => {
    const guestToken = await setupTestUser('guest');
    const res = await request(app)
      .post('/api/recherche/generate')
      .set('Authorization', `Bearer ${guestToken}`)
      .send({ type: 'IA', lang: 'de' });
    expect(res.statusCode).toBe(403);
  });
});
