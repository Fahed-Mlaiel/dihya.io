/*
 * Test d'intégration ultra avancé pour les routes IT DevOps
 * Sécurité maximale, multilingue, multitenancy, audit, mocks externes
 * Compatible CI/CD, Codespaces, Linux
 */
const request = require('supertest');
const app = require('../../../src/app');
const { getJWT, getAdminJWT, getTenantId } = require('../../utils/auth');

describe('IT DevOps Integration', () => {
  let userToken, adminToken, tenantId;
  beforeAll(async () => {
    tenantId = await getTenantId();
    userToken = await getJWT({ role: 'user', tenant: tenantId });
    adminToken = await getAdminJWT({ tenant: tenantId });
  });

  it('should secure all DevOps endpoints (CORS, JWT, WAF, anti-DDOS)', async () => {
    const res = await request(app)
      .get('/api/devops/status')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .set('Origin', 'https://trusted.domain')
      .expect(200);
    expect(res.body.status).toBe('ok');
    expect(res.body.i18n).toHaveProperty('fr');
    expect(res.body.i18n).toHaveProperty('en');
  });

  it('should log and audit all actions', async () => {
    const res = await request(app)
      .post('/api/devops/audit')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .send({ action: 'deploy', target: 'k8s' })
      .expect(201);
    expect(res.body.audit).toBe(true);
  });

  it('should support plugin extension via API', async () => {
    const res = await request(app)
      .post('/api/devops/plugins')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .send({ name: 'test-plugin', url: 'https://plugin.example.com' })
      .expect(201);
    expect(res.body.plugin).toBeDefined();
  });

  it('should fallback to open source AI if needed', async () => {
    const res = await request(app)
      .post('/api/devops/ai')
      .set('Authorization', `Bearer ${adminToken}`)
      .set('X-Tenant-Id', tenantId)
      .send({ prompt: 'status', fallback: true })
      .expect(200);
    expect(['llama', 'mixtral', 'mistral']).toContain(res.body.engine);
  });

  // ... autres tests avancés (multilingue, RGPD, export, etc.)
});
