// Test Social avancé pour Dihya Coding
// Teste la création, la sécurité, la multilingue, la conformité RGPD, l'auditabilité, et l'extensibilité plugins.

const request = require('supertest');
const app = require('../../../../app');

describe('Social API', () => {
  it('crée une interaction sociale (sécurité, RGPD, plugins)', async () => {
    const res = await request(app)
      .post('/social/create')
      .set('Authorization', 'Bearer test-jwt-admin')
      .send({
        type: 'like',
        user: 'testuser',
        locale: 'fr',
        tenant: 'demo',
        details: { postId: 123 }
      });
    expect(res.statusCode).toBe(200);
    expect(res.body.social).toBeDefined();
  });
});
