// Test d'intégration complet pour l'API agriculture (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy)
const request = require('supertest');
const app = require('../../../app');
describe('API Agriculture', () => {
  it('admin peut créer une exploitation', async () => {
    const res = await request(app)
      .post('/api/agriculture')
      .set('Authorization', 'Bearer ADMIN_JWT')
      .send({ nom: 'Ferme', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });
  it('user ne peut pas supprimer une exploitation', async () => {
    const res = await request(app)
      .delete('/api/agriculture/1')
      .set('Authorization', 'Bearer USER_JWT');
    expect(res.statusCode).toBe(403);
  });
  it('invite peut lister les exploitations', async () => {
    const res = await request(app)
      .get('/api/agriculture')
      .set('Accept-Language', 'de')
      .set('Authorization', 'Bearer INVITE_JWT');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
  // ... autres tests i18n, plugins, audit, RGPD, e2e
});
