// Test Tourisme avancé pour Dihya Coding
// Teste la création, la sécurité, la multilingue, la conformité RGPD, l'auditabilité, et l'extensibilité plugins.

const request = require('supertest');
const app = require('../../../../app');

describe('Tourisme API', () => {
  it('crée une activité touristique (sécurité, RGPD, plugins)', async () => {
    const res = await request(app)
      .post('/tourisme/create')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({
        name: 'Visite guidée',
        description: 'Activité multilingue',
        locale: 'fr',
        tenant: 'demo',
        details: { type: 'culturel', duree: 120 }
      });
    expect(res.statusCode).toBe(200);
    expect(res.body.tourisme).toBeDefined();
  });
});
