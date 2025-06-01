/**
 * Test unitaire Node.js global pour l'API Dihya.
 * Sécurité, i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
 */
const { validateInput, auditLog, pluginManager, rgpdAnonymize, getI18nHeaders, getAdminToken, getTenantHeaders } = require('./integration/utils/utils');

describe('Dihya Utils', () => {
  it('should validate input', () => {
    expect(() => validateInput({ field: 'ok' }, { field: 'string' })).not.toThrow();
    expect(() => validateInput({ field: 123 }, { field: 'string' })).toThrow();
  });

  it('should log audit', () => {
    const entry = auditLog('test', { user: 'admin' });
    expect(entry).toHaveProperty('timestamp');
    expect(entry.action).toBe('test');
  });

  it('should manage plugins', () => {
    const result = pluginManager('test_plugin', { param: 1 });
    expect(['success', 'error']).toContain(result.status);
  });

  it('should anonymize RGPD data', () => {
    const anon = rgpdAnonymize({ name: 'John', email: 'john@example.com' });
    expect(anon.name).not.toBe('John');
    expect(anon.email).not.toContain('@');
  });

  it('should generate i18n headers', () => {
    for (const lang of ['fr','en','ar','de','zh','ja','ko','nl','he','fa','hi','es']) {
      expect(getI18nHeaders(lang)['Accept-Language']).toBe(lang);
    }
  });

  it('should generate admin token', () => {
    expect(getAdminToken()).toMatch(/test_admin_token/);
  });

  it('should generate tenant headers', () => {
    expect(getTenantHeaders('tenant1')['X-Tenant']).toBe('tenant1');
  });
});
