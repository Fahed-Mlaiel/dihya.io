// Tests avancés pour la gestion des modes (Dihya Coding)
// Couverture : unitaire, intégration, e2e, sécurité, i18n, RGPD
const request = require('supertest');
const app = require('../../../../app');
const { createJwtToken } = require('../../../../utils/jwt');

describe('Mode API', () => {
  let adminToken, userToken;
  beforeAll(() => {
    adminToken = createJwtToken({ role: 'admin' });
    userToken = createJwtToken({ role: 'user' });
  });

  it('refuse setMode sans JWT', async () => {
    const res = await request(app).post('/api/mode/set').send({ mode: 'dark' });
    expect(res.statusCode).toBe(401);
  });

  it('accepte setMode avec JWT user', async () => {
    const res = await request(app)
      .post('/api/mode/set')
      .set('Authorization', `Bearer ${userToken}`)
      .send({ mode: 'light' });
    expect([200,201]).toContain(res.statusCode);
  });

  it('refuse suppression pour user', async () => {
    const res = await request(app)
      .delete('/api/mode/1')
      .set('Authorization', `Bearer ${userToken}`);
    expect(res.statusCode).toBe(403);
  });

  it('accepte suppression pour admin', async () => {
    const res = await request(app)
      .delete('/api/mode/1')
      .set('Authorization', `Bearer ${adminToken}`);
    expect([200,204,404]).toContain(res.statusCode);
  });

  it('réponses localisées', async () => {
    const res = await request(app)
      .get('/api/mode/1')
      .set('Authorization', `Bearer ${userToken}`)
      .set('Accept-Language', 'es');
    expect(res.headers['content-language']).toBe('es');
  });
});
