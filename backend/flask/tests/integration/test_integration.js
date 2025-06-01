/**
 * Test d'intégration Node.js global pour l'API Flask Dihya.
 * Couvre sécurité, i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
 */
const request = require('supertest');
const API_URL = process.env.API_URL || 'http://localhost:5000';

describe('Dihya API Integration (Node.js)', () => {
  it('should return 200 and admin role for secure route', async () => {
    const res = await request(API_URL)
      .get('/api/health/secure')
      .set('Authorization', 'Bearer test_admin_token')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(res.body.role).toBe('admin');
  });

  it('should support i18n for all supported languages', async () => {
    for (const lang of ['fr','en','ar','de','zh','ja','ko','nl','he','fa','hi','es']) {
      const res = await request(API_URL)
        .get('/api/health/i18n')
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body.lang).toBe(lang);
    }
  });

  it('should support multitenancy', async () => {
    const res = await request(API_URL)
      .get('/api/health/tenant')
      .set('X-Tenant', 'tenant1');
    expect(res.statusCode).toBe(200);
    expect(res.body.tenant).toBe('tenant1');
  });

  it('should return plugin info', async () => {
    const res = await request(API_URL)
      .get('/api/health/plugin-test');
    expect(res.statusCode).toBe(200);
    expect(res.body.plugin).toBeDefined();
  });

  it('should fallback to open source AI', async () => {
    const res = await request(API_URL)
      .get('/api/health/ia-fallback');
    expect(res.statusCode).toBe(200);
    expect(['LLaMA','Mixtral','Mistral']).toContain(res.body.ia);
  });

  it('should export RGPD data', async () => {
    const res = await request(API_URL)
      .get('/api/health/rgpd/export');
    expect(res.statusCode).toBe(200);
    expect(res.body.export).toBeDefined();
  });

  it('should return audit logs', async () => {
    const res = await request(API_URL)
      .get('/api/health/audit-log');
    expect(res.statusCode).toBe(200);
    expect(res.body.audit).toBeDefined();
  });

  it('should serve robots.txt for SEO', async () => {
    const res = await request(API_URL)
      .get('/api/health/seo/robots.txt');
    expect(res.statusCode).toBe(200);
    expect(res.text).toContain('User-agent');
  });
});
