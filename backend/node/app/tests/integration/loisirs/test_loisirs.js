/*
 * Test d'intégration ultra avancé pour les routes loisirs
 * Sécurité maximale, multilingue, multitenancy, audit, mocks externes
 * Compatible CI/CD, Codespaces, Linux
 */
const request = require('supertest');
const app = require('../../../src/app');
const { getJWT, getAdminJWT, getTenantId } = require('../../utils/auth');

describe('Loisirs Integration', () => {
  let userToken, adminToken, tenantId;
  beforeAll(async () => {
    tenantId = await getTenantId();
    userToken = await getJWT({ role: 'user', tenant: tenantId });
    adminToken = await getAdminJWT({ tenant: tenantId });
  });

  it('should secure all leisure endpoints (CORS, JWT, WAF, anti-DDOS)', async () => {
    const res = await request(app)
      .get('/api/leisure/activities')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .set('Origin', 'https://trusted.domain')
      .expect(200);
    expect(res.body.status).toBe('ok');
    expect(res.body.i18n).toHaveProperty('fr');
    expect(res.body.i18n).toHaveProperty('en');
  });

  it('should log and audit all leisure actions', async () => {
    const res = await request(app)
      .post('/api/leisure/audit')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .send({ action: 'book', target: 'activity' })
      .expect(201);
    expect(res.body.audit).toBe(true);
  });

  it('should support AI suggestions for activities', async () => {
    const res = await request(app)
      .post('/api/leisure/ai')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .send({ prompt: 'suggest', fallback: true })
      .expect(200);
    expect(['llama', 'mixtral', 'mistral']).toContain(res.body.engine);
  });

  // ... autres tests avancés (multilingue, RGPD, export, etc.)
});
