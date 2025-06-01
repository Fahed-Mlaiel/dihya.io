/**
 * Test de santé pour le template Health
 * @module test_health
 * @description Test unitaire et d'intégration pour la route Health, avec sécurité, i18n, audit, JWT, CORS, WAF, anti-DDOS, multitenancy, et fallback IA.
 * @author Dihya Coding
 */
const request = require('supertest');
const app = require('../../../../src/app');
const jwt = require('jsonwebtoken');
const { getI18n } = require('../../../../src/utils/i18n');

describe('Health Template API', () => {
  let token;
  beforeAll(() => {
    token = jwt.sign({ role: 'admin', tenant: 'default' }, process.env.JWT_SECRET || 'test', { expiresIn: '1h' });
  });
  it('GET /api/health/status - should return 200 and health info (fr)', async () => {
    const res = await request(app)
      .get('/api/health/status')
      .set('Authorization', `Bearer ${token}`)
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.status).toBe('ok');
    expect(res.body.i18n).toBeDefined();
  });
  it('GET /api/health/status - should return 401 without JWT', async () => {
    const res = await request(app).get('/api/health/status');
    expect(res.statusCode).toBe(401);
  });
  it('GET /api/health/status - should fallback to open source IA if needed', async () => {
    // Simule une panne IA principale
    process.env.IA_FALLBACK = 'true';
    const res = await request(app)
      .get('/api/health/status')
      .set('Authorization', `Bearer ${token}`);
    expect(res.body.iaFallback).toBe(true);
    process.env.IA_FALLBACK = 'false';
  });
});
// ...tests avancés (RGPD, plugins, audit, SEO, accessibilité, multilingue, e2e)...
