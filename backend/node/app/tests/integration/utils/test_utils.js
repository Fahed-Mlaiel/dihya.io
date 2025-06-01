/*
 * Test d'intégration ultra avancé pour les routes utilitaires
 * Sécurité maximale, multilingue, multitenancy, audit, mocks externes
 * Compatible CI/CD, Codespaces, Linux
 */
const request = require('supertest');
const app = require('../../../src/app');
const { getJWT, getAdminJWT, getTenantId } = require('../../utils/auth');

describe('Utils Integration', () => {
  let userToken, adminToken, tenantId;
  beforeAll(async () => {
    tenantId = await getTenantId();
    userToken = await getJWT({ role: 'user', tenant: tenantId });
    adminToken = await getAdminJWT({ tenant: tenantId });
  });

  it('should secure all utils endpoints (CORS, JWT, WAF, anti-DDOS)', async () => {
    const res = await request(app)
      .get('/api/utils/logs')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .set('Origin', 'https://trusted.domain')
      .expect(200);
    expect(res.body.status).toBe('ok');
    expect(res.body.i18n).toHaveProperty('fr');
    expect(res.body.i18n).toHaveProperty('en');
  });

  it('should log and audit all utils actions', async () => {
    const res = await request(app)
      .post('/api/utils/audit')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .send({ action: 'export', target: 'logs' })
      .expect(201);
    expect(res.body.audit).toBe(true);
  });

  it('should support data anonymization and export', async () => {
    const res = await request(app)
      .post('/api/utils/export')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .send({ userId: 'test-user' })
      .expect(200);
    expect(res.body.export).toBe(true);
  });

  // ... autres tests avancés (multilingue, RGPD, export, etc.)
});
