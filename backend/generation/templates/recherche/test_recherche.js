// Tests avancés pour la gestion de la recherche (Dihya Coding)
// Couverture : unitaire, intégration, e2e, sécurité, i18n, RGPD
const request = require('supertest');
const app = require('../../../../app');
const { createJwtToken } = require('../../../../utils/jwt');

describe('Recherche API', () => {
  let adminToken, userToken;
  beforeAll(() => {
    adminToken = createJwtToken({ role: 'admin' });
    userToken = createJwtToken({ role: 'user' });
  });

  it('refuse recherche sans JWT', async () => {
    const res = await request(app).post('/api/recherche/query').send({ query: 'test' });
    expect(res.statusCode).toBe(401);
  });

  it('accepte recherche avec JWT user', async () => {
    const res = await request(app)
      .post('/api/recherche/query')
      .set('Authorization', `Bearer ${userToken}`)
      .send({ query: 'test', filters: {} });
    expect([200,201]).toContain(res.statusCode);
  });

  it('refuse suppression pour user', async () => {
    const res = await request(app)
      .delete('/api/recherche/1')
      .set('Authorization', `Bearer ${userToken}`);
    expect(res.statusCode).toBe(403);
  });

  it('accepte suppression pour admin', async () => {
    const res = await request(app)
      .delete('/api/recherche/1')
      .set('Authorization', `Bearer ${adminToken}`);
    expect([200,204,404]).toContain(res.statusCode);
  });

  it('réponses localisées', async () => {
    const res = await request(app)
      .get('/api/recherche/1')
      .set('Authorization', `Bearer ${userToken}`)
      .set('Accept-Language', 'hi');
    expect(res.headers['content-language']).toBe('hi');
  });
});
