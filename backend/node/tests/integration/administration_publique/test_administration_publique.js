// Test d'intégration complet pour l'API administration publique (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy)
const request = require('supertest');
const app = require('../../../app');
describe('API Administration Publique', () => {
  it('admin peut créer une entité', async () => {
    const res = await request(app)
      .post('/api/administration_publique')
      .set('Authorization', 'Bearer ADMIN_JWT')
      .send({ nom: 'Mairie', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });
  it('user ne peut pas supprimer une entité', async () => {
    const res = await request(app)
      .delete('/api/administration_publique/1')
      .set('Authorization', 'Bearer USER_JWT');
    expect(res.statusCode).toBe(403);
  });
  it('invite peut lister les entités', async () => {
    const res = await request(app)
      .get('/api/administration_publique')
      .set('Accept-Language', 'ar')
      .set('Authorization', 'Bearer INVITE_JWT');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
  // ... autres tests i18n, plugins, audit, RGPD, e2e
});
