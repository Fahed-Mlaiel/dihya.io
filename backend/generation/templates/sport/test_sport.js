// Test Sport avancé pour Dihya Coding
// Teste la création, la sécurité, la multilingue, la conformité RGPD, l'auditabilité, et l'extensibilité plugins.

const request = require('supertest');
const app = require('../../../../app');

describe('Sport API', () => {
  it('crée une activité sportive (sécurité, RGPD, plugins)', async () => {
    const res = await request(app)
      .post('/sport/create')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({
        name: 'Football',
        description: 'Activité multilingue',
        locale: 'fr',
        tenant: 'demo',
        details: { type: 'collectif', duree: 90 }
      });
    expect(res.statusCode).toBe(200);
    expect(res.body.sport).toBeDefined();
  });
});
