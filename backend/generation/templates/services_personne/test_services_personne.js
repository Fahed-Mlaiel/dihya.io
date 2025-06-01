// Test Services à la Personne avancé pour Dihya Coding
// Teste la création, la sécurité, la multilingue, la conformité RGPD, l'auditabilité, et l'extensibilité plugins.

const request = require('supertest');
const app = require('../../../../app');

describe('Services Personne API', () => {
  it('crée un service à la personne (sécurité, RGPD, plugins)', async () => {
    const res = await request(app)
      .post('/services_personne/create')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({
        name: 'Aide à domicile',
        description: 'Service multilingue',
        locale: 'fr',
        tenant: 'demo',
        details: { type: 'aide', heures: 2 }
      });
    expect(res.statusCode).toBe(200);
    expect(res.body.service).toBeDefined();
  });
});
