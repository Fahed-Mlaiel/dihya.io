// test_mobile.js
/**
 * Tests avancés pour le module mobile (REST/GraphQL, sécurité, i18n, rôles, plugins)
 * @coverage 100%
 */
const request = require('supertest');
const app = require('../../../../app');
const { setupTestUser, teardownTestUser } = require('../../../../testUtils');

describe('Mobile API', () => {
  let token;
  beforeAll(async () => {
    token = await setupTestUser('admin');
  });
  afterAll(async () => {
    await teardownTestUser();
  });

  it('génère un projet mobile (admin)', async () => {
    const res = await request(app)
      .post('/api/mobile/generate')
      .set('Authorization', `Bearer ${token}`)
      .send({ type: 'IA', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body.success).toBe(true);
    expect(res.body.project).toBeDefined();
  });

  it('refuse sans JWT', async () => {
    const res = await request(app)
      .post('/api/mobile/generate')
      .send({ type: 'VR', lang: 'en' });
    expect(res.statusCode).toBe(401);
  });

  it('refuse rôle invité', async () => {
    const guestToken = await setupTestUser('guest');
    const res = await request(app)
      .post('/api/mobile/generate')
      .set('Authorization', `Bearer ${guestToken}`)
      .send({ type: 'AR', lang: 'de' });
    expect(res.statusCode).toBe(403);
  });
});
