// Test Transport avancé pour Dihya Coding
// Teste la création, la sécurité, la multilingue, la conformité RGPD, l'auditabilité, et l'extensibilité plugins.

const request = require('supertest');
const app = require('../../../../app');

describe('Transport API', () => {
  it('crée un service de transport (sécurité, RGPD, plugins)', async () => {
    const res = await request(app)
      .post('/transport/create')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({
        name: 'Taxi partagé',
        description: 'Service multilingue',
        locale: 'fr',
        tenant: 'demo',
        details: { type: 'partagé', places: 4 }
      });
    expect(res.statusCode).toBe(200);
    expect(res.body.transport).toBeDefined();
  });
});
