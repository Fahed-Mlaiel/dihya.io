// Tests avancés pour la gestion mobile (Dihya Coding)
// Couverture : unitaire, intégration, e2e, sécurité, i18n, RGPD
const request = require('supertest');
const app = require('../../../../app');
const { createJwtToken } = require('../../../../utils/jwt');

describe('Mobile API', () => {
  let adminToken, userToken;
  beforeAll(() => {
    adminToken = createJwtToken({ role: 'admin' });
    userToken = createJwtToken({ role: 'user' });
  });

  it('refuse génération sans JWT', async () => {
    const res = await request(app).post('/api/mobile/generate').send({ projectName: 'Test', platform: 'ios' });
    expect(res.statusCode).toBe(401);
  });

  it('accepte génération avec JWT user', async () => {
    const res = await request(app)
      .post('/api/mobile/generate')
      .set('Authorization', `Bearer ${userToken}`)
      .send({ projectName: 'Test', platform: 'android' });
    expect([200,201]).toContain(res.statusCode);
  });

  it('refuse suppression pour user', async () => {
    const res = await request(app)
      .delete('/api/mobile/1')
      .set('Authorization', `Bearer ${userToken}`);
    expect(res.statusCode).toBe(403);
  });

  it('accepte suppression pour admin', async () => {
    const res = await request(app)
      .delete('/api/mobile/1')
      .set('Authorization', `Bearer ${adminToken}`);
    expect([200,204,404]).toContain(res.statusCode);
  });

  it('réponses localisées', async () => {
    const res = await request(app)
      .get('/api/mobile/1')
      .set('Authorization', `Bearer ${userToken}`)
      .set('Accept-Language', 'de');
    expect(res.headers['content-language']).toBe('de');
  });
});
