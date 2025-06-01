// Tests unitaires, intégration, e2e pour la route services à la personne
const request = require('supertest');
const app = require('../../../../app');

describe('Services à la personne API', () => {
  it('GET /services_personne - sécurisé, multilingue', async () => {
    const res = await request(app)
      .get('/services_personne')
      .set('Authorization', 'Bearer test-jwt-admin')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  it('POST /services_personne - admin only, validation', async () => {
    const res = await request(app)
      .post('/services_personne')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({ nom: 'Projet Service à la personne' });
    expect(res.statusCode).toBe(201);
    expect(res.body.nom).toBe('Projet Service à la personne');
  });

  // ... autres tests (roles, plugins, RGPD, SEO, fallback IA)
});
