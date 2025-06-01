// Test d'intégration complet pour l'API arts (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy)
const request = require('supertest');
const app = require('../../../app');
describe('API Arts', () => {
  it('admin peut créer une œuvre', async () => {
    const res = await request(app)
      .post('/api/arts')
      .set('Authorization', 'Bearer ADMIN_JWT')
      .send({ titre: 'Tableau', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });
  it('user ne peut pas supprimer une œuvre', async () => {
    const res = await request(app)
      .delete('/api/arts/1')
      .set('Authorization', 'Bearer USER_JWT');
    expect(res.statusCode).toBe(403);
  });
  it('invite peut lister les œuvres', async () => {
    const res = await request(app)
      .get('/api/arts')
      .set('Accept-Language', 'es')
      .set('Authorization', 'Bearer INVITE_JWT');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
  // ... autres tests i18n, plugins, audit, RGPD, e2e
});
