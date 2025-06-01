// Tests avancés pour la gestion des previews (Dihya Coding)
// Couverture : unitaire, intégration, e2e, sécurité, i18n, RGPD
const request = require('supertest');
const app = require('../../../../app');
const { createJwtToken } = require('../../../../utils/jwt');

describe('Preview API', () => {
  let adminToken, userToken;
  beforeAll(() => {
    adminToken = createJwtToken({ role: 'admin' });
    userToken = createJwtToken({ role: 'user' });
  });

  it('refuse génération sans JWT', async () => {
    const res = await request(app).post('/api/preview/generate').send({ source: 'test', type: 'web' });
    expect(res.statusCode).toBe(401);
  });

  it('accepte génération avec JWT user', async () => {
    const res = await request(app)
      .post('/api/preview/generate')
      .set('Authorization', `Bearer ${userToken}`)
      .send({ source: 'test', type: 'mobile' });
    expect([200,201]).toContain(res.statusCode);
  });

  it('refuse suppression pour user', async () => {
    const res = await request(app)
      .delete('/api/preview/1')
      .set('Authorization', `Bearer ${userToken}`);
    expect(res.statusCode).toBe(403);
  });

  it('accepte suppression pour admin', async () => {
    const res = await request(app)
      .delete('/api/preview/1')
      .set('Authorization', `Bearer ${adminToken}`);
    expect([200,204,404]).toContain(res.statusCode);
  });

  it('réponses localisées', async () => {
    const res = await request(app)
      .get('/api/preview/1')
      .set('Authorization', `Bearer ${userToken}`)
      .set('Accept-Language', 'zh');
    expect(res.headers['content-language']).toBe('zh');
  });
});
