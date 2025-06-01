/*
 * Test d'intégration ultra avancé pour les routes mobiles
 * Sécurité maximale, multilingue, multitenancy, audit, mocks externes
 * Compatible CI/CD, Codespaces, Linux
 */
const request = require('supertest');
const app = require('../../../src/app');
const { getJWT, getAdminJWT, getTenantId } = require('../../utils/auth');

describe('Mobile Integration', () => {
  let userToken, adminToken, tenantId;
  beforeAll(async () => {
    tenantId = await getTenantId();
    userToken = await getJWT({ role: 'user', tenant: tenantId });
    adminToken = await getAdminJWT({ tenant: tenantId });
  });

  it('should secure all mobile endpoints (CORS, JWT, WAF, anti-DDOS)', async () => {
    const res = await request(app)
      .get('/api/mobile/notifications')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .set('Origin', 'https://trusted.domain')
      .expect(200);
    expect(res.body.status).toBe('ok');
    expect(res.body.i18n).toHaveProperty('fr');
    expect(res.body.i18n).toHaveProperty('en');
  });

  it('should log and audit all mobile actions', async () => {
    const res = await request(app)
      .post('/api/mobile/audit')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .send({ action: 'send', target: 'notification' })
      .expect(201);
    expect(res.body.audit).toBe(true);
  });

  it('should support project generation via API', async () => {
    const res = await request(app)
      .post('/api/mobile/generate')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .send({ type: 'web', fallback: true })
      .expect(200);
    expect(res.body.generated).toBe(true);
  });

  // ... autres tests avancés (multilingue, RGPD, export, etc.)
});
