// Tests unitaires, intégration, e2e pour la route sécurité
const request = require('supertest');
const app = require('../../../../app');

describe('Sécurité API', () => {
  it('GET /securite - sécurisé, multilingue', async () => {
    const res = await request(app)
      .get('/securite')
      .set('Authorization', 'Bearer test-jwt-admin')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  it('POST /securite - admin only, validation', async () => {
    const res = await request(app)
      .post('/securite')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({ nom: 'Projet Sécurité' });
    expect(res.statusCode).toBe(201);
    expect(res.body.nom).toBe('Projet Sécurité');
  });

  // ... autres tests (roles, plugins, RGPD, SEO, fallback IA)
});
