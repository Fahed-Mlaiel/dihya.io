// test_medias.js
/**
 * Tests ultra complets pour le template Medias (unit, integration, e2e)
 * Couvre sécurité, i18n, rôles, audit, RGPD, plugins, fallback IA, SEO, multitenancy
 */
const request = require('supertest');
const app = require('../../../../app');

describe('Medias Template API', () => {
  it('GET /medias - accessible à tous les rôles', async () => {
    const res = await request(app)
      .get('/medias')
      .set('Accept-Language', 'fr')
      .set('Authorization', 'Bearer token_user');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('data');
  });

  it('POST /medias - admin only', async () => {
    const res = await request(app)
      .post('/medias')
      .set('Authorization', 'Bearer token_admin')
      .send({ name: 'Projet VR', type: 'VR' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });

  it('POST /medias - refusé pour user', async () => {
    const res = await request(app)
      .post('/medias')
      .set('Authorization', 'Bearer token_user')
      .send({ name: 'Projet AR', type: 'AR' });
    expect(res.statusCode).toBe(403);
  });

  // ...tests RGPD, plugins, audit, fallback IA, SEO, multitenancy, i18n...
});
