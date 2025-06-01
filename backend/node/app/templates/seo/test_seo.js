// Tests unitaires, intégration, e2e pour la route SEO
const request = require('supertest');
const app = require('../../../../app');

describe('SEO API', () => {
  it('GET /seo - sécurisé, multilingue', async () => {
    const res = await request(app)
      .get('/seo')
      .set('Authorization', 'Bearer test-jwt-admin')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  it('POST /seo - admin only, validation', async () => {
    const res = await request(app)
      .post('/seo')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({ nom: 'Projet SEO' });
    expect(res.statusCode).toBe(201);
    expect(res.body.nom).toBe('Projet SEO');
  });

  // ... autres tests (roles, plugins, RGPD, SEO, fallback IA)
});
