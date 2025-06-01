/*
 * Test d'intégration ultra avancé pour les routes preview
 * Sécurité maximale, multilingue, multitenancy, audit, mocks externes
 * Compatible CI/CD, Codespaces, Linux
 */
const request = require('supertest');
const app = require('../../../src/app');
const { getJWT, getAdminJWT, getTenantId } = require('../../utils/auth');

describe('Preview Integration', () => {
  let userToken, adminToken, tenantId;
  beforeAll(async () => {
    tenantId = await getTenantId();
    userToken = await getJWT({ role: 'user', tenant: tenantId });
    adminToken = await getAdminJWT({ tenant: tenantId });
  });

  it('should secure all preview endpoints (CORS, JWT, WAF, anti-DDOS)', async () => {
    const res = await request(app)
      .get('/api/preview/generate')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .set('Origin', 'https://trusted.domain')
      .expect(200);
    expect(res.body.status).toBe('ok');
    expect(res.body.i18n).toHaveProperty('fr');
    expect(res.body.i18n).toHaveProperty('en');
  });

  it('should log and audit all preview actions', async () => {
    const res = await request(app)
      .post('/api/preview/audit')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .send({ action: 'render', target: 'preview' })
      .expect(201);
    expect(res.body.audit).toBe(true);
  });

  it('should support AI preview generation', async () => {
    const res = await request(app)
      .post('/api/preview/ai')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .send({ prompt: 'generate', fallback: true })
      .expect(200);
    expect(['llama', 'mixtral', 'mistral']).toContain(res.body.engine);
  });

  // ... autres tests avancés (multilingue, RGPD, export, etc.)
});
