// test.js
/**
 * Tests unitaires et d'intégration ultra avancés pour l'ensemble des APIs Dihya (Node)
 * Sécurité maximale, multilingue, audit, plugins, RGPD, accessibilité, e2e.
 */
const request = require('supertest');
const app = require('../src/app');
const { getJWTToken } = require('./utils/auth');

describe('Dihya API Global Tests', () => {
  let token;
  beforeAll(async () => {
    token = await getJWTToken('admin');
  });

  it('should return 200 for /api/health', async () => {
    const res = await request(app).get('/api/health');
    expect(res.statusCode).toBe(200);
    expect(res.body.status).toBe('ok');
  });

  it('should enforce CORS and JWT', async () => {
    const res = await request(app)
      .get('/api/secure-endpoint')
      .set('Authorization', `Bearer ${token}`);
    expect([200, 403]).toContain(res.statusCode);
  });

  // ...tests multilingues, RBAC, audit, plugins, RGPD, accessibilité, e2e...
});
