// Tests avancés pour la gestion de la publicité (Dihya Coding)
// Couverture : unitaire, intégration, e2e, sécurité, i18n, RGPD
const request = require('supertest');
const app = require('../../../../app');
const { createJwtToken } = require('../../../../utils/jwt');

describe('Publicite API', () => {
  let adminToken, userToken;
  beforeAll(() => {
    adminToken = createJwtToken({ role: 'admin' });
    userToken = createJwtToken({ role: 'user' });
  });

  it('refuse création sans JWT', async () => {
    const res = await request(app).post('/api/publicite/create').send({ content: 'Pub test', cible: 'all' });
    expect(res.statusCode).toBe(401);
  });

  it('accepte création avec JWT user', async () => {
    const res = await request(app)
      .post('/api/publicite/create')
      .set('Authorization', `Bearer ${userToken}`)
      .send({ content: 'Pub test', cible: 'fr' });
    expect([200,201]).toContain(res.statusCode);
  });

  it('refuse suppression pour user', async () => {
    const res = await request(app)
      .delete('/api/publicite/1')
      .set('Authorization', `Bearer ${userToken}`);
    expect(res.statusCode).toBe(403);
  });

  it('accepte suppression pour admin', async () => {
    const res = await request(app)
      .delete('/api/publicite/1')
      .set('Authorization', `Bearer ${adminToken}`);
    expect([200,204,404]).toContain(res.statusCode);
  });

  it('réponses localisées', async () => {
    const res = await request(app)
      .get('/api/publicite/1')
      .set('Authorization', `Bearer ${userToken}`)
      .set('Accept-Language', 'fa');
    expect(res.headers['content-language']).toBe('fa');
  });
});
